---
title: 访问和更新单元格的富文本部分
linktitle: 富格式文本
type: docs
weight: 40
url: /zh/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: 学习如何通过Aspose.Cells for Node.js via C++ API访问和更新单元格丰富文本的部分内容。
keywords: 访问和更新单元格的富文本，获取单元格的富文本，编辑单元格的富文本，访问单元格的富文本，更新单元格的富文本，更改单元格的富文本
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++允许您访问和更新单元格丰富文本的部分内容。为此，您可以使用[**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--)和[**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)方法。这些方法将返回和接受[**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)对象数组，您可以用它们访问和更新字体的各种属性，如字体名称、字体颜色、加粗等。

{{% /alert %}}

## **访问和更新单元格的富文本部分**

以下代码演示了使用[源Excel文件](5112369.xlsx)调用[**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--)和[**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)方法，您可以从提供的链接下载。源Excel文件中，单元格A1含有丰富的文本，有3个部分，每个部分的字体不同。以下代码片段访问这些部分，并用新字体名称更新第一个部分。最后，将工作簿保存为[输出Excel文件](5112366.xlsx)。打开后，您会发现第一部分的字体已变为**"Arial"**。

### 使用Nodejs访问和更新单元格丰富文本部分的代码

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

### 样本代码生成的控制台输出

以下是使用[source excel file](5112369.xlsx)的上述示例代码的控制台输出。

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

{{< app/cells/assistant language="nodejs-cpp" >}}
