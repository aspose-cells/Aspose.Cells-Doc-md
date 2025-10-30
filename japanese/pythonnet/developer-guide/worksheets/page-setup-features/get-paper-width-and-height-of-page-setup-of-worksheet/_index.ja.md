---
title: ワークシートのページ設定の用紙幅と用紙高さを取得する方法
type: docs
weight: 50
url: /ja/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して、Pythonコードを通じてExcelのワークシートのページ設定の用紙幅と用紙高さを取得する方法を解説します。
keywords: Python Excelライブラリを使って、PythonでExcelのページ設定の用紙幅と用紙高さを取得します。
---

## **可能な使用シナリオ**

時々、ワークシートのページ設定で設定された用紙サイズの幅と高さを知る必要があります。この場合は、[**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) プロパティおよび [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) プロパティを使用してください。

## **ワークシートのページ設定の用紙の幅と高さを取得**

以下のサンプルコードは、[**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width)および[**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height)プロパティの使用方法を示しています。最初に用紙サイズを *A2* に変更し、その後用紙の幅と高さを検索し、次に *A3*、*A4*、*Letter* に変更し、それぞれの用紙の幅と高さを検索します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **コンソール出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
