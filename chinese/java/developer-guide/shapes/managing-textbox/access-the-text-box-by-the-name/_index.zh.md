---
title: 通过名称访问文本框
type: docs
weight: 580
url: /zh/java/access-the-text-box-by-the-name/
---

{{% alert color="primary" %}} 

以前，文本框是通过[Workheet.getTextBoxes()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes)集合的索引进行访问的，但现在您也可以通过名称从该集合中访问文本框。如果您已经知道其名称，这是访问文本框的一种便捷快速方式。

{{% /alert %}} 
## **通过名称访问文本框**
以下示例代码首先创建一个文本框并为其分配一些文本和名称。然后在接下来的几行中，我们通过其名称访问同一文本框并打印其文本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessTextBoxName-AccessTextBoxName.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight java >}}

 This is MyTextBox

{{< /highlight >}}
