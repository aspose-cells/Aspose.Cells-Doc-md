---
title: ピボットテーブル内のPivot Fieldをグループ化
type: docs
weight: 80
url: /ja/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: Aspose.Cells for Node.js via C++を使ったピボットフィールドのグループ化方法
keywords: Aspose.Cells for Node.js via C++ Excel、Excel Node.jsライブラリ、ピボットテーブル内のピボットフィールドのグループ化方法 Aspose.Cells for Node.js via C++ Excelライブラリを使用して
---

## **可能な使用シナリオ**

Microsoft Excelでは、ピボットフィールドをグループ化できます。大量のデータが関連する場合にセクションにまとめることが有効です。Aspose.Cells for Node.js via C++もこの機能を[**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-)メソッドで提供しています。

## **Pivot TableでPivot Fieldsをグループ化する方法**

以下のサンプルコードは、[サンプルExcelファイル](64716818.xlsx)をロードし、[**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-)メソッドを使用して最初のピボットフィールドにグループ化を行います。それからピボットテーブルのデータをリフレッシュして計算し、ブックを[出力Excelファイル](64716817.xlsx)として保存します。スクリーンショットは、サンプルコードのサンプルExcelファイルに対する効果を示しています。スクリーンショットに示されているように、最初のピボットフィールドは現在月ごとと四半期ごとにグループ化されています。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
