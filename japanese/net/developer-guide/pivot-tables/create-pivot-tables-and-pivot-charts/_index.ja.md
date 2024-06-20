---
title: ピボットテーブルとピボットチャートの作成
type: docs
weight: 20
url: /ja/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

ピボットテーブルは、レコードのインタラクティブな集計です。たとえば、ワークシートのリストには数百の請求書エントリがあります。ピボットテーブルは、顧客、製品、または日付別に請求書を合計することができます。Microsoft Excelを使用すると、ピボットテーブル内の情報をボタンをドラッグするだけで素早く再配置することが可能です。

ピボットチャートは、ピボットテーブルのデータのインタラクティブなグラフィカルな表現です。ピボットチャートはExcel 2000で導入されました。ピボットテーブルが自動的に小計と合計を作成するため、ピボットチャートを使用することでデータを理解することがさらに容易になります。

Aspose.Cellsは[pivot tables](/cells/ja/net/create-pivot-tables-and-pivot-charts/)と[pivot charts](/cells/ja/net/create-pivot-tables-and-pivot-charts/)をサポートしています。

{{% /alert %}}

## **ピボットテーブルとチャートの追加**

Aspose.Cellsは、ピボットテーブルを作成するために使用される特別なクラスセットを提供しています。これらのクラスは、PivotTableオブジェクトを作成し、設定するために使用されます。これらのオブジェクトはPivotTableオブジェクトの基本的な構成要素として機能します:

- PivotField、ピボットテーブルレポート内のフィールド。
- PivotFields、ピボットテーブル内のすべてのPivotFieldオブジェクトのコレクション。
- PivotTable、ワークシート上のPivotTableレポート。
- PivotTables、ワークシート上のすべてのPivotTableオブジェクトのコレクション。

### **Aspose.Cellsの使用準備**

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [Aspose.Cellsをダウンロード](https://downloads.aspose.com/cells/net)します。 
   1. 開発コンピュータにインストールします。
      すべての[Aspose](http://www.aspose.com/)コンポーネントはインストールされると評価モードで動作します。評価モードには時間制限はなく、生成されたドキュメントにウォーターマークが注入されるのみです。コンポーネントをフル機能で使用するには、有効なライセンスが必要です。
1. プロジェクトを作成します。
   1. Visual Studio.Net を起動します。
   1. 新しいコンソールアプリケーションを作成します。
1. 参照を追加します。
   Aspose.Cellsコンポーネントをプロジェクトに参照として追加します。たとえば...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **ピボットテーブルの追加**

Aspose.Cellsを使用してピボットテーブルを作成するには:

1. CellオブジェクトのPutValue/setValueメソッドを使用してワークシートセルにデータを追加します。また、データがすでに入力されたテンプレートファイルを使用することもできます。これらのデータはピボットテーブルのデータソースとして使用されます。
1. PivotTablesコレクションのaddメソッド（Worksheetオブジェクトにカプセル化されています）を呼び出すことによって、ワークシートにピボットテーブルを追加します。
1. ピボットテーブルの新しいPivotTableオブジェクトにアクセスするには、そのインデックスを渡してPivotTablesコレクションからアクセスします。#PivotTableオブジェクトにカプセル化されているピボットテーブルオブジェクトを使用して、テーブルを管理します。

以下にコード例を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **ピボットチャートの追加**

Aspose.Cellsを使用してPivotChartを作成するには:

1. チャートを追加します。
1. グラフのPivotSourceを、スプレッドシート内の既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

