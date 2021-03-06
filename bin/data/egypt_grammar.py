time_signature 4
form_length 32
harmonic_rhythm 1 //each non-t production applies to 1 bar (e.g. I1 : 1, I2 : 2), i.e. seq_t[3]==1, seq_t[3]==2 etc.

//spaces are significant
decision_bars { 1 5 9 11 13 15 17 21 25 27 29 31 } //for now
cadence_bars { 3 7 11 15 19 23 27 31 } //no need for 11 as it is the form's' end, but just to make it more 'cadency' (see cad_11)
optimal_form { I I bVII I I bII bVII I IV IIIo IV I IV IV bVII bVII I I bVII I I bII bVII I bII I bVII I bII I bVII I }
terminals { i i6 i7 bii iim7 iiim iiim7 iiio iv iv6 iv7 ivm v7 vo bvi bviim }

//decision_heads dec_* //apply to decision_bars elem
//I(0+1)_head
//non-t
//root:(defined by "dec_*") type: ("_*") inv: pos:

TIMED RULES: //left_str.size() ===(MUST EQUAL) right_side[x].rigth_str.size() ???

//when writing a (timed?) rule for e.g. I_1, all other I_1 rules should have same context size
//general rules are timely exposed to be tested without centre-element (of left_str)
//so at any point, all of general_rules[x].left_str has to be tested by expanding the current element (chord) back n forth based on left_str.size()

//context { 0 0 }//no context-awarenes here (for now..)
//12th iteration in main()

DOCUMENTATION
//right_str.size() must be >= left_str.size()


   ===========
|| TIMED RULES || //normally they should only look ahead only for higher-level context such as IV in bar 5 (improvisor's mind..), not for specific chord shape/form etc
   ===========

==============(DEC 1)===============
(1)==============================

-----(DEC 1)

//for each chord, one tag based on decisio_bar+harmonic_rh
//each new line should start with "->"

1 5 9 11 13 15 17 21 25 27 29 31

rule: dec_1 -> 0.4 I I bVII I
	  		-> 0.2 I I bII I
	  		-> 0.1 I I Vo I
	  		-> 0.2 I bII bVII I
	  		-> 0.1 I bII Vo I
	  		:end_rule

rule: dec_5 -> 0.4 I I bVII I
	  		-> 0.2 I I bII I
	  		-> 0.1 I I Vo I
	  		-> 0.2 I bII bVII I
	  		-> 0.1 I bII Vo I
	  		:end_rule

rule: dec_9 -> 0.4 IV IV
			-> 0.1 IV I
			-> 0.3 IV bVI
			-> 0.2 IV IIIo
	  		:end_rule

//if it doesnt work only keep the context-insensitive rule just underneath
rule: i dec_11 i -> 0.6 i IV IV
				 -> 0.4 i IV Vo
				:end_rule
rule: ivm dec_11 i -> 0.6 ivm IV I
				   -> 0.4 ivm IV Vo
				  :end_rule

rule: dec_11 -> 0.6 IV I
			 -> 0.3 IV Vo
			 -> 0.1 IV IV
			:end_rule

rule: dec_13 -> 0.6 IV I
			 -> 0.4 IV IV
			:end_rule

rule: dec_15 -> 0.1 bVII I
			 -> 0.3 bVII bII
			 -> 0.2 bVII Vo
			 -> 0.4 bVII bVII
			:end_rule

rule: dec_17 -> 0.4 I I bVII I
	  		-> 0.2 I I bII I
	  		-> 0.1 I I Vo I
	  		-> 0.2 I bII bVII I
	  		-> 0.1 I bII Vo I
	  		:end_rule

rule: dec_21 -> 0.4 I I bVII I
	  		-> 0.2 I I bII I
	  		-> 0.1 I I Vo I
	  		-> 0.2 I bII bVII I
	  		-> 0.1 I bII Vo I
	  		:end_rule

rule: dec_25 -> 0.3 bII I
			 -> 0.6 bVII I
			 -> 0.1 Vo I
	  		:end_rule

rule: dec_27 -> 0.3 bII I
			 -> 0.6 bVII I
			 -> 0.1 Vo I
	  		:end_rule

rule: dec_29 -> 0.3 bII I
			 -> 0.6 bVII I
			 -> 0.1 Vo I
	  		:end_rule

rule: dec_31 -> 0.3 bII I
			 -> 0.6 bVII I
			 -> 0.1 Vo IV
	  		:end_rule


//MOVE TO END NECESSARY??
//translating straight for now in case more decision-making is necessary for terminal productions
rule: I -> 1.0 i :end_rule
rule: bII -> 1.0 bii :end_rule
rule: IIIo -> 1.0 iiio :end_rule
rule: IV -> 1.0 ivm :end_rule
rule: Vo -> 1.0 vo :end_rule
rule: bVI -> 1.0 bvi :end_rule
rule: bVII -> 1.0 bviim :end_rule
