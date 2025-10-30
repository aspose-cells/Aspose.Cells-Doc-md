---
title: Golang ile C++ üzerinden PDF ye Eklenti Ekleme
linktitle: Ekli Dosya Ekle PDF ye
type: docs
weight: 380
url: /tr/go-cpp/embed-attachment-to-pdf/
description: Golang ile C++ kullanarak PDF ye ekleri gömmeyi öğrenin.
---

Excel'de, kaynağı verilerle Ole Nesnesi ekleyebilirsiniz ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Ole Nesnesine çift tıklayınca gömülü dosya açılır.

Genellikle, PDF'ye dönüştürürken, Ole Nesnesi bir simge veya küçük resim olarak gösterilir ve Ole Nesnesi kaynak verisi gösterilmez. [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/) seçeneği ile Ole Nesnesi kaynak verisini PDF'ye ekleyebilirsiniz. PDF'deki simgeye veya küçük resme çift tıklayarak Ole Nesne kaynağını açabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
