---
title: 按名称访问文本框
type: docs
weight: 580
url: /zh/java/access-the-text-box-by-the-name/
---

{{% alert color="primary" %}} 

以前，文本框是通过从 [Workheet.getTextBoxes()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) 集合中的索引进行访问的，但现在还可以通过该集合的名称访问文本框。如果您已知其名称，这是一种方便快捷的访问文本框的方式。

{{% /alert %}} 
## **通过名称访问文本框**
以下示例代码首先创建了一个文本框并分配了一些文本和名称。然后在接下来的行中，我们通过其名称访问相同的文本框并打印其文本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessTextBoxName-AccessTextBoxName.java" >}}
## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

 This is MyTextBox

{{< /highlight >}}
