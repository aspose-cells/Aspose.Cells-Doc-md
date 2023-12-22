---
title: Licensing
type: docs
weight: 50
url: /ar/cpp/licensing/
---
##  **قيود إصدار التقييم**
 يمكن تنزيل نسخة تقييمية مجانية من Aspose.Cells for C++ من قسم التنزيلات في موقع الويب الخاص بـ Aspose على:<https://downloads.aspose.com/cells/cpp>.
##  **تطبيق الترخيص باستخدام ملف أو كائن دفق**
يمكن تحميل الترخيص من ملف أو كائن دفق. Aspose.Cells for C++ سيحاول العثور على الرخصة في المواقع التالية:

1. المسار الصريح.
1. المجلد الذي يحتوي على Aspose.Cells.dll.
1. المجلد الذي يحتوي على التجميع الذي يسمى Aspose.Cells.dll.
1. المجلد الذي يحتوي على مجموعة الإدخال (.exe الخاص بك).
1. مورد مضمن في التجميع يسمى Aspose.Cells.dll.

أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل الملف Aspose.Cells.dll وتحديد اسم الملف، بدون مسار، كما هو موضح في المثال أدناه.
###  **تحميل الترخيص من الملف**
أسهل طريقة لتطبيق الترخيص هي وضع ملف الترخيص في نفس المجلد مثل الملف Aspose.Cells.dll وتحديد اسم الملف فقط بدون مسار.

{{% alert color="primary" %}} 

عند استدعاء الأسلوب SetLicense، يجب أن يكون اسم الترخيص الذي تقوم بتمريره هو اسم ملف الترخيص. على سبيل المثال، إذا قمت بتغيير اسم ملف الترخيص إلى "Aspose.Cells.lic.xml"، فقم بتمرير اسم الملف هذا إلى الأسلوب Cells->SetLicense(...).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
###  **تحميل ترخيص من كائن دفق**
يوضح المثال التالي كيفية تحميل ترخيص من الدفق.

**C++**

{{< highlight "csharp" >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
