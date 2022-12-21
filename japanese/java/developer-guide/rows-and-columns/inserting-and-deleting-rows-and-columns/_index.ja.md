---
title: 行と列の挿入と削除
type: docs
weight: 60
url: /ja/java/inserting-and-deleting-rows-and-columns/
---
## **序章**
新しいワークシートをゼロから作成する場合でも、既存のワークシートで作業する場合でも、より多くのデータを収容するために余分な行または列を追加する必要がある場合があります。逆に、ワークシートの指定された位置から行または列を削除する必要がある場合もあります。

これらの要件を満たすために、Aspose.Cells は、以下で説明する非常に単純なクラスとメソッドのセットを提供します。
## **行/列の管理**
Aspose.Cells は[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)ワークシート内のすべてのセルを表すコレクション。

の[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションには、ワークシートの行と列を管理するためのメソッドがいくつか用意されています。これらのいくつかを以下で説明します。

{{% alert color="primary" %}} 

行または列が追加されると、ワークシートのコンテンツは下または右にシフトされますが、行または列が削除されると、コンテンツは上または左にシフトされます。

{{% /alert %}} 
## **行の挿入**
を呼び出して、任意の場所に行を挿入します。[挿入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[挿入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))method は、新しい行が挿入される行のインデックスを最初の引数として取り、挿入される行の数を 2 番目の引数として取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **複数行の挿入**
ワークシートに複数の行を挿入するには、[挿入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[挿入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) メソッドは 2 つのパラメーターを取ります。

- 行インデックス: 新しい行が挿入される行のインデックス。
- 行数: 挿入する必要がある行の総数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **書式を設定して行を挿入する**
書式設定オプションを含む行を挿入するには、[挿入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) かかるオーバーロード[挿入オプション](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)パラメータとして。をセットする[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)のプロパティ[挿入オプション](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)クラス[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)列挙。の[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Enumeration には、以下に示す 3 つのメンバーがあります。

- [同じ_なので_その上](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)上記の行と同じように行をフォーマットします。
- [同じ_なので_未満](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW)下の行と同じように行をフォーマットします。
- [クリア](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR)フォーマットをクリアします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **行の削除**
任意の場所で行を削除するには、[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) メソッドは 2 つのパラメーターを取ります。

- 行インデックス: 行が削除される行のインデックス。
- 行数: 削除する必要がある行の総数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **複数行の削除**
ワークシートから複数の行を削除するには、[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) メソッドは 2 つのパラメーターを取ります。

- 行インデックス: 行が削除される行のインデックス。
- 行数: 削除する必要がある行の総数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **1 つまたは複数の列の挿入**
開発者は、を呼び出して、ワークシートの任意の場所に列を挿入することもできます[挿入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[挿入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) メソッドは 2 つのパラメーターを取ります。

- 列インデックス、列が挿入される列のインデックス
- 列数、挿入する必要がある列の総数

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **列の削除**
ワークシートの任意の場所から列を削除するには、[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)メソッドは、次のパラメーターを取ります。

- 列インデックス: 列が削除される列のインデックス。
- 列数: 削除する必要がある列の総数。
- 参照の更新: 他のワークシートの参照を更新するかどうかを示すブール値パラメーター。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

