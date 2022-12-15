---
title: الترخيص
type: docs
weight: 50
url: /ar/cpp/licensing/
---
## **قيود إصدار التقييم**
 يمكن تنزيل نسخة تقييم مجانية من Aspose.Cells for C++ من قسم التنزيلات في موقع الويب Aspose على:<https://downloads.aspose.com/cells/cpp>.
## **تطبيق الترخيص باستخدام ملف أو كائن دفق**
يمكن تحميل الترخيص من ملف أو كائن دفق. Aspose.Cells for C++ سيحاول العثور على الترخيص في المواقع التالية:

1. مسار صريح.
1. المجلد الذي يحتوي على Aspose.Cells.dll.
1. المجلد الذي يحتوي على التجميع الذي يسمى Aspose.Cells.dll.
1. المجلد الذي يحتوي على تجميع الإدخال (الخاص بك. exe).
1. مورد مضمن في التجميع يسمى Aspose.Cells.dll.

أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل ملف Aspose.Cells.dll وتحديد اسم الملف ، بدون مسار ، كما هو موضح في المثال أدناه.
### **تحميل ترخيص من ملف**
أسهل طريقة لتطبيق ترخيص هي وضع ملف الترخيص في نفس المجلد مثل ملف Aspose.Cells.dll وتحديد اسم الملف فقط بدون مسار.

{{% alert color="primary" %}} 

عند استدعاء طريقة SetLicense ، يجب أن يكون اسم الترخيص الذي تمرره هو اسم ملف الترخيص. على سبيل المثال ، إذا قمت بتغيير اسم ملف الترخيص إلى "Aspose.Cells.lic.xml" ، فمرر اسم الملف هذا إلى الأسلوب Cells-> SetLicense (…).

{{% /alert %}} 

**C ++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **تحميل ترخيص من كائن تيار**
يوضح المثال التالي كيفية تحميل ترخيص من دفق.

**C ++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
