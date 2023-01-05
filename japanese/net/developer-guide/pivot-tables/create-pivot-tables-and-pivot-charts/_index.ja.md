---
title: ピボット テーブルとピボット チャートを作成する
type: docs
weight: 20
url: /ja/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

ピボット テーブルは、レコードのインタラクティブな要約です。たとえば、ワークシートのリストに何百もの請求書エントリがあるとします。ピボット テーブルは、顧客、製品、または日付ごとに請求書を合計できます。 Microsoft Excel では、ボタンを新しい位置にドラッグすることで、ピボット テーブル内の情報をすばやく再配置できます。

ピボット チャートは、ピボット テーブル内のデータをインタラクティブにグラフィカルに表現したものです。ピボット グラフは、Excel 2000 で導入されました。ピボット テーブルを使用すると、小計と合計が自動的に作成されるため、データをさらに理解しやすくなります。

 Aspose.Cells サポート[ピボットテーブル](/cells/ja/net/create-pivot-tables-and-pivot-charts/)と[ピボット チャート](/cells/ja/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **ピボット テーブルとグラフの追加**

Aspose.Cells は、ピボット テーブルの作成に使用されるクラスの特別なセットを提供します。これらのクラスは、PivotTable オブジェクトの基本的な構成要素として機能する PivotTable オブジェクトを作成および設定するために使用されます。

- ピボット テーブル レポートのフィールドである PivotField。
- ピボット テーブル内のすべての PivotField オブジェクトのコレクションである PivotFields。
- ピボットテーブル、ワークシート上のピボットテーブル レポート。
- ワークシート上のすべての PivotTable オブジェクトのコレクションである PivotTables。

### **利用準備中 Aspose.Cells**

1. Aspose.Cells をダウンロードしてインストールします。
   1. [ダウンロード Aspose.Cells](https://downloads.aspose.com/cells/net).
 1. 開発用コンピューターにインストールします。
全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。コンポーネントを最大限に活用するには、有効なライセンスが必要です。
1. プロジェクトを作成します。
 1. Visual Studio.Net を起動します。
 1. 新しいコンソール アプリケーションを作成します。
1. 参照を追加します。
 Aspose.Cells コンポーネントへの参照をプロジェクトに追加します。例: ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **ピボット テーブルの追加**

Aspose.Cells を使用してピボット テーブルを作成するには:

1. Cell オブジェクトの PutValue/setValue メソッドを使用して、ワークシートのセルにデータを追加します。また、既にデータが入力されているテンプレート ファイルも使用します。データは、ピボット テーブルのデータ ソースとして使用されます。
1. PivotTables コレクションの add メソッド (Worksheet オブジェクトにカプセル化されている) を呼び出して、ワークシートにピボット テーブルを追加します。
1. インデックスを渡して、PivotTables コレクションから新しい PivotTable オブジェクトにアクセスします。 # PivotTable オブジェクトにカプセル化されたピボット テーブル オブジェクトのいずれかを使用して、テーブルを管理します。

コード例を以下に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **ピボット チャートの追加**

Aspose.Cells を使用してピボットグラフを作成するには:

1. グラフを追加します。
1. チャートの PivotSource を設定して、スプレッドシート内の既存のピボット テーブルを参照します。
1. その他の属性を設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

