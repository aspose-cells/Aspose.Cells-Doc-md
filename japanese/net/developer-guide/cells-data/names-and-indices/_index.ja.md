---
title: セル名と行/列インデックス間の変換
linktitle: Cell 名前とインデックスの変換
type: docs
weight: 10
url: /ja/net/names-and-indices/
description: Aspose.Cells for .NET API を通じてセル名と行/列インデックス間の変換を取得する方法を学びます。
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
---
##  **行と列のインデックスから Cell の名前を取得する**
行と列のインデックスを指定すると、セルの名前を見つけることができます。この記事ではその方法を説明します。
Aspose.Cells は、開発者が行と列のインデックスを指定した場合にセルの名前を取得できるようにする CellsHelper.CellIndexToName メソッドを提供します。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、CellsHelper.CellIndexToName を使用して、既知の行インデックスと列インデックスを指定してセルの名前にアクセスする方法を示しています。このコードは次の出力を生成します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
##  **Cell 名前から行と列のインデックスを取得**
セルの名前からセルの行と列のインデックスを見つけることができます。この記事ではその方法を説明します。
Aspose.Cells は、開発者がセルの名前から行と列のインデックスを取得できるようにする CellsHelper.CellNameToIndex メソッドを提供します。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、CellsHelper.CellNameToIndex を使用してセルの名前から行と列のインデックスを取得する方法を示しています。このコードは次の出力を生成します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
##  **セーフシート名の作成**
場合によっては、実行時にシート名を割り当てる必要があります。このシナリオでは、シート名に次のような追加文字が含まれる可能性があります。<>+(?”。シート名として許可されていないこのような文字は、ユーザーが指定したプリセット文字に置き換える必要があります。同様に、長さが 31 文字を超える場合があるため、切り詰める必要があります。Apache POI は、安全な名前を作成する特定の機能があるため、これらすべての問題を処理するために、Aspose.Cells によって同様の機能が提供されています。次のサンプル コードは、この機能を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

出力：

これはcreという名前です

` `<> (形容詞プライベート_「プライベート」
