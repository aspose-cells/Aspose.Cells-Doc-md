---
title: セル名と行/列インデックスの変換
linktitle: セル名とインデックス変換
type: docs
weight: 5
url: /ja/java/names-and-indices/
description: Aspose.Cells for Java API を使用して、セル名と行/列のインデックスの変換結果を取得する方法を学ぶ。
keywords: Java でセルインデックスを名前に変換、セル名を行/列インデックスに変換するjava apis、セル名から行と列のインデックスを取得する方法。
---

## **行と列のインデックスからセル名を取得する方法**
行と列のインデックスを指定すると、セルの名前を見つけることが可能です。 この記事では、その方法について説明します。

Aspose.Cellsは、開発者が行と列のインデックスを指定することでセルの名前を取得できる[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-)メソッドを提供します。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1からカウントして開始します。Aspose.Cellsはこれに対して、0からカウントします。

{{% /alert %}} 

次のサンプルコードは、既知の行と列のインデックスを指定してセルの名前にアクセスするための[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-)の使い方を示しています。このコードは次の出力を生成します。

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **セル名から行と列のインデックスを取得する方法**
セルの名前から行と列のインデックスを見つけることが可能です。 この記事では、その方法について説明します。

Aspose.Cellsは、開発者がセルの名前から行と列のインデックスを取得できる[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-)メソッドを提供します。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1からカウントして開始します。Aspose.Cellsはこれに対して、0からカウントします。

{{% /alert %}} 

次のサンプルコードは、セルの名前から行と列のインデックスを取得するために[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-)を使用する例です。このコードは次の出力を生成します。

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **安全なシート名の作成方法**
時には、ランタイムでシート名を割り当てる必要があります。このシナリオでは、'<>+(?'のような追加文字が含まれる可能性のあるシート名があるかもしれません。シート名として許可されていない文字はユーザーが提供するあらかじめ設定された文字に置き換える必要があります。同様に、31文字を超える長さが増加する可能性があるため、切り捨てる必要があります。Apache POIは安全な名前を作成するための特定の機能を提供していますが、Aspose.Cellsではこれらの問題を処理するための類似した機能が提供されています。次のサンプルコードは、この機能を示しています。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**コンソール出力**

これは最初の名前です。

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
