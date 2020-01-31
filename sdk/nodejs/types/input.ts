// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";


export namespace udb {
}

export namespace uhost {
    export interface InstanceDiskSet {
        id?: pulumi.Input<string>;
        isBoot?: pulumi.Input<boolean>;
        size?: pulumi.Input<number>;
        type?: pulumi.Input<string>;
    }

    export interface InstanceIpSet {
        internetType?: pulumi.Input<string>;
        ip?: pulumi.Input<string>;
    }
}

export namespace ulb {
    export interface LbIpSet {
        internetType?: pulumi.Input<string>;
        ip?: pulumi.Input<string>;
    }
}

export namespace umem {
    export interface MemcacheInstanceIpSet {
        ip?: pulumi.Input<string>;
        port?: pulumi.Input<number>;
    }

    export interface RedisInstanceIpSet {
        ip?: pulumi.Input<string>;
        port?: pulumi.Input<number>;
    }
}

export namespace unet {
    export interface EipIpSet {
        internetType?: pulumi.Input<string>;
        ip?: pulumi.Input<string>;
    }

    export interface EipResource {
        id?: pulumi.Input<string>;
        type?: pulumi.Input<string>;
    }

    export interface SecurityGroupRule {
        cidrBlock?: pulumi.Input<string>;
        policy?: pulumi.Input<string>;
        portRange?: pulumi.Input<string>;
        priority?: pulumi.Input<string>;
        protocol?: pulumi.Input<string>;
    }
}

export namespace vpc {
    export interface VpcNetworkInfo {
        cidrBlock?: pulumi.Input<string>;
    }
}
