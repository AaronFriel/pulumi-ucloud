// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package uhost

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This data source providers a list of available image resources according to their availability zone, image ID and other fields.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-ucloud/blob/master/website/docs/d/images.html.markdown.
func LookupImages(ctx *pulumi.Context, args *LookupImagesArgs) (*LookupImagesResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["availabilityZone"] = args.AvailabilityZone
		inputs["imageId"] = args.ImageId
		inputs["imageType"] = args.ImageType
		inputs["mostRecent"] = args.MostRecent
		inputs["nameRegex"] = args.NameRegex
		inputs["osType"] = args.OsType
		inputs["outputFile"] = args.OutputFile
	}
	outputs, err := ctx.Invoke("ucloud:uhost/lookupImages:lookupImages", inputs)
	if err != nil {
		return nil, err
	}
	return &LookupImagesResult{
		AvailabilityZone: outputs["availabilityZone"],
		ImageId:          outputs["imageId"],
		ImageType:        outputs["imageType"],
		Images:           outputs["images"],
		MostRecent:       outputs["mostRecent"],
		NameRegex:        outputs["nameRegex"],
		OsType:           outputs["osType"],
		OutputFile:       outputs["outputFile"],
		TotalCount:       outputs["totalCount"],
		Id:               outputs["id"],
	}, nil
}

// A collection of arguments for invoking lookupImages.
type LookupImagesArgs struct {
	// Availability zone where images are located. such as: `cn-bj2-02`. You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist).
	AvailabilityZone interface{}
	// The ID of image.
	ImageId interface{}
	// The type of image. Possible values are: `base` as standard image, `business` as owned by market place, and `custom` as custom-image, all the image types will be retrieved by default.
	ImageType interface{}
	// If more than one result is returned, use the most recent image.
	MostRecent interface{}
	// A regex string to filter resulting images by name. (Such as: `^CentOS 7.[1-2] 64` means CentOS 7.1 of 64-bit operating system or CentOS 7.2 of 64-bit operating system, "^Ubuntu 16.04 64" means Ubuntu 16.04 of 64-bit operating system).
	NameRegex interface{}
	// The type of OS. Possible values are: `linux` and `windows`, all the OS types will be retrieved by default.
	OsType     interface{}
	OutputFile interface{}
}

// A collection of values returned by lookupImages.
type LookupImagesResult struct {
	// Availability zone where image is located.
	AvailabilityZone interface{}
	ImageId          interface{}
	ImageType        interface{}
	// It is a nested type which documented below.
	Images     interface{}
	MostRecent interface{}
	NameRegex  interface{}
	// The type of OS.
	OsType     interface{}
	OutputFile interface{}
	// Total number of images that satisfy the condition.
	TotalCount interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
