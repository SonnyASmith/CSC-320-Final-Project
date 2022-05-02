__author__ = "Jason, Sonny, Matt, Jeremy"
__Copyright__ = "Copyright @2022"

class circuit(object):              #Circuit Class
    def __init__(self, in1, in2):
        self.in1_ = in1
        self.in2_ = in2

class andgate(circuit):             #AND Gate
    def getCircuitOutput(self):
        if self.in1_ == 1 and self.in2_ == 1:
            return 1
        else:
            return 0

class orgate(circuit):              #OR Gate
    def getCircuitOutput(self):
        if self.in1_ == 0 and self.in2_ == 0:
            return 0
        else:
            return 1

class notgate(circuit):             #NOT Gate
    def __init__(self, in1):
        self.in1_ = in1

    def getCircuitOutput(self):
        if self.in1_ == 1:
            return 0
        elif self.in1_ == 0:
            return 1

class orgate3(circuit):             # 3to1 OR implemented with 2to1 ORs
    def __init__(self, in1, in2, in3):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3

    def getCircuitOutput(self):
        org0 = orgate(self.in1_, self.in2_)
        out_org0 = org0.getCircuitOutput()

        org1 = orgate(out_org0, self.in3_)
        out_org1 = org1.getCircuitOutput()

        return out_org1

class orgate4(circuit):             # 4to1 OR implemented with 3to1 OR & 2to1 OR
    def __init__(self, in1, in2, in3, in4):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3
        self.in4_ = in4

    def getCircuitOutput(self):
        org0 = orgate3(self.in1_, self.in2_, self.in3_)
        out_org0 = org0.getCircuitOutput()

        org1 = orgate(out_org0, self.in4_)
        out_org1 = org1.getCircuitOutput()

        return out_org1
 
class orgate8(circuit):             # 8to1 OR implemented with 4to1 ORs & 2to1 OR
    def __init__(self, in1, in2, in3, in4, in5, in6, in7, in8):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3
        self.in4_ = in4
        self.in5_ = in5
        self.in6_ = in6
        self.in7_ = in7
        self.in8_ = in8

    def getCircuitOutput(self):
        org0 = orgate4(self.in1_, self.in2_, self.in3_, self.in4_)
        out_org0 = org0.getCircuitOutput()

        org1 = orgate4(self.in5_, self.in6_, self.in7_, self.in8_)
        out_org1 = org1.getCircuitOutput()

        org2 = orgate(out_org0, out_org1)
        out_org2 = org2.getCircuitOutput()

        return out_org2

class andgate3(circuit):            #3 input AND Gate implemented with 2 to 1 AND gates
    def __init__(self, in1, in2, in3):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3

    def getCircuitOutput(self):
        andg0 = andgate(self.in1_, self.in2_)
        out_andg0 = andg0.getCircuitOutput()

        andg1 = andgate(out_andg0, self.in3_)
        out_andg1 = andg1.getCircuitOutput()

        return out_andg1

class andgate4(circuit):            # 4to1 AND gate implemented with 3to1 AND & 2to1 AND
    def __init__(self, in1, in2, in3, in4):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3
        self.in4_ = in4

    def getCircuitOutput(self):
        andg0 = andgate3(self.in1_, self.in2_, self.in3_)
        out_andg0 = andg0.getCircuitOutput()

        andg1 = andgate(out_andg0, self.in4_)
        out_andg1 = andg1.getCircuitOutput()

        return out_andg1

class andgate6(circuit):            # 6to1 AND gate implemented with 2x 3to1 AND gates & 1 2to1 AND gate
    def __init__(self, in1, in2, in3, in4, in5, in6):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3
        self.in4_ = in4
        self.in5_ = in5
        self.in6_ = in6

    def getCircuitOutput(self):
        andg0 = andgate3(self.in1_, self.in2_, self.in3_)
        out_andg0 = andg0.getCircuitOutput()

        andg1 = andgate3(self.in4_, self.in5_, self.in6_)
        out_andg1 = andg1.getCircuitOutput()

        and_result = andgate(out_andg0, out_andg1)
        out_and_result = and_result.getCircuitOutput()

        return out_and_result

class mux_2to1(circuit):            # 2to1 MUX implemented with NOT gate, AND gates and OR gates
    def __init__(self, in1, in2, inS):
        self.in1_ = in1
        self.in2_ = in2
        self.inS_ = inS

    def getCircuitOutput(self):
        notg0 = notgate(self.inS_)
        out_notg0 = notg0.getCircuitOutput()

        andg0 = andgate(out_notg0, self.in1_)
        out_andg0 = andg0.getCircuitOutput()

        andg1 = andgate(self.in2_, self.inS_)
        out_andg1 = andg1.getCircuitOutput()

        org0 = orgate(out_andg0, out_andg1)
        out_org0 = org0.getCircuitOutput()

        return out_org0

class mux_4to1(circuit):            # 4to1 MUX implemented by 2to1 MUXes
    def __init__(self, in1, in2, in3, in4, inS0, inS1):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3
        self.in4_ = in4
        self.inS0_ = inS0
        self.inS1_ = inS1

    # 3 multiplexers used. First two get same control signal S0, last gets S1.
    def getCircuitOutput(self):
        mux0 = mux_2to1(self.in1_, self.in2_, self.inS0_)
        out_mux0 = mux0.getCircuitOutput()

        mux1 = mux_2to1(self.in3_, self.in4_, self.inS0_)
        out_mux1 = mux1.getCircuitOutput()

        mux3 = mux_2to1(out_mux0, out_mux1, self.inS1_)
        out_mux3 = mux3.getCircuitOutput()

        return out_mux3

class fulladder(circuit):           # fulladder implemented with logic gates
    def __init__(self, in1, in2, in3):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3

    def getCout(self):              # Carry-Out portion of adder
        cout1 = andgate(self.in1_, self.in2_)
        out_cout1 = cout1.getCircuitOutput()

        cout2 = andgate(self.in1_, self.in3_)
        out_cout2 = cout2.getCircuitOutput()

        cout3 = andgate(self.in2_, self.in3_)
        out_cout3 = cout3.getCircuitOutput()

        cout_OR = orgate3(out_cout1, out_cout2, out_cout3)
        out_cout_OR = cout_OR.getCircuitOutput()

        return out_cout_OR

    def getSum(self):               # Sum portion of adder
        andg0 = andgate3(notgate(self.in1_).getCircuitOutput(), notgate(self.in2_).getCircuitOutput(), self.in3_) 
        out_andg0 = andg0.getCircuitOutput()

        andg1 = andgate3(notgate(self.in1_).getCircuitOutput(), self.in2_, notgate(self.in3_).getCircuitOutput())
        out_andg1 = andg1.getCircuitOutput()

        andg2 = andgate3(self.in1_, notgate(self.in2_).getCircuitOutput(), notgate(self.in3_).getCircuitOutput())
        out_andg2 = andg2.getCircuitOutput()

        andg3 = andgate3(self.in1_, self.in2_, self.in3_)
        out_andg3 = andg3.getCircuitOutput()

        sum_OR = orgate4(out_andg0, out_andg1, out_andg2, out_andg3)
        out_sum_OR = sum_OR.getCircuitOutput()

        return out_sum_OR

class ALU_1bit(object):             # 1-bit ALU implemented with logic gates

    def __init__(self, a_vert, b_vert, in0, in1, cin, op0, op1):
        self.a_vert = a_vert
        self.b_vert = b_vert
        self.in0 = in0
        self.in1 = in1
        self.cin = cin
        self.op0 = op0
        self.op1 = op1
        self.less = 0

    # --------Inverters----------
    def a_mux(self):
        notg0 = notgate(self.in0)
        out_notg0 = notg0.getCircuitOutput()

        mux0 = mux_2to1(self.in0, out_notg0, self.a_vert)
        output_mux0 = mux0.getCircuitOutput()
        return output_mux0

    def b_mux(self):
        notg1 = notgate(self.in1)
        out_notg1 = notg1.getCircuitOutput()

        mux1 = mux_2to1(self.in1, out_notg1, self.b_vert)
        output_mux1 = mux1.getCircuitOutput()
        return output_mux1

    # --------- AND Operation-----
    def getAND(self):
        and0 = andgate(self.a_mux(), self.b_mux())
        out_and0 = and0.getCircuitOutput()

        return out_and0

    # ------- OR Operation--------
    def getOR(self):
        or0 = orgate(self.a_mux(), self.b_mux())
        out_or0 = or0.getCircuitOutput()

        return out_or0

    # ------ADDER Operations-------
    def getSum(self):
        sum0 = fulladder(self.a_mux(), self.b_mux(), self.cin)
        out_sum0 = sum0.getSum()

        return out_sum0

    def getCout(self):
        cout0 = fulladder(self.a_mux(), self.b_mux(), self.cin)
        out_cout0 = cout0.getCout()

        return out_cout0

    # ------SLT Operation----------
    def getLess(self):
        return self.less

    # Used by ALU_0 to set the Less variable equal to the sum of ALU_31
    def setLess(self, lessValue):
        self.less = lessValue

    # ------Result Multiplexer-----

    def getResult(self):
        result = mux_4to1(self.getAND(), self.getOR(), self.getSum(), self.getLess(), self.op1, self.op0).getCircuitOutput()
        return result

    # ------Overflow Detection-----

    def getOverflow(self):   # Overflow Detection
        overflow_r = fulladder(self.a_mux(), self.b_mux(), self.cin).getSum()
        overflow_not_r = notgate(overflow_r).getCircuitOutput()
        overflow_not_in0 = notgate(self.a_mux()).getCircuitOutput()
        overflow_not_in1 = notgate(self.b_mux()).getCircuitOutput()

        overflow0 = andgate3(self.a_mux(), self.b_mux(), overflow_not_r)
        out_overflow0 = overflow0.getCircuitOutput()

        overflow1 = andgate3(overflow_not_in0, overflow_not_in1, overflow_r)
        out_overflow1 = overflow1.getCircuitOutput()

        overflow_or = orgate(out_overflow0, out_overflow1)
        out_overflow_or = overflow_or.getCircuitOutput()

        return out_overflow_or

#===========================32-Bit ALU=================================
class ALU_32bit(object):
    def __init__(self, a_vert, b_vert, in0, in1, init_cin, op1, op0):
        self.a_vert = a_vert
        self.b_vert = b_vert
        self.in0 = in0
        self.in1 = in1
        self.init_cin = init_cin
        self.op0 = op0
        self.op1 = op1

    def getCircuitOutput(self):
        ALU_0 = ALU_1bit(self.a_vert, self.b_vert, self.in0[31], self.in1[31], self.init_cin, self.op1, self.op0)

        ALU_1 = ALU_1bit(self.a_vert, self.b_vert, self.in0[30], self.in1[30], ALU_0.getCout(), self.op1, self.op0)

        ALU_2 = ALU_1bit(self.a_vert, self.b_vert, self.in0[29], self.in1[29], ALU_1.getCout(), self.op1, self.op0)

        ALU_3 = ALU_1bit(self.a_vert, self.b_vert, self.in0[28], self.in1[28], ALU_2.getCout(), self.op1, self.op0)

        ALU_4 = ALU_1bit(self.a_vert, self.b_vert, self.in0[27], self.in1[27], ALU_3.getCout(), self.op1, self.op0)

        ALU_5 = ALU_1bit(self.a_vert, self.b_vert, self.in0[26], self.in1[26], ALU_4.getCout(), self.op1, self.op0)

        ALU_6 = ALU_1bit(self.a_vert, self.b_vert, self.in0[25], self.in1[25], ALU_5.getCout(), self.op1, self.op0)

        ALU_7 = ALU_1bit(self.a_vert, self.b_vert, self.in0[24], self.in1[24], ALU_6.getCout(), self.op1, self.op0)

        ALU_8 = ALU_1bit(self.a_vert, self.b_vert, self.in0[23], self.in1[23], ALU_7.getCout(), self.op1, self.op0)

        ALU_9 = ALU_1bit(self.a_vert, self.b_vert, self.in0[22], self.in1[22], ALU_8.getCout(), self.op1, self.op0)

        ALU_10 = ALU_1bit(self.a_vert, self.b_vert, self.in0[21], self.in1[21], ALU_9.getCout(), self.op1, self.op0)

        ALU_11 = ALU_1bit(self.a_vert, self.b_vert, self.in0[20], self.in1[20], ALU_10.getCout(), self.op1, self.op0)

        ALU_12 = ALU_1bit(self.a_vert, self.b_vert, self.in0[19], self.in1[19], ALU_11.getCout(), self.op1, self.op0)

        ALU_13 = ALU_1bit(self.a_vert, self.b_vert, self.in0[18], self.in1[18], ALU_12.getCout(), self.op1, self.op0)

        ALU_14 = ALU_1bit(self.a_vert, self.b_vert, self.in0[17], self.in1[17], ALU_13.getCout(), self.op1, self.op0)

        ALU_15 = ALU_1bit(self.a_vert, self.b_vert, self.in0[16], self.in1[16], ALU_14.getCout(), self.op1, self.op0)

        ALU_16 = ALU_1bit(self.a_vert, self.b_vert, self.in0[15], self.in1[15], ALU_15.getCout(), self.op1, self.op0)

        ALU_17 = ALU_1bit(self.a_vert, self.b_vert, self.in0[14], self.in1[14], ALU_16.getCout(), self.op1, self.op0)

        ALU_18 = ALU_1bit(self.a_vert, self.b_vert, self.in0[13], self.in1[13], ALU_17.getCout(), self.op1, self.op0)

        ALU_19 = ALU_1bit(self.a_vert, self.b_vert, self.in0[12], self.in1[12], ALU_18.getCout(), self.op1, self.op0)

        ALU_20 = ALU_1bit(self.a_vert, self.b_vert, self.in0[11], self.in1[11], ALU_19.getCout(), self.op1, self.op0)

        ALU_21 = ALU_1bit(self.a_vert, self.b_vert, self.in0[10], self.in1[10], ALU_20.getCout(), self.op1, self.op0)

        ALU_22 = ALU_1bit(self.a_vert, self.b_vert, self.in0[9], self.in1[9], ALU_21.getCout(), self.op1, self.op0)

        ALU_23 = ALU_1bit(self.a_vert, self.b_vert, self.in0[8], self.in1[8], ALU_22.getCout(), self.op1, self.op0)

        ALU_24 = ALU_1bit(self.a_vert, self.b_vert, self.in0[7], self.in1[7], ALU_23.getCout(), self.op1, self.op0)

        ALU_25 = ALU_1bit(self.a_vert, self.b_vert, self.in0[6], self.in1[6], ALU_24.getCout(), self.op1, self.op0)

        ALU_26 = ALU_1bit(self.a_vert, self.b_vert, self.in0[5], self.in1[5], ALU_25.getCout(), self.op1, self.op0)

        ALU_27 = ALU_1bit(self.a_vert, self.b_vert, self.in0[4], self.in1[4], ALU_26.getCout(), self.op1, self.op0)

        ALU_28 = ALU_1bit(self.a_vert, self.b_vert, self.in0[3], self.in1[3], ALU_27.getCout(), self.op1, self.op0)

        ALU_29 = ALU_1bit(self.a_vert, self.b_vert, self.in0[2], self.in1[2], ALU_28.getCout(), self.op1, self.op0)

        ALU_30 = ALU_1bit(self.a_vert, self.b_vert, self.in0[1], self.in1[1], ALU_29.getCout(), self.op1, self.op0)

        ALU_31 = ALU_1bit(self.a_vert, self.b_vert, self.in0[0], self.in1[0], ALU_30.getCout(), self.op1, self.op0)

        # Assign less than value for ALU_0
        ALU_0.setLess(ALU_31.getSum())

        ALU_32bit_result = [
                             ALU_31.getResult(), ALU_30.getResult(), ALU_29.getResult(), ALU_28.getResult(),
                             ALU_27.getResult(),
                             ALU_26.getResult(), ALU_25.getResult(), ALU_24.getResult(), ALU_23.getResult(),
                             ALU_22.getResult(),
                             ALU_21.getResult(), ALU_20.getResult(), ALU_19.getResult(), ALU_18.getResult(),
                             ALU_17.getResult(),
                             ALU_16.getResult(), ALU_15.getResult(), ALU_14.getResult(), ALU_13.getResult(),
                             ALU_12.getResult(),
                             ALU_11.getResult(), ALU_10.getResult(), ALU_9.getResult(), ALU_8.getResult(),
                             ALU_7.getResult(),
                             ALU_6.getResult(), ALU_5.getResult(), ALU_4.getResult(), ALU_3.getResult(),
                             ALU_2.getResult(),
                             ALU_1.getResult(), ALU_0.getResult()
                           ]
        return ALU_32bit_result

# ---------------Sign-Extended Operation-----------------------------------
class signExt(circuit):
    def __init__(self, instru):
        self.sign = instru[16]
        self.bit14 = instru[17]
        self.bit13 = instru[18]
        self.bit12 = instru[19]
        self.bit11 = instru[20]
        self.bit10 = instru[21]
        self.bit9 = instru[22]
        self.bit8 = instru[23]
        self.bit7 = instru[24]
        self.bit6 = instru[25]
        self.bit5 = instru[26]
        self.bit4 = instru[27]
        self.bit3 = instru[28]
        self.bit2 = instru[29]
        self.bit1 = instru[30]
        self.bit0 = instru[31]

    def getSignExtend(self):
        extended = [self.sign, self.sign, self.sign, self.sign, self.sign, self.sign, self.sign, self.sign,
                    self.sign, self.sign, self.sign, self.sign, self.sign, self.sign, self.sign, self.sign,
                    self.sign, self.bit14, self.bit13, self.bit12, self.bit11, self.bit10, self.bit9,
                    self.bit8, self.bit7, self.bit6, self.bit5, self.bit4, self.bit3, self.bit2,
                    self.bit1, self.bit0]
        return extended

#==================ALU Control =============================================
class aluControl(circuit):

    def __init__(self, aluOp2, aluOp1, fCode):
        self.aluOp1 = aluOp1
        self.aluOp2 = aluOp2
        self.f5 = fCode[26]
        self.f4 = fCode[27]
        self.f3 = fCode[28]
        self.f2 = fCode[29]
        self.f1 = fCode[30]
        self.f0 = fCode[31]
        self.aluResult = [0, 0, 0, 0]

    def getCircuitOutput(self):
        # operation0
        andg0a = andgate(self.aluOp2, orgate(self.f0, self.f3).getCircuitOutput() )
        out_andg0a = andg0a.getCircuitOutput()
        andg0b = andgate(out_andg0a, notgate(andgate4(notgate(self.f3).getCircuitOutput(), self.f2, self.f1, self.f0).getCircuitOutput() ).getCircuitOutput() ) 
        out_andg0 = andg0b.getCircuitOutput()

        # operation1
        org0 = orgate(notgate(self.aluOp2).getCircuitOutput(), notgate(self.f2).getCircuitOutput())
        out_org0 = org0.getCircuitOutput()

        # operation2
        org1 = orgate(self.aluOp1, andgate(self.aluOp2, self.f1).getCircuitOutput())
        out_org1 = org1.getCircuitOutput()

        # operation3
        andg1 = andgate4(notgate(self.f3).getCircuitOutput(), self.f2, self.f1, self.f0 ) 
        out_andg1 = andg1.getCircuitOutput()

        self.aluResult = [out_andg1, out_org1, out_org0, out_andg0]  #[a_invert, b_invert, ALU_OP1, ALU_OP0]

        return self.aluResult


    
    
#-------------Carry-In Operation--------------------------------------------    
class getCin(circuit):

    def getCircuitOutput(aluCont):
        sub_op = andgate4(notgate(aluCont[0]).getCircuitOutput(), aluCont[1], aluCont[2], notgate(aluCont[3]).getCircuitOutput() )
        sub_out = sub_op.getCircuitOutput()

        slt_op = andgate4(notgate(aluCont[0]).getCircuitOutput(), aluCont[1], aluCont[2], aluCont[3] )
        slt_out = slt_op.getCircuitOutput()

        cin_test = orgate(sub_out, slt_out)
        cin_result = cin_test.getCircuitOutput()

        return cin_result
    
# ====================Registers ===========================================
class registerFile(circuit):
    def __init__(self, initValue):
        self.reg_zero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.reg_at = initValue
        self.reg_v0 = initValue
        self.reg_v1 = initValue
        self.reg_a0 = initValue
        self.reg_a1 = initValue
        self.reg_a2 = initValue
        self.reg_a3 = initValue
        self.reg_t0 = initValue
        self.reg_t1 = initValue
        self.reg_t2 = initValue
        self.reg_t3 = initValue
        self.reg_t4 = initValue
        self.reg_t5 = initValue
        self.reg_t6 = initValue
        self.reg_t7 = initValue
        self.reg_s0 = initValue
        self.reg_s1 = initValue
        self.reg_s2 = initValue
        self.reg_s3 = initValue
        self.reg_s4 = initValue
        self.reg_s5 = initValue
        self.reg_s6 = initValue
        self.reg_s7 = initValue
        self.reg_t8 = initValue
        self.reg_t9 = initValue
        self.reg_k0 = initValue
        self.reg_k1 = initValue
        self.reg_gp = initValue
        self.reg_sp = initValue
        self.reg_fp = initValue
        self.reg_ra = initValue
        
        self.registers = [self.reg_ra, self.reg_fp, self.reg_sp, self.reg_gp, self.reg_k1, self.reg_k0, self.reg_t9,
                          self.reg_t8,
                          self.reg_s7, self.reg_s6, self.reg_s5, self.reg_s4, self.reg_s3, self.reg_s2, self.reg_s1,
                          self.reg_s0,
                          self.reg_t7, self.reg_t6, self.reg_t5, self.reg_t4, self.reg_t3, self.reg_t2, self.reg_t1,
                          self.reg_t0,
                          self.reg_a3, self.reg_a2, self.reg_a1, self.reg_a0, self.reg_v1, self.reg_v0, self.reg_at,
                          self.reg_zero
                         ]

    def setRegValue(self, o_regDecoder, valueToSet): #Stores a 32-bit value in a register

        i = 31
        x = o_regDecoder[i]
        if x == 1:
            return #Prevents overwriting register zero

        else:
            while (x != 1 and i > -1):
                x = o_regDecoder[i]
                if x == 1:
                    self.registers[i] = valueToSet
                    break
                else:
                    i -= 1
            else:
                print("Register Not Found")


    def getRegValue(self, o_regDecoder):        #Returns a 32-bit value that was stored in a register

        i = 31
        x = o_regDecoder[i]
        if x == 1:
            return self.registers[i]

        else:
            while (x != 1 and i > -1):
                x = o_regDecoder[i]
                if x == 1:
                    return self.registers[i]
                else:
                    i -= 1
                    '''
            else:
                print("Register Not Found")
                    '''
                    
    def getAllRegValues(self):          #Returns all of the 32-bit values that are stored in the registers

        all_registers = self.registers

        return all_registers

#--------------Register Decoder-----------------------
    
class decoder_3to8(circuit):
    def __init__(self, in2, in1, in0, control):
        self.in0 = in0
        self.in1 = in1
        self.in2 = in2
        self.control = control

    def getCircuitOutput(self):
        # Not Gates
        in0_not = notgate(self.in0).getCircuitOutput()
        in1_not = notgate(self.in1).getCircuitOutput()
        in2_not = notgate(self.in2).getCircuitOutput()

        andg0 = andgate4(in0_not, in1_not, in2_not, self.control).getCircuitOutput()
        andg1 = andgate4(in0_not, in1_not, self.in2, self.control).getCircuitOutput()
        andg2 = andgate4(in0_not, self.in1, in2_not, self.control).getCircuitOutput()
        andg3 = andgate4(in0_not, self.in1, self.in2, self.control).getCircuitOutput()
        andg4 = andgate4(self.in0, in1_not, in2_not, self.control).getCircuitOutput()
        andg5 = andgate4(self.in0, in1_not, self.in2, self.control).getCircuitOutput()
        andg6 = andgate4(self.in0, self.in1, in2_not, self.control).getCircuitOutput()
        andg7 = andgate4(self.in0, self.in1, self.in2, self.control).getCircuitOutput()

        return [andg7, andg6, andg5, andg4, andg3, andg2, andg1, andg0]


class decoder_2to4(circuit):
    def __init__(self, in1, in0):
        self.in0 = in0
        self.in1 = in1

    def getCircuitOutput(self):
        andgate0 = andgate(notgate(self.in1).getCircuitOutput(),
                           notgate(self.in0).getCircuitOutput()).getCircuitOutput()
        andgate1 = andgate(self.in1, notgate(self.in0).getCircuitOutput()).getCircuitOutput()
        andgate2 = andgate(notgate(self.in1).getCircuitOutput(), self.in0).getCircuitOutput()
        andgate3 = andgate(self.in1, self.in0).getCircuitOutput()

        AndValues = [andgate3, andgate2, andgate1, andgate0]

        return AndValues


class decoderReg(circuit):
    def __init__(self, regIns1, regIns2, regIns3, regIns4, regIns5):
        self.in4 = regIns1
        self.in3 = regIns2
        self.in2 = regIns3
        self.in1 = regIns4
        self.in0 = regIns5

    def getCircuitOutput(self):
        decoder2to4 = decoder_2to4(self.in3, self.in4).getCircuitOutput()
        decoder3 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[0]).getCircuitOutput()
        decoder2 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[1]).getCircuitOutput()
        decoder1 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[2]).getCircuitOutput()
        decoder0 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[3]).getCircuitOutput()

        return decoder3 + decoder2 + decoder1 + decoder0

class decoderReg(circuit):          #5 to 32 register decoder implemented with 2 to 4 decoder and 3 to 8 decoders
    def __init__(self, regIns1, regIns2, regIns3, regIns4, regIns5):
        self.in4 = regIns1
        self.in3 = regIns2
        self.in2 = regIns3
        self.in1 = regIns4
        self.in0 = regIns5

    def getCircuitOutput(self):
        decoder2to4 = decoder_2to4(self.in3, self.in4).getCircuitOutput()
        decoder3 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[0]).getCircuitOutput()
        decoder2 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[1]).getCircuitOutput()
        decoder1 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[2]).getCircuitOutput()
        decoder0 = decoder_3to8(self.in0, self.in1, self.in2, decoder2to4[3]).getCircuitOutput()

        return decoder3 + decoder2 + decoder1 + decoder0

#============Main Control Module ============================================
class mainCtrl(object):
    def __init__(self, opCode):
        self.op0 = opCode[0]
        self.op1 = opCode[1]
        self.op2 = opCode[2]
        self.op3 = opCode[3]
        self.op4 = opCode[4]
        self.op5 = opCode[5]

        self.not0 = notgate(self.op0).getCircuitOutput()
        self.not1 = notgate(self.op1).getCircuitOutput()
        self.not2 = notgate(self.op2).getCircuitOutput()
        self.not3 = notgate(self.op3).getCircuitOutput()
        self.not4 = notgate(self.op4).getCircuitOutput()
        self.not5 = notgate(self.op5).getCircuitOutput()

        self.opCode = opCode

#----------------------- MainControl Operations-----------------------------------
     
    def getR_Format(self):          #R_Format Operations(RegDst, RegWrite, ALU_Op1)
        and0 = andgate6(self.not0, self.not1, self.not2, self.not3, self.not4, self.not5)
        out_and0 = and0.getCircuitOutput()

        return out_and0

    def getLW(self):                #LW Operations(ALUSrc, MemtoReg, RegWrite, MemRead)
        and1 = andgate6(self.op0, self.not1, self.not2, self.not3, self.op4, self.op5)
        out_and1 = and1.getCircuitOutput()

        return out_and1

    def getSW(self):                #SW Operations(ALUSrc, MemWrite)
        and2 = andgate6(self.op0, self.not1, self.op2, self.not3, self.op4, self.op5)
        out_and2 = and2.getCircuitOutput()

        return out_and2

    def getBEQ(self):               #BEQ Operations(Branch & ALU_Op0)
        and3 = andgate6(self.not0, self.not1, self.not2, self.op3, self.not4, self.not5)
        out_and3 = and3.getCircuitOutput()

        return out_and3

#------------------ MainCtrol Outputs---------------------------------------
    def getReg_Dst(self, mainOut):          #Reg_Dst Output
        return mainOut.getR_Format()

    def getALU_Src(self, mainOut):          #ALU_Src Output
        or0 = orgate(mainOut.getLW(), mainOut.getSW())
        ALU_Src = or0.getCircuitOutput()

        return ALU_Src

    def getReg_Write(self, mainOut):        #Reg_Write Output
        or1 = orgate(mainOut.getR_Format(), mainOut.getLW())
        Reg_Write = or1.getCircuitOutput()

        return Reg_Write

    def getALU_OP(self, mainOut):           #ALU_Op1 & ALU_Op0 Output
        return aluControl(mainOut.getR_Format(), mainOut.getBEQ(), self.opCode)  

    '''===========================Simple MIPS============================='''
class simpleMIPS(circuit):
    def __init__(self, regValue):       #Initialize Registers
        
        self.registers = registerFile(regValue)

    def getCircuitOutput(self, instru):         # Input 32-bit instructions as a single array/list

        main = mainCtrl(instru)                             #Creates MainCtrl Object
        
        aluOp = main.getALU_OP(main).getCircuitOutput()     #Retrieves [ainv, binv, op1, op0]
        
        cin = getCin.getCircuitOutput(aluOp)                #Retreives Carry-In Value
    
        Reg1 = self.registers.getRegValue( decoderReg(instru[6], instru[7], instru[8],          #Retrieves the location of the first input register
                          instru[9], instru[10]).getCircuitOutput() ) 
        
        Reg2 = self.registers.getRegValue( decoderReg(instru[11], instru[12], instru[13],       #Retrieves the location of the second input register
                          instru[14], instru[15]).getCircuitOutput() )

    
        rt = [instru[11], instru[12], instru[13], instru[14], instru[15] ]      #MUX that is used to determine the destination register that is written to
        rd = [instru[16], instru[17], instru[18], instru[19], instru[20] ]      #    while loop is used to process 32-bit value
        writeReg = [0,0,0,0,0]
        i = 0
        while i < len(writeReg):
            writeReg[i] = mux_2to1(rt[i], rd[i], main.getReg_Dst(main) ).getCircuitOutput()
            i += 1

        extended = signExt(instru).getSignExtend()              #Retrieves the sign-extended value
        
        in2 = [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,1 ] # <- random value used to create a 32-bit array
        j = 0
        while j < len(in2):                                                                           #MUX that is used to determine the second input for the ALU
            in2[j] = mux_2to1(Reg2[j], extended[j], main.getALU_Src(main) ).getCircuitOutput()    #   while loop is used to process 32-bit value
            j += 1
        
     
        alu = ALU_32bit(aluOp[0], aluOp[1], Reg1, in2, cin, aluOp[2], aluOp[3])

        writeData = alu.getCircuitOutput()      #Stores the output of the ALU

        if main.getReg_Write(main) == 1:        #Determines if the ALU output should be stored in the destination register
            self.registers.setRegValue(decoderReg(writeReg[0], writeReg[1], writeReg[2], writeReg[3], writeReg[4]).getCircuitOutput(), writeData )

        ''' 
        out2 = "After Instruction: {}"  
        out3 = "Register {0} :  {1} " 
        print(out2.format(instru) ) 
        print("Registers Store: ")
        r = self.registers.getAllRegValues()
        k = 31
        for x in r:                             #for loop that prints the contents of the registers
            print(out3.format(k, x) ) 
            k -= 1
        print( " ")
        '''
        
