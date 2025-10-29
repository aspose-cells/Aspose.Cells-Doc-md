---
title: 使用 Golang 通过 C++ 实现换行符和文本换行
description: 如何在C++中使用Aspose.Cells库实现文本换行和自动换行。通过使用Aspose.Cells库，您可以轻松在单元格中插入文本并设置文本换行方式，例如手动换行、自动换行等。本文件详细介绍了如何实现这些功能，并提供了示例代码供您参考。
keywords: Aspose.Cells，行尾，文本换行，文本布局
type: docs
weight: 60
url: /zh/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

为了确保单元格中的文本可以被读取，可以应用明确的行尾和文本换行。文本换行将单元格中的一行变成了多行，而明确的行尾则将文本换行放在您想要的确切位置。

{{% /alert %}}

## **将单元格中的文本自动换行**

 要在单元格中换行，请使用 [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) 属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **使用显式换行符**

 您可以在C++中使用 '\n' 在单元格中插入显式换行符。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
