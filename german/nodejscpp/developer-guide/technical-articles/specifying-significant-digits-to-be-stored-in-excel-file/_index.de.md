---  
title: Signifikante Ziffern, die in Excel Dateien mit Node.js via C++ gespeichert werden sollen  
linktitle: Angabe von signifikanten Ziffern, die in der Excel Datei gespeichert werden sollen  
type: docs  
weight: 30  
url: /de/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Lernen Sie, wie Sie festlegen, welche signifikanten Ziffern in einer Excel Datei gespeichert werden sollen mit Aspose.Cells for Node.js via C++.  
---  

## **Mögliche Verwendungsszenarien**  

Standardmäßig speichert Aspose.Cells for Node.js via C++ 17 signifikante Ziffern von Double-Werten in der Excel-Datei, im Gegensatz zu MS-Excel, das nur 15 signifikante Ziffern speichert. Sie können das Standardverhalten von Aspose.Cells von 17 auf 15 signifikante Ziffern ändern, indem Sie die Eigenschaft [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) verwenden.  

## **Angabe von signifikanten Ziffern, die in der Excel-Datei gespeichert werden sollen**  

Der folgende Beispielcode erzwingt, dass Aspose.Cells 15 signifikante Ziffern beim Speichern von Double-Werten in der Excel-Datei verwendet. Überprüfen Sie die [Ausgabedatei](22774105.xlsx). Ändern Sie die Erweiterung auf .zip, entpacken Sie sie und Sie sehen, dass nur 15 signifikante Ziffern in der Excel-Datei gespeichert sind. Die folgende Abbildung zeigt die Wirkung der [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--)-Eigenschaft auf die Ausgabedatei.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

