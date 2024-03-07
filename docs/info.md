<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

# How it works

This section will include a logic table indicating the operation

- **File**: project.v

## Diagram
![Diagram](tt_um_damor_rbz.svg "Diagram")
## Ports

| Port name | Direction | Type       | Description |
| --------- | --------- | ---------- | ----------- |
| ui_in     | input     | wire [7:0] |             |
| uo_out    | output    | wire [7:0] |             |
| uio_in    | input     | wire [7:0] |             |
| uio_out   | output    | wire [7:0] |             |
| uio_oe    | output    | wire [7:0] |             |
| ena       | input     | wire       |             |
| clk       | input     | wire       |             |
| rst_n     | input     | wire       |             |

## Signals

| Name             | Type       | Description |
| ---------------- | ---------- | ----------- |
| quotient_w       | wire [2:0] |             |
| quotient_sign_w  | wire       |             |
| remainder_w      | wire [2:0] |             |
| remainder_sign_w | wire       |             |
| quotient         | reg [2:0]  |             |
| quotient_sign    | reg        |             |
| remainder        | reg [2:0]  |             |
| remainder_sign   | reg        |             |
| dividend_w       | wire [2:0] |             |
| dividend_sign_w  | wire       |             |
| divisor_w        | wire [2:0] |             |
| divisor_sign_w   | wire       |             |

## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always


# How to test

Change inputs and see outputs

# External hardware

LEDs are a good way to show the result
