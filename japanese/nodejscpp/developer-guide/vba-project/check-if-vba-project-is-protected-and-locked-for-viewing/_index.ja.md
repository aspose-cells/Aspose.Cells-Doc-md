---
title: VBAプロジェクトが保護されていて閲覧のためにロックされているかどうかをNode.js経由で確認（C++利用）
linktitle: VBA（Visual Basic for Applications）プロジェクトが保護されて表示ロックされているかどうかを確認
type: docs
weight: 30
url: /ja/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Microsoft ExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されていて閲覧のためにロックされているかどうかをNode.js経由で確認する方法を学ぶ（Aspose.Cells for Node.js via C++利用）
---

## VBAプロジェクトが保護されていて閲覧のためにロックされているかどうかをNode.jsで確認

Aspose.Cellsを使用すると、ExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されているかつ、閲覧のためにロックされているかどうかを確認できます。そのためにAPIは[**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--)プロパティを提供します。閲覧用にロックされている場合、[**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--)プロパティは**true**を返します。

## **サンプルコード**

以下のサンプルコードは、[サンプルExcelファイル](43352065.xlsm)を読み込み、そのExcelファイルのVBA（Visual Basic for Applications）プロジェクトが保護されてロックされているかどうかを確認します。コンソール出力も参考にしてください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **コンソール出力**

上記のサンプルコードを提供された[サンプル Excelファイル](43352065.xlsm)で実行した際のConsoleの出力です。

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
