---
title: ピボット テーブルとピボット チャートを作成する
type: docs
weight: 10
url: /ja/java/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Java API でピボット テーブルとピボット グラフを作成します。
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

ピボット テーブルは、レコードのインタラクティブな要約です。たとえば、ワークシートのリストに何百もの請求書エントリがあるとします。ピボット テーブルは、顧客、製品、または日付ごとに請求書を合計できます。 Microsoft Excel では、ボタンを新しい位置にドラッグすることで、ピボット テーブル内の情報をすばやく再配置できます。

ピボット チャートは、ピボット テーブル内のデータをインタラクティブにグラフィカルに表現したものです。ピボット グラフは、Excel 2000 で導入されました。ピボット テーブルを使用すると、小計と合計が自動的に作成されるため、データをさらに理解しやすくなります。

 Aspose.Cells サポート[ピボットテーブル](/cells/ja/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table)と[ピボット チャート](/cells/ja/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **ピボット テーブルとグラフの追加**

Aspose.Cells は、ピボット テーブルの作成に使用されるクラスの特別なセットを提供します。これらのクラスは、PivotTable オブジェクトの基本的な構成要素として機能する PivotTable オブジェクトを作成および設定するために使用されます。

- ピボット テーブル レポートのフィールドである PivotField。
- ピボット テーブル内のすべての PivotField オブジェクトのコレクションである PivotFields。
- ピボットテーブル、ワークシート上のピボットテーブル レポート。
- ワークシート上のすべての PivotTable オブジェクトのコレクションである PivotTables。

### **利用準備中 Aspose.Cells**

1. Aspose.Cells.Zip をダウンロードしてインストールします。
   1. [ダウンロード Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 開発用コンピューターで解凍します。
全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。
1. プロジェクトを作成する
 1. Eclipse などの Java エディタを使用してプロジェクトを作成するか、メモ帳を使用して簡単なプログラムを作成することができます。
1. クラスパスを追加:
 Eclipse を使用してクラスパスを設定するには:
1. Aspose.Cells.zip から Aspose.Cells.jar と dom4j_1.6.1.jar を抽出します。
 1. Eclipse でプロジェクトのクラスパスを設定します。
1. Eclipse でプロジェクトを選択し、メニューの [Project] - [Properties] をクリックします。
 1. ポップアップ ウィンドウの左側で [Java Build Path] を選択し、[Libraries] タブを選択し、[Add JARs] または [Add External JARs] をクリックして Aspose.Cells.jar と dom4j_1.6.1.jar を選択して追加します。ビルドパスに。
 1. Aspose のコンポーネントの API を呼び出すアプリケーションを作成します。
または、Windows の dos プロンプトで実行時に設定することもできます。

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **ピボット テーブルの作成**

Aspose.Cells を使用してピボット テーブルを作成するには:

1. Cell オブジェクトの PutValue/setValue メソッドを使用して、ワークシートのセルにデータを追加します。また、既にデータが入力されているテンプレート ファイルも使用します。データは、ピボット テーブルのデータ ソースとして使用されます。
1. PivotTables コレクションの add メソッド (Worksheet オブジェクトにカプセル化されている) を呼び出して、ワークシートにピボット テーブルを追加します。
1. インデックスを渡して、PivotTables コレクションから新しい PivotTable オブジェクトにアクセスします。
1. PivotTable オブジェクトにカプセル化されたピボット テーブル オブジェクトのいずれかを使用して、テーブルを管理します。

コードサンプルを以下に示します。コードを実行すると、pivotTable_test.xls という新しいファイルが生成されます。

**入力データ** 

![todo:画像_代替_文章](create-pivot-tables-and-pivot-charts_1.png)

**出力ピボット テーブル**

![todo:画像_代替_文章](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **ピボット テーブルに基づいてピボット グラフを作成する**

Aspose.Cells を使用してピボット チャートを作成するには:

1. グラフを追加します。
1. チャートの PivotSource を設定して、スプレッドシート内の既存のピボット テーブルを参照します。
1. その他の属性を設定します。

以下は、タスクを実行するためにコンポーネントによって使用されるコードです。コードを実行すると、pivotChart_test.xls という新しいファイルが生成されます。

**ピボット チャート シート**

![todo:画像_代替_文章](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

この記事では、Aspose.Cells を使用してピボット テーブルとピボット グラフを作成する方法を示します。これらの機能を独自のシナリオで使用するのに役立つことを願っています。

Aspose.Cells は、何年にもわたる研究、設計、慎重な調整の恩恵を受けてきました。

ご質問、ご意見、ご提案は、[Aspose.Cells フォーラム](https://forum.aspose.com/c/cells/9).迅速な返信を保証します。

{{% /alert %}}

## 関連記事

- [ピボット テーブルでのカスタム並べ替え](/cells/ja/java/custom-sorting-in-pivot-table/)
- [ピボット テーブルの書式設定](/cells/ja/java/formatting-pivot-table/)
- [計算項目を含むピボット テーブルの更新と計算](/cells/ja/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [ピボット テーブル リボンを無効にする](/cells/ja/java/disable-pivot-table-ribbons/)

