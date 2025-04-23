---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.1.2
type: docs
weight: 60
url: /ar/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.1.1 إلى 8.1.2، التي قد تكون مهمة لمطوري الوحدات/التطبيقات. ويتضمن ليس فقط أساليب الواجهة العامة الجديدة والمحدثة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الداخلي في Aspose.Cells.

{{% /alert %}} 
## **إضافة دعم للتحذير عند حدوث استبدال الخط**
مع Aspose.Cells for .NET 8.1.2، تمت إضافة فئتي WarningInfo وWarningType وواجهة IWarningCallback وخصائص SaveOptions.WarningCallback وImageOrPrintOptions.WarningCallback لتيسير استقبال المستخدم لتحذير في حالة حدوث استبدال الخطوط أثناء تحويل جداول البيانات إلى صور أو صيغة PDF. 

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل عن [الحصول على تحذيرات لاستبدال الخطوط أثناء تقديم جداول البيانات](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **حذف خاصية PdfSaveOptions.ChartImageType العتيقة**
قامت Aspose.Cells for .NET 8.1.2 بإزالة الخاصية القديمة PdfSaveOptions.ChartImageType من واجهة برمجة التطبيقات العامة.
{{< app/cells/assistant language="csharp" >}}
