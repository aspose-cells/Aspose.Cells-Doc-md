---
title: セル名と行/列インデックスの変換
linktitle: セル名とインデックス変換
type: docs
weight: 10
url: /ja/net/names-and-indices/
description: Aspose.Cells for .NET API を通じてセル名と行/列インデックスの変換方法を学びます。
keywords: 行および列のインデックスからセル名を取得する、セル名から行および列のインデックスを取得する、安全なワークシート名を作成する、安全なワークシート名を追加する
---

## **行と列のインデックスからセル名を取得**
行と列のインデックスを指定すると、セルの名前を見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells は CellsHelper.CellIndexToName メソッドを提供し、開発者が行および列のインデックスを提供するとセルの名前を取得できるようにします。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1から数えます。Microsoft Excelとは異なり、Aspose.Cellsは行と列のインデックスを0から数えます。

{{% /alert %}} 

以下のサンプルコードは、CellsHelper.CellIndexToName を使用して既知の行および列インデックスからセルの名前にアクセスする方法を示しています。コードは以下の出力を生成します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **セル名から行と列のインデックスを取得**
セルの名前から行と列のインデックスを見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells は CellsHelper.CellNameToIndex メソッドを提供し、開発者がセルの名前から行および列のインデックスを取得できるようにします。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1から数えます。Microsoft Excelとは異なり、Aspose.Cellsは行と列のインデックスを0から数えます。

{{% /alert %}} 

以下のサンプルコードは、CellsHelper.CellNameToIndex を使用してセルの名前から行および列のインデックスを取得する方法を示しています。コードは以下の出力を生成します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **安全なシート名を作成します。**
ランタイムでシート名を割り当てる必要がある場合があります。このシナリオでは、<>+(?”のような追加の文字が含まれる場合があります。シート名として許可されていない文字を特定のユーザーによって提供された事前設定文字で置き換える必要があります。同様に、31文字を超える長さになる可能性があるため、これを切り詰める必要があります。Apache POI は安全な名前を作成する特定の機能を提供しています。これらの問題をすべて処理するために、Aspose.Cells によって同様の機能が提供されています。次のサンプルコードはこの機能を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

出力:

これは最初の名前です。

` <> + (形容詞Private _ " Private"
