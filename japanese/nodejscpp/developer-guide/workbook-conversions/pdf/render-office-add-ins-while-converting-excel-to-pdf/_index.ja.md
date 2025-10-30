---
title: ExcelからPDFへの変換中にOfficeアドインをレンダリングするNode.js経由のC++
linktitle: ExcelをPDFに変換する際のOffice Add Insのレンダリング
type: docs
weight: 100
url: /ja/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **可能な使用シナリオ**

以前は、Aspose.CellsはExcelファイルをPDF形式に保存するときにOfficeアドインをレンダリングできませんでした。現在、Aspose.Cellsは正常にレンダリングします。出力PDFにOfficeアドインをレンダリングするために、特別な方法やプロパティを使用する必要はありません。ただExcelファイルをPDF形式で保存するだけで、Officeアドインがレンダリングされます。

## **ExcelをPDFに変換する際のOffice Add-Insのレンダリング**

以下のサンプルコードは、Office アドインを含むサンプル Excel ファイル（60489769.xlsx）を保存します。以前のバージョン（例：17.11）で生成された出力 PDF と、新しいバージョン（例：17.12以降）で生成された出力 PDF をご覧ください。前のバージョンの出力 PDF は空白ですが、新しいバージョンは Office アドインを表示します。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
