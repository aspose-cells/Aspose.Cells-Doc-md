---
title: PDFに添付ファイルを埋め込む
type: docs
weight: 380
url: /ja/net/embed-attachment-to-pdf/

---

Excelでは、元のデータを持つOleオブジェクトを挿入できます（embedded-attachments-example.xlsx）。Oleオブジェクトをダブルクリックすると、埋め込まれたファイルが開かれます。

一般的に、PDFに変換する際に、Oleオブジェクトはアイコンまたはサムネイルとしてレンダリングされ、Oleオブジェクトの元のデータは表示されません。[PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/)オプションを使用すると、PDF内にOleオブジェクトの元のデータを添付ファイルとして埋め込むことができます。PDF内のアイコンやサムネイルをダブルクリックして、Oleオブジェクトの元のファイルを開くことができます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
