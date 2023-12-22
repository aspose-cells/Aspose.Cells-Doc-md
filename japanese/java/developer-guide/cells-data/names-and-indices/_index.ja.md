---
title: セル名と行/列インデックス間の変換
linktitle: Cell 名前とインデックスの変換
type: docs
weight: 5
url: /ja/java/names-and-indices/
description: Aspose.Cells for Java API を使用してセル名と行/列インデックス間の変換結果を取得する方法を学びます。
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **行と列のインデックスから Cell の名前を取得する方法**
行と列のインデックスを指定すると、セルの名前を見つけることができます。この記事ではその方法を説明します。

 Aspose.Cells は、[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) メソッドを使用すると、開発者は行と列のインデックスを指定した場合にセルの名前を取得できます。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、使用方法を示しています。[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) 既知の行と列のインデックスで指定されたセルの名前にアクセスします。このコードは次の出力を生成します。



Cell [0, 0] の名前: A1

Cell [4, 0] の名前: A5

Cell [0, 4] の名前: E1

Cell [2, 2] の名前: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **Cell 名前から行と列のインデックスを取得する方法**
セルの名前からセルの行と列のインデックスを見つけることができます。この記事ではその方法を説明します。

 Aspose.Cells は、[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) メソッドを使用すると、開発者はセルの名前から行と列のインデックスを取得できます。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、使用方法を示しています。[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) セルの名前から行と列のインデックスを取得します。このコードは次の出力を生成します。



Cell C6 の行インデックス: 5

Cell C6 の列インデックス: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **セーフシート名の作成方法**
場合によっては、実行時にシート名を割り当てる必要があります。このシナリオでは、シート名に次のような追加文字が含まれる可能性があります。<>+(?”。シート名として許可されていないこのような文字は、ユーザーが指定したプリセット文字に置き換える必要があります。同様に、長さが 31 文字を超える場合があるため、切り詰める必要があります。Apache POI は、安全な名前を作成する特定の機能を提供するため、これらすべての問題を処理するために、同様の機能が Aspose.Cells によって提供されます。次のサンプル コードは、この機能を示しています。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**コンソール出力**

これはcreという名前です

` `<> (形容詞プライベート_「プライベート」
