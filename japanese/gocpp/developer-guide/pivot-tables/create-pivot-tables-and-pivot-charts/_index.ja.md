---
title: Golang経由でC++を使ったピボットテーブルとピボットチャートの作成
linktitle: ピボットテーブルとピボットチャートの作成
type: docs
weight: 20
url: /ja/go-cpp/create-pivot-tables-and-pivot-charts/
description: Golang経由でC++を使用してAspose.CellsでExcelファイルのピボットテーブルとピボットチャートを作成する方法を学ぶ。
---

{{% alert color="primary" %}}

ピボットテーブルは、レコードの対話的な概要です。例えば、ワークシートのリストに数百の請求書エントリーがある場合、ピボットテーブルは顧客、製品、または日付で請求書の合計を表示できます。Microsoft Excelを使えば、ボタンをドラッグしてピボットテーブルの情報を素早く再配置可能です。

ピボットチャートは、ピボットテーブルのデータのインタラクティブなグラフィカルな表現です。ピボットチャートはExcel 2000で導入されました。ピボットテーブルが自動的に小計と合計を作成するため、ピボットチャートを使用することでデータを理解することがさらに容易になります。

Aspose.Cellsは [ピボットテーブル] (/cells/ja/cpp/create-pivot-tables-and-pivot-charts/) と [ピボットチャート] (/cells/ja/cpp/create-pivot-tables-and-pivot-charts/) をサポートします。

{{% /alert %}}

## **ピボットテーブルとチャートの追加**

Aspose.Cellsは、ピボットテーブルを作成するために使用される特別なクラスセットを提供しています。これらのクラスは、PivotTableオブジェクトを作成し、設定するために使用されます。これらのオブジェクトはPivotTableオブジェクトの基本的な構成要素として機能します:

- **PivotField**：ピボットテーブルレポート内のフィールド。
- **PivotFields**：ピボットテーブル内のすべてのPivotFieldオブジェクトのコレクション。
- **PivotTable**：ワークシート上のピボットテーブルレポート。
- **PivotTables**：ワークシート上のすべてのPivotTableオブジェクトのコレクション。

### **Aspose.Cellsの使用準備**

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [Aspose.Cellsをダウンロード](https://downloads.aspose.com/cells/go-cpp/).
   1. 開発コンピュータにインストールします。
      すべての [Aspose](http://www.aspose.com/) コンポーネントは、インストール時に評価モードで動作します。評価モードには時間制限はなく、生成されたドキュメントに透かしだけが入ります。コンポーネントを完全に使用するには、有効なライセンスが必要です。
1. プロジェクトを作成します。
   1. C++ IDE（例：Visual Studio）を起動します。
   1. 新しいコンソールアプリケーションを作成します。
1. 参照を追加します。
   プロジェクトに Aspose.Cells コンポーネントへの参照を追加します。例：`...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`。

### **ピボットテーブルの追加**

Aspose.Cellsを使用してピボットテーブルを作成するには:

1. `Cell` オブジェクトの `PutValue` メソッドを使ってワークシートのセルにデータを追加します。既にデータが入力されたテンプレートファイルを使うこともできます。データはピボットテーブルのデータソースとして使用されます。
1. `PivotTables` コレクションの `Add` メソッドを呼び出してワークシートにピボットテーブルを追加します（`Worksheet` オブジェクトにカプセル化されています）。
1. `PivotTables` コレクションから新しい `PivotTable` オブジェクトにアクセスし、そのインデックスを渡します。管理するために `PivotTable` オブジェクトにカプセル化された任意のピボットテーブルを使用します。

以下にコード例を示します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **ピボットチャートの追加**

Aspose.Cellsを使用してPivotChartを作成するには:

1. チャートを追加します。
1. グラフの `PivotSource` を既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
