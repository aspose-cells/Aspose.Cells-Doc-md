---
title: كيفية تشغيل الأمثلة
type: docs
weight: 140
url: /ar/net/how-to-run-the-examples/
---

## **متطلبات البرنامج**
يرجى التأكد من تلبية الشروط التالية قبل تنزيل وتشغيل الأمثلة.

1. Visual Studio 2015 أو أحدث
1. تم تثبيت مدير حزم NuGet في Visual Studio. في الغالب يكون مثبتًا بالفعل في Visual Studio 2015. للحصول على تفاصيل حول كيفية تثبيت مدير حزم NuGet ، يرجى التحقق: [تثبيت أدوات عميل NuGet](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1. اذهب إلى Tools->Options->NuGet Package Manager->Package Sources وتأكد من أن الخيار **nuget.org** محدد
1. يستخدم المشروع المثالي ميزة استعادة حزمة NuGet التلقائية لذلك يجب أن يكون لديك اتصال إنترنت نشط. إذا لم يكن لديك اتصال إنترنت نشط على الجهاز الذي سيتم تنفيذ الأمثلة عليه ، يرجى التحقق من [التثبيت](/cells/ar/net/installation-and-deployment/) وإضافة المرجع يدويًا إلى Aspose.Cells.dll في مشروع النموذج.
## **تحميل من GitHub**
جميع أمثلة Aspose.Cells for .NET مستضافة على [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
## **أمثلة Aspose.Cells**
- يمكنك إما نسخ المستودع باستخدام عميل GitHub المفضل لديك أو تنزيل ملف ZIP من [هنا](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- استخراج محتويات ملف ZIP إلى أي مجلد على جهاز الكمبيوتر الخاص بك. يقع جميع الأمثلة في مجلد **Examples**.
- هناك ملف حل Visual Studio لأمثلة C# أي **Aspose.Cells.Examples.CSharp.sln**.
- تم إنشاء المشروع وصيانته في Visual Studio 2015.
- افتح ملف الحل في Visual Studio وقم ببناء المشروع.
- في التشغيل الأول ، سيتم تنزيل التبعيات تلقائيًا عبر NuGet. يمكنك أيضًا تنزيل ملفات DLL بشكل منفصل من [هنا](https://downloads.aspose.com/cells/net).
- يحتوي مجلد **Data** في الجذر مجلد **Examples** على ملفات الإدخال التي تستخدم أمثلة CSharp. من الضروري تنزيل مجلد **Data** إلى جانب مشروع الأمثلة.
- افتح **RunExamples.cs** ، وتم استدعاء جميع الأمثلة من هنا.
- قم بإزالة التعليق عن الأمثلة التي ترغب في تشغيلها من داخل المشروع.
## **أمثلة Aspose.Cells.GridDesktop**
- تتضمن أمثلة Aspose.Cells.GridDesktop أيضًا مستودع [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) وسوف تكون متاحة كجزء من ملف ZIP القابل للتنزيل من [هنا](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- تقع جميع الأمثلة في مجلد **Examples_GridDesktop**.
- على غرار أمثلة Aspose.Cells ، اسم ملف الحل لأمثلة GridWeb هو **Aspose.Cells.GridDesktop.Examples.CSharp.sln**.
- افتح ملف الحل في Visual Studio وقم ببناء المشروع.
- تم تضمين جميع التبعيات كجزء من مشروع الأمثلة. يمكنك أيضًا تحميل ملفات DLL بشكل منفصل من [هنا](https://downloads.aspose.com/cells/net).
- المجلد **Data** في جذر مجلد **Examples_GridDesktop** يحتوي على ملفات الإدخال المستخدمة في الأمثلة. من الضروري تحميل المجلد **Data** جنبًا إلى جنب مع مشروع الأمثلة.
- افتح وشغّل المشروع.
- انقر فوق الأمثلة في القائمة التي ترغب في تشغيلها من خلال الاستمارة.
## **أمثلة Aspose.Cells.GridWeb**
- تتضمن أمثلة Aspose.Cells.GridWeb أيضًا في مستودع [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) وسيكون متاحًا كجزء من ملف ZIP القابل للتنزيل من [هنا](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- جميع الأمثلة موجودة في المجلد **Examples_GridWeb**.
- مشابهة لأمثلة Aspose.Cells، يكون اسم ملف الحل لأمثلة GridWeb هو **Aspose.Cells.GridWeb.Examples.CSharp.sln**.
- افتح ملف الحل في Visual Studio وقم ببناء المشروع.
- تم تضمين جميع التبعيات كجزء من مشاريع الأمثلة. يمكنك أيضًا تحميل ملفات DLL بشكل منفصل من [هنا](https://downloads.aspose.com/cells/net).
- المجلد **Data** في الجذر المجلد **Examples_GridWeb** يحتوي على ملفات الإدخال المستخدمة في الأمثلة. من الضروري تحميل المجلد **Data** جنبًا إلى جنب مع مشروع الأمثلة.
- افتح وشغل **Examples.aspx** في مشروع الأمثلة.
- انقر على الأمثلة في المتصفح التي ترغب في تشغيلها من داخل المشروع.
{{< app/cells/assistant language="csharp" >}}
