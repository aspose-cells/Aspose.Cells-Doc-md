---  
title: Node.js経由でC++を使用してExcelの互換性チェッカーを無効化する  
linktitle: Excelでの互換性チェッカーを無効にする  
type: docs  
weight: 170  
url: /ja/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Aspose.Cells for Node.js via C++ APIを通じて互換性チェッカーを無効にする方法を学びます。  
keywords: Node.jsで互換性チェッカーを無効にする、C++を通じてExcelの互換性チェッカーをNode.jsで無効化、ブック内の互換性チェッカーを無効化。  
---  

## Node.jsを使用したExcelワークシートの互換性チェッカー無効化  

{{% alert color="primary" %}}  
Microsoft Excelの互換性チェッカーは、以前のファイル形式でファイルを保存すると機能の問題や精度の低下が引き起こされる可能性があるとして警告を出します。互換性チェッカーはMicrosoft Office Excel 2007およびMicrosoft Excel 2010の機能です。  

以前のバージョンのワークブックをExcel 2007またはExcel 2010からExcel 97からExcel 2003に保存する場合、互換性チェッカーは、以前のバージョンではサポートされていない機能が含まれていないかどうかをワークブックをスキャンします。互換性の問題についての決定を支援するために、互換性チェッカーはオプションを含むダイアログボックスを表示します。また、ワークブックの問題に関するレポートを作成したり、機能を無効にすることもできます。  

時には、特定のスプレッドシートに対して互換性チェッカーを無効にする必要があります。Aspose.CellsのAPIを使えば、これをプログラムで行うことができ、ユーザーがMicrosoft Excelでファイルを再保存する際に互換性チェッカーのダイアログボックスが表示されて混乱したりイライラしたりしません。  
{{% /alert %}}  

## **Microsoft Excelを使用して互換性チェッカーを無効にする方法**  

Microsoft Excel（例: Microsoft Excel 2007/2010）で互換性チェッカーを無効にする場合:  

- （Excel 2007）[Office] ボタンをクリックし、「準備」、[互換性の確認] をクリックし、「このブックを保存するときに互換性を確認する」オプションをクリアします.  
- (Excel 2010) ファイルタブをクリックし**情報**、**問題の確認**、**互換性を確認**をクリックし、最後に**このブックを保存する場合に互換性をチェック**のチェックを外します。  

## **Aspose.Cells APIを使用して互換性チェッカーを無効にする方法**  

Microsoft Excelの互換性チェッカーを無効にするには、[**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--)プロパティを**false**に設定します。  

### **コード例**  

以下のコード例では、Aspose.Cells for Node.js via C++を使用して互換性チェッカーを無効にする方法を示します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

