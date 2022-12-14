---
title: عام API تغييرات في Aspose.Cells 8.1.2
type: docs
weight: 70
url: /ar/java/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.1.1 إلى 8.1.2 ، والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة دعم للتحذير في حالة حدوث استبدال للخط**
مع Aspose.Cells for Java 8.1.2 ، تمت إضافة الفئتين WarningInfo و WarningType وواجهة IWarningCallback و SaveOptions.WarningCallback و ImageOrPrintOptions.WarningCallback للسماح للمطورين بتلقي تحذيرات عند حدوث استبدال الخط عند تحويل جداول البيانات إلى تنسيقات XPS و PDF.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[الحصول على تحذيرات لاستبدال الخط أثناء عرض جداول البيانات](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) للمزيد من المعلومات.

{{% /alert %}}
## **تم حذف خاصية PdfSaveOptions.ChartImageType القديمة**
قام Aspose.Cells for Java 8.1.2 بإزالة خاصية PdfSaveOptions.ChartImageType القديمة من API العامة.
