---
title: PivotTableがExcel2003に互換性があるかどうかを指定する
type: docs
weight: 880
url: /ja/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells は、PivotTable をリフレッシュする際の Excel2003 との互換性を指定するための [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) プロパティを提供しており、**true** の場合は、文字列は255文字以下である必要があります。したがって、文字列が255文字を超える場合、切り捨てられます。**false** の場合は、文字列に前述の制限はありません。デフォルト値は **true** です。

{{% /alert %}} 
## **PivotTableを更新する際にExcel2003に互換性があるかどうかを指定する**
次のサンプルコードは、[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) プロパティの使用方法を説明しています。元の文字列は383文字です。しかし、[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) プロパティを **true** に設定し、ピボットテーブルをリフレッシュすると、ピボットテーブルのセル B5 のデータが切り捨てられ、255文字になります。ただし、[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) プロパティを **false** に設定し、ピボットテーブルを再度リフレッシュすると、ピボットテーブルのセル B5 のデータは切り捨てられず、383文字のままです。このコードで使用されている [サンプルエクセルファイル](5472558.xlsx)、生成された [出力エクセルファイル](5472557.xlsx)、およびコンソール出力をダウンロードして参照してください。このプロパティの理解を深めるために、コード内のコメントも必ずお読みください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **コンソール出力**
上記のサンプルコードを指定の [サンプルエクセルファイル](5472558.xlsx) で実行した際のコンソール出力はこちらです。



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
