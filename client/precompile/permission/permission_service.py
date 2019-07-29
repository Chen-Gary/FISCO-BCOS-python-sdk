'''
  bcosliteclientpy is a python client for FISCO BCOS2.0 (https://github.com/FISCO-BCOS/)
  bcosliteclientpy is free software: you can redistribute it and/or modify it under the
  terms of the MIT License as published by the Free Software Foundation. This project is
  distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
  the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Thanks for
  authors and contributors of eth-abi, eth-account, eth-hash，eth-keys, eth-typing, eth-utils,
  rlp, eth-rlp , hexbytes ... and relative projects
  @file: permission_service.py
  @function:
  @author: yujiechen
  @date: 2019-07
'''
from client.common import transaction_common
from client.precompile.crud.crud_service import CRUDService
from client.precompile.crud.crud_service import PrecompileGlobalConfig


class PermissionService:
    """
    implementation of PermissionService
    """

    def __init__(self, contract_path):
        """
        init the address and contract path for PermissionService
        """
        self.permission_address = "0x0000000000000000000000000000000000001005"
        self.contract_path = contract_path
        self.client = transaction_common.TransactionCommon(
            self.permission_abi, contract_path, "permission")

    def __del__(self):
        """
        finish the client
        """
        self.client.finish()

    def grant(self, table_name, account_address):
        """
        grant write permission of table_name to account_address
        related api:
        function insert(string table_name, string addr) public returns(int256);
        """
        fn_name = "insert"
        fn_args = [table_name, account_address]
        return self.client.send_transaction_getReceipt(fn_name, fn_args)

    def revoke(self, table_name, account_address):
        """
        revoke write permission to table_name from account_address
        related api:
        function remove(string table_name, string addr) public returns(int256);
        """
        fn_name = "remove"
        fn_args = [table_name, account_address]
        return self.client.send_transaction_getReceipt(fn_name, fn_args)

    def list_permission(self, table_name):
        """
        list write-permitted accounts to table_name
        related api:
        function queryByName(string table_name) public constant returns(string);
        """
        fn_name = "queryByName"
        fn_args = [table_name]
        return self.client.call_and_decode(fn_name, fn_args)

    def grantUserTableManager(self, table_name, account_address):
        """
        """
        crud_service = CRUDService(self.contract_path)
        crud_service.desc(table_name)
        return self.grant(table_name, account_address)

    def revokeUserTableManager(self, table_name, account_address):
        """
        """
        return self.revoke(table_name, account_address)

    def listUserTableManager(self, table_name):
        return self.list_permission(table_name)

    def grantDeployAndCreateManager(self, account_address):
        return self.grant(PrecompileGlobalConfig.SYS_TABLE, account_address)

    def revokeDeployAndCreateManager(self, account_addr):
        return self.revoke(PrecompileGlobalConfig.SYS_TABLE, account_addr)

    def listDeployAndCreateManager(self):
        return self.list_permission(PrecompileGlobalConfig.SYS_TABLE)

    def grantPermissionManager(self, account_addr):
        return self.grant(PrecompileGlobalConfig.SYS_TABLE_ACCESS, account_addr)

    def revokePermissionManager(self, account_addr):
        return self.revoke(PrecompileGlobalConfig.SYS_TABLE_ACCESS, account_addr)

    def listPermissionManager(self):
        return self.list_permission(PrecompileGlobalConfig.SYS_TABLE_ACCESS)

    def grantNodeManager(self, account_addr):
        return self.grant(PrecompileGlobalConfig.SYS_CONSENSUS, account_addr)

    def revokeNodeManager(self, account_addr):
        return self.revoke(PrecompileGlobalConfig.SYS_CONSENSUS, account_addr)

    def listNodeManager(self):
        return self.list_permission(PrecompileGlobalConfig.SYS_CONSENSUS)

    def grantCNSManager(self, account_addr):
        return self.grant(PrecompileGlobalConfig.SYS_CNS, account_addr)

    def revokeCNSManager(self, account_addr):
        return self.revoke(PrecompileGlobalConfig.SYS_CNS, account_addr)

    def listCNSManager(self):
        return self.list_permission(PrecompileGlobalConfig.SYS_CNS)

    def grantSysConfigManager(self, account_addr):
        return self.grant(PrecompileGlobalConfig.SYS_CONFIG, account_addr)

    def revokeSysConfigManager(self, account_addr):
        return self.revoke(PrecompileGlobalConfig.SYS_CONFIG, account_addr)

    def listSysConfigManager(self):
        return self.list_permission(PrecompileGlobalConfig.SYS_CONFIG)
