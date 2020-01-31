// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function lookupVpcs(args?: LookupVpcsArgs, opts?: pulumi.InvokeOptions): Promise<LookupVpcsResult> & LookupVpcsResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<LookupVpcsResult> = pulumi.runtime.invoke("ucloud:vpc/lookupVpcs:lookupVpcs", {
        "ids": args.ids,
        "nameRegex": args.nameRegex,
        "outputFile": args.outputFile,
        "tag": args.tag,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking lookupVpcs.
 */
export interface LookupVpcsArgs {
    readonly ids?: string[];
    readonly nameRegex?: string;
    readonly outputFile?: string;
    readonly tag?: string;
}

/**
 * A collection of values returned by lookupVpcs.
 */
export interface LookupVpcsResult {
    readonly ids?: string[];
    readonly nameRegex?: string;
    readonly outputFile?: string;
    readonly tag?: string;
    readonly totalCount: number;
    readonly vpcs: outputs.vpc.LookupVpcsVpc[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
