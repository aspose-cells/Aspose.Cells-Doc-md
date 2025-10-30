---
title: C++経由のGolangでPDFに添付ファイルを埋め込む
linktitle: PDFに添付を埋め込む
type: docs
weight: 380
url: /ja/go-cpp/embed-attachment-to-pdf/
description: C++経由のGolangでAspose.Cellsを使用してPDFに添付ファイルを埋め込む方法を学びます。
---

Excelではソースデータを持つOle Objectを挿入できます（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。Ole Objectをダブルクリックすると、埋め込みファイルが開きます。

一般的に、変換時にOleオブジェクトはアイコンまたはサムネイルとしてレンダリングされ、Oleオブジェクトのソースデータは含まれません。[PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/)オプションを使用すると、OleオブジェクトのソースデータをPDFに添付ファイルとして埋め込むことができます。PDF内のアイコンやサムネイルをダブルクリックすると、Oleオブジェクトのソースファイルを開くことができます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
