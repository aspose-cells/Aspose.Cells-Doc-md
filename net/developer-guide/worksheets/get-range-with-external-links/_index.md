---
title: Get Range with External Links
type: docs
weight: 120
url: /net/get-range-with-external-links/
---

## **Get Range with External Links**

A lot of times Excel files access data from other Excel files using external links. Aspose.Cells provides the option to retrieve these external links by using the [**Name.GetReferredAreas**](https://apireference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) method. The [**Name.GetReferredAreas**](https://apireference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) method returns an array of type [**ReferredArea**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea). The [**ReferredArea**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea) class provides an [**ExternalFileName**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename) property which returns the name of the external file. The [**ReferredArea**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea) class exposes the following members.

- [**EndColumn**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): The end column of the area
- [**EndRow**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): The end row of the area
- [**ExternalFileName**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Get the external file name if this is an external reference
- [**IsArea**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indicates whether this is an area
- [**IsExternalLink**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indicates whether this is an external link
- [**SheetName**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indicates which sheet this reference is in
- [**StartColumn**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): The start column of the area
- [**StartRow**](https://apireference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): The start row of the area

The sample code given below demonstrates the use of [**Name.GetReferredAreas**](https://apireference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) method to get Ranges with external links.

## **Sample Code**

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
