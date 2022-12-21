---
title: HTML リンクのターゲット タイプを変更する
type: docs
weight: 320
url: /ja/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells では、HTML リンクのターゲット タイプを変更できます。 HTMLリンクはこんな感じ

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上記の HTML リンクの target 属性は **_self** です。 [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) プロパティを使用して、このターゲット属性を制御できます。このプロパティは、次の値を持つ [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) 列挙型を取ります。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

次のコードは、[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype)財産。リンクターゲットタイプをに変更します**空欄**.デフォルトでは、**親**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
