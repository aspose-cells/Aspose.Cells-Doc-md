---
title: 访问和更新单元格的富文本部分
linktitle: 富格式文本
type: docs
weight: 440
url: /zh/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells允许您访问和更新单元格的富文本部分。为此，您可以使用Cell.getCharacters()和Cell.setCharacters()方法。这些方法将返回和接受FontSetting对象的数组，您可以使用它们来访问和更新字体的各种属性，如字体名称、字体颜色、粗体等。

{{% /alert %}} 
## **访问和更新单元格的富文本部分**
以下代码演示了使用Cell.getCharacters()和Cell.setCharacters()方法来操作[source excel file](5472937.xlsx)中的富文本，您可以从提供的链接中下载。源excel文件的单元格A1中包含富文本，其中有3个部分，每个部分的字体都不同。我们将访问这些部分，并使用新的字体名称更新第一个部分。最后，将工作簿保存为[output excel file](5472930.xlsx)。当您打开它时，会发现文本的第一个部分的字体已更改为"Arial"。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **控制台输出**
以下是使用[source excel file](5472937.xlsx)的上述示例代码的控制台输出。

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
