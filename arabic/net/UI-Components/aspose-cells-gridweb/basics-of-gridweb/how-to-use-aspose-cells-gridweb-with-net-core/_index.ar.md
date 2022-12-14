---
title: كيفية استخدام Aspose.Cells.GridWeb مع .NET Core
type: docs
weight: 40
url: /ar/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

يشرح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb مع تطبيقات .NET Core باستخدام Visual Studio.NET 2019. هذا الموضوع مفيد للمطورين على مستوى المبتدئين الذين يعملون مع Aspose.Cells.GridWeb.

{{% /alert %}} 
## **استخدم Aspose.Cells.GridWeb مع .NET Core**
يوضح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb من خلال إنشاء نموذج لموقع ويب في Visual Studio 2019. وقد تم تقسيم العملية إلى خطوات.
### **الخطوة الأولى: إنشاء مشروع جديد**
1. افتح Visual Studio 2019.
1.  من**ملف** القائمة ، حدد**جديد** ، ومن بعد**مشروع**.
 يتم فتح مربع حوار إنشاء مشروع جديد.
1.  يختار**ASP.NET تطبيق الويب الأساسي** من Visual Studio تثبيت قوالب المشروع وانقر فوق**التالي**.

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  حدد موقعًا حيث موقع واسم المشروع وانقر**خلق**.

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  حدد ملف**تطبيق الويب (Model-View-Controller)** وتأكد من ذلك**ASP .NET Core 2.1.2 تحديث** تم الإختيار.

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  انقر**خلق**.
### **الخطوة 2: فحص العرض الأولي**
يؤدي تشغيل المشروع الذي تم إنشاؤه حديثًا إلى إظهار القالب الافتراضي في المتصفح كما هو موضح في الصورة أدناه.



![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **الخطوة 3: إضافة Aspose.Cells.GridWeb**
1. أضف الحزم Nuget التالية إلى المشروع

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. إضافة Aspose.Cells.GridWeb Package

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. أضف ما يلي إلى ملف ** _ ViewImports.cshtml ** في مجلد Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

سيبدو الملف هكذا بعد التعديلات

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. ضع الكود التالي في طريقة فهرس HomeController's.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

تذكر أن تقوم بتحديث SessionStorePath ومسار ImportExcelFile.

{{% /alert %}} 

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  أضف التعليمات البرمجية التالية في ملف**Index.cshtml** ملف في عرض> الدليل الرئيسي.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

سيبدو الملف هكذا بعد التغيير.

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. إضافة دعم الجلسة و GridScheduedService في ملف Startup.cs
 1. قم بإضافة مقتطف الشفرة التالي في طريقة ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. أضف مقتطف الشفرة التالي في طريقة التكوين.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. ضع أحدث acw_client في الدليل: ** wwwroot / js ** {{% alert color="primary" %}} {{% /alert %}}
1.  يضيف**AcwController**في وحدات التحكم للتعامل مع خريطة مسار ACW التي يمكن أن توفر جميع العمليات الافتراضية لإجراء التحرير العام.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **الخطوة 4: اختبر التطبيق**
سيؤدي تشغيل التطبيق إلى إخراج مشابه لما هو موضح في الصورة أدناه.

![ما يجب القيام به: image_بديل_نص](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
