---  
title: Microsoft Excelを使用してOLEオブジェクトを自動的に更新（リフレッシュ）する方法 Aspose.Cells for Node.js via C++  
linktitle: Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する  
type: docs  
weight: 270  
url: /ja/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: ExcelのOLEオブジェクトを自動的に更新する方法をAspose.Cells for Node.js via C++で学習します。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは、ExcelファイルがMicrosoft Excelで開かれるときにOLEオブジェクトを再表示するための[**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--)プロパティを提供します。このプロパティにより、OLEオブジェクトは、Microsoft Excelによって生成された正しいOLEイメージを表示します。  
{{% /alert %}}  

次のサンプルコードでは、実際のOLEイメージでないOLEオブジェクトを含む[サンプルExcelファイル](5115231.xlsx)を読み込みます。OLEオブジェクトは実際にはMicrosoft Wordドキュメントですが、サンプルExcelファイルではMicrosoft Wordイメージの代わりに動物のイメージが表示されます。しかし、[出力Excelファイル](5115225.xlsx)を開くと、Microsoft Excelが正しいOLEイメージを表示します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
