/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`define default_netname none

module tt_um_damor_rbz (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // will go high when the design is enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);
	assign uio_out = 0;
	assign uio_oe  = 0;
	
	/* register creation */
	reg [2:0] quotient;
    reg       quotient_sign;
    reg [2:0] remainder;
    reg       remainder_sign;
	/* internal to external connection */
	assign uo_out[2:0] = quotient;
	assign uo_out[3]   = quotient_sign;
	assign uo_out[6:4] = remainder;
	assign uo_out[7]   = remainder_sign;

	/* input configuration */
	wire [2:0] dividend_w;
	wire 	   dividend_sign_w;
	wire [2:0] divisor_w;
	wire       divisor_sign_w;
	/* External to internal connection */
	assign dividend_w = ui_in[2:0];
	assign dividend_sign_w = ui_in[3];
	assign divisor_w = ui_in[6:4];
	assign divisor_sign_w = ui_in[7];

	always @(posedge clk) begin
		if(rst_n == 0) begin
			quotient <= 0;
	        quotient_sign <= 0;
	        remainder <= 0;
	        remainder_sign <= 0;
		end else begin
			if ( divisor_w == 0 ) begin
			/* divide by cero results in overflow */
				quotient <= 3'b111;
				quotient_sign <= 1;
				remainder <= 3'b111;
				remainder_sign <= 1;
			end else begin
			/* divisor not cero */
			/* first check if dividend is cero */
				if ( dividend_w == 0) begin
					quotient <= 0;
	            	quotient_sign <= 0;
	            	remainder <= 0;
	            	remainder_sign <= 0;
				end else begin
				/* dividend and divisor not zero */
					quotient <= 0;
                	quotient_sign <= 0;
                	remainder <= 0;
                	remainder_sign <= 0;
				end
			end
		end
	end

endmodule
