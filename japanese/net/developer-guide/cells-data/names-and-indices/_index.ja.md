---
title: セル名と行/列インデックス間の変換
linktitle: Cell 名前とインデックスの変換
type: docs
weight: 10
url: /ja/net/names-and-indices/
---
## **行と列のインデックスから Cell の名前を取得**
行と列のインデックスがあれば、セルの名前を見つけることができます。この記事では、その方法について説明します。
Aspose.Cells は、CellsHelper.CellIndexToName メソッドを提供します。これにより、開発者は、行と列のインデックスを提供する場合にセルの名前を取得できます。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、CellsHelper.CellIndexToName を使用して、既知の行と列のインデックスを指定してセルの名前にアクセスする方法を示しています。コードは次の出力を生成します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Cell 名前から行と列のインデックスを取得**
名前からセルの行と列のインデックスを見つけることができます。この記事では、その方法について説明します。
Aspose.Cells は、開発者がセルの名前から行と列のインデックスを取得できるようにする CellsHelper.CellNameToIndex メソッドを提供します。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、CellsHelper.CellNameToIndex を使用して、セルの名前から行と列のインデックスを取得する方法を示しています。コードは次の出力を生成します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **安全なシート名を作成する**
実行時にシート名を割り当てる必要がある場合があります。このシナリオでは、シート名に次のような追加の文字が含まれる場合があります。<>+(?”. シート名として許可されていないそのような文字は、ユーザーが提供するプリセット文字に置き換える必要があります. 同様に、長さが 31 文字を超える可能性があり、切り詰める必要があります. Apache POI は提供します安全な名前を作成する特定の機能, したがって、同様の機能が Aspose.Cells によって提供され、これらすべての問題を処理します. 次のサンプル コードは、この機能を示しています:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

出力：

これは名前です。

` `<> + (adj.プライベート_「プライベート」
