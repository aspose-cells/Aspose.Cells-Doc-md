---
title: تضمين مرفق في ملف PDF
type: docs
weight: 380
url: /ar/net/embed-attachment-to-pdf/

---

في إكسل، يمكنك إدراج كائن Ole مع مصدر البيانات([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) . انقر نقراً مزدوجاً على كائن Ole، سيتم فتح الملف المدمج.

عموماً، أثناء التحويل إلى PDF، سيتم عرض عنصر Ole كرمز أو صورة مصغر بدون بيانات مصدر عنصر Ole. باستخدام خيار [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/)، يمكنك تضمين بيانات مصدر عنصر Ole كمرفق في الـ PDF. يمكنك النقر المزدوج على الرمز أو الصورة المصغرة في الـ PDF لفتح ملف المصدر الخاص بـ Ole Object.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
