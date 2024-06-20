---
title: كيفية استخدام Aspose.Cells.GridWeb مع .NET Core
type: docs
weight: 40
url: /ar/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: يقدم هذا المقال كيفية استخدام GridWeb في تطبيق ويب .net core
---

{{% alert color="primary" %}} 

يشرح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb مع تطبيقات .NET Core باستخدام Visual Studio.NET 2019. هذا الموضوع مفيد للمطورين على مستوى المبتدئين الذين يعملون مع Aspose.Cells.GridWeb.

{{% /alert %}} 
## **استخدام Aspose.Cells.GridWeb مع .NET Core**
يوضح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb عن طريق إنشاء موقع ويب عيني في Visual Studio 2019. تم تقسيم العملية إلى خطوات.
### **الخطوة 1: إنشاء مشروع جديد**
1. قم بفتح برنامج Visual Studio 2019.
1. من قائمة **ملف**, حدد **جديد**, ثم **مشروع**.
   يتم فتح مربع حوار إنشاء مشروع جديد.
1. حدد **ASP.NET Core Web Application** من قوالب المشاريع المثبتة في برنامج Visual Studio وانقر **التالي**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. حدد الموقع واسم المشروع ثم انقر **إنشاء**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. حدد قالب **Web Application (Model-View-Controller)** وتأكد من تحديد **ASP .NET Core 2.1**. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. انقر **إنشاء**.
### **الخطوة 2: فحص العرض الأولي**
تشغيل المشروع الذي تم إنشاؤه مؤخرًا يعرض النموذج الافتراضي في المتصفح كما هو موضح في الصورة أدناه.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **الخطوة 3: إضافة Aspose.Cells.GridWeb**
1. أضف حزم Nuget التالية إلى المشروع.

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. أضف حزمة Aspose.Cells.GridWeb

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. أضف الكود التالي إلى ملف **_ViewImports.cshtml** في مجلدات العرض.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

سيبدو الملف بهذا الشكل بعد التعديلات

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. ضع الكود التالي في طريقة Index في ملف HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

تذكر تحديث مسار SessionStorePath ومسار ImportExcelFile.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. أضف الكود التالي في ملف **Index.cshtml** في مجلد العرض > الرئيسي.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

سيبدو الملف بهذا الشكل بعد التغيير.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. أضف دعم الجلسة و GridScheduedService في ملف Startup.cs
   1. أضف كود المقتطف التالي في طريقة الـ ConfigureService.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. أضف قطعة الكود التالية في طريقة التكوين.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. ضع أحدث acw_client في الدليل: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. أضف **AcwController** في المتحكمات للتعامل مع خريطة مسار الـ acw التي يمكن أن توفر جميع العمليات الافتراضية لإجراءات تحرير عامة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **الخطوة 4: اختبار التطبيق**
تشغيل التطبيق سيكون المخرج مشابهًا لما هو موضح في الصورة أدناه.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
