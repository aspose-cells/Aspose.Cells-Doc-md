---
title: Node.jsを使用してExcelワークブックをOds、Sxc、Fods（OpenOffice / LibreOffice calc）に変換
linktitle: Ods
type: docs
weight: 20
url: /ja/nodejs-cpp/convert-excel-to-ods/
description: Aspose.Cells for Node.js via C++を使用してExcelをOds（OpenOffice / LibreOffice Calc）に変換する方法、またはOdsをExcelに変換する方法について
---

## **OpenDocumentについて**
[OpenDocument format（ODF）](https://en.wikipedia.org/wiki/OpenDocument)は、SunによってOpen Officeスイート向けに開発された電子オフィス文書のための無料かつオープンなファイルフォーマットです。OpenDocument Spreadsheet（ODS）はExcel文書のファイルフォーマットです。OpenDocumentは現在、OASISとISOの標準です。

## **Ods（OpenOffice / LibreOffice calc）をExcelに変換する**
Aspose.Cells for Node.js via C++は、OpenOffice / LibreOffice CalcでサポートされているOds、Sxc、Fodsを読み込み、[Ods](book1.ods)、[Sxc](book1.sxc)、[Fods](book1.fods)をExcelファイルに変換します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **ExcelをOds（OpenOffice / LibreOffice Calc）に変換する**
Aspose.Cells for Node.js via C++はExcelファイルをOds、Sxc、Fodsファイルに変換することをサポートしています。以下のコード例では、[テンプレート](book1.xlsx)をOds、Sxc、Fodsファイルに変換する方法を示します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **高度なトピック**
- [ODF 1.1および1.2仕様でODSファイルを保存する](/cells/ja/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [ODSファイルで背景を操作する](/cells/ja/nodejs-cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="nodejs-cpp" >}}
