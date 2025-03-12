---
title: Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties with Node.js via C++
linktitle: Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties
type: docs
weight: 320
url: /nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Learn how to set ScaleCrop and LinksUpToDate properties of built-in document properties using Aspose.Cells for Node.js via C++.
---

## **Possible Usage Scenarios**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) and [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) are two extended built-in document properties defined inside the OpenXml format. The purpose of these properties are following.

## **1) ScaleCrop**
This element indicates the display mode of the document thumbnail. Set this element to **TRUE** to enable scaling of the document thumbnail to the display. Set this element to **FALSE** to enable cropping of the document thumbnail to show only sections that fit the display.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **2) LinksUpToDate**
This element indicates whether hyperlinks in a document are up-to-date. Set this element to **TRUE** to indicate that hyperlinks are updated. Set this element to **FALSE** to indicate that hyperlinks are outdated.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **Screenshot showing these properties inside the app.xml file**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties**
The following sample code sets the [BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) and [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) extended built-in document properties of the workbook. Please check the [output excel file](5115500.xlsx) generated with this code, change its extension to .zip and extract its contents and view the app.xml as shown in the screenshot above.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
