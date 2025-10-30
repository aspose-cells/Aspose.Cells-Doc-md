---
title: HTMLリンクのターゲットタイプを変更する
type: docs
weight: 320
url: /ja/python-net/change-the-html-link-target-type/
description: Aspose.Cells for Python via NETを使用して、HTMLからのインポート時にHTMLリンクのターゲットタイプを変更する方法を示しています。
keywords: HTMLリンクのターゲットタイプを変更し、ブランクターゲットタイプ、親ターゲットタイプ、トップターゲットタイプ、セルフターゲットタイプ。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via NETでは、HTMLリンクのターゲットタイプを変更することができます。HTMLリンクは次のように見えます。

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上記のHTMLリンクで、target属性が**_self**になっています。このtarget属性を[**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/)プロパティを使用して制御できます。このプロパティは以下の値を持つ[**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype)列挙型を受け入れます。

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

次のコードは、[**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/)プロパティの使用方法を示しています。リンクのターゲットタイプを**BLANK**に変更します。デフォルトでは**PARENT**になっています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
