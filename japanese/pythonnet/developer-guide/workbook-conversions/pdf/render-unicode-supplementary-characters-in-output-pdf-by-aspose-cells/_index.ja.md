---
title: 出力で Unicode 補助文字をレンダリング PDF by Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /ja/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Excel を Aspose.Cells for Python via .NET API で PDF に変換する際に Unicode 補助文字をレンダリングする方法を学びます。
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

通常の Unicode 文字の長さは 2 バイトですが、Unicode 補助文字の長さは 4 バイトです。 Aspose.Cells for Python via .NET は、これらの 4 バイト Unicode 文字のレンダリングをサポートするようになりました。

Unicode 文字標準では、補助文字は、U+10000 から U+10FFFF までのコード ポイントが割り当てられた文字です。言い換えれば、これらは U+FFFF より大きい Unicode 文字です。

- UTF-8 では、これらの文字の長さはそれぞれ 4 バイトです。
- UTF-16 では、これらの文字には 2 つのサロゲート (16 ビット単位) が必要です。

{{% /alert %}}

## 出力で Unicode 補助文字をレンダリング PDF by Aspose.Cells for Python via .NET

次のスクリーンショットは、Aspose.Cells for Python via .NET がどのようにレンダリングしたかを示しています。[ソースエクセルファイル](5115563.xlsx)に[出力PDF](5115564.pdf)。ご覧のとおり、3 つの Unicode 補助文字はすべて、Microsoft Excel で行われたものとまったく同じようにレンダリングされています。

![todo:image_alt_text](output.png)

## サンプルコード

このサンプルコードを使用して変換できます[ソースエクセルファイル](5115563.xlsx)の中へ[出力PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
