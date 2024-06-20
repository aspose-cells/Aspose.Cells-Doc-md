---
title: Aspose.Cells for Python via .NETによる出力PDFのUnicodeサプリメンタリ文字のレンダリング
type: docs
weight: 350
url: /ja/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for Python via .NET APIを使用してExcelをPDFに変換する際のUnicodeサプリメンタリ文字のレンダリング方法
keywords: PythonでファイルをPDFに保存する際のUnicodeサプリメンタリ文字のレンダリング、PythonでExcelをPDFに保存する際のUnicodeサプリメンタリ文字の表示、ExcelをPDFに変換する際のUnicodeサプリメンタリ文字の出力、ExcelからPDFへのUnicodeサプリメンタリ文字の出力
---

{{% alert color="primary" %}}

通常のUnicode文字は2バイト長ですが、Unicodeサプリメンタリ文字は4バイト長です。Aspose.Cells for Python via .NETはこれらの4バイトUnicode文字のレンダリングをサポートしています。

Unicode文字標準では、補助文字はU+10000からU+10FFFFまでのコードポイントが割り当てられています。つまり、これらはU+FFFFよりも大きいUnicode文字です。

- UTF-8では、これらの文字はそれぞれ4バイトです。
- UTF-16では、これらの文字は2つのサロゲート（16ビットユニット）が必要です。

{{% /alert %}}

Aspose.Cells for Python via .NETによる出力PDFのUnicodeサプリメンタリ文字のレンダリング

以下のスクリーンショットは、Aspose.Cells for Python via .NETが[元のExcelファイル](5115563.xlsx)を[出力PDF](5115564.pdf)にレンダリングした様子を示しています。すべての3つのUnicodeサプリメンタリ文字がMicrosoft Excelによって行われたのとまったく同じようにレンダリングされていることがわかります。

![todo:image_alt_text](output.png)

## サンプルコード

[ソースExcelファイル](5115563.xlsx)を[出力PDF](5115564.pdf)に変換するためのサンプルコードを使用できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
