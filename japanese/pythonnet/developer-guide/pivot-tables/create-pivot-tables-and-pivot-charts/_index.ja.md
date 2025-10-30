---
title: ピボットテーブルとピボットチャートの作成
type: docs
weight: 20
url: /ja/python-net/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Python via .NETを使用してピボットテーブルとピボットチャートを追加する方法
keywords: Aspose.Cells for Python Excelライブラリを使用して、Aspose.Cells for Python Excelライブラリを使用してピボットテーブルとピボットチャートを追加する
---

{{% alert color="primary" %}}

ピボットテーブルは、レコードのインタラクティブな集計です。たとえば、ワークシートのリストには数百の請求書エントリがあります。ピボットテーブルは、顧客、製品、または日付別に請求書を合計することができます。Microsoft Excelを使用すると、ピボットテーブル内の情報をボタンをドラッグするだけで素早く再配置することが可能です。

ピボットチャートは、ピボットテーブルのデータのインタラクティブなグラフィカルな表現です。ピボットチャートはExcel 2000で導入されました。ピボットテーブルが自動的に小計と合計を作成するため、ピボットチャートを使用することでデータを理解することがさらに容易になります。

Aspose.Cells for Python via .NET は [ピボットテーブル](/cells/ja/python-net/create-pivot-tables-and-pivot-charts/) と [ピボットチャート](/cells/ja/python-net/create-pivot-tables-and-pivot-charts/) をサポートしています。

{{% /alert %}}

## **Excel ライブラリの Aspose.Cells for Python によるピボットテーブルおよびチャートの追加**

Aspose.Cells for Python via .NET は、ピボットテーブルを作成するための特別なクラスのセットを提供しています。これらのクラスは、PivotTable オブジェクトを作成および設定するために使用され、PivotTable オブジェクトの基本的な構成要素として機能します:

- PivotField、ピボットテーブルレポート内のフィールド。
- PivotFields、ピボットテーブル内のすべてのPivotFieldオブジェクトのコレクション。
- PivotTable、ワークシート上のPivotTableレポート。
- PivotTables、ワークシート上のすべてのPivotTableオブジェクトのコレクション。

### **Aspose.Cells for Python via .NET の使用の準備**
1. [pypi](https://pypi.org/project/aspose-cells-python/) から Aspose.Cells for Python via .NET をインストールします。コマンドは次のとおりです: $ pip install aspose-cells-python。
1. 開発環境に “Aspose.Cells for Python via .NET” をインストールする手順については、ステップバイステップの手順に従うこともできます。


### **Aspose.Cells for Python Excel ライブラリを使用してピボットテーブルを追加する方法**

Aspose.Cells for Python via .NET を使用してピボットテーブルを作成するには:

1. Cell オブジェクトの put_value メソッドを使用してワークシートのセルにデータを追加します。また、データが入力済みのテンプレートファイルを使用することもできます。このデータは、ピボットテーブルのデータソースとして使用されます。
1. PivotTablesコレクションのaddメソッド（Worksheetオブジェクトにカプセル化されています）を呼び出すことによって、ワークシートにピボットテーブルを追加します。
1. ピボットテーブルの新しいPivotTableオブジェクトにアクセスするには、そのインデックスを渡してPivotTablesコレクションからアクセスします。#PivotTableオブジェクトにカプセル化されているピボットテーブルオブジェクトを使用して、テーブルを管理します。

以下にコード例を示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Aspsoe.Cells for Python Excel ライブラリを使用してピボットチャートを追加する方法**

Aspose.Cells for Python via .NET を使用してPivotChartを作成するには:

1. チャートを追加します。
1. グラフのPivotSourceを、スプレッドシート内の既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
