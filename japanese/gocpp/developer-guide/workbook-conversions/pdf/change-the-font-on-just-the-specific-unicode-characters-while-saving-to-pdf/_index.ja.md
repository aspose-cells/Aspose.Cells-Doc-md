---
title: Golangを使ってC++で特定のUnicode文字だけのフォントを変更し、PDFに保存
linktitle: Unicode文字のフォントを変更する
type: docs
weight: 260
url: /ja/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aspose.Cellsを使って特定のUnicode文字のフォントを変更し、PDFに保存する方法を学ぶ
---

{{% alert color="primary" %}}

一部のUnicode文字は、ユーザー指定のフォントでは表示されません。そのようなUnicode文字の1つが **Non-breaking Hyphen** (U+2011) で、Unicode番号は8209です。この文字は **Times New Roman** では表示できませんが、**Arial Unicode MS** のような他のフォントでは表示できます。

特定の単語や文章内にこのような文字が出現し、それがTimes New Romanのような特定のフォントである場合、Aspose.Cellsはその文字を表示できるフォント（Arial Unicode MSなど）に変換し、全体の単語や文章のフォントを変更します。

ただし、これは一部のユーザーにとって望ましくない動作であり、特定の文字だけのフォントを変更し、全体のフォントを変更しないようにしたい場合があります。

この問題に対処するために、Aspose.Cellsは`PdfSaveOptions.IsFontSubstitutionCharGranularity`プロパティを提供しており、これを`true`に設定すると、表示できない文字だけのフォントが置き換えられ、残りの部分は元のフォントのまま維持されます。

{{% /alert %}}

## **例**

以下のスクリーンショットは、以下のサンプルコードによって生成された2つの出力 PDF を比較しています。

一つは`PdfSaveOptions.IsFontSubstitutionCharGranularity`を設定しない状態で生成されたもので、もう一つは設定後に`true`にしたもので生成されたものです。

最初のPDFでは、ノンブレッディングハイフンのために全体のフォントがTimes New RomanからArial Unicode MSに変わっていますが、二つ目のPDFでは、ノンブレッディングハイフンだけのフォントが変更されています。

|**最初のPDFファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**二つ目のPDFファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}
