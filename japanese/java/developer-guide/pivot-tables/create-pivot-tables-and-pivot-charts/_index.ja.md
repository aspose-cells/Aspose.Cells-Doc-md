---
title: ピボットテーブルとピボットチャートの作成
type: docs
weight: 10
url: /ja/java/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Java API を使用してピボットテーブルおよびピボットチャートを作成する
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---

{{% alert color="primary" %}}

ピボットテーブルは、レコードのインタラクティブな集計です。たとえば、ワークシートのリストには数百の請求書エントリがあります。ピボットテーブルは、顧客、製品、または日付別に請求書を合計することができます。Microsoft Excelを使用すると、ピボットテーブル内の情報をボタンをドラッグするだけで素早く再配置することが可能です。

ピボットチャートは、ピボットテーブルのデータのインタラクティブなグラフィカルな表現です。ピボットチャートはExcel 2000で導入されました。ピボットテーブルが自動的に小計と合計を作成するため、ピボットチャートを使用することでデータを理解することがさらに容易になります。

Aspose.Cellsは[ピボットテーブル](/cells/ja/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table)および[ピボットチャート](/cells/ja/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table)をサポートしています。

{{% /alert %}}

## **ピボットテーブルとチャートの追加**

Aspose.Cellsは、ピボットテーブルを作成するために使用される特別なクラスセットを提供しています。これらのクラスは、PivotTableオブジェクトを作成し、設定するために使用されます。これらのオブジェクトはPivotTableオブジェクトの基本的な構成要素として機能します:

- PivotField、ピボットテーブルレポート内のフィールド。
- PivotFields、ピボットテーブル内のすべてのPivotFieldオブジェクトのコレクション。
- PivotTable、ワークシート上のPivotTableレポート。
- PivotTables、ワークシート上のすべてのPivotTableオブジェクトのコレクション。

### **Aspose.Cellsの使用準備**

1. Aspose.Cells.Zipをダウンロードしてインストールします。
   1. [Aspose.Cells for Javaをダウンロード](https://downloads.aspose.com/cells/java)します。
   1. 開発コンピュータにそれを解凍します。
      すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、生成された文書にウォーターマークしか挿入されません。
1. プロジェクトを作成します。
   1. EclipseなどのJavaエディタを使用してプロジェクトを作成するか、またはNotePadを使用して簡単なプログラムを作成します。
1. クラスパスを追加します。
   Eclipseを使用してクラスパスを設定するには:
   1. Aspose.Cells.zipからAspose.Cells.jarとdom4j_1.6.1.jarを抽出します。
   1. Eclipseでプロジェクトのクラスパスを設定します。
   1. Eclipseでプロジェクトを選択し、[Project-Properties]をクリックします。
   1. ポップアップウィンドウの左側で「Javaビルドパス」を選択し、[ライブラリ]タブを選択し、「JARの追加」または「外部JARの追加」をクリックして、Aspose.Cells.jarおよびdom4j_1.6.1.jarを選択し、それらをビルドパスに追加します。
   1. AsposeのコンポーネントのAPIを呼び出すアプリケーションを作成します。
      または、Windowsのdosプロンプトで実行時に設定することもできます。

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **ピボットテーブルの作成**

Aspose.Cellsを使用してピボットテーブルを作成するには:

1. CellオブジェクトのPutValue/setValueメソッドを使用してワークシートセルにデータを追加します。また、データがすでに入力されたテンプレートファイルを使用することもできます。これらのデータはピボットテーブルのデータソースとして使用されます。
1. PivotTablesコレクションのaddメソッド（Worksheetオブジェクトにカプセル化されています）を呼び出すことによって、ワークシートにピボットテーブルを追加します。
1. インデックスを渡してPivotTablesコレクションから新しいPivotTableオブジェクトにアクセスします。
1. PivotTableオブジェクトにカプセル化されたピボットテーブルのオブジェクトのいずれかを使用してテーブルを管理します。

下記のコードサンプルがあります。このコードを実行すると新しいファイル「pivotTable_test.xls」が生成されます。

**入力データ** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**出力のピボットテーブル**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **ピボットテーブルを基にしたピボットチャートの作成**

Aspose.Cellsを使用してピボットチャートを作成するには:

1. チャートを追加します。
1. グラフのPivotSourceを、スプレッドシート内の既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

以下は、コンポーネントがこのタスクを実行するために使用するコードです。このコードを実行すると、新しいファイル「pivotChart_test.xls」が生成されます。

ピボットチャートシート

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

この記事では、Aspose.Cellsを使用してピボットテーブルとピボットチャートを作成する方法を示しています。これにより、これらの機能を独自のシナリオで使用する際に役立つはずです。

Aspose.Cellsは、長年の研究、設計、そして注意深い調整の成果です。

[Aspose.Cellsフォーラム](https://forum.aspose.com/c/cells/9)でのお問い合わせ、コメント、提案を歓迎します。迅速な回答を保証します。

{{% /alert %}}

## 関連記事

- [ピボットテーブルのカスタムソート](/cells/ja/java/custom-sorting-in-pivot-table/)
- [ピボットテーブルの書式設定](/cells/ja/java/formatting-pivot-table/)
- [計算項目を持つピボットテーブルを更新および計算する](/cells/ja/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [ピボットテーブルリボンの無効化](/cells/ja/java/disable-pivot-table-ribbons/)

{{< app/cells/assistant language="java" >}}
