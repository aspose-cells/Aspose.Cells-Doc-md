---
title: Golangを使ったC++経由でHTMLのリンクターゲットタイプを変更する
linktitle: HTMLリンクのターゲットタイプを変更する
type: docs
weight: 320
url: /ja/go-cpp/change-the-html-link-target-type/
description: Aspose.Cells for C++を使用してHTMLリンクのターゲット属性をプログラムで制御し、ターゲットタイプを変更する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、HTMLリンクのターゲットタイプを変更できます。HTMLリンクは以下のようになります。

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上記のHTMLリンクで、target属性が**_self**になっています。このtarget属性を[**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/)プロパティを使用して制御できます。このプロパティは以下の値を持つ[**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/)列挙型を受け入れます。

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

次のコードは、[**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/)プロパティの使用方法を示しています。リンクのターゲットタイプを**blank**に変更します。デフォルトでは**parent**が設定されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
