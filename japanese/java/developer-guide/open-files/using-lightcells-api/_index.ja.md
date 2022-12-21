---
title: LightCells の使用 API
type: docs
weight: 80
url: /ja/java/using-lightcells-api/
---
{{% alert color="primary" %}}

場合によっては、ワークシート内の膨大なデータまたはコンテンツのリストを含む大きな Microsoft Excel ファイルを読み書きする必要があります。 LightCells API は、巨大な Excel スプレッドシートを作成するのに役立ちます。これを使用すると、メモリが必要になり、パフォーマンスと効率が向上します。

{{% /alert %}}

## **イベント駆動型アーキテクチャ**

Aspose.Cells は LightCells API を提供します。これは主に、(Cell コレクションなどを使用して) 完全なデータ モデル ブロックをメモリに構築することなく、セル データを 1 つずつ操作するように設計されています。イベント駆動モードで動作します。

ワークブックを保存するには、保存時にセルの内容をセルごとに提供し、コンポーネントはそれを出力ファイルに直接保存します。

テンプレート ファイルを読み取るとき、コンポーネントはすべてのセルを解析し、その値を 1 つずつ提供します。

どちらの手順でも、1 つの Cell オブジェクトが処理されてから破棄され、Workbook オブジェクトはコレクションを保持しません。したがって、このモードでは、Microsoft 大量のメモリを使用する大規模なデータ セットを含む Excel ファイルをインポートおよびエクスポートするときに、メモリが節約されます。

LightCells API は、XLSX ファイルと XLS ファイルに対して同じ方法でセルを処理しますが (実際にはすべてのセルをメモリにロードするのではなく、1 つのセルを処理してから破棄します)、XLS ファイルよりも XLSX ファイルの方がメモリを効果的に節約できます。 2 つの形式の異なるデータ モデルと構造。

でも、**XLS ファイル用**、より多くのメモリを節約するために、開発者は、保存プロセス中に生成された一時データを保存するための一時的な場所を指定できます。一般的に、**LightCells API を使用して XLSX ファイルを保存すると、50% 以上のメモリを節約できる場合があります**一般的な方法を使用するよりも、**XLS を保存すると、約 20 ～ 40% のメモリを節約できます**.

### **大きな Excel ファイルの書き込み**

Aspose.Cells は、プログラムに実装する必要があるインターフェイス LightCellsDataProvider を提供します。インターフェイスは、軽量モードで大きなスプレッドシート ファイルを保存するためのデータ プロバイダーを表します。

このモードでワークブックを保存する場合、ワークブック内のすべてのワークシートを保存するときに startSheet(int) がチェックされます。 1 つのシートの場合、startSheet(int) が true の場合、保存されるこのシートの行とセルのすべてのデータとプロパティは、この実装によって提供されます。まず、保存する次の行インデックスを取得するために nextRow() が呼び出されます。有効な行インデックスが返された場合 (行を保存するには行インデックスが昇順である必要があります)、この行を表す Row オブジェクトが実装用に提供され、startRow(Row) によってそのプロパティを設定します。

1 つの行については、 nextCell() が最初にチェックされます。有効な列インデックスが返された場合 (1 行のすべてのセルを保存するには、列インデックスが昇順である必要があります)、このセルを表す Cell オブジェクトが提供され、startCell(Cell) によってデータとプロパティが設定されます。このセルのデータが設定されると、このセルは生成されたスプレッドシート ファイルに直接保存され、次のセルがチェックされて処理されます。

次の例は、LightCells API がどのように機能するかを示しています。

次のプログラムは、データで満たされたワークシートに 100,000 レコードを含む巨大なファイルを作成します。ワークシートの特定のセルにハイパーリンク、文字列値、数値、および数式を追加しました。さらに、セルの範囲もフォーマットしました。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **大きな Excel ファイルの読み取り**

Aspose.Cells は、プログラムに実装する必要があるインターフェイス LightCellsDataHandler を提供します。インターフェイスは、軽量モードで大きなスプレッドシート ファイルを読み取るためのデータ プロバイダーを表します。

このモードでワークブックを読み取る場合、ワークブック内のすべてのワークシートを読み取るときに startSheet() がチェックされます。シートの場合、startSheet() が true を返す場合、シートの行と列のセルのすべてのデータとプロパティがチェックされ、処理されます。行ごとに startRow() が呼び出され、処理が必要かどうかが確認されます。行を処理する必要がある場合、行のプロパティが最初に読み取られ、開発者は processRow() を使用してそのプロパティにアクセスできます。

行のセルも処理する必要がある場合、processRow() は true を返し、行内の既存のすべてのセルに対して startCell() が呼び出され、処理が必要かどうかが確認されます。存在する場合、processCell() が呼び出されます。

次のサンプル コードは、このプロセスを示しています。プログラムは、何百万ものレコードを含む大きなファイルを読み取ります。ワークブックの各シートを読み取るには、少し時間がかかります。サンプル コードはファイルを読み取り、各ワークシートのセルの総数、文字列の数、および数式の数を取得します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

LightCellsDataHandler インターフェイスを実装するクラス

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
