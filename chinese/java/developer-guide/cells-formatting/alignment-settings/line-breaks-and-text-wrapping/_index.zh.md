---
title: 行尾和文本换行
type: docs
weight: 10
url: /zh/java/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

为了确保单元格中的文本可以被读取，可以应用明确的行尾和文本换行。文本换行将单元格中的一行变成了多行，而明确的行尾则将文本换行放在您想要的确切位置。

{{% /alert %}}

## **将单元格中的文本自动换行**

要将单元格中的文本自动换行，请使用 [**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped) 属性。

以下示例代码显示了如何在单元格中使用文本换行和显式换行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **使用显式换行符**

您可以在Java中使用'\n'来在单元格中插入显式换行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
{{< app/cells/assistant language="java" >}}
