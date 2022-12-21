---
title: HTML リンクのターゲット タイプを変更する
type: docs
weight: 450
url: /ja/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells では、HTML リンクのターゲット タイプを変更できます。 HTML リンクは次のようになります。

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上記の HTML リンクの target 属性は **_self** です。 [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) プロパティを使用して、このターゲット属性を制御できます。このプロパティは、次の値を持つ [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) 列挙型を取ります。

- [空欄](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [親](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [自己](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [上](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **HTML リンクのターゲット タイプを変更する**
次のコードは、[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType)財産。リンクターゲットタイプをに変更します**空欄**.デフォルトでは、**親**.あなたは得ることができます[ソースエクセルファイル](5472932.xlsx)ただし、このリンクから、内部に HTML ハイパーリンクを含む任意の Excel ファイルを使用して、このコードを実行できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
