---
title: HTMLリンクのターゲットタイプを変更する
type: docs
weight: 320
url: /ja/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、HTMLリンクのターゲットタイプを変更できます。HTMLリンクは以下のようになります。

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上記のHTMLリンクで、target属性が**_self**になっています。このtarget属性を[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype)プロパティを使用して制御できます。このプロパティは以下の値を持つ[**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype)列挙型を受け入れます。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

次のコードは、[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype)プロパティの使用方法を示しています。リンクのターゲットタイプを**blank**に変更します。デフォルトでは**parent**が設定されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
