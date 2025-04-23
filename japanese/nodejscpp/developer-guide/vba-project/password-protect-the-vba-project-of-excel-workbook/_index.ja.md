---  
title: C++経由でNode.jsを使ってExcelブックのVBAプロジェクトにパスワード保護を設定する  
linktitle: ExcelワークブックのVBAプロジェクトにパスワードを設定する  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Aspose.Cells for Node.js via C++を使用してExcelブックのVBAプロジェクトにパスワード保護を設定する方法を学びます。  
---  

## **Node.jsでExcelブックのVBAプロジェクトにパスワード保護を設定する**  

[**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-)メソッドを使用してAspose.CellsでExcelブックのVBA（Visual Basic for Applications）プロジェクトをパスワードで保護できます。  

## **サンプルコード**  

以下のサンプルコードは、[サンプルExcelファイル](43352067.xlsm)をロードし、そのVBAプロジェクトにアクセスし、パスワードで保護します。最後に[出力Excelファイル](43352068.xlsm)として保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

