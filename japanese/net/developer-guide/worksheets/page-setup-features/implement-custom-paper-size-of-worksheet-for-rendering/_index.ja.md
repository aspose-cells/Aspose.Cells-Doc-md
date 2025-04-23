---
title: レンダリング用のワークシートのカスタム用紙サイズを実装する
type: docs
weight: 70
url: /ja/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: この記事では、ExcelファイルをPDFファイル形式にプログラムでレンダリングする際に、C# APIまたは.NETライブラリのサンプルコードを使用して、希望のワークシートのカスタム用紙サイズを設定する方法について説明します。
keywords: ExcelをPDFにレンダリングする際にカスタム用紙サイズを設定する方法 C#
---

## **可能な使用シナリオ**

MS Excelでは直接カスタム用紙サイズを作成するオプションはありませんが、ExcelファイルをPDFファイル形式にレンダリングする際に、希望のワークシートのカスタム用紙サイズを設定できます。このドキュメントでは、Aspose.Cells APIを使用してワークシートのカスタム用紙サイズを設定する方法について説明します。

## **レンダリングのためのワークシートのカスタム用紙サイズを実装する**

Aspose.Cellsを使用すると、ワークブックの最初のワークシートのカスタム用紙サイズを指定するために、[**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) メソッドを使用できます。以下のサンプルコードは、この目的のために生成された[output PDF](45056028.pdf)とともに、最初のワークシートのカスタム用紙サイズの指定方法を示します。

## **スクリーンショット**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
{{< app/cells/assistant language="csharp" >}}
