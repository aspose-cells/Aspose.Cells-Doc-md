---
title: PDFに添付を埋め込む
type: docs
weight: 380
url: /ja/net/embed-attachment-to-pdf/

---

Excelでは、Oleオブジェクト([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx))を挿入できます。Oleオブジェクトをダブルクリックすると、埋め込みファイルが開きます。

一般的に、PDFに変換する際、Oleオブジェクトはアイコンまたはサムネイルとしてレンダリングされ、Oleオブジェクトのソースデータは表示されません。[PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/)オプションを使用すると、Oleオブジェクトのソースデータを添付ファイルとしてPDFに埋め込むことができます。PDF内のアイコンまたはサムネイルをダブルクリックすると、Oleオブジェクトのソースファイルを開くことができます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
