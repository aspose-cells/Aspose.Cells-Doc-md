---
title: ピボットテーブルとピボットチャートを作成する
type: docs
weight: 20
url: /ja/python-net/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Python via .NET を使用してピボット テーブルとピボット チャートを追加する方法。
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

ピボット テーブルは、レコードのインタラクティブな要約です。たとえば、ワークシートのリストに数百もの請求書エントリがあるとします。ピボット テーブルを使用すると、顧客、製品、または日付ごとに請求書を合計できます。 Microsoft Excel では、ボタンを新しい位置にドラッグすることで、ピボット テーブル内の情報をすばやく再配置することができます。

ピボット チャートは、ピボット テーブル内のデータを対話的にグラフィカルに表現したものです。ピボット グラフは Excel 2000 で導入されました。ピボット グラフを使用すると、ピボット テーブルで小計と合計が自動的に作成されるため、データをさらに理解しやすくなります。

 Aspose.Cells for Python via .NET をサポートします[ピボットテーブル](/cells/ja/python-net/create-pivot-tables-and-pivot-charts/)そして[ピボット チャート](/cells/ja/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **ピボットテーブルとグラフの追加**

Aspose.Cells for Python via .NET は、ピボット テーブルの作成に使用される特別なクラスのセットを提供します。これらのクラスは、ピボットテーブル オブジェクトの基本的な構成要素として機能するピボットテーブル オブジェクトの作成と設定に使用されます。

- ピボットフィールド、ピボット テーブル レポートのフィールド。
- PivotFields: ピボット テーブル内のすべての PivotField オブジェクトのコレクション。
- ピボットテーブル、ワークシート上のピボットテーブル レポート。
- ピボットテーブル: ワークシート上のすべてのピボットテーブル オブジェクトのコレクション。

###  **使用の準備中 Aspose.Cells for Python via .NET**
1.  Aspose.Cells for Python via .NET をからインストールします[ピピ](https://pypi.org/project/aspose-cells-python/)、コマンドを $ pip install aspose-cells-python として使用します。
1. 「Aspose.Cells for Python via .NET」を開発者環境にインストールする方法に関する段階的な手順に従うこともできます。


###  **ピボットテーブルの追加**

Aspose.Cells for Python via .NET を使用してピボット テーブルを作成するには:

1. Cell オブジェクトの put_value メソッドを使用して、ワークシートのセルにデータを追加します。すでにデータが入力されているテンプレート ファイルを使用することもできます。データはピボット テーブルのデータ ソースとして使用されます。
1. PivotTables コレクションの add メソッド (Worksheet オブジェクトにカプセル化されている) を呼び出して、ピボット テーブルをワークシートに追加します。
1. インデックスを渡すことにより、ピボットテーブル コレクションから新しいピボットテーブル オブジェクトにアクセスします。 # PivotTable オブジェクトにカプセル化されたピボット テーブル オブジェクトのいずれかを使用してテーブルを管理します。

コード例を以下に示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **ピボット チャートの追加**

Aspose.Cells for Python via .NET を使用してピボットグラフを作成するには:

1. グラフを追加します。
1. スプレッドシート内の既存のピボット テーブルを参照するようにグラフの PivotSource を設定します。
1. 他の属性を設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

