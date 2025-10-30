---
title: Golang を使った C++ によるチャートのワークシート取得
linktitle: チャートのワークシートを取得
description: Aspose.Cells for C++を使用して Excel のチャートに関連付けられたワークシートを取得する方法を学びます。ガイドでは、ワークシートにアクセスし、操作を行ってチャートの基礎データを操作する方法を示します。
keywords: Aspose.Cells for C++、Excelチャート、ワークシート、データ操作、基礎データ、操作
type: docs
weight: 1000
url: /ja/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

時には、チャートのリファレンスからワークシートにアクセスしたい場合があります。Aspose.Cellsは、[**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/)メソッドを提供しており、これによりチャートを含むワークシートのリファレンスを返します。

{{% /alert %}}

以下の例では、[**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/)メソッドの使用方法を示します。まずワークシートの名前を出力し、その後最初のチャートにアクセスします。次に、[**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/)メソッドを使用して再びワークシートの名前を出力します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
以下はサンプルコードのコンソール出力です。同じワークシート名が2回印刷されることがわかります。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
