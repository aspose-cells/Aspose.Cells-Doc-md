---
title: PDF に保存するときに、特定の Unicode 文字だけのフォントを変更します
type: docs
weight: 150
url: /ja/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

一部の Unicode 文字は、ユーザー指定のフォントでは表示できません。そのような Unicode 文字の 1 つが**非改行ハイフン**(U+2011) であり、その Unicode 番号は 8209 です。この文字は、**タイムズ ニュー ローマン** 、しかし、それはのような他のフォントで表示することができます**Arial ユニコード MS**.

そのような文字が、Times New Roman のような特定のフォントの単語または文の中にある場合、Aspose.Cells は単語または文全体のフォントを、Arial Unicode のようなこの文字を MS に表示できるフォントに変更します。

ただし、これは一部のユーザーにとって望ましくない動作であり、単語または文全体のフォントを変更するのではなく、特定の文字のフォントのみを変更する必要があることを望んでいます。

この問題に対処するために、Aspose.Cells が提供します。[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)設定するプロパティ**真実**これにより、表示できない特定の文字のフォントのみが変更され、残りの単語または文のフォントは同じままになります。

{{% /alert %}}

## **例**

次のスクリーンショットは、以下のサンプル コードによって生成された 2 つの出力 PDF を比較しています。 1つは設定せずに生成されました[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)プロパティと、もう一方は を設定した後に生成されたものです[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)プロパティへ**真実**.最初の PDF でわかるように、Non-Breaking Hyphen により、文全体のフォントが Times New Roman から Arial Unicode MS に変更されています。 2 番目の PDF では、Non-Breaking Hyphen のフォントのみが変更されています。

![todo:画像_代替_文章](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
