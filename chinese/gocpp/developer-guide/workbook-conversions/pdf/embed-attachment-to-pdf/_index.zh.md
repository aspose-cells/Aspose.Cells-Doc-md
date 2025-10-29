---
title: 将附件嵌入到 PDF 中，使用 Golang 通过 C++
linktitle: 将附件嵌入到PDF中
type: docs
weight: 380
url: /zh/go-cpp/embed-attachment-to-pdf/
description: 学习如何使用 Aspose.Cells 通过 Golang 嵌入附件到 PDF 中。
---

在Excel中，您可以插入带有源数据的Ole对象（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。双击Ole对象，嵌入的文件将被打开。

一般在转换为 PDF 时，Ole 对象将作为图标或缩略图渲染，不含 Ole 对象源数据。通过选项 [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/)，可以将 Ole 对象源数据作为附件嵌入到 PDF 中。双击 PDF 中的图标或缩略图即可打开 Ole 对象的源文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
