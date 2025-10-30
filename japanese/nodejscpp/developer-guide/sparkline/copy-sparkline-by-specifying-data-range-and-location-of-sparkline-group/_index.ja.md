---  
title: Node.jsをC++経由で使用して、データ範囲とスパークライングループの位置を指定してスパークラインをコピーする方法  
linktitle: データ範囲とスパークライングループの位置を指定してスパークラインをコピーする  
type: docs  
weight: 300  
url: /ja/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Aspose.Cells for Node.js via C++を使用してExcelでスパークラインをコピーし、データ範囲とスパークライングループの位置を指定する方法について学びます。  
---  

{{% alert color="primary" %}}  
Microsoft Excelでは、データ範囲とスパークライングループの位置を指定してスパークラインをコピーすることができます。Aspose.Cellsでは、この機能をサポートしています。  
{{% /alert %}}  

Microsoft Excelでスパークラインを他のセルにコピーするには:  

1. スパークラインを含むセルを選択します。  
1. **デザイン**タブの**スパークライン**セクションから**データの編集**を選択します。  
1. **グループの位置とデータの編集**を選択します。  
1. データ範囲と位置を指定します。  
1. **OK** をクリックします。  

Aspose.Cellsは、`SparklineCollection.add(dataRange, row, column)`メソッドを提供し、スパークライングループのデータ範囲と位置を指定できます。以下のサンプルコードは、上述のスクリーンショットのようにソースExcelファイルを読み込み、最初のスパークライングループにアクセスし、データ範囲と位置を追加します。最後に、結果のExcelファイルをディスクに書き出します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
