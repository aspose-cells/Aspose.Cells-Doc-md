---
title: PDFに添付を埋め込む
type: docs
weight: 370
url: /ja/java/embed-attachment-to-pdf/

---

Excelでは、Oleオブジェクト([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx))を挿入できます。Oleオブジェクトをダブルクリックすると、埋め込みファイルが開きます。

通常、PDFに変換するとき、OLEオブジェクトはアイコンまたはサムネイルとしてレンダリングされ、そのソースデータは表示されません。ただし、[PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-)オプションを使用することで、OLEオブジェクトのソースデータを添付としてPDFに埋め込むことができます。アイコンやサムネイルをダブルクリックするとOLEオブジェクトのソースファイルを開くことができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
