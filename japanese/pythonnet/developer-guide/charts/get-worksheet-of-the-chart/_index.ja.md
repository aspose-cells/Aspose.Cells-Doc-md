---
title: チャートのワークシートを取得
description: Excelチャートに関連付けられたワークシートを Aspose.Cells for Python via .NET で取得する方法を学びます。ガイドでは、ワークシートにアクセスし、操作を行ってチャートの基本データを操作する方法を紹介します。
keywords: Aspose.Cells for Python via .NET、Excelチャート、ワークシート、データ操作、基本データ、操作。
type: docs
weight: 1000
url: /ja/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

時には、チャートの参照からワークシートにアクセスしたい場合があります。Aspose.Cells for Python via .NET は、それが含まれるワークシートの参照を返す [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) プロパティを提供しています。

{{% /alert %}}

以下の例は、[**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet)プロパティを使用する方法を示しています。コードはまずワークシートの名前を印刷し、次にワークシート上の最初のチャートにアクセスし、その後再度[**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet)プロパティを使用してワークシート名を印刷します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

以下はサンプルコードのコンソール出力です。同じワークシート名が2回印刷されることがわかります。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
