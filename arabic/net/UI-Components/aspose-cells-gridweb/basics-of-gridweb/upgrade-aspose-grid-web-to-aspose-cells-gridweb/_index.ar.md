---
title: ترقية Aspose.Grid.Web إلى Aspose.Cells.GridWeb
type: docs
weight: 30
url: /ar/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: يُقدم هذا المقال كيفية الترقية في GridWeb.
---

{{% alert color="primary" %}}

لجعل عملية الترقية أسهل، نحن نحتفظ بوثيقة تصف المعلومات الحرجة للمستخدمين الحاليين، خاصة الذين استخدموا الإصدار السابق لـ Aspose.Grid.Web ويحتاجون للترقية إلى Aspose.Cells.GridWeb.

من المفترض أن تكون هذه ملاحظات موجزة، ويجب أن تتمكن من العثور على مزيد من المعلومات من خلال النظر إلى أقسام ال[دليل المطور](/cells/ar/net/aspose-cells-gridweb/developer-guide/).

{{% /alert %}}

## **الترقية إلى Aspose.Cells.GridWeb**

قد يواجه مستخدمو Aspose.Grid.Web مشاكل باستخدام الإصدار الجديد من Aspose.Cells.GridWeb عند الترقية إليه. يجدر بذكر أن Aspose.Grid.Web قد تمت إعادة تسميته وأصبح جزءًا من Aspose.Cells لذلك لن نواصل أو نجري تعديلات على الإصدارات القديمة للتحكم. 

ليس من الصعب الترقية إلى مكون Aspose.Cells.GridWeb الأحدث.

{{% alert color="primary" %}}

هناك بعض التغييرات في واجهة البرمجة التطبيقية حيث تظل الفئات مع الأعضاء والهياكل والتعدادات إلخ تبقى كما هي. تم إجراء معظم التغييرات على مساحات أسماء التحكم وعلامات أو سمات أخرى.

{{% /alert %}}

التالي هو قائمة بمساحات الأسماء والسمات/العلامات الأخرى التي تغيرت الآن:

1. تمت إعادة تسمية مساحة أسماء Aspose.Grid.Web إلى Aspose.Cells.GridWeb.
1. تمت إعادة تسمية مساحة أسماء Aspose.Grid.Web.Data إلى Aspose.Cells.GridWeb.Data.
1. تمت إعادة تسمية مساحة أسماء Aspose.Grid.Web.Design إلى Aspose.Cells.GridWeb.Design.
1. تمت إعادة تسمية مساحة أسماء Aspose.Grid.Formula إلى Aspose.Cells.GridFormula، ومع الإصدارات الأخيرة للمكون، تمت إزالة المساحة المذكورة تمامًا من واجهة برمجة التطبيق العامة.
1. تم تغيير العلامة agw:GridWeb إلى acw:GridWeb في نموذج aspx.
1. تغيرت المسارات القديمة لعميل Aspose.Grid.Web، agw_client، إلى acw_client لـ Aspose.Cells.GridWeb.
1. تم تغيير إعداد المسار لعميل في ملف web.config، على سبيل المثال: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

تم التغيير إلى 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
