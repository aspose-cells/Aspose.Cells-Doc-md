---
title: 特定のUnicode文字のみのフォントを変更してPDFに保存する
type: docs
weight: 260
url: /ja/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

ユーザー指定のフォントで表示できない Unicode 文字がいくつかあります。そのような Unicode 文字の1つが **ノンブレーキングハイフン** (U+2011) で、Unicode 番号は 8209 です。この文字は **Times New Roman** では表示できませんが、 **Arial Unicode MS** のような他のフォントでは表示できます。

このような文字が特定のフォントである単語や文章内にある場合、Aspose.Cells は、Arial Unicode MS のようにこの文字を表示できるフォントに変更し、その単語や文章全体のフォントを変更します。

ただし、これは一部のユーザーにとって望ましくない動作であり、単語や文章全体のフォントを変更するのではなく、特定の文字のフォントのみを変更したいと考えています。

この問題に対処するため、Aspose.Cells では、PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティが true に設定されている必要があります。これにより、表示できない特定の文字のフォントだけが表示可能なフォントに変更され、単語や文章の残りの部分は元のフォントのままになります。

{{% /alert %}} 
## **例**
以下のスクリーンショットは、以下のサンプルコードによって生成された2つの出力 PDF を比較しています。

1つは、PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティを設定しないまま生成されたもので、もう1つは、PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティを true に設定した後に生成されたものです。

最初の PDF では、ノンブレーキングハイフンのために全文のフォントが Times New Roman から Arial Unicode MS に変更されたことがわかります。一方、2番目の PDF では、ノンブレーキングハイフンのフォントのみが変更されています。

|**最初の PDF ファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**2 番目の PDF ファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **サンプルコード**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



{{< app/cells/assistant language="csharp" >}}
