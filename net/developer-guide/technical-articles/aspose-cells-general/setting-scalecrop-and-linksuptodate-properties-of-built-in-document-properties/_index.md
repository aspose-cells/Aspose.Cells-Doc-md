---
title: Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties
type: docs
weight: 320
url: /net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Possible Usage Scenarios**
[ScaleCrop](https://apireference.aspose.com/net/cells/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) and [LinksUpToDate](https://apireference.aspose.com/net/cells/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) are two extended built-in document properties defined inside the OpenXml format. The purpose of these properties are following
## **1) ScaleCrop**
This element indicates the display mode of the document thumbnail. Set this element to **TRUE** to enable scaling of the document thumbnail to the display. Set this element to **FALSE** to enable cropping of the document thumbnail to show only sections that fit the display.

The possible values for this element are defined by the W3C XML Schema boolean datatype.
## **2) LinksUpToDate**
This element indicates whether hyperlinks in a document are up-to-date. Set this element to **TRUE** to indicate that hyperlinks are updated. Set this element to **FALSE** to indicate that hyperlinks are outdated.

The possible values for this element are defined by the W3C XML Schema boolean datatype.
## **Screenshot showing these properties inside the app.xml file**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties**
The following sample code sets the [ScaleCrop](https://apireference.aspose.com/net/cells/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) and [LinksUpToDate](https://apireference.aspose.com/net/cells/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) extended built-in document properties of the workbook. Please check the [output excel file](5115500.xlsx) generated with this code, change its extension to .zip and extract its contents and view the app.xml as shown in the screenshot above.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
