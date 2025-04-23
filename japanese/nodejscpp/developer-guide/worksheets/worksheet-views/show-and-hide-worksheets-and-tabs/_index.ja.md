---  
title: Node.jsをC++経由で使用して、ワークシートやタブの表示と非表示を行う方法に関する記事  
linktitle: ワークシートとタブの表示と非表示  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: このサンプルコードは、Node.js APIまたはNode.jsライブラリを使用して、Excelワークシートの表示と非表示をプログラム的に行う方法を示しています。さらに、Excelワークブックのタブの表示と非表示についても解説します。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsはユーザーに、ワークブック内のワークシートやタブなどの要素を表示または非表示にする機能を提供します。  
{{% /alert %}}  

## **ワークシートの表示と非表示**  

Excelファイルには1つ以上のワークシートが含まれることがあります。Excelファイルを作成するときには、作業するExcelファイルにワークシートを追加します。Excelファイル内の各ワークシートは、独自のデータや書式設定などを持つため、他のワークシートから独立しています。開発者は時々、Excelファイル内で特定のワークシートを非表示にし、他のワークシートを表示したい場合があります。そのため、Aspose.Cellsは開発者がExcelファイル内のワークシートの表示を制御することを可能にします。  

Aspose.Cellsは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。  

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。ワークシートの表示状態を制御するには、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--)プロパティを使用します。[**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--)はBoolean型のプロパティであり、**true**または**false**の値しか保存できません。  

### **ワークシートを表示する**  

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--)プロパティを**true**に設定して、ワークシートを表示します。  

### **ワークシートを非表示にする**  

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--)プロパティを**false**に設定して、ワークシートを非表示にします。  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **タブの表示と非表示**  

Microsoft Excelの下部をよく見ると、いくつかのコントロールが表示されます。これには次のものが含まれます:  

- シートタブ。  
- タブのスクロールボタン。  

シートタブはExcelファイル内のワークシートを表します。任意のタブをクリックするとそのワークシートに切り替えることができます。ワークブック内にワークシートが多いほど、シートタブも多く表示されます。Excelファイルに多くのワークシートが含まれている場合は、それらをナビゲートするためのボタンが必要になります。そのため、Microsoft Excelはシートタブのスクロールボタンを提供しています。  

Aspose.Cellsを使用すると、開発者はExcelファイル内のシートタブとタブのスクロールボタンの表示を制御できます。  

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイルを管理するためのさまざまなプロパティとメソッドを提供します。Excelファイルのタブの表示状態を制御するには、開発者は[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)プロパティを使用できます。[**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)はBoolean型のプロパティであり、**true**または**false**の値しか保存できません。  

### **タブを表示する**  

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)プロパティを**true**に設定してタブを表示します。  

### **タブを非表示にする**  

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)プロパティを**false**に設定して、Excelファイルのタブを非表示にします。  

以下は、Excelファイル（book1.xls）を開き、そのタブを非表示にして修正したファイルをoutput.xlsとして保存する完全な例です。コードの実行後、ワークブックのタブが非表示になっていることが確認できます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **タブバーの幅を制御する**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

