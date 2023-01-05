---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /ar/net/aspose-cells-net-for-php/
---
## **ابدء**

### **مقدمة**

### **متطلبات النظام والأنظمة الأساسية المدعومة**

#### **متطلبات النظام**

**فيما يلي متطلبات النظام لاستخدام Aspose.Cells .NET for PHP:**

- IIS مع PHP و PHP Manager مثبتين.
- Aspose.Total واجهات برمجة التطبيقات.
- Aspose.Cells ملف Interop dll و tlb.

#### **المنصات المدعومة**

**فيما يلي المنصات المدعومة:**

- PHP 5.3 أو أعلى
- Windows نظام التشغيل

### **التنزيل والتكوين**

#### **تحميل المكتبات المطلوبة**

تحميل المكتبات المطلوبة المذكورة أدناه. هذه هي المطلوبة لتنفيذ Aspose.Cells Java for PHP أمثلة.

- [قم بتنزيل ملفات Aspose.Cells for .NET (DLL أو MSI) من قسم التنزيل](https://downloads.aspose.com/cells/net)
- [تحميل Aspose.Cells for .NET interop dll](https://downloads.aspose.com/cells/net)

إذا قمت بتنزيل إصدار MSI ، فستجد Aspose.Cells.dll في الموقع المثبت وهو المجلد C: \ Program Files (x86) \ Aspose \ Aspose.Cells for .NET \ Bin \ net2.0 افتراضيًا.
ومع ذلك ، في حالة تنزيل إصدار DLL ، يمكنك استخراجه ثم نسخ Aspose.Cells.dll من مجلد .NET 2.0 إلى مجلد c: \ temp لسهولة الاستخدام.
وبالمثل استخراج ملف مضغوط interop ونسخ Aspose.Inteop.dll إلى c: \ temp

#### **تنزيل أمثلة من مواقع الترميز الاجتماعي**

الإصدارات التالية من الأمثلة قيد التشغيل متاحة للتنزيل على مواقع الترميز الاجتماعي المذكورة أدناه:

-----

##### **جيثب**

- **Aspose.Cells .NET for PHP أمثلة**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **كيفية تكوين كود المصدر على النظام الأساسي Windows**

يرجى اتباع هذه الخطوات البسيطة لفتح كود المصدر وتوسيعه أثناء استخدام:

##### **1. قم بتسجيل ملفات dll و interop.dll على سبيل المثال Aspose.Cells.dll و Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. قم بتمكين امتدادات COM و DOTNET في PHP.**

في IIS ، افتح PHP Manager ، ثم انقر فوق "Enable to Disable and Extension". ابحث عن ملف php_كوم_dotnet.dll وتأكد من تمكينه.

##### **3. قم بتكوين Aspose.Cells .NET for PHP أمثلة**

###### **طريقة 1**

 أمثلة استنساخ PHP من[جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
وقم بتشغيل الأمر التالي

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **الطريقة الثانية**

أضف الأسطر التالية في ملف composer.json الخاص بمشروع PHP

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

وقم بتشغيل أمر التثبيت

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 لقراءة عن الملحن زيارة<https://getcomposer.org/>

### **توسيع الدعم والمساهمة**

#### **الدعم**

منذ الأيام الأولى من Aspose ، علمنا أن مجرد تقديم منتجات جيدة لعملائنا لن يكون كافيًا. كنا بحاجة أيضًا إلى تقديم خدمة جيدة. نحن مطورون بأنفسنا ونفهم مدى الإحباط عندما تمنعك مشكلة فنية أو غرابة في البرنامج من القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل وليس خلقها.

هذا هو السبب في أننا نقدم الدعم المجاني. أي شخص يستخدم منتجاتنا ، سواء اشتراها أو استخدم تقييمًا ، يستحق كامل اهتمامنا واحترامنا.

يمكنك تسجيل أي مشكلات أو اقتراحات تتعلق بـ Aspose.Cells .NET for PHP باستخدام أي من الأنظمة الأساسية التالية:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **تمديد والمساهمة**

Aspose.Cells .NET for PHP مفتوح المصدر وكود المصدر الخاص به متاح على مواقع الترميز الاجتماعي الرئيسية المدرجة أدناه. يتم تشجيع المطورين على تنزيل الكود المصدري والمساهمة من خلال اقتراح أو إضافة ميزة جديدة أو تحسين الميزات الموجودة ، بحيث يمكن للآخرين الاستفادة منها أيضًا.

#### **مصدر الرمز**

يمكنك الحصول على أحدث كود مصدر من أحد المواقع التالية

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **أمثلة على التعليمات البرمجية النموذجية**

يتضمن هذا القسم المواضيع التالية

- [دليل مبرمجي PHP](/cells/ar/net/php-programmers-guide/)
  - [العمل مع الملفات في PHP](/cells/ar/net/working-with-files-in-php/)
    - [ميزات معالجة الملفات في PHP](/cells/ar/net/file-handling-features-in-php/)
      - [فتح الملفات في PHP](/cells/ar/net/opening-files-in-php/)
      - [حفظ الملفات في PHP](/cells/ar/net/saving-files-in-php/)
    - [ميزات المنفعة في PHP](/cells/ar/net/utility-features-in-php/)
      - [تشفير الملفات في PHP](/cells/ar/net/encrypting-files-in-php/)
      - [Excel إلى PDF التحويل في PHP](/cells/ar/net/excel-to-pdf-conversion-in-php/)
      - [إدارة خصائص الوثيقة في PHP](/cells/ar/net/managing-document-properties-in-php/)
      - [ورقة العمل لتحويل الصورة في PHP](/cells/ar/net/worksheet-to-image-conversion-in-php/)
  - [العمل مع الصيغ في PHP](/cells/ar/net/working-with-formulas-in-php/)
    - [حساب الصيغ في PHP](/cells/ar/net/calculating-formulas-in-php/)
  - [العمل مع أوراق العمل في PHP](/cells/ar/net/working-with-worksheets-in-php/)
    - [ميزات الإدارة في PHP](/cells/ar/net/management-features-in-php/)
      - [إدارة أوراق العمل في PHP](/cells/ar/net/managing-worksheets-in-php/)
        - [أضف أوراق العمل إلى ملف Excel الموجود في PHP](/cells/ar/net/add-worksheets-to-existing-excel-file-in-php/)
        - [أضف أوراق عمل إلى ملف Excel جديد في PHP](/cells/ar/net/add-worksheets-to-new-excel-file-in-php/)
        - [إزالة أوراق العمل باستخدام فهرس الورقة في PHP](/cells/ar/net/removing-worksheets-using-sheet-index-in-php/)
        - [إزالة أوراق العمل باستخدام اسم الورقة في PHP](/cells/ar/net/removing-worksheets-using-sheet-name-in-php/)
