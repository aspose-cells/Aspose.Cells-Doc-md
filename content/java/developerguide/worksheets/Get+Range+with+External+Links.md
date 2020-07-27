+++
title = "Get Range with External Links" 
description = "" 
weight = 12144 
+++

Aspose.Cells for Java : Get Range with External Links  

# Aspose.Cells for Java : Get Range with External Links


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Get Range with External Links](#GetRangewithExternalLinks-GetRangewithExternalLinks)
*   2 [Sample Code](#GetRangewithExternalLinks-SampleCode)
{{< /panel >}}
 

## Get Range with External Links

A lot of times Excel files access data from other Excel files using external links. Aspose.Cells provides the option to retrieve these external links by using the [Name.GetReferredAreas](https://apireference.aspose.com/java/cells/com.aspose.cells/name#getReferredAreas(boolean)) method. The [Name.GetReferredAreas](https://apireference.aspose.com/java/cells/com.aspose.cells/name#getReferredAreas(boolean)) method returns an array of type [ReferredArea](https://apireference.aspose.com/java/cells/com.aspose.cells/ReferredArea). The [ReferredArea](https://apireference.aspose.com/java/cells/com.aspose.cells/ReferredArea)class provides an [ExternalFileName](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#ExternalFileName) property which returns the name of the external file. The [ReferredArea](https://apireference.aspose.com/java/cells/com.aspose.cells/ReferredArea)class exposes the following members.

*   [EndColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#EndColumn): The end column of the area
*   [EndRow](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#EndRow): The end row of the area
*   [ExternalFileName](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#ExternalFileName): Get the external file name if this is an external reference
*   [IsArea](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#IsArea): Indicates whether this is an area
*   [IsExternalLink](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#IsExternalLink): Indicates whether this is an external link
*   [SheetName](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#SheetName): Indicates which sheet this reference is in
*   [StartColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#StartColumn): The start column of the area
*   [StartRow](https://apireference.aspose.com/java/cells/com.aspose.cells/referredarea#StartRow): The start row of the area

The sample code given below demonstrates the use of [Name.GetReferredAreas](https://apireference.aspose.com/java/cells/com.aspose.cells/name#getReferredAreas(boolean)) method to get Ranges with external links.

## Sample Code

