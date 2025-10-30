---  
title: Node.js を通じて C++ でスプレッドシートを CSV 形式にエクスポートする際に空白行のセパレータを保持する  
linktitle: スプレッドシートをCSV形式にエクスポートする際に、空行のセパレーターを保持します  
type: docs  
weight: 160  
url: /ja/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する**  

Aspose.Cells は、スプレッドシートを CSV 形式に変換する際に行の区切りを保持する機能を提供します。これには [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/) の [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) プロパティを使用します。[**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) はブール型のプロパティです。Excel ファイルを CSV に変換する際に空白行の区切りを保持したい場合は、[**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) プロパティを **true** に設定します。  

以下のサンプルコードは、[ソースExcelファイル](84378743.xlsx)を読み込み、[**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--)プロパティを**true**に設定し、[出力.csv](84378744.csv)として保存します。スクリーンショットは、ソースExcelファイル、CSV変換時に生成されたデフォルト出力、そして[**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--)を**true**に設定した場合の出力の比較を示しています。  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
