---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /ar/net/aspose-cells-net-for-php/
---

## **البدء**

### **مقدمة**

### **متطلبات النظام والمنصات المدعومة**

#### **متطلبات النظام**

**إليك المتطلبات النظامية لاستخدام Aspose.Cells .NET لـ PHP:**

- IIS مع PHP ومدير PHP مثبت.
- Aspose.Total APIs.
- Aspose.Cells ملف tlb وـ dll.

#### **المنصات المدعومة**

**إليك المنصات المدعومة:**

- PHP 5.3 أو أحدث
- نظام التشغيل Windows

### **تحميل وتكوين**

#### **تحميل المكتبات المطلوبة**

قم بتحميل المكتبات المطلوبة المذكورة أدناه. هذه المكتبات مطلوبة لتنفيذ أمثلة Aspose.Cells Java لـ PHP.

- [قم بتحميل ملفات Aspose.Cells for .NET (DLL أو MSI) من القسم](https://downloads.aspose.com/cells/net)
- [قم بتحميل Aspose.Cells for .NET interop dll](https://downloads.aspose.com/cells/net)

إذا قمت بتحميل الإصدار MSI ، فستجد Aspose.Cells.dll في الموقع المثبت وهو C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 افتراضيًا.
ومع ذلك ، في حالة قمت بتنزيل إصدار DLL ، يمكنك استخراجه ثم نسخ Aspose.Cells.dll من مجلد .NET 2.0 إلى مجلد c:\temp لسهولة الاستخدام.
بالمثل قم بإستخراج ملف الضغط الخاص بالانتروب ونسخ Aspose.Inteop.dll إلى c:\temp

#### **تحميل الأمثلة من مواقع الترميز الاجتماعي**

الإصدارات التالية لأمثلة تشغيل متوفرة للتنزيل على المواقع التالية المذكورة أدناه:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **كيفية تكوين كود المصدر على منصة Windows**

يرجى اتباع هذه الخطوات البسيطة لفتح وتوسيع الكود المصدري أثناء الاستخدام:

##### **1. سجل كل من ملفات dll و interop.dll على سبيل المثال Aspose.Cells.dll و Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. قم بتمكين ملحقات COM و DOTNET في PHP.**

في IIS افتح PHP Manager ثم انقر على ‘تمكين لتعطيل وتوسيع‘. ابحث عن php_com_dotnet.dll وتأكد من تمكينه.

##### **3. تكوين أمثلة Aspose.Cells .NET لـ PHP**

###### **الطريقة 1**

نسخ أمثلة PHP من [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
ثم قم بتشغيل الأمر التالي

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **الطريقة الثانية**

في ملف composer.json لمشروع PHP الخاص بك ، أضف الأسطر التالية

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

ثم قم بتشغيل الأمر التثبيت

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **دعم التوسيع والمساهمة**

#### **الدعم**

منذ الأيام الأولى لـ Aspose ، كنا نعلم أن مجرد منح عملائنا منتجات جيدة لن يكون كافيًا. كنا بحاجة أيضًا إلى تقديم خدمة جيدة. نحن أنفسنا مطورين ونفهم مدى إزعاج القضايا التقنية أو العيوب في البرمجيات التي توقفك عن القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل ، وليس لخلقها.

هذا هو السبب في أننا نقدم الدعم المجاني. يستحق أي شخص يستخدم منتجاتنا ، سواء اشتروها أو كانوا يستخدمون تقييمًا ، كامل انتباهنا واحترامنا.

يمكنك تسجيل أي قضايا أو اقتراحات متعلقة بـ Aspose.Cells .NET for PHP باستخدام أي من البيئات التالية:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **تمديد والمساهمة**

Aspose.Cells .NET for PHP مفتوح المصدر ويتوفر رمزها المصدري على مواقع الويب الرئيسية للكود الاجتماعي المدرجة أدناه. يتم تشجيع المطورين على تنزيل رمز المصدر والمساهمة من خلال اقتراح أو إضافة ميزة جديدة أو تحسين تلك الموجودة ، بحيث يمكن للآخرين أيضًا الاستفادة منها.

#### **رمز المصدر**

يمكنك الحصول على آخر رمز مصدري من أحد المواقع التالية

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **أمثلة رمز البرنامج**

تتضمن هذا القسم المواضيع التالية

- [دليل مبرمجي PHP](/cells/ar/net/php-programmers-guide/)
  - [العمل مع الملفات في لغة PHP](/cells/ar/net/working-with-files-in-php/)
    - [ميزات معالجة الملفات في PHP](/cells/ar/net/file-handling-features-in-php/)
      - [فتح الملفات في PHP](/cells/ar/net/opening-files-in-php/)
      - [حفظ الملفات في PHP](/cells/ar/net/saving-files-in-php/)
    - [ميزات الأدوات في PHP](/cells/ar/net/utility-features-in-php/)
      - [تشفير الملفات في PHP](/cells/ar/net/encrypting-files-in-php/)
      - [تحويل Excel إلى PDF في PHP](/cells/ar/net/excel-to-pdf-conversion-in-php/)
      - [إدارة خصائص المستند في PHP](/cells/ar/net/managing-document-properties-in-php/)
      - [تحويل الجدول إلى صورة في PHP](/cells/ar/net/worksheet-to-image-conversion-in-php/)
  - [العمل مع الصيغ في PHP](/cells/ar/net/working-with-formulas-in-php/)
    - [حساب الصيغ في PHP](/cells/ar/net/calculating-formulas-in-php/)
  - [العمل مع أوراق العمل في PHP](/cells/ar/net/working-with-worksheets-in-php/)
    - [ميزات الإدارة في PHP](/cells/ar/net/management-features-in-php/)
      - [إدارة أوراق العمل في PHP](/cells/ar/net/managing-worksheets-in-php/)
        - [إضافة أوراق عمل إلى ملف Excel الحالي في PHP](/cells/ar/net/add-worksheets-to-existing-excel-file-in-php/)
        - [إضافة أوراق عمل إلى ملف Excel جديد في PHP](/cells/ar/net/add-worksheets-to-new-excel-file-in-php/)
        - [إزالة أوراق العمل باستخدام فهرس الورقة في PHP](/cells/ar/net/removing-worksheets-using-sheet-index-in-php/)
        - [إزالة أوراق العمل باستخدام اسم الورقة في PHP](/cells/ar/net/removing-worksheets-using-sheet-name-in-php/)
