---  
title: Node.js経由でC++を使用してExcelファイルの印刷禁止を設定する方法  
linktitle: Excelファイルの印刷を防止する方法  
type: docs  
weight: 600  
url: /ja/nodejs-cpp/how-to-prevent-printing-excel/  
description: Aspose.Cells for Node.js via C++を使用して、Excelファイルの印刷を防止する方法を学びます。  
keywords: excel印刷、excel印刷を防ぐ、Excelファイルの印刷を防ぐ方法、excel印刷を防ぐ、ブック全体の印刷を防ぐ、VBAでブック全体の印刷を防ぐ。  
---  

## **可能な使用シナリオ**  
日常の仕事の中で、重要な情報を含むExcelファイルがあります。内部データの拡散を防ぐために、会社は印刷を許可しません。このドキュメントは、他者がExcelファイルを印刷できないようにする方法を説明します。  

## **MS-Excelでファイルの印刷を防ぐ方法**  
次のVBAコードを適用して、特定のファイルの印刷を防ぐことができます。  
1. 印刷を許可しないブックを開きます。  
1. Excelリボンの「開発」タブを選択し、「コントロール」セクションの「コードの表示」ボタンをクリックします。あるいは、ALT + F11キーを押してMicrosoft Visual Basic for Applicationsウィンドウを開きます。  
<br>  
<img src="1.png" width=70% />  
1. 次に、左側のProject ExplorerでThisWorkbookをダブルクリックしてモジュールを開き、VBAコードを追加します。  
<br>  
<img src="2.png" width=70% />  
1. その後、コードを保存して閉じ、ブックに戻ります。次にサンプルファイルを印刷しようとすると、印刷が許可されず、次の警告ボックスが表示されます。  
<br>  
<img src="3.png" width=70% />  

## **Aspose.Cells for Node.js via C++を使用して、Excelファイルの印刷を防止する方法**  

次のサンプルコードは、Excelファイルの印刷を防ぐ方法を示しています。  

1. [サンプルファイル](sample.xlsx)をロードする。  
1. WorkbookのVbaProjectプロパティからVbaModuleCollectionオブジェクトを取得します。  
1. "ThisWorkbook"名を通じてVbaModuleオブジェクトを取得します。  
1. VbaModuleのcodesプロパティを設定します。  
1. サンプルファイルを[xlsm形式](out.xlsm)で保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

wb.save("out.xlsm");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
