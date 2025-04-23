---  
title: Gridlinesと行・列のヘッダーの表示/非表示をNode.jsとC++を使って制御する方法  
linktitle: グリッド線と行列ヘッダーの表示および非表示  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: この資料は、Node.js APIをC++経由で使用してExcelシートのグリッド線や行・列の見出しをプログラムで非表示または表示するサンプルコードを提供します。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは、デフォルトで表示されているワークシートのグリッド線の非表示および表示をサポートしています。また、ワークシートの行列ヘッダーの表示を制御する機能も提供しています。  
{{% /alert %}}  

## **グリッド線の表示と非表示**  

すべてのExcelワークシートはデフォルトでグリッド線を持っています。これにより、特定のセルにデータを入力することが簡単になります。グリッド線により、ワークシートをセルのコレクションとして表示し、各セルを簡単に識別することができます。  

### **グリッド線の表示の制御**  

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) コレクションを含んでいます。ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。グリッド線の表示制御には、[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) プロパティを使用します。[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)はブール型のプロパティで、「true」または「false」の値のみを格納できます。  

#### **グリッド線を表示する**  

[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)プロパティを**true**に設定してグリッド線を表示します。  

#### **グリッド線を非表示にする**  

[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--)プロパティを**false**に設定してグリッド線を非表示にします。  

以下に完全な例を示します。この例では、Excelファイル（book1.xls）を開き、最初のワークシートのグリッド線を非表示にし、変更後のファイルをoutput.xlsとして保存します。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **行列ヘッダーの表示および非表示**  

Excelファイルのすべてのワークシートは、行と列で配置されたセルから構成されています。すべての行と列には、それぞれユニークな値があり、行と列、また個々のセルを識別するために使用されます。たとえば、行には数字が付いています- 1、2、3、4など- そして列はアルファベット順に並んでいます- A、B、C、Dなど- 行と列の値はヘッダーに表示されます。Aspose.Cellsを使用すると、これらの行列ヘッダーの表示を制御することができます。  

### **ワークシートの表示を制御する**  

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) コレクションを含んでいます。ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。行と列の見出しの表示・非表示を制御するには、[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) プロパティを使用します。[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--)はブール型のプロパティで、「true」または「false」の値のみを格納できます。  

#### **行/列ヘッダーを表示する**  

行と列の見出しを表示するには、[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) プロパティを **true** に設定します。  

#### **行/列ヘッダーを非表示にする**  

行と列の見出しを非表示にするには、[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) プロパティを **false** に設定します。  

以下に完全な例を示します。この例では、Excelファイル（book1.xls）を開き、最初のワークシートの行と列の見出しを非表示にし、変更後のファイルをoutput.xlsとして保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
[**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-)と[**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-)のメソッドを使用して複数の行と列を表示させることも可能です。  
{{% /alert %}}  

