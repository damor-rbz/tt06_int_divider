# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, RisingEdge, FallingEdge
from cocotb.binary import BinaryRepresentation, BinaryValue

## Test coverage
# test with divider to cero
# test with dividend to cero


@cocotb.test()
# This test wil check the case when the inpuit has cero as a divider
# all output values must result in overflow
# 32 cases
async def test_divider_cero(dut):
  # common init
  dut._log.info("Reset")
  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())
  dut.ui_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  dut.rst_n.value = 1
  dut._log.info("Test")
  # Set the input values, wait one clock cycle, and check the output
  dut._log.info("Test 0 divider positive sign")

  for x in range(16):
    await RisingEdge(dut.clk)
    dut.ui_in.value = x
    print(dut.ui_in.value)
    await FallingEdge(dut.clk)
    assert dut.uo_out.value == 0b11111111

  dut._log.info("Test 0 divider negative sign")
  for x in range(16):
    await RisingEdge(dut.clk)
    dut.ui_in.value = 0b10000000 + x
    print(dut.ui_in.value)
    await FallingEdge(dut.clk)
    assert dut.uo_out.value == 0b11111111

@cocotb.test()
async def test_dividend_cero(dut):
  # common init
  dut._log.info("Reset")
  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())
  dut.ui_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  dut.rst_n.value = 1

  dut._log.info("Test dividend cero positive sign")
  for x in range(16):
    dut.ui_in.value = x*16
    print(x, dut.ui_in.value)
    if(x != 0): 
        await FallingEdge(dut.clk)
        if ( x-1 == 0):
            assert dut.uo_out.value == 0b11111111
        elif ( x-1 == 8):
            assert dut.uo_out.value == 0b11111111
        else:
            assert dut.uo_out.value == 0b00000000
    await RisingEdge(dut.clk)
  await FallingEdge(dut.clk)
  assert dut.uo_out.value == 0b00000000
  await RisingEdge(dut.clk)

  dut._log.info("Test dividend cero negative sign")
  for x in range(16):
    dut.ui_in.value = 0b00001000 + x*16
    print(x, dut.ui_in.value)
    if(x != 0):
        await FallingEdge(dut.clk)
        if (x-1 == 0):
            assert dut.uo_out.value == 0b11111111
        elif (x-1 == 8):
            assert dut.uo_out.value == 0b11111111
        else:
            assert dut.uo_out.value == 0b00000000
    await RisingEdge(dut.clk)
  await FallingEdge(dut.clk)
  assert dut.uo_out.value == 0b00000000

@cocotb.test()
async def test_divider_one(dut):
  # common init
  dut._log.info("Reset")
  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())
  dut.ui_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  dut.rst_n.value = 1

  # Set the input values, wait one clock cycle, and check the output
  dut._log.info("Test 0 divider positive sign")

  for x in range(16):
    await RisingEdge(dut.clk)
    dut.ui_in.value = x + 16
    await FallingEdge(dut.clk)
    print(dut.ui_in.value)
    print(dut.uo_out.value)
    #assert dut.uo_out.value == x 

print()
