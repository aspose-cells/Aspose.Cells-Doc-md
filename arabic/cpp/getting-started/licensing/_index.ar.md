---
title: ترخيص
type: docs
weight: 50
url: /ar/cpp/licensing/
---

## **قيود النسخة التقييمية**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **تطبيق الترخيص باستخدام ملف أو كائن تيار**
يمكن تحميل الترخيص من ملف أو كائن تيار. Aspose.Cells for C++ سيحاول العثور على الترخيص في المواقع التالية:

1. المسار الصريح.
1. المجلد الذي يحتوي على Aspose.Cells.dll.
1. المجلد الذي يحتوي على التجميع الذي دعا Aspose.Cells.dll.
1. المجلد الذي يحتوي على التجميع الرئيسي (.exe الخاص بك).
1. مورد مضمن في التجميع الذي دعا Aspose.Cells.dll.

أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس مجلد ملف Aspose.Cells.dll وتحديد اسم الملف، بدون مسار، كما هو موضح في المثال أدناه.
### **تحميل ترخيص من ملف**
أسهل طريقة لتطبيق ترخيص هي وضع ملف الترخيص في نفس مجلد ملف Aspose.Cells.dll وتحديد اسم الملف فقط بدون مسار.

{{% alert color="primary" %}} 

عند استدعاء طريقة SetLicense، يجب أن يكون اسم الترخيص الذي تمر به اسم ملف الترخيص. على سبيل المثال، إذا قمت بتغيير اسم ملف الترخيص إلى "Aspose.Cells.lic.xml"، فضع هذا الاسم في وسيلة الطرد(…) Cells->SetLicense.

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **تحميل ترخيص من كائن تيار**
المثال التالي يوضح كيفية تحميل ترخيص من تيار.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
