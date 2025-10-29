---
title: إدراج مرفق في ملف PDF باستخدام Golang عبر C++
linktitle: تضمين مرفق في ملف PDF
type: docs
weight: 380
url: /ar/go-cpp/embed-attachment-to-pdf/
description: تعلم كيفية تضمين المرفقات في PDF باستخدام Aspose.Cells مع Golang عبر C++.
---

في Excel، يمكنك إدراج كائن Ole ببيانات مصدر ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). بالنقر المزدوج على كائن Ole، سيتم فتح الملف المضمّن.

عموماً، عند التحويل إلى PDF، سيتم عرض كائن Ole كرمز أو صورة مصغرة بدون بيانات مصدر كائن Ole. مع خيار [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/)، يمكنك تضمين بيانات مصدر كائن Ole كمرفق في PDF. يمكنك النقر المزدوج على الرمز أو الصورة المصغرة لفتح الملف المصدر للكائن Ole.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
