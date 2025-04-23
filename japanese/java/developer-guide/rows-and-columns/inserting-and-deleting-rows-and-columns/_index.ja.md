---
title: Excelファイルの行と列の挿入と削除
type: docs
weight: 60
url: /ja/java/inserting-and-deleting-rows-and-columns/
description: Aspose.Cells for JavaのAPIを介して行と列の挿入および削除を行う方法を学びます。
keywords: Javaで行や列を挿入および削除する方法、Javaで行や列を挿入する方法、Javaで行や列を削除する方法、Javaで行または列を挿入する方法、行または列をJavaで削除する方法via Java。
---

## **紹介**
ワークシートをゼロから作成するか、既存のワークシートで作業する場合、さらなるデータを収容するために追加の行や列を必要とする場合があります。逆に、ワークシート内の特定の位置から行や列を削除する必要がある場合もあります。

これらの要件を満たすために、Aspose.Cellsは以下で説明されている非常にシンプルな一連のクラスとメソッドを提供しています。
## **行/列の管理方法**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートへのアクセスを可能にする[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) コレクションを提供します。

ワークシートの行と列を管理するために、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) コレクションはいくつかの方法を提供します。そのうちいくつかについては以下で議論されています。

{{% alert color="primary" %}} 

行または列が追加されると、ワークシートの内容は下や右にシフトされますが、行または列が削除されると、内容は上や左にシフトされます。

{{% /alert %}} 
## **行の挿入方法**
[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) メソッドを呼び出すことで、任意の位置に行を挿入できます。[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) メソッドは、最初の引数に挿入する行のインデックス、2番目の引数に挿入する行数を取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **複数の行を挿入する方法**
複数の行をワークシートに挿入するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) メソッドを呼び出します。[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) は2つのパラメータを取ります：

- 行インデックス: 新しい行を挿入する行のインデックス。
- 行数: 挿入する行の合計数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **書式付きで行を挿入する方法**
書式付きの行を挿入するには、[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) オーバーロードを使用します。これは [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) をパラメータとして取ります。[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) の [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) プロパティを [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) 列挙値で設定します。 [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) 列挙値は以下の3つです：

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): 上の行と同じフォーマットで行を設定します。
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW): 下の行と同じフォーマットで行を設定します。
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): 書式設定をクリアします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **行の削除方法**
任意の位置に行を削除するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) メソッドを呼び出します。 [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) メソッドは、2つのパラメータを取ります：

- 行インデックス: 削除する行のインデックス。
- 行数: 削除する行の合計数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **複数の行を削除する方法**
複数の行をワークシートから削除するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) メソッドを呼び出します。 [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) は2つのパラメータを取ります：

- 行インデックス: 削除する行のインデックス。
- 行数: 削除する行の合計数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **1つまたは複数の列の挿入方法**
開発者は、任意の位置に列を挿入するために [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) メソッドを呼び出すこともできます。 [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) は二つのパラメータを取ります：

- 列インデックス: 挿入する列のインデックス
- 列数: 挿入する列の合計数

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **列を削除する方法**
任意の位置に列を削除するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) メソッドを呼び出します。[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) は以下のパラメータを取ります：

- 列インデックス: 削除する列のインデックス。
- 列数: 削除する列の合計数。
- 参照の更新: 他のワークシートで参照を更新するかどうかを示すブール値。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
