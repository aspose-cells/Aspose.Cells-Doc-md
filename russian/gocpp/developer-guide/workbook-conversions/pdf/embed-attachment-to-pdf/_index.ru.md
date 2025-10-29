---
title: Вставка вложений в PDF с помощью Golang через C++
linktitle: Встроить вложение в PDF
type: docs
weight: 380
url: /ru/go-cpp/embed-attachment-to-pdf/
description: Узнайте, как вставлять вложения в PDF с помощью Aspose.Cells и Golang через C++.
---

В Excel вы можете вставить Ole Object с исходными данными ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Дважды щелкните по Ole Object, и встроенный файл откроется.

Во время преобразования в PDF Ole Object обычно отображается как значок или эскиз без исходных данных Ole Object. С опцией [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/) вы можете встроить исходные данные Ole Object как вложение в PDF. Двойным щелчком по значку или эскизу в PDF можно открыть исходный файл Ole Object.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
