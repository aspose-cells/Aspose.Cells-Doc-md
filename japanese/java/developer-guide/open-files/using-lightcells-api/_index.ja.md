---
title: LightCells APIの使用
type: docs
weight: 80
url: /ja/java/using-lightcells-api/
---

{{% alert color="primary" %}}

大量のデータやコンテンツを持つ巨大なExcelスプレッドシートの読み込みや書き込みを行う場合、LightCells APIは役立ちます。これにより、メモリが必要となり、パフォーマンスと効率が向上します。

{{% /alert %}}

## **イベント駆動型アーキテクチャ**

Aspose.Cellsは、セルのコレクションなどの完全なデータモデルブロックをメモリに構築せずに、イベント駆動モードでセルデータを1つずつ操作するために、LightCells APIを提供しています。

ワークブックを保存するには、セルの内容を1つずつ提供し、コンポーネントがそれを直接出力ファイルに保存します。

テンプレートファイルを読み込む際に、コンポーネントはすべてのセルを解析し、その値を1つずつ提供します。

両手順ともに、1つのCellオブジェクトが処理され、その後破棄され、Workbookオブジェクトはコレクションを保持しません。そのため、このモードでは、大規模なデータセットを持つMicrosoft Excelファイルのインポートおよびエクスポート時にメモリを節約することができます。

LightCells APIは、XLSXファイルとXLSファイルでセルを同じように処理します（実際にはすべてのセルをメモリに読み込むのではなく、1つのセルを処理してから破棄します）が、XLSXファイルではXLSファイルよりもメモリを効果的に節約します。これは2つのフォーマットの異なるデータモデルと構造のためです。

ただし、**XLSファイル**の場合、より多くのメモリを節約するには、開発者が保存プロセス中に生成される一時データの保存に一時的な場所を指定することができます。通常、**LightCells APIを使用してXLSXファイルを保存する場合、約50%以上のメモリを節約**できますが、**XLSを保存する場合は20-40%のメモリを節約**できます。

### **大きなExcelファイルの書き込み**

Aspose.CellsはLightCellsDataProviderというインタフェースを提供しており、プログラムに実装する必要があります。このインタフェースは、軽量モードで大きなスプレッドシートファイルを保存するためのデータプロバイダを表します。

このモードでワークブックを保存する際、ワークブック内の各ワークシートを保存する際にstartSheet(int)がチェックされます。1枚のシートについて、startSheet(int)がtrueの場合、この実装によって保存するシートの行とセルのすべてのデータとプロパティが提供されます。最初に、nextRow()が呼び出されて保存する次の行インデックスを取得します。有効な行インデックスが返されると（行インデックスは保存する行の順序にする必要があります）、この行を表すRowオブジェクトが、そのプロパティを設定するためにstartRow(Row)によって提供されます。

1行に対して、まずnextCell()がチェックされます。有効な列インデックスが返されると（1行のすべてのセルの列インデックスは保存するために昇順にする必要があります）、このセルを表すCellオブジェクトがstartCell(Cell)によって提供されてデータとプロパティを設定することができます。このセルのデータが設定された後、このセルは直接生成されたスプレッドシートファイルに保存され、次のセルがチェックおよび処理されます。

次の例では、LightCells APIの動作を示しています。

次のプログラムは、データで満たされたワークシートに10万レコードを持つ巨大なファイルを作成します。ワークシートには、特定のセルにハイパーリンク、文字列値、数値値、また一部のセルには数式も追加されます。さらに、セルの範囲にも書式が設定されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **大きなExcelファイルの読み取り**

Aspose.Cellsは、プログラムに実装する必要があるLightCellsDataHandlerというインタフェースを提供しています。このインタフェースは、軽量モードで大きなスプレッドシートファイルを読み込むためのデータプロバイダを表します。

このモードでワークブックを読み込む際、ワークブック内の各ワークシートを読み込む際にstartSheet()がチェックされます。シートに対して、startSheet()がtrueを返すと、シートのすべての行と列のセルのデータとプロパティがチェックされて処理されます。各行に対して、まずstartRow()が呼び出され、それを処理する必要があるかどうかをチェックします。行を処理する必要がある場合、まず行のプロパティが読み込まれ、processRow()を使用してそのプロパティにアクセスできます。

行のセルも処理する必要がある場合、processRow()はtrueを返し、行内のすべてのセルに対してstartCell()が呼び出され、それを処理する必要があるかどうかをチェックします。それを処理する必要がある場合は、processCell()が呼び出されます。

次のサンプルコードは、このプロセスを説明しています。プログラムは数百万のレコードを持つ大きなファイルを読み込みます。ワークブック内の各シートを読み込むのに少し時間がかかります。サンプルコードはファイルを読み込み、各ワークシートごとの合計セル数、文字列のカウントおよび数式のカウントを取得します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

LightCellsDataHandlerインタフェースを実装するクラス

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
