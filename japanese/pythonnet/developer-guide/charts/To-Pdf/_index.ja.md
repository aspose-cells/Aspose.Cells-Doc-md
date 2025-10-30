---
title: グラフをPDFに変換する 
description: Aspose.Cells for Python via .NETを使用してチャートをPDFドキュメントに変換する方法を学びましょう。Microsoft Excelからチャートをエクスポートし、それをPDFとして保存して配布およびアーカイブに役立てる方法を解説します。
keywords: Aspose.Cells for Python via .NET、チャートからPDF、Microsoft Excel、PDF変換、エクスポート、配布、アーカイブ。
type: docs
weight: 47
url: /ja/python-net/chart-to-pdf/
---

## **PDFへのチャートのレンダリング**

チャートをPDF形式にレンダリングするために、Aspose.Cells for Python via .NET APIは[**Chart.to_pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_pdf)メソッドを公開し、結果のPDFをディスクパスまたはStreamに保存できるようにしています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRenderingChartToPDF.py" >}}

## **希望のページサイズでチャートPDFを作成**
Aspose.Cells for Python via .NETを使用して、希望するページサイズのチャートPDFを作成し、ページ内でのチャートの配置（上、下、中央、左、右など）を指定できます。さらに、出力されたチャートはStreamまたはディスク上に作成可能です。以下のサンプルコードは、[サンプルExcelファイル](64716906.xlsx)をロードし、ワークシート内の最初のチャートにアクセスし、希望のページサイズで[出力PDF](64716907.pdf)に変換する例です。スクリーンショットは、出力PDFのページサイズがコード内で指定された7x7で、チャートは水平方向および垂直方向の両方で中央に配置されていることを示しています。 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateChartPDFWithDesiredPageSize.py" >}}

{{< app/cells/assistant language="python-net" >}}
