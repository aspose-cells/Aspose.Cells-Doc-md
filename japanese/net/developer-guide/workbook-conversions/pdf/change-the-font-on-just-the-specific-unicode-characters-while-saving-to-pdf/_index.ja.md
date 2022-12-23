---
title: PDF に保存するときに、特定の Unicode 文字だけのフォントを変更します
type: docs
weight: 260
url: /ja/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

一部の Unicode 文字は、ユーザー指定のフォントでは表示できません。そのような Unicode 文字の 1 つが**非改行ハイフン**(U+2011) であり、その Unicode 番号は 8209 です。この文字は、**タイムズ ニュー ローマン** 、しかし、それはのような他のフォントで表示することができます**Arial ユニコード MS**.

そのような文字が、Times New Roman のような特定のフォントの単語または文の中にある場合、Aspose.Cells は、単語または文全体のフォントを、Arial Unicode のようなこの文字を MS に表示できるフォントに変更します。

ただし、これは一部のユーザーにとって望ましくない動作であり、単語または文全体のフォントを変更するのではなく、特定の文字のフォントのみを変更する必要があることを望んでいます。

この問題に対処するために、Aspose.Cells は PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティを提供します。これを true に設定すると、表示できない特定の文字のフォントのみを表示可能なフォントに変更し、残りの単語または文は元のフォントのままにする必要があります。

{{% /alert %}} 
## **例**
次のスクリーンショットは、以下のサンプル コードによって生成された 2 つの出力 PDF を比較しています。

1 つは PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティを設定せずに生成され、もう 1 つは PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティを true に設定した後に生成されました。

最初の Pdf でわかるように、Non-Breaking Hyphen のために、文全体のフォントが Times New Roman から Arial Unicode MS に変更されています。 2 番目の Pdf では、Non-Breaking Hyphen のフォントのみが変更されています。

|**最初の Pdf ファイル**|
|:- |
|![todo:画像_代替_文章](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**番目の PDF ファイル**|
|:- |
|![todo:画像_代替_文章](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **サンプルコード**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



