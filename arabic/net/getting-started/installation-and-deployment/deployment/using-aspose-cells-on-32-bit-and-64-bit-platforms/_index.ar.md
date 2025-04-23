---
title: استخدام Aspose.Cells على منصات 32 بت و 64 بت
type: docs
weight: 10
url: /ar/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells هو مكون .NET نقي يمكن أن يبسط عملية النشر الخاصة بك عن طريق استخدام نسخة XCOPY. لتثبيت Aspose.Cells، يمكنك ببساطة نسخ تجميع المكون (Aspose.Cells.dll) في دليل لتطبيقك: يمكن للتطبيق أن يبدأ في استخدامه على الفور. هذا ممكن بسبب الطبيعة الذاتية الواصفة لمكونات .NET. هذا النوع من النشر لا يؤثر أيضًا على عملية التثبيت.

{{% /alert %}} 
## **النشر**
تدعم Aspose.Cells كل من البيئات 32-bit و 64-bit. عند تثبيت Aspose.Cells for .NET باستخدام مثبت MSI لـ Aspose.Cells، يتم إضافة مكتبات DLL مختلفة إلى مجلدات مختلفة في مجلد Aspose.Cells ${installation_Path}. انظر الوصف في الجدول لمعرفة أي مجلد يحتوي على المجمعات التي تحتاج إلى استخدامها مع إصدار معين من .NET Framework.

|**المجلد**|**الوصف**|
| :- | :- |
|net2.0|يحتوي على التجميعات المستخدمة مع .NET Framework 2.0، 3.0، 3.5، 4.0 و Mono. هذه هي التجميعات التي يجب عادة استخدامها لكلا البيئتين 32 بت و 64 بت.|
|net2.0_AuthenticodeSigned|نفس الشيء كما هو مذكور أعلاه، ولكن التجمعات موقعة رقميًا بـ Authenticode. قد تتحمل التجميعات الموقعة بشكل أبطأ من دون Authenticode|
|net3.5_ClientProfile|يحتوي على التجميعات المستخدمة مع .NET Framework 3.5 أو 4.0 Client Profile.|
|net3.5_ClientProfile_AuthenticodeSigned|نفس الشيء كما هو مذكور أعلاه، ولكن التجمعات موقعة رقميًا بـ Authenticode. قد تتحمل التجمعات الموقعة بشكل أبطأ من دون Authenticode.|
|net3.5|يحتوي على التجميعات المستخدمة مع .NET Framework 3.5 أو 4.0.|
|net3.5_AuthenticodeSigned|نفس الشيء كما هو مذكور أعلاه، ولكن التجمعات موقعة رقميًا بـ Authenticode. قد تتحمل التجمعات الموقعة بشكل أبطأ من دون Authenticode.|
|net4.0|يحتوي على التجميعات المستخدمة مع .NET Framework 4.0 و 4.5.|
|netStandard|يحتوي على مكتبات للاستخدام مع .Net Standard 2.0|
|netcoreapp2.1|يحتوي على مكتبات للاستخدام مع .Net core 2.1|
|Xamarin.iOS|يحتوي على مكتبات للاستخدام مع Xamarin.iOS|
|Xamarin.Android|يحتوي على مكتبات للاستخدام مع Xamarin.Android|
|net5.0|يحتوي على مكتبات للاستخدام مع .net5.0.|
|net6.0|يحتوي على مكتبات للاستخدام مع .net6.0.|
{{% alert color="primary" %}} 

في مشاريع VS.NET (على سبيل المثال 2005، 2008، 2010، 2012 الخ)، عند إضافة مرجع لـ Aspose.Cells، يُشير مربع الحوار إضافة المرجع إلى ملفات Aspose.Cells.dll في مجلد(مجلدي) net2.0 أو net3.5 على التوالي. (للمزيد من المعلومات، اقرأ الإشارة إلى Aspose.Cells من مشروع .NET.) يمكنك تغيير المرجع للمكتبة وفقًا لبيئتك. يرجى ملاحظة أنه إذا كان إطار العمل المستهدف للمشروع هو .NET Framework 3.5/4 Client Profile، استخدم ملف مكون Aspose.Cells.dll الموجود في مجلد net_ClientProfile.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
