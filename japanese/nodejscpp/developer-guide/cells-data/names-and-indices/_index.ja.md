---
title: セル名と行/列インデックスの変換
linktitle: セル名とインデックス変換
type: docs
weight: 10
url: /ja/nodejs-cpp/names-and-indices/
description: セル名と行/列インデックス間の変換をAspose.Cells for Node.js via C++ APIを通じて学ぶ。
keywords: Node.js C++からセルの行と列のインデックスからセル名を取得、セル名から行と列のインデックスを取得、安全なシート名を作成、シート名を追加。
---

## **行と列のインデックスからセル名を取得**
行と列のインデックスを指定すると、セルの名前を見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells for Node.js via C++は、CellsHelper.cellIndexToNameメソッドを提供し、行と列のインデックスを提供すれば、セルの名前を取得できます。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1から数え始めます。これに対し、Aspose.Cells for Node.js via C++は0から数え始めます。

{{% /alert %}} 

以下のサンプルコードは、CellsHelper.cellIndexToNameを使用して、既知の行と列のインデックスからセルの名前にアクセスする方法を示しています。コードの出力例：



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **セル名から行と列のインデックスを取得**
セルの名前から行と列のインデックスを見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells for Node.js via C++は、CellsHelper.cellNameToIndexメソッドを提供し、これによりセルの名前から行と列のインデックスを取得できます。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1から数え始めます。これに対し、Aspose.Cells for Node.js via C++は0から数え始めます。

{{% /alert %}} 

以下のサンプルコードは、CellsHelper.cellNameToIndexを使用して、セルの名前から行と列のインデックスを取得する方法を示しています。コードは次の出力を生成します。



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **安全なシート名を作成します。**
時には実行時にシート名を割り当てる必要があります。このシナリオでは、<>,+,(?”, などの追加文字を含むシート名が存在する場合があります。これらの文字はシート名として許可されていないため、それらの文字をユーザーが提供した事前設定の文字に置き換える必要があります。同様に、長さが31文字を超える場合は切り捨てる必要があります。Apache POIは安全な名前を作成するいくつかの機能を提供しており、同様の機能はAspose.Cells for Node.js via C++によってこれらの問題を処理するために提供されています。以下のサンプルコードはこの機能を示しています。



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

出力:

これは最初の名前です。

` <> + (形容詞Private _ " Private"
{{< app/cells/assistant language="nodejs-cpp" >}}
