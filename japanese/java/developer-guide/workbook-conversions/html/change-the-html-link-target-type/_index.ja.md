---
title: HTMLリンクのターゲットタイプを変更する
type: docs
weight: 450
url: /ja/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cellsでは、HTMLリンクのターゲットタイプを変更することができます。HTMLリンクは次のようになります。

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上記のHTMLリンクにおけるtarget属性が **_self** になっています。[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType)プロパティを使用してこのtarget属性を制御できます。このプロパティは [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) enumを取り、以下の値を持ちます。

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **HTMLリンクのターゲットタイプを変更する**
[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) プロパティの使用方法を以下のコードで説明しています。このコードはリンクのターゲットタイプを **blank** に変更しています。デフォルトは **parent** です。このコードを実行するためには[ソースエクセルファイル](5472932.xlsx)を取得できますが、内部にHTMLハイパーリンクを含む任意のエクセルファイルを使用することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
