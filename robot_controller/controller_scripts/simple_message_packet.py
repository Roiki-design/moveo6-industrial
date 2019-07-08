from scapy.all import*
from pprint import pprint


class simpleMessage(Packet):
    name = "joint_feedback"
    fields_desc = [ByteEnumField("length", 4),
                   ByteEnumField("message_ID", 10),
                   ByteEnumField("comm_type",0, {1:"TOPIC",2:"REQUEST",3:"RESPONSE"}),
                   ByteEnumField("reply",1 {1:"SUCCESS",2:"FAILURE"}),
                   ByteEnumField("seq_number",None),
                   FieldList("joint_data", "joint_array", None, fld=None, shift=0, length_from=None, count_from=None),
                   FieldLenField(),


                   ]
