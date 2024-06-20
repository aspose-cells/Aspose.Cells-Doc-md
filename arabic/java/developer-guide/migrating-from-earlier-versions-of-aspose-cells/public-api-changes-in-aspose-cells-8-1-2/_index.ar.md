---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.1.2
type: docs
weight: 70
url: /ar/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.1.1 إلى 8.1.2، التي قد تكون مهمة لمطوري الوحدات/التطبيقات. ويتضمن ليس فقط أساليب الواجهة العامة الجديدة والمحدثة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الداخلي في Aspose.Cells.

{{% /alert %}} 
## **إضافة دعم للتحذير عند حدوث استبدال الخط**
مع Aspose.Cells for Java 8.1.2، تمت إضافة فئات WarningInfo وWarningType وواجهة IWarningCallback، وخصائص SaveOptions.WarningCallback وImageOrPrintOptions.WarningCallback للسماح للمطورين بتلقي التحذيرات عند حدوث استبدال الخط أثناء تحويل جداول البيانات إلى صور وتنسيقات XPS وPDF. 

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [الحصول على تحذيرات لاستبدال الخط أثناء عرض جداول البيانات](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) لمزيد من المعلومات.

{{% /alert %}}
## **حذف خاصية PdfSaveOptions.ChartImageType العتيقة**
Aspose.Cells for Java 8.1.2 قام بإزالة خاصية PdfSaveOptions.ChartImageType العتيقة من الواجهة البرمجية العامة.
