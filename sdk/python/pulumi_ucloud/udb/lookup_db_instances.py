# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class LookupDbInstancesResult:
    """
    A collection of values returned by lookupDbInstances.
    """
    def __init__(__self__, availability_zone=None, db_instances=None, ids=None, name_regex=None, output_file=None, total_count=None, id=None):
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        __self__.availability_zone = availability_zone
        """
        Availability zone where database instance is located.
        """
        if db_instances and not isinstance(db_instances, list):
            raise TypeError("Expected argument 'db_instances' to be a list")
        __self__.db_instances = db_instances
        """
        It is a nested type which documented below.
        """
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        __self__.output_file = output_file
        if total_count and not isinstance(total_count, float):
            raise TypeError("Expected argument 'total_count' to be a float")
        __self__.total_count = total_count
        """
        Total number of database instances that satisfy the condition.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableLookupDbInstancesResult(LookupDbInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return LookupDbInstancesResult(
            availability_zone=self.availability_zone,
            db_instances=self.db_instances,
            ids=self.ids,
            name_regex=self.name_regex,
            output_file=self.output_file,
            total_count=self.total_count,
            id=self.id)

def lookup_db_instances(availability_zone=None,ids=None,name_regex=None,output_file=None,opts=None):
    """
    This data source provides a list of database instance resources according to their database instance ID and name.
    
    :param str availability_zone: Availability zone where database instances are located. Such as: "cn-bj2-02". You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist)
    :param list ids: A list of database instance IDs, all the database instances belong to this region will be retrieved if the ID is `""`.
    :param str name_regex: A regex string to filter resulting database instances by name.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/d/db_instances.html.markdown.
    """
    __args__ = dict()

    __args__['availabilityZone'] = availability_zone
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('ucloud:udb/lookupDbInstances:lookupDbInstances', __args__, opts=opts).value

    return AwaitableLookupDbInstancesResult(
        availability_zone=__ret__.get('availabilityZone'),
        db_instances=__ret__.get('dbInstances'),
        ids=__ret__.get('ids'),
        name_regex=__ret__.get('nameRegex'),
        output_file=__ret__.get('outputFile'),
        total_count=__ret__.get('totalCount'),
        id=__ret__.get('id'))
