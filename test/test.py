# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb.binary import BinaryRepresentation, BinaryValue


@cocotb.test()
async def test_divider(dut):
  dut._log.info("Start")
  
  # Our example module doesn't use clock and reset, but we show how to use them here anyway.
  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())

  # Reset
  dut._log.info("Reset")
  #dut.ena.value = 1
  dut.ui_in.value = 0
  #dut.uio_in.value = 0
  #dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  #dut.rst_n.value = 1

  # Set the input values, wait one clock cycle, and check the output
  dut._log.info("Test 0 divisor")
  dut.ui_in.value = 0
  await ClockCycles(dut.clk, 2)
  print(dut.uo_out.value)
  assert dut.uo_out.value == 0b11111111
  
  dut._log.info("Test different from 0 divisor")
  dut.ui_in.value = 0b11111111
  await ClockCycles(dut.clk, 2)
  print(dut.uo_out.value)
  assert dut.uo_out.value == 0b00000000

print()
