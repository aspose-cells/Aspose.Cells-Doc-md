---
title: 按名称访问文本框
type: docs
weight: 580
url: /zh/java/access-the-text-box-by-the-name/
---
{{% alert color="primary" %}} 

早些时候，文本框是通过索引从[工作表.getTextBoxes()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes)集合，但现在您还可以从此集合中按名称访问文本框。如果您已经知道文本框的名称，这是访问文本框的一种方便快捷的方法。

{{% /alert %}} 
## **按名称访问文本框**
下面的示例代码首先创建一个文本框并为其分配一些文本和名称。然后在接下来的几行中，我们通过名称访问同一个文本框并打印其文本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessTextBoxName-AccessTextBoxName.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight "java" >}}

 This is MyTextBox

{{< /highlight >}}
