---  
title: 行と列、およびスクロールバーの表示/非表示をNode.jsとC++を使って制御する  
linktitle: 行、列、およびスクロールバーを表示して非表示にする  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: この記事は、C++を介してNode.jsを使用し、Excelのワークシートの行と列をプログラム的に表示および非表示にする方法を示しています。スクロールバーの表示制御や複数の行と列を効率的に非表示にする方法も解説しています。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsはワークシートの行、列、およびスクロールバーの表示を制御する方法を提供しています。  
{{% /alert %}}  

## **行や列の表示と非表示**  

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、そのワークシート内のすべてのセルを表す[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供します。[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションは、ワークシートの行や列を管理するための複数のメソッドを提供します。その一部を以下に示します。  

### **行と列を表示**  

開発者は、[**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-)と[**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-)のメソッドを呼び出すことで、非表示になっている行や列を表示させることができます。どちらのメソッドも、2つのパラメータを取ります：  

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。  
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
隠された列を表示する場合、以前に割り当てられた幅や元の幅に復元したい場合は、負の幅で列を非表示解除してください。例：worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **行と列を非表示**  

開発者は、[**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-)と[**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-)のメソッドを呼び出すことで、行や列を非表示にできます。どちらのメソッドも、特定の行や列のインデックスをパラメータとして受け取り、その行または列を非表示にします。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。  
{{% /alert %}}  

### **複数の行と列を非表示**  

開発者は、[**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-)と[**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-)のメソッドを呼び出し、複数の行や列を一度に非表示にできます。これらの両方のメソッドは、開始行または列のインデックスと隠す行または列の数をパラメータとして受け取ります。  

```javascript
const fs = require('fs');
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **スクロールバーの表示と非表示**  

スクロールバーは、どのファイルの内容をナビゲートするために使用されます。通常、2種類のスクロールバーがあります。  

- 垂直スクロールバー  
- 水平スクロールバー  

Microsoft Excelは、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロールバーを提供しています。Aspose.Cellsを使用すると、Excelファイルの両方のタイプのスクロールバーの表示/非表示を制御することができます。  

### **スクロールバーの表示を制御する**  

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイルの管理に役立つさまざまなプロパティとメソッドを備えています。スクロールバーの表示制御には、[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)と[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)プロパティを使用します。[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)と[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)はBoolean型のプロパティであり、これらは**true**または**false**のみを格納できます。  

#### **スクロールバーを表示する**  

スクロールバーを表示するには、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)または[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)プロパティを**true**に設定します。  

#### **スクロールバーを非表示にする**  

スクロールバーを非表示にするには、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)または[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)プロパティを**false**に設定します。  

**サンプルコード**  

以下は、Excelファイルであるbook1.xlsを開き、両方のスクロールバーを非表示にし、変更されたファイルをoutput.xlsとして保存する完全なコードです。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
