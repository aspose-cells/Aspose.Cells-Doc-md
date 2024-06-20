---
title: 特定のUnicode文字のみのフォントを変更してPDFに保存する
type: docs
weight: 150
url: /ja/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

一部のUnicode文字は、ユーザー指定のフォントでは表示されません。そのようなUnicode文字の1つが **Non-breaking Hyphen** (U+2011) で、Unicode番号は8209です。この文字は **Times New Roman** では表示できませんが、**Arial Unicode MS** のような他のフォントでは表示できます。

そのような文字が特定のフォント（例: Times New Roman）で単語や文章の中に含まれている場合、Aspose.CellsはArial Unicode MSなどでこの文字を表示できるフォントに全体の単語や文章のフォントを変更します。

しかし、これは一部のユーザーにとって望ましくない動作です。彼らは特定の文字のフォントのみを変更したいとし、単語や文章全体のフォントを変更したくありません。

この問題に対処するために、Aspose.Cellsは [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) プロパティを提供しており、表示できない特定の文字のフォントだけを変更し、単語や文章の残りの部分のフォントを変更しないように **true** に設定する必要があります。

{{% /alert %}}

## **例**

以下のスクリーンショットは、[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) プロパティを設定せずに生成された2つの出力PDFを比較しています。1つは [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) プロパティを **true** に設定した後に生成されたものです。最初のPDFでは、非改行ハイフンのために、全体の文のフォントがTimes New RomanからArial Unicode MSに変更されています。一方、2番目のPDFでは、非改行ハイフンのみのフォントが変更されています。

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
