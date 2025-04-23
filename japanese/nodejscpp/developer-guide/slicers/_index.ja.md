---
title: スライサーの挿入
linktitle: スライサー
type: docs
weight: 170
url: /ja/nodejs-cpp/create-slicer/
description: Aspose.Cells for Node.js via C++を使用したExcelファイルのスライサー管理。
---

## **可能な使用シナリオ**

スライサーはデータを迅速にフィルタリングするために使用されます。テーブルまたはピボットテーブルの両方でデータをフィルタリングできます。Microsoft Excelでは、テーブルまたはピボットテーブルを選択し、「挿入」>「スライサー」をクリックすることでスライサーを作成できます。Aspose.Cells for Node.js via C++では、[**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-)メソッドを使用してスライサーを作成することも可能です。

## **ピボットテーブルにスライサーを作成する**

以下のサンプルコードを参照してください。これにより、ピボットテーブルを含む[サンプルExcelファイル](67338470.xlsx)が読み込まれます。その後、最初の基本ピボットフィールドに基づいてスライサーが作成されます。最後に、ワークブックを[出力 XLSX](67338471.xlsx)および[出力 XLSB](67338472.xlsb)形式で保存します。以下のスクリーンショットは、Aspose.Cells for Node.js via C++が作成したスライサーを出力Excelファイルに示しています。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Excelテーブルにスライサーを作成する**

次のサンプルコードをご覧ください。これは、テーブルを含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込みます。それから最初の列に基づいてスライサーを作成します。最後に、ブックを[出力XLSX](outputCreateSlicerToExcelTable.xlsx)形式で保存します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
