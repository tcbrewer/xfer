initial begin
		assertion_SP01_RECEIVE_M_AXI_RDATA_result_result_ready = 1'b0 ;
		
		
		#0 assertion_SP01_RECEIVE_M_AXI_RDATA_result_result_ready = 1'b1 ;
		assertion_SP01_RECEIVE_M_AXI_RDATA_result = assertion_SP01_RECEIVE_M_AXI_RDATA_result_wire;
	end

	// ----- Assertion result

	assign assertion_SP01_RECEIVE_M_AXI_RDATA_result_wire = ( ((TTGSHADOWPKG::resolvex_legal === 1'b1) ? ( ( |( shadow_dut.shadow_M_AXI_RDATA_wire[31:0] ) !== 1'b1 && |( shadow_dut.shadow_M_AXI_RDATA_wire[31:0] ) !== 1'bx ) ) :  (( |( shadow_dut.shadow_M_AXI_RDATA_wire[31:0] ) !== 1'b1 ) )) || ( (shadow_dut.ARESETN) != 0 ) );

	always@(assertion_SP01_RECEIVE_M_AXI_RDATA_result_wire) begin
		assertion_SP01_RECEIVE_M_AXI_RDATA_result <= ( ( assertion_SP01_RECEIVE_M_AXI_RDATA_result_wire === 1'b1 ) || ( assertion_SP01_RECEIVE_M_AXI_RDATA_result_wire === 1'bz ) ) ;
	end

	// ----- Check assertion pass conditions

	always@( posedge assertion_SP01_RECEIVE_M_AXI_RDATA_result ) begin
		if (assertion_SP01_RECEIVE_M_AXI_RDATA_result_result_ready === 1'b1 ) begin
			$display("[RADIX] -PASS- Security property assertion_SP01_RECEIVE_M_AXI_RDATA passes at time %0d", $time);
		end
	end

	// ----- Check assertion fail conditions

	longint assertion_SP01_RECEIVE_M_AXI_RDATA_result_count;
	longint assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR;

	initial begin
		assertion_SP01_RECEIVE_M_AXI_RDATA_result_count = 0 ;
		if (!$value$plusargs("TTG_MAX_AST_ERROR_COUNT=%d", assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR)) begin
			$display("[RADIX] Maximum security property error count not set for security property <assertion_SP01_RECEIVE_M_AXI_RDATA>. Running until finish.");
			assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR = 0 ;
		end else if ( assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR <= 0 ) begin
			$display("[RADIX] Maximum security property error count set to non-positive integer (%0d) for security property <assertion_SP01_RECEIVE_M_AXI_RDATA>. Running until finish.", assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR);
		end else begin
			$display("[RADIX] Maximum security property error count set to: (%0d) for security property <assertion_SP01_RECEIVE_M_AXI_RDATA>.", assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR);
		end
	end

	always@( negedge assertion_SP01_RECEIVE_M_AXI_RDATA_result ) begin
		if (assertion_SP01_RECEIVE_M_AXI_RDATA_result_result_ready === 1'b1 ) begin
			if ( assertion_SP01_RECEIVE_M_AXI_RDATA_result == 1'b0 ) begin
				assertion_SP01_RECEIVE_M_AXI_RDATA_result_count += 1 ;
				$display("[RADIX] -FAIL- Security property assertion_SP01_RECEIVE_M_AXI_RDATA failed at time %0d", $time);
				$display("[RADIX] - Occurred (%0d) time(s).", assertion_SP01_RECEIVE_M_AXI_RDATA_result_count);

				if ( ( assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR > 0 ) && ( assertion_SP01_RECEIVE_M_AXI_RDATA_result_count >= assertion_SP01_RECEIVE_M_AXI_RDATA_MAX_ERROR) ) begin
					$finish;
				end
			end
		end
	end

	// ----- Monitor for assertion tracking

	logic assertion_SP01_RECEIVE_M_AXI_RDATA_is_tracking ;

	always_comb begin
		assertion_SP01_RECEIVE_M_AXI_RDATA_is_tracking = (|( shadow_dut.shadow_M_AXI_RDATA_tnt )) ;
	end

	always@( assertion_SP01_RECEIVE_M_AXI_RDATA_is_tracking ) begin
		if ( assertion_SP01_RECEIVE_M_AXI_RDATA_is_tracking === 1'b1 ) begin
			$display("[RADIX] Security property assertion_SP01_RECEIVE_M_AXI_RDATA is tagging information flow from assertion sources at time (%0d).", $time);
		end
		else if ( assertion_SP01_RECEIVE_M_AXI_RDATA_is_tracking === 1'bx ) begin
			$display("[RADIX] Security Property assertion_SP01_RECEIVE_M_AXI_RDATA is tagging information flow (assertion conditions resolve to x) from assertion sources at time (%0d).", $time);
		end
		else begin
			$display("[RADIX] Assertion assertion_SP01_RECEIVE_M_AXI_RDATA has stopped tagging information flow from assertion sources at time (%0d).", $time);
		end
	end

	final begin
		$display("[RADIX] Total failures for security property <assertion_SP01_RECEIVE_M_AXI_RDATA>: (%0d)", assertion_SP01_RECEIVE_M_AXI_RDATA_result_count );
	end
