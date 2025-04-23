---
title: تضمين مرفق في ملف PDF
type: docs
weight: 370
url: /ar/java/embed-attachment-to-pdf/

---

في إكسل، يمكنك إدراج كائن Ole مع مصدر البيانات([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) . انقر نقراً مزدوجاً على كائن Ole، سيتم فتح الملف المدمج.

عموماً، أثناء التحويل إلى PDF، سيتم عرض كائن Ole كرأي أيقونة أو صورة مصغرة بدون بيانات مصدر الكائن Ole. باستخدام خيار [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-)، يمكنك تضمين بيانات مصدر الكائن Ole كمرفق في ملف PDF. يمكنك النقر المزدوج على الأيقونة أو الصورة المصغرة في PDF لفتح الملف المصدر الخاص بكائن Ole.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
