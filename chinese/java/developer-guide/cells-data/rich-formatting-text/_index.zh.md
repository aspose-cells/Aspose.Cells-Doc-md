---
title: 访问和更新单元格中的富文本部分
linktitle: 富文本格式化
type: docs
weight: 440
url: /zh/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells允许您访问和更新单元格的富文本部分。为此，您可以使用Cell.getCharacters()和Cell.setCharacters()方法。这些方法将返回并接受FontSetting对象数组，您可以使用这些对象来访问和更新字体的各种属性，如字体名称、字体颜色、加粗等。

{{% /alert %}} 
## **访问和更新单元格中的富文本部分**
以下代码演示了使用[源Excel文件](5472937.xlsx)的Cell.getCharacters()和Cell.setCharacters()方法的用法，您可以从提供的链接中下载该文件。源Excel文件中的单元格A1中有富文本。它有3个部分，每个部分有不同的字体。我们将访问这些部分，并使用新的字体名称更新第一个部分。最后将其另存为[输出Excel文件](5472930.xlsx)。当您打开它时，您会发现文本的第一个部分的字体已更改为**"Arial"**。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **控制台输出**
这是使用[源Excel文件](5472937.xlsx)的上述示例代码的控制台输出。

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
