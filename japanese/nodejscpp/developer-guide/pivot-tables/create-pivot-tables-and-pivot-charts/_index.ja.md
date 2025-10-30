---
title: ピボットテーブルとピボットチャートの作成
type: docs
weight: 20
url: /ja/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Node.js via C++を使用してピボットテーブルとピボットチャートを追加する方法。
keywords: Aspose.Cells for Node.js via C++ Excel、Excel Node.jsライブラリを使用して、ピボットテーブルとピボットチャートを追加する方法。
---

{{% alert color="primary" %}}

ピボットテーブルは、レコードのインタラクティブな集計です。たとえば、ワークシートのリストには数百の請求書エントリがあります。ピボットテーブルは、顧客、製品、または日付別に請求書を合計することができます。Microsoft Excelを使用すると、ピボットテーブル内の情報をボタンをドラッグするだけで素早く再配置することが可能です。

ピボットチャートは、ピボットテーブルのデータのインタラクティブなグラフィカルな表現です。ピボットチャートはExcel 2000で導入されました。ピボットテーブルが自動的に小計と合計を作成するため、ピボットチャートを使用することでデータを理解することがさらに容易になります。

Aspose.Cells for Node.js via C++は[pivot tables](/cells/ja/nodejs-cpp/create-pivot-tables-and-pivot-charts/)と[pivot charts](/cells/ja/nodejs-cpp/create-pivot-tables-and-pivot-charts/)をサポートしています。

{{% /alert %}}

## **Aspose.Cells for Node.js via C++を使用してピボットテーブルとチャートを追加する。**

Aspose.Cells for Node.js via C++は、ピボットテーブルを作成するために使用される特別なクラスセットを提供します。これらのクラスは、ピボットテーブルオブジェクトを作成し設定するために使用され、ピボットテーブルの基本的な構成要素として機能します：

- PivotField、ピボットテーブルレポート内のフィールド。
- PivotFields、ピボットテーブル内のすべてのPivotFieldオブジェクトのコレクション。
- PivotTable、ワークシート上のPivotTableレポート。
- PivotTables、ワークシート上のすべてのPivotTableオブジェクトのコレクション。

### **Aspose.Cells for Node.js via C++の使用準備。**
1. NPMからAspose.Cells for Node.js via C++をインストールし、コマンドは： $ npm install aspose.cells.node。
1. 「Aspose.Cells for Node.js via C++」のインストール手順を段階的に説明する方法もあります。


### **Aspose.Cells for Node.js via C++を使用してピボットテーブルを追加する方法。**

Aspose.Cells for Node.js via C++を使用してピボットテーブルを作成するには：

1. Cell オブジェクトの put_value メソッドを使用してワークシートのセルにデータを追加します。また、データが入力済みのテンプレートファイルを使用することもできます。このデータは、ピボットテーブルのデータソースとして使用されます。
1. PivotTablesコレクションのaddメソッド（Worksheetオブジェクトにカプセル化されています）を呼び出すことによって、ワークシートにピボットテーブルを追加します。
1. ピボットテーブルの新しいPivotTableオブジェクトにアクセスするには、そのインデックスを渡してPivotTablesコレクションからアクセスします。#PivotTableオブジェクトにカプセル化されているピボットテーブルオブジェクトを使用して、テーブルを管理します。

以下にコード例を示します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Aspose.Cells for Node.js via C++ライブラリを使用してピボットチャートを追加する方法。**

Aspose.Cells for Node.js via C++を使用してピボットチャートを作成するには：

1. チャートを追加します。
1. グラフのPivotSourceを、スプレッドシート内の既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
