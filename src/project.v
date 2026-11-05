/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (1=output, 0=input)
    input  wire       ena,      // enable pin (active high)
    input  wire       clk,      // clock pin
    input  wire       rst_n     // reset pin (active low)
);

    // 1. Configure all bidirectional pins safely as inputs
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // 2. Define the 8-bit counter register array
    reg [7:0] counter_reg;
    
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            counter_reg <= 8'b00000000;
        end else if (ui_in[0]) begin // ui_in[0] acts as your count enable switch
            counter_reg <= counter_reg + 1'b1;
        end
    end

    // 3. Drive the counter register outputs out to the physical pins
    assign uo_out = counter_reg;

endmodule