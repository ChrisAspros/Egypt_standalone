time_signature 4
form_length 32
harmonic_rhythm 1 //each non-t production applies to 1 bar (e.g. I1 : 1, I2 : 2), i.e. seq_t[3]==1, seq_t[3]==2 etc.

//spaces are significant
//decision_bars { 1 5 9 11 13 15 17 21 25 27 29 31 } //for recovery? (if e.g. in middle of the form)
//decision_bars { 1 9 17 25 }
//decision_bars { 1 9 }
//cadence_bars { 3 7 11 15 19 23 27 31 } //no need for 11 as it is the form's' end, but just to make it more 'cadency' (see cad_11)
//optimal_form { I I bVII I I bII bVII I IV IIIo IV I IV IV bVII bVII I I bVII I I bII bVII I bII I bVII I bII I bVII I }
terminals { i im immaj i6 i7 bii iim7 iiim iiim7 iiio iv iv6 iv7 ivm v7 vo bvi bviim }

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


//in the Sect_* rules, the _* simply indicates the placement for the human reader. 
//The actual sect positions are set in the basic vectors above - get_basic_vectors() in the code


//time offset from main non-T IN PARENTHESES

rule: S -> 1.0 SectA(1) SectB(9) SectA(17) SectC(25) //SectC(16) SectA(24) //SectB(2) //SectA(8) SectC(8) //
		:end_rule

rule: SectA -> 1.0 decA(1) decA(5) //could be decA1(1) decA2(5) || decA(1) decA(5) || dec(1) dec(5) for dec_1 dec_5 etc..
			:end_rule

rule: decA -> 1.0 T SD D T :end_rule

rule: T -> 1.0 I :end_rule
rule: SD -> 1.0 bII :end_rule
rule: D -> 1.0 bVII :end_rule


rule: SectB -> 1.0 decB1(1) decB2(5)
			:end_rule

rule: decB1 -> 1.0 SD T SD D :end_rule

rule: decB2 -> 1.0 SD T D T :end_rule


rule: SectC -> 1.0 decC(1) decC(3) decC(5) decC(7) :end_rule

rule: decC -> 1.0 D T :end_rule

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

rule: dec_13 -> 0.6 IV I bVII I
			 -> 0.4 IV IV bVII I
			:end_rule



//MOVE TO END NECESSARY??
//translating straight for now in case more decision-making is necessary for terminal productions
rule: I_1 -> 1.0 i
	:end_rule
		-> 0.5 i
		-> 0.5 immaj
		:end_rule
rule: I -> 1.0 i :end_rule
rule: bII -> 1.0 bii :end_rule
rule: IIIo -> 1.0 iiio :end_rule
rule: IV -> 1.0 ivm :end_rule
rule: Vo -> 1.0 vo :end_rule
rule: bVI -> 1.0 bvi :end_rule
rule: bVII -> 1.0 bviim :end_rule


//contect-aware must have equal length both sides(?)
//could also support I_1_1 (1st beat of bar one?? - bar_time_str, beat_time_str)
//optional members of the right side (i.e. i|iv) are not updated in update_cycle() 