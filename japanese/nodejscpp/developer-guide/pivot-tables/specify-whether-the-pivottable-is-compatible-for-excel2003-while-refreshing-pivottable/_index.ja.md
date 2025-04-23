---
title: PivotTableがExcel2003に互換性があるかどうかを指定する
type: docs
weight: 80
url: /ja/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++は、Excel2003と互換性のあるピボットテーブルかどうかを指定するために[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)プロパティを提供します。これがtrueの場合、文字列は255文字以下でなければならず、255文字を超える場合は切り捨てられます。**false**の場合、文字列は上記の制限を受けません。デフォルト値は**true**です。

{{% /alert %}}

## **PivotTableを更新する際にExcel2003に互換性があるかどうかを指定する**

次のサンプルコードは、[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)プロパティの使用方法を説明しています。元の文字列は383文字ですが、[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)プロパティをtrueに設定してピボットテーブルを更新すると、ピボットテーブルのセルB5のデータが切り捨てられて255文字になります。ただし、[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)プロパティをfalseに設定してピボットテーブルを再度更新すると、ピボットテーブルのセルB5のデータが切り捨てられず、383文字のままです。このプロパティの理解のためにコード内のコメントをお読みください。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

