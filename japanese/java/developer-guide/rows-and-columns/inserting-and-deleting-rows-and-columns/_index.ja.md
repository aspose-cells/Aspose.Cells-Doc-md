---
title: 行と列の挿入と削除
type: docs
weight: 60
url: /ja/java/inserting-and-deleting-rows-and-columns/
description: Aspose.Cells for Java API を使用して行と列を挿入および削除する方法を学習します。
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **導入**
新しいワークシートを最初から作成する場合でも、既存のワークシートで作業する場合でも、より多くのデータを収容するために行や列を追加する必要がある場合があります。逆に、ワークシート内の指定された位置から行または列を削除する必要がある場合もあります。

これらの要件を満たすために、Aspose.Cells は、以下で説明する非常に単純なクラスとメソッドのセットを提供します。
##  **行/列の管理方法**
Aspose.Cells は、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel ファイルを表すクラス。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシートコレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできるようになります。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスが提供するのは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)ワークシート内のすべてのセルを表すコレクション。

の[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションには、ワークシート内の行と列を管理するためのメソッドがいくつか用意されています。これらのいくつかについては以下で説明します。

{{% alert color="primary" %}} 

行または列を追加すると、ワークシート内のコンテンツは下または右に移動しますが、行または列を削除すると、コンテンツは上または左に移動します。

{{% /alert %}} 
##  **行を挿入する方法**
を呼び出して、任意の場所に行を挿入します。[行の挿入](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[行の挿入](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))メソッドは、最初の引数として新しい行が挿入される行のインデックスを受け取り、2番目の引数として挿入される行の数を受け取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **複数の行を挿入する方法**
ワークシートに複数の行を挿入するには、[行の挿入](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[行の挿入](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)メソッドは 2 つのパラメータを取ります。

- 行インデックス: 新しい行が挿入される行のインデックス。
- 行数: 挿入する必要がある行の合計数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **書式設定を使用して行を挿入する方法**
書式設定オプションを使用して行を挿入するには、[行の挿入](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)かかる過負荷[挿入オプション](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)パラメータとして。をセットする[コピーフォーマットタイプ](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)の財産[挿入オプション](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)とのクラス[コピーフォーマットタイプ](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)列挙。の[コピーフォーマットタイプ](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Enumeration には以下に示す 3 つのメンバーがあります。

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): 行を上記の行と同じ形式に設定します。
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): 行を以下の行と同じ形式に設定します。
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR)：書式設定をクリアします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **行を削除する方法**
任意の場所の行を削除するには、[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)メソッドは 2 つのパラメータを取ります。

- 行インデックス: 行が削除される行のインデックス。
- 行数: 削除する必要がある行の合計数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **複数の行を削除する方法**
ワークシートから複数の行を削除するには、[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[行の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)メソッドは 2 つのパラメータを取ります。

- 行インデックス: 行が削除される行のインデックス。
- 行数: 削除する必要がある行の合計数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **つまたは複数の列を挿入する方法**
開発者は、[挿入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[挿入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)メソッドは 2 つのパラメータを取ります。

- 列インデックス、列が挿入される列のインデックス
- 列の数、挿入する必要がある列の合計数

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **列を削除する方法**
ワークシートの任意の場所から列を削除するには、[列の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の[列の削除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)メソッドは次のパラメーターを受け取ります。

- 列インデックス: 列が削除される列のインデックス。
- 列数: 削除する必要がある列の合計数。
- 参照の更新: 他のワークシートの参照を更新するかどうかを示すブール パラメーター。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

