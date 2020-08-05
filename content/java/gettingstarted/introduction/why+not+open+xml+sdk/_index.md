---
title : "Why Not Open XML SDK" 
description : "" 
weight : 12037 
toc : false
type: docs
url: /java/gettingstarted/introduction/why+not+open+xml+sdk/
---

# Aspose.Cells for Java : Why Not Open XML SDK


We sometimes hear this question:

**Why should we use Aspose products rather than the free Open XML SDK?**

This question is easy to answer: **features and functionality**.

#### *What is Open XML SDK?*

According to the [MSDN Library](http://msdn.microsoft.com/en-us/library/bb448854.aspx), Open XML SDK is defined as:The Open XML SDK 2.0 simplifies the task of manipulating Open XML packages and the underlying Open XML schema elements within a package. The Open XML SDK 2.0 encapsulates many common tasks that developers perform on Open XML packages, so that you can perform complex operations with just a few lines of code.OOXML documents are essentially zipped XML files and Open XML SDK is a collection of classes that allows you to work with the content of OOXML documents in a strongly-typed way. That is instead of unzipping a file to extract XML, loading that XML into a DOM tree and working with XML elements and attributes directly, Open XML SDK provides classes to do that.

#### *What is Aspose.Cells?*

Aspose.Cells is a class library that allows your application to perform the following spreadsheet processing tasks:

*   High Quality conversions between all popular Excel formats, including conversion to PDF, HTML, TIFF and printing.
*   Programming with a workbook object model.
*   Ability to build documents from fragments, from one or multiple documents, while automatically merging data by stylistic formatting, charts and graphics.
*   High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet.
*   Robust Formula Calculation Engine that supports almost all of the standard and advanced Microsoft Excel Functions.

#### *Compare Open XML SDK and Aspose.Words*

![image](https://docs2.aspose.com/cells/java/attachments/thumbnails/41550542/ri.png)The following table compares Open XML SDK and Aspose.Cells features.

{{< table style="table-striped" >}}
|Feature or Feature Category|Open XML SDK|Aspose.Cells|
|:----|:----|:----|
|Supported Excel or other formats|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tab Delimited, ODS, Plain Text (TXT), PDF, XPS|
|Convert between Excel formats|No|Yes|
|High-level programming with a workbook object model:*   Find and replace.*   Assemble spreadsheets.*   Copy fragments and worksheets between workbooks.|No|Yes|
|Detailed programming with a document object model, access to individual elements and formatting properties of all spreadsheet elements.|Yes|Yes|
|Low-level direct and full access to the underlying XML elements and attributes such as relationship identifiers, list identifiers of an OOXML document.|Yes|No|
|Generate reports, populate documents with data:*   Import/Export data to/from a *DataTable / *ResultSet.*   Smart Markers feature.*   Insert/Delete Rows/Columns/Ranges.*   Custom data sources.|No|Yes|
|Rendering and Printing:\* Render worksheet pages to raster images (TIFF, multipage TIFF, PNG, JPEG, BMP).\* Render spreadsheet pages to vector images (EMF).\* Convert charts to images (TIFF, multipage TIFF, PNG, JPEG, BMP, EMF etc.) *   Specify image resolution, quality, compression and other options.*   Print spreadsheets using the .NET printing infrastructure. The component has built-in print method to print the worksheets as shown in Print Preview of MS Excel.|No|Yes|
|Calculate/ Recalculate formulas dynamically  |No|Yes|
|Supported platforms|Windows, .NET|Windows, Linux, Java, .NET, Mono|
{{< /table >}}

#### *Conclusion*

![image](https://docs2.aspose.com/cells/java/attachments/thumbnails/41550542/ri.png)Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option:

*   Support other file formats in addition to XLSX.
*   Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner.
*   Replace formatted or unformatted text.
*   High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet.
*   Generate a business document, such as an order with order details from a data source.
*   Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it.
*   Develop a .NET or Java application.

