---
title: ワークシートのページ設定の用紙幅と用紙高さを取得する方法
type: docs
weight: 50
url: /ja/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: この記事では、.NET API またはライブラリを使用して、C# コードで Excel ワークシートのページ設定の用紙幅と用紙高さをプログラムで取得する方法についてご紹介します。
keywords: C#でのExcelページ設定用紙の幅、Excelページ設定用紙の高さ
---

## **可能な使用シナリオ**

時々、ワークシートのページ設定で設定された用紙サイズの幅と高さを知る必要があります。この場合は、[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) プロパティおよび [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) プロパティを使用してください。

## **ワークシートのページ設定の用紙の幅と高さを取得**

以下のサンプルコードは、[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) プロパティと [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) プロパティの使用方法を説明しています。まず用紙サイズを *A2* に変更し、次に用紙の幅と高さを見つけ、その後それぞれを *A3*、*A4*、*Letter* に変更して、用紙の幅と高さを見つけます。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **コンソール出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
