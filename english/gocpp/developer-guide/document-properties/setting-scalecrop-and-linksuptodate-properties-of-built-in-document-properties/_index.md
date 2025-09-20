---
title: Setting ScaleCrop and LinksUpToDate Properties of Built-In Document Properties with Golang via C++
linktitle: Setting ScaleCrop and LinksUpToDate Properties
type: docs
weight: 320
url: /go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Learn how to set ScaleCrop and LinksUpToDate properties of built-in document properties using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) and [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) are two extended built-in document properties defined inside the OpenXml format. The purpose of these properties are as follows:

## **1) ScaleCrop**
This element indicates the display mode of the document thumbnail. Set this element to **TRUE** to enable scaling of the document thumbnail to the display. Set this element to **FALSE** to enable cropping of the document thumbnail to show only sections that fit the display.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **2) LinksUpToDate**
This element indicates whether hyperlinks in a document are up-to-date. Set this element to **TRUE** to indicate that hyperlinks are updated. Set this element to **FALSE** to indicate that hyperlinks are outdated.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **Screenshot showing these properties inside the app.xml file**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Setting ScaleCrop and LinksUpToDate Properties of Built-In Document Properties**
The following sample code sets the [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) and [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) extended built-in document properties of the workbook. Please check the [output excel file](5115500.xlsx) generated with this code, change its extension to .zip and extract its contents and view the app.xml as shown in the screenshot above.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}