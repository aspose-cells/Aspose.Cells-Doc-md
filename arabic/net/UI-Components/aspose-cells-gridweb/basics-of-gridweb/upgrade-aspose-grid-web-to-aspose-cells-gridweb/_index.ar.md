---
title: قم بالترقية Aspose.Grid.Web إلى Aspose.Cells.GridWeb
type: docs
weight: 30
url: /ar/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

لتسهيل الترقية ، نحتفظ بمستند يصف المعلومات الهامة للمستخدمين الحاليين ، وخاصة أولئك الذين استخدموا Aspose.Grid.Web الأقدم ويحتاجون إلى الترقية إلى Aspose.Cells.GridWeb المدمج.

 تهدف هذه إلى أن تكون ملاحظات موجزة ، ويجب أن تكون قادرًا على العثور على مزيد من المعلومات من خلال الاطلاع على أقسام[دليل المطور](/cells/ar/net/developer-guide/).

{{% /alert %}}

## **الترقية إلى Aspose.Cells.GridWeb**

 Aspose.Grid. قد يواجه مستخدمو الويب مشكلات باستخدام Aspose.Cells.GridWeb الجديد عند الترقية إليه. وتجدر الإشارة إلى أنه تمت إعادة تسمية Aspose.Grid.Web وأصبح جزءًا من Aspose.Cells لذلك لن نواصل أو نجري تعديلات على الإصدارات الأقدم من عنصر التحكم.

ليس من الصعب الترقية إلى أحدث مكون Aspose.Cells.GridWeb.

{{% alert color="primary" %}}

هناك بعض التغييرات في API حيث تظل الفئات التي تحتوي على الأعضاء والتركيبات والتعدادات وما إلى ذلك كما هي. تم إجراء معظم التغييرات على مساحات أسماء عناصر التحكم والعلامات أو السمات الأخرى.

{{% /alert %}}

فيما يلي قائمة مساحات الأسماء والسمات / العلامات الأخرى التي تم تغييرها الآن:

1. تمت إعادة تسمية مساحة اسم الويب Aspose.Grid.Web إلى Aspose.Cells.GridWeb.
1. تم تغيير مساحة الاسم Aspose.Grid.Web.Data تسمية Aspose.Cells.GridWeb.Data.
1. تمت إعادة تسمية مساحة الاسم Aspose.Grid.Web.Design باسم Aspose.Cells.GridWeb.Design.
1. تمت إعادة تسمية مساحة الاسم Aspose.Grid.Formula إلى Aspose.Cells.GridFormula ، ومع الإصدارات الأخيرة من المكون ، تمت إزالة مساحة الاسم المذكورة بالكامل من API العام.
1. agw العلامة: تم تغيير GridWeb إلى acw: GridWeb في نموذج aspx.
1. أقدم Aspose.Grid.Web مسار العميل ، agw_العميل ، قد تغير إلى ACW_العميل Aspose.Cells.GridWeb.
1.  إعداد مسار العميل في ملف web.config ، على سبيل المثال:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 قد تغير إلى

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
