<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project is an 8-bit synchronous up-counter. When the chip is enabled (`ena` is high) and the count enable switch (`ui_in[0]`) is active, the internal 8-bit register increments by 1 on every rising edge of the clock signal (`clk`). The current count value is output directly to the dedicated output pins (`uo_out`). The counter resets back to zero whenever the active-low reset pin (`rst_n`) is pulled low. All bidirectional I/O pins are safely configured as inputs.

## How to test

1. Apply an active-low reset pulse by driving `rst_n` low for several clock cycles, then bring it back high to initialize the counter to 0.
2. Set the chip enable pin `ena` high.
3. Drive the count enable pin `ui_in[0]` high to allow the counter to increment.
4. Toggle the clock pin `clk` and observe the binary counter value incrementing on the dedicated outputs `uo_out`.

## External hardware

None. This project operates entirely using the onboard internal logic registers, inputs, and outputs.
