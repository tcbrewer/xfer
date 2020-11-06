// Andy said look here: https://github.com/KastnerRG/Access_Control_ext/blob/master/RADIX-S/sp_01/prospect.work/aac_explore/assertion_SP01_RECEIVE_M_AXI_BID.work/top_wrapper_TvfnZi.v

// In terms of values at program points, this really looks like the assertions are looking for ARESETN != 0 || REG != 0. That is easy to find but not exciting and doesn't use IFT.

// PART 1: INITIALIZATION.  This prevents assertion failures during start-up. This is managed using Daikon orig()

  initial begin
		assertion_REG_result_result_ready = 1'b0 ;
		
		
		#0 assertion_REG_result_result_ready = 1'b1 ;
		assertion_REG_result = assertion_REG_result_wire;
	end
  
// PART 2: ASSERTION DESCRIPTION.  This pivots on encrypted state we don't have. 

	// ----- Assertion result
  
// This says:  if <encrpt> REG != 0, else ARESETN != 0 || REG != 0. 
// Note the VCDs I have never use z or x post intialization, REG must be 0 or 1. I suspect this in an init guard as well.

	assign assertion_REG_result_wire = ( ((TTGSHADOWPKG::resolvex_legal === 1'b1) ? ( ( |( REG_wire ) !== 1'b1 && |( REG_wire ) !== 1'bx ) ) :  (( |( REG_wire) !== 1'b1 ) )) || ( (ARESETN) != 0 ) );

// Latent code as we don't have z.

	always@(assertion_REG_result_wire) begin
		assertion_REG_result <= ( ( assertion_REG_result_wire === 1'b1 ) || ( assertion_REG_result_wire === 1'bz ) ) ;
	end

// This says: when the result_wire expression becomes true, if initialization is complete, the assertion passes.

	// ----- Check assertion pass conditions

	always@( posedge assertion_REG_result ) begin
		if (assertion_REG_result_result_ready === 1'b1 ) begin
			$display("[RADIX] -PASS- Security property assertion_REG passes at time %0d", $time);
		end
	end
  
// PART 3: FAILURE COUNTING.  This is uninteresting.

	// ----- Check assertion fail conditions

	longint assertion_REG_result_count;
	longint assertion_REG_MAX_ERROR;

	initial begin
		assertion_REG_result_count = 0 ;
		if (!$value$plusargs("TTG_MAX_AST_ERROR_COUNT=%d", assertion_REG_MAX_ERROR)) begin
			$display("[RADIX] Maximum security property error count not set for security property <assertion_REG>. Running until finish.");
			assertion_REG_MAX_ERROR = 0 ;
		end else if ( assertion_REG_MAX_ERROR <= 0 ) begin
			$display("[RADIX] Maximum security property error count set to non-positive integer (%0d) for security property <assertion_REG>. Running until finish.", assertion_REG_MAX_ERROR);
		end else begin
			$display("[RADIX] Maximum security property error count set to: (%0d) for security property <assertion_REG>.", assertion_REG_MAX_ERROR);
		end
	end

	always@( negedge assertion_REG_result ) begin
		if (assertion_REG_result_result_ready === 1'b1 ) begin
			if ( assertion_REG_result == 1'b0 ) begin
				assertion_REG_result_count += 1 ;
				$display("[RADIX] -FAIL- Security property assertion_REG failed at time %0d", $time);
				$display("[RADIX] - Occurred (%0d) time(s).", assertion_REG_result_count);

				if ( ( assertion_REG_MAX_ERROR > 0 ) && ( assertion_REG_result_count >= assertion_REG_MAX_ERROR) ) begin
					$finish;
				end
			end
		end
	end

// PART 4: MONITOR. This shows when the assertions are tracked.

	// ----- Monitor for assertion tracking

	logic assertion_REG_is_tracking ;
  
// In all cases, REG_tnt == !ARESETN

	always_comb begin
		assertion_REG_is_tracking = (|( REG_tnt )) ;
	end

	always@( assertion_REG_is_tracking ) begin
		if ( assertion_REG_is_tracking === 1'b1 ) begin
			$display("[RADIX] Security property assertion_REG is tagging information flow from assertion sources at time (%0d).", $time);
		end
		else if ( assertion_REG_is_tracking === 1'bx ) begin
			$display("[RADIX] Security Property assertion_REG is tagging information flow (assertion conditions resolve to x) from assertion sources at time (%0d).", $time);
		end
		else begin
			$display("[RADIX] Assertion assertion_REG has stopped tagging information flow from assertion sources at time (%0d).", $time);
		end
	end

	final begin
		$display("[RADIX] Total failures for security property <assertion_REG>: (%0d)", assertion_REG_result_count );
	end
