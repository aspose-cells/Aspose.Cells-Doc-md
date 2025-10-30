---  
title: Node.jsとC++を使用して行と列を自動調整  
linktitle: 行と列の自動調整  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/autofit-rows-and-columns/  
description: この記事では、Aspose.Cells for Node.js via C++を使用してセル範囲の行、列、結合セルの行、行の自動調整方法を示します。  
keywords: Node.jsとC++を使用した行の自動調整、列の自動調整、範囲内のセルの行の自動調整、結合セルの行の自動調整  
---  

{{% alert color="primary" %}}  
Microsoft Excelでは、セルの内容に応じてセルの幅と高さを自動調整できます。この機能はAspose.Cells for Node.js via C++を通じても利用可能で、開発者はランタイムでセルの寸法を自動調整できます。  
{{% /alert %}}  

## **自動調整**  

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイルの各シートにアクセスできる[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。シートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスはシート管理のための多くのプロパティとメソッドを提供します。この記事では、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスを使用した行や列の自動調整について説明します。  

### **行の自動調整 - シンプル**  

行の幅と高さを自動調整する最も簡単な方法は、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)メソッドを呼び出すことです。[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)メソッドは調整対象の行のインデックスをパラメータとして受け取ります。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **セル範囲内の行を自動調整する方法**  

行は多くの列で構成されます。Aspose.Cellsでは、行内のセル範囲の内容に基づいて行を自動調整できるように、[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-)メソッドのオーバーロード版を呼び出すことが可能です。引数は次の通りです。  

- **行インデックス**：自動調整される行のインデックス。  
- **最初の列インデックス**：行の最初の列のインデックス。  
- **最後の列インデックス**：行の最後の列のインデックス。  

[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-)メソッドは、行内のすべての列の内容をチェックし、その後行を自動調整します。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **セル範囲内の列を自動調整する方法**  

列は多くの行から構成されます。列内のセル範囲の内容に基づいて列を自動調整するには、次のパラメータを受け取る[**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)メソッドのオーバーロード版を呼び出します。  

- **列インデックス**：自動調整される列のインデックス。  
- **最初の行インデックス**：列の最初の行のインデックス。  
- **最後の行インデックス**：列の最後の行のインデックス。  

[**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)メソッドは、列内のすべての行の内容をチェックし、その後列を自動調整します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **結合セルの行を自動調整する方法**  

Aspose.Cellsを使用すれば、[**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) APIを用いて結合セルを含むセルの行も自動調整可能です。[**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions)クラスは、結合セル用に行自動調整に使える[**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--)プロパティを提供しています。[**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--)は、[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype)列挙可能な値と次のメンバーを受け入れます。  

- なし: 結合セルを無視します。  
- 最初の行のみ: 最初の行の高さのみ拡張します。  
- 最終行のみ: 最後の行の高さのみ拡張します。  
- 各行: 各行の高さのみ拡張します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
また、[**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-)や[**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-)のオーバーロード版を使用して、行や列の範囲と[**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions)のインスタンスを渡し、選択した行や列の高さや幅を desired [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) に自動調整することも可能です。  

上記メソッドのシグニチャは次の通りです：  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **重要なこと**  

{{% alert color="primary" %}}  
セルが結合されている場合、autoFitメソッドは適用されません。これはMicrosoft Excelと同じ動作です。これを回避するには autofilter API を使用してください。さらに、セル内のテキストが折り返されている場合も、[**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)メソッドは適用されません。autoFitメソッドは時間がかかるため、アプリケーションの効率性を保つためにこれらの呼び出しはできるだけ少なくしてください。  
{{% /alert %}}  

## **高度なトピック**  
- [結合されたセルの行のAutoFit](/cells/ja/nodejs-cpp/autofit-rows-for-merged-cells/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
