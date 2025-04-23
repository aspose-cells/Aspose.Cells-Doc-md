---  
title: Node.jsを通じてC++でWorkbookをStrict Open XML Spreadsheet形式で保存する方法  
linktitle: 厳密なOpen XMLスプレッドシート形式へのブックの保存  
type: docs  
weight: 150  
url: /ja/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Aspose.Cells for Node.js via C++を使用して、WorkbookをStrict Open XML Spreadsheet形式で保存する方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.Cells for Node.js via C++は、Workbookを*Strict Open XML Spreadsheet*形式で保存することを可能にします。そのために、[**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--)プロパティを提供します。その値を[**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance)に設定すると、出力されるExcelファイルはStrict Open XML Spreadsheet形式で保存されます。  

## **ストリクトなOpen XMLスプレッドシート形式でワークブックを保存**  

次のサンプルコードは、Workbookを作成し、[**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--)プロパティの値を[**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance)に設定して、[出力Excelファイル](67338272.xlsx)として保存します。Microsoft Excelで出力されたExcelファイルを開き、「名前を付けて保存...」ダイアログを開くと、その形式が*Strict Open XML Spreadsheet*として表示されることがこのスクリーンショットに示されています。  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Specify - Strict Open XML Spreadsheet - Format.
wb.getSettings().setCompliance(AsposeCells.OoxmlCompliance.Iso29500_2008_Strict);

// Add message in cell B4 of first worksheet.
const b4 = wb.getWorksheets().get(0).getCells().get("B4");
b4.putValue("This Excel file has Strict Open XML Spreadsheet format.");

// Save to output Excel file.
wb.save("outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

