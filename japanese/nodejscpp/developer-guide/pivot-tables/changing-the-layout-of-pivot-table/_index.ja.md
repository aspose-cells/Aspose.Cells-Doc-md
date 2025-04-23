---
title: ピボットテーブルのレイアウトを変更する
type: docs
weight: 10
url: /ja/nodejs-cpp/changing-the-layout-of-pivot-table/
description: Aspose.Cells for Node.js via C++を使ったピボットテーブルのレイアウト変更方法。
keywords: Aspose.Cells for Node.js via C++のExcel、Node.jsライブラリを使ったピボットテーブルのレイアウト変更
---

## **MS-Excelでのピボットテーブルのレイアウトの変更方法**
Microsoft Excelでは、*PivotTable Tools > Design > Report Layout*メニューコマンドを使用してピボットテーブルのレイアウトを変更できます。これらの3つの形式でレイアウトを変更できます

- コンパクト形式で表示
- アウトライン形式で表示
- 表形式で表示

## **ピボットテーブルのレイアウトをAspose.Cells for Node.js via C++を使用して変更する方法**
Aspose.Cells for Node.js via C++ライブラリは、これら三つの形式でピボットテーブルのレイアウトを変更する [**PivotTable.showInCompactForm()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#showInCompactForm--)、[**PivotTable.showInOutlineForm()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#showInOutlineForm--)、[**PivotTable.showInTabularForm()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#showInTabularForm--) メソッドも提供しています。


## **サンプルコード**
次のサンプルコードでは、まずPivot Tableを**コンパクト形式**で表示し、次に**アウトライン形式**でPivot Tableを表示し、最後にPivot Tableを**表形式**で表示します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ChangingLayoutOfPivotTable.js" >}}
