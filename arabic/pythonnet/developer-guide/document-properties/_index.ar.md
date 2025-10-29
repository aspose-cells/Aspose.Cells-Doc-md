---
title: إدارة خصائص المستند
linktitle: خصائص المستند
type: docs
weight: 80
url: /ar/python-net/managing-document-properties/
description: تعلم كيف تدير خصائص المستند من خلال API الخاص بـ Aspose.Cells لبايثون via .NET.
keywords: كيفية إدارة خصائص المستند في لغة C#، الحصول أو تعيين خصائص المستند باستخدام C#، إضافة أو حذف خصائص المستند عبر C#، إدراج أو إزالة خصائص المستند باستخدام C#، كيفية الوصول إلى خصائص المستند باستخدام API الخاص بـ Aspose.Cells لبايثون via .NET.
---


## **مقدمة**

يوفر Microsoft Excel القدرة على إضافة خصائص إلى ملفات جداول البيانات. توفر هذه الخصائص المستندية معلومات مفيدة وتنقسم إلى فئتين كما هو موضح أدناه.

- الخصائص المعرفة مسبقًا (المدمجة): الخصائص المدمجة تحتوي على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المخصصة (المخصصة): الخصائص المخصصة المحددة من قبل المستخدم النهائي في شكل زوج اسم-قيمة.

{{% alert color="primary" %}}

أهم نقطة لمعرفتها حول الخصائص المدمجة والمخصصة هي أنه يمكن الوصول إلى الخصائص المدمجة وتعديلها، ولكن لا يمكن إنشاؤها أو إزالتها. ومع ذلك، يمكن إنشاء الخصائص المخصصة وإدارتها.

{{% /alert %}}

## **كيفية إدارة خصائص المستند باستخدام Microsoft Excel**

يسمح Microsoft Excel لك بإدارة خصائص المستندات لملفات Excel بطريقة WYSIWYG. يرجى اتباع الخطوات التالية لفتح مربع حوار **الخصائص** في Excel 2016.

1. من القائمة **ملف**, حدد **معلومات**.

|**اختيار قائمة المعلومات**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. انقر على عنوان **الخصائص** وحدد "الخصائص المتقدمة".

|**النقر على اختيار الخصائص المتقدمة**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. إدارة خصائص مستند الملف.

|**مربع الحوار الخصائص**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
في مربع حوار الخصائص، هناك علامات تبويب مختلفة، مثل العامة، والملخص، والإحصائيات، والمحتويات، والمخصصة. تساعد كل علامة تبويب في تكوين أنواع مختلفة من المعلومات ذات الصلة بالملف. تُستخدم علامة التبويب المخصصة لإدارة الخصائص المخصصة.

## **كيفية العمل مع خصائص المستند باستخدام Aspose.Cells**

يمكن للمطورين إدارة خصائص المستند ديناميكيًا باستخدام API الخاص بـ Aspose.Cells لبايثون via .NET. تساعد هذه الميزة المطورين على تخزين معلومات مفيدة مع الملف، مثل وقت استلام الملف، المعالجة، التوقيت، وهلم جرا.

{{% alert color="primary" %}}

يكتب Aspose.Cells لبايثون via .NET مباشرة معلومات حول API ورقم الإصدار في المستندات الناتجة. على سبيل المثال، عند تحويل المستند إلى PDF، يُملأ حقل **التطبيق** بالقيمة 'Aspose.Cells' وحقل **منتج PDF** بالقيمة، مثلاً 'Aspose.Cells لبايثون via .NET الإصدار 17.9'.

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells لبايثون via .NET لتغيير أو إزالة هذه المعلومات من المستندات الناتجة.

{{% /alert %}}


### **كيفية إضافة أو إزالة خصائص المستند المخصصة**

كما وصفنا في وقت سابق في بداية هذا الموضوع ، لا يمكن للمطورين إضافة أو إزالة الخصائص المدمجة لأن هذه الخصائص محددة من النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها معرفة من قبل المستخدم.

### **كيفية إضافة الخصائص المخصصة**

لقد كشف API الخاص بـ Aspose.Cells لبايثون via .NET عن طريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) لفئة [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) لإضافة خصائص مخصصة إلى المجموعة. تضيف طريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) الخاصية إلى ملف Excel وتعيد مرجعًا للخصيصة الجديدة ككائن [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **مواضيع متقدمة**
- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة](/cells/ar/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة](/cells/ar/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند](/cells/ar/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

{{< app/cells/assistant language="python-net" >}}
