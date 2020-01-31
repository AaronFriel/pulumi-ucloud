# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class LookupLbsResult:
    """
    A collection of values returned by lookupLbs.
    """
    def __init__(__self__, ids=None, lbs=None, name_regex=None, output_file=None, subnet_id=None, total_count=None, vpc_id=None, id=None):
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        if lbs and not isinstance(lbs, list):
            raise TypeError("Expected argument 'lbs' to be a list")
        __self__.lbs = lbs
        """
        It is a nested type which documented below.
        """
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        __self__.output_file = output_file
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        __self__.subnet_id = subnet_id
        """
        (Optional) The ID of subnet that intrant load balancer belongs to. 
        """
        if total_count and not isinstance(total_count, float):
            raise TypeError("Expected argument 'total_count' to be a float")
        __self__.total_count = total_count
        """
        Total number of Load Balancers that satisfy the condition.
        """
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id
        """
        The ID of the VPC linked to the Load Balancers.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableLookupLbsResult(LookupLbsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return LookupLbsResult(
            ids=self.ids,
            lbs=self.lbs,
            name_regex=self.name_regex,
            output_file=self.output_file,
            subnet_id=self.subnet_id,
            total_count=self.total_count,
            vpc_id=self.vpc_id,
            id=self.id)

def lookup_lbs(ids=None,name_regex=None,output_file=None,subnet_id=None,vpc_id=None,opts=None):
    """
    This data source provides a list of Load Balancer resources according to their Load Balancer ID, VPC ID and Subnet ID.
    
    :param list ids: A list of Load Balancer IDs, all the LBs belong to this region will be retrieved if the ID is `""`.
    :param str name_regex: A regex string to filter resulting lbs by name.
    :param str subnet_id: The ID of subnet that intrant load balancer belongs to.
    :param str vpc_id: The ID of the VPC linked to the Load Balancers.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/d/lbs.html.markdown.
    """
    __args__ = dict()

    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['subnetId'] = subnet_id
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('ucloud:ulb/lookupLbs:lookupLbs', __args__, opts=opts).value

    return AwaitableLookupLbsResult(
        ids=__ret__.get('ids'),
        lbs=__ret__.get('lbs'),
        name_regex=__ret__.get('nameRegex'),
        output_file=__ret__.get('outputFile'),
        subnet_id=__ret__.get('subnetId'),
        total_count=__ret__.get('totalCount'),
        vpc_id=__ret__.get('vpcId'),
        id=__ret__.get('id'))
