#!/usr/bin/env python
# -*- coding: utf-8 -*-


from client.contractnote import ContractNote
#from client.bcosclient import BcosClient
from client.bcosclienteth import BcosClientEth
import os
from eth_utils import to_checksum_address
from client.datatype_parser import DatatypeParser
from client.common.compiler import Compiler
from client.bcoserror import BcosException, BcosError
from client_config import client_config
import sys
import traceback


# 接口：私钥签名交易demo
def HelloWorld_set(privateKey, newStr):
    try:
        # 使用私钥初始化client
        client = BcosClientEth(privateKey)

        # 签名交易
        args = [newStr]
        receipt = client.sendRawTransactionGetReceipt(to_address, contract_abi, "set", args)
        print("receipt:", receipt)

    except BcosException as e:
        print("execute demo_transaction failed ,BcosException for: {}".format(e))
        traceback.print_exc()
    except BcosError as e:
        print("execute demo_transaction failed ,BcosError for: {}".format(e))
        traceback.print_exc()
    except Exception as e:
        client.finish()
        traceback.print_exc()
    client.finish()


# 接口：从区块链上读数据（无需私钥）
def HelloWorld_get():
    try:
        # 初始化client (不使用私钥)
        client = BcosClientEth(dummy_privateKey)

        # 读数据
        res = client.call(to_address, contract_abi, "get")
        print("call getbalance result:", res)

    except BcosException as e:
        print("execute demo_transaction failed ,BcosException for: {}".format(e))
        traceback.print_exc()
    except BcosError as e:
        print("execute demo_transaction failed ,BcosError for: {}".format(e))
        traceback.print_exc()
    except Exception as e:
        client.finish()
        traceback.print_exc()
    client.finish()



# 测试函数
def demo():
    # 初始化以太坊钱包（以下公私钥由Metamask生成）
    #address:     0x820f3E244D73c5bF5c92A34Cc0B56E5912129f55
    #privateKey:  0x3e14b5b682d9768a1e37a39a6510e51b813b071c05c33b378157fbbb10c3a7ae
    user_privateKey = "0x3e14b5b682d9768a1e37a39a6510e51b813b071c05c33b378157fbbb10c3a7ae"

    print("================================================================")
    print("================== HelloWorld_get ==============================")
    HelloWorld_get()
    print("================== HelloWorld_set ==============================")
    HelloWorld_set(user_privateKey, "你好世界，测试字符串，随便换着输点啥")
    print("================== HelloWorld_get ==============================")
    HelloWorld_get()
    print("================================================================")




# 运行入口

# 声明全局变量: contract_abi, to_address, dummy_privateKey
# 加载合约ABI (这样python才能知道要如何与合约进行交互)
abi_file = "contracts/HelloWorld.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi                    #全局变量，在接口中被使用
to_address = "0x60b364cab35c19678c6fa3d4a6cdf705a2adea89"  #全局变量，在接口中被使用 (合约地址)
dummy_privateKey = "0x3c8ebf53a8b84f06a09f0207a314f5aed3d5a123c1539d3485f0afd7b36c77f6"  #全局变量，从区块链上读数据实际不需要私钥签名，但由于sdk限制，在此设定一个无用的私钥用于初始化client("address":"0xab5159fa9222e4787e53fb67394bf65c23d88ac9")

demo()
