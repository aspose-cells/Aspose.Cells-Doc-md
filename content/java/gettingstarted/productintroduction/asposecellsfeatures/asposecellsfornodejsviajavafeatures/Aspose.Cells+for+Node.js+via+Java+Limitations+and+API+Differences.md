+++
title = "Aspose.Cells for Node.js via Java Limitations and API Differences" 
description = "" 
weight = 20024 
+++

Aspose.Cells for Java : Aspose.Cells for Node.js via Java Limitations and API Differences  

# Aspose.Cells for Java : Aspose.Cells for Node.js via Java Limitations and API Differences


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Public API Differences](#Aspose.CellsforNode.jsviaJavaLimitationsandAPIDifferences-PublicAPIDifferences)
    *   1.1 [Importing library (Package Comparisons)](#Aspose.CellsforNode.jsviaJavaLimitationsandAPIDifferences-Importinglibrary(PackageComparisons))
    *   1.2 [Instantiating a new Workbook](#Aspose.CellsforNode.jsviaJavaLimitationsandAPIDifferences-InstantiatinganewWorkbook)
    *   1.3 [Enums or Constants](#Aspose.CellsforNode.jsviaJavaLimitationsandAPIDifferences-EnumsorConstants)
    *   1.4 [Streaming Files](#Aspose.CellsforNode.jsviaJavaLimitationsandAPIDifferences-StreamingFiles)
*   2 [Other Limitations of Aspose.Cells for Node.js via Java API compared to Aspose.Cells for Java API](#Aspose.CellsforNode.jsviaJavaLimitationsandAPIDifferences-OtherLimitationsofAspose.CellsforNode.jsviaJavaAPIcomparedtoAspose.CellsforJavaAPI)
{{< /panel >}}
 

## Public API Differences

The following list (with sample code segments) shows some differences between Aspose.Cells for Java and Aspose.Cells for Node.js via Java APIs.

### Importing library (Package Comparisons)

**Aspose.Cells for Java**

import com.aspose.cells.\*;

**Aspose.Cells for Node.js via Java**

var aspose = aspose || {};aspose.cells = require("aspose.cells");

### Instantiating a new Workbook

**Aspose.Cells for Java**

Workbook excelbook = new Workbook();

**Aspose.Cells for Node.js via Java**

var excelbook = new aspose.cells.Workbook();

### Enums or Constants

**Aspose.Cells for Java**

arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

**Aspose.Cells for Node.js via Java**

arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

### Streaming Files

**Aspose.Cells for Java**

InputStream inputstream = new FileInputStream(“Book1.xlsx”);Workbook workbook = new Workbook(inputstream);workbook.save(“result.xlsx”);

**Aspose.Cells for Node.js via Java**

var aspose = aspose || {};aspose.cells = require("aspose.cells");var fs = require("fs");var readStream = fs.createReadStream("Book1.xlsx");aspose.cells.Workbook.createWorkbookFromStream(readStream, function(workbook, err) {    if (err) {        console.log("open workbook error");        return;    }   workbook.save('result.xlsx');    console.log('saved to file');});

## Other Limitations of Aspose.Cells for Node.js via Java API compared to Aspose.Cells for Java API

1.  Importing/exporting data from an `Array`, `ArrayList`, `ResultSet` etc. is not supported.
2.  Printing is not supported.

