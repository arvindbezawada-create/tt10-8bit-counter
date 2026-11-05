# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # 1. Enable the counter by making sure ui_in[0] is equal to 1.
    # (1 is 00000001 in binary, which sets ui_in[0] high)
    dut.ui_in.value = 1 
    dut.uio_in.value = 0

    # 2. Wait for exactly 50 clock cycles so the counter increments to 50
    await ClockCycles(dut.clk, 50)

    # 3. ADD THIS LINE: Wait for the falling edge so the 50th count fully stabilizes
    await FallingEdge(dut.clk)

    # 4. Assert that the output has reached 50
    assert dut.uo_out.value == 50
    dut._log.info("Test passed successfully!")