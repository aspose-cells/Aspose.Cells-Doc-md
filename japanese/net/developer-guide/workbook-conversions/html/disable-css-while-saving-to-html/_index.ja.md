---
title: HTMLに保存する際にCSSを無効にする
type: docs
weight: 320
url: /ja/net/disable-css-while-saving-to-html/
---

## **可能な使用シナリオ**

Excelファイルを1ページのHTMLに保存すると、通常CSS要素はHTMLファイル内に埋め込まれ、HEADセクションに配置されます。メールの本文として貼り付ける場合、ほとんどのメールクライアントはCSS要素を除去し、正しくレンダリングされないことがあります。Aspose.Cellsのバージョン24.12では、任意でCSSを無効にできるオプションが導入されており、スタイルをHTML要素内に直接適用できるようになっています。メールの本文に設定したい場合は、[**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss)プロパティを**true**に設定してください。



## **HTML保存時にCSSを無効にする**

以下のサンプルコードは、[**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss)プロパティの使用例を示しています。 



## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-DisableCss-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
