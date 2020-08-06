---
title : "Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties" 
description : "" 
weight : 12572 
toc : false
type: docs
url: /java/developerguide/technicalarticles/setting+scalecrop+and+linksuptodate+properties+of+built-in+document+properties/
---

# Aspose.Cells for Java : Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties



## Possible Usage Scenarios

[ScaleCrop](https://apireference.aspose.com/java/cells/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) and [LinksUpToDate](https://apireference.aspose.com/java/cells/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) are two extended built-in document properties defined inside the OpenXml format. The purpose of these properties are following

## 1) ScaleCrop

This element indicates the display mode of the document thumbnail. Set this element to **true** to enable scaling of the document thumbnail to the display. Set this element to **false** to enable cropping of the document thumbnail to show only sections that fit the display.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## 2) LinksUpToDate

This element indicates whether hyperlinks in a document are up-to-date. Set this element to **true** to indicate that hyperlinks are updated. Set this element to **false** to indicate that hyperlinks are outdated.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## Screenshot showing these properties inside the `app.xml` file

![image](5472495.png)

## Setting ScaleCrop and LinksUpToDate properties of Built-In Document Properties

The following sample code sets the [ScaleCrop](https://apireference.aspose.com/java/cells/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) and [LinksUpToDate](https://apireference.aspose.com/java/cells/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) extended built-in document properties of the workbook. Please check the [output excel file](https://docs2.aspose.com/cells/java/attachments/5276000/5472494.xlsx) generated with this code, change its extension to `.zip` and extract its contents and view the `aap.xml` as shown in the screenshot above.

