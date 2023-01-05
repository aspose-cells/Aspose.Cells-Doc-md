---
title: 访问和更新 Cell 的富文本部分
linktitle: 富格式文本
type: docs
weight: 440
url: /zh/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells 允许您访问和更新单元格的富文本部分。为此，您可以使用 Cell.getCharacters() 和 Cell.setCharacters() 方法。这些方法将返回并接受 FontSetting 对象数组，您可以使用这些对象来访问和更新字体的各种属性，如字体名称、字体颜色、粗体等。

{{% /alert %}} 
## **访问和更新 Cell 的富文本部分**
以下代码演示了使用 Cell.getCharacters() 和 Cell.setCharacters() 方法的用法[源文件](5472937.xlsx)您可以从提供的链接下载。源 excel 文件在单元格 A1 中包含富文本。它有 3 个部分，每个部分都有不同的字体。我们将访问这些部分并使用新字体名称更新第一部分。最后它将工作簿另存为[输出excel文件](5472930.xlsx).当你打开它时，你会发现第一部分文字的字体已经变成了**“宋体”**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **控制台输出**
这是上面示例代码的控制台输出，使用[源文件](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
