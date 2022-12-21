---
title: ピボットテーブルの更新中に、ピボットテーブルが Excel2003 と互換性があるかどうかを指定します
type: docs
weight: 880
url: /ja/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

Aspose.Cells は[PivotTable.IsExcel2003互換](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)ピボットテーブルを更新するときに、ピボットテーブルが Excel2003 と互換性があるかどうかを指定するために使用できるプロパティ。もしも**真実**、文字列は 255 文字以下である必要があるため、文字列が 255 文字を超える場合は切り捨てられます。もしも**間違い**、文字列には前述の制限はありません。デフォルト値は**真実**.

{{% /alert %}} 
## **ピボットテーブルの更新中に、ピボットテーブルが Excel2003 と互換性があるかどうかを指定します**
次のサンプル コードは、[PivotTable.IsExcel2003互換](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)財産。元の文字列の長さは 383 文字です。でもいつ[PivotTable.IsExcel2003互換](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)プロパティはに設定されています**真実**ピボット テーブルを更新すると、ピボット テーブルのセル B5 のデータが切り捨てられ、255 文字になります。ただし、[PivotTable.IsExcel2003互換](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)プロパティが設定されています**間違い**ピボット テーブルを再度更新すると、ピボット テーブルのセル B5 のデータは切り捨てられず、383 文字のままです。をダウンロードしてください[サンプルエクセルファイル](5472558.xlsx)このコードで使用されている、[出力エクセルファイル](5472557.xlsx)それによって生成されたものと、参照用のコンソール出力。このプロパティをよりよく理解するために、コード内のコメントもお読みください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **コンソール出力**
上記のサンプル コードを特定のコマンドで実行した場合のコンソール出力は次のとおりです。[サンプルエクセルファイル](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
