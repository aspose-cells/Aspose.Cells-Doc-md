---  
title: Node.js経由でC++を使ったセル範囲のデータラベル表示  
linktitle: データラベルとしてのセル範囲を表示  
description: Aspose.Cells for Node.js via C++を使用して、チャート内にセル範囲をデータラベルとして表示する方法を学びます。ガイドでは、ラベルをデータソースにリンクさせ、それらをフォーマットして正確で意味のある情報を提供する方法を示します。  
keywords: Aspose.Cells for Node.js via C++、チャート作成、データラベル、セル範囲、データソース、フォーマッティング、精度、意味のある情報。  
type: docs  
weight: 130  
url: /ja/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
Microsoft Excel 2013では、セル範囲をデータラベルとして表示できます。Node.js用Aspose.Cellsはこの機能をサポートしています。  
{{% /alert %}}  

## **セル範囲をデータラベルとして表示するためのチェックボックス**  

Microsoft Excelでセルの範囲をデータラベルとして表示するには：  

1. シリーズのデータラベルを選択して、コンテキストメニューを開くために右クリックします。  
1. **データラベルの書式設定**を選択します。ラベルのオプションが表示されます。  
1. **ラベルに値を含める**オプションを選択またはクリアします。  

以下のサンプルコードは、チャートシリーズのデータラベルにアクセスし、その[**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--)プロパティを**true**に設定して、「セル値からのラベル」オプションを選択します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
