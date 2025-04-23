---
title: إدارة خصائص المستند
linktitle: خصائص المستند
type: docs
weight: 80
url: /ar/net/managing-document-properties/
description: تعلم كيفية إدارة خصائص المستند من خلال واجهات برمجة التطبيقات Aspose.Cells for NET.
keywords: كيفية إدارة خصائص المستند في C#، الحصول على خصائص المستند أو تعيينها باستخدام C#، إضافة خصائص المستند أو حذفها عبر C#، إدراج خصائص المستند أو إزالتها باستخدام C#، كيفية الوصول إلى خصائص المستند باستخدام واجهات برمجة التطبيقات Aspose.Cells for NET.
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

يمكن للمطورين إدارة خصائص الوثيقة بشكل ديناميكي باستخدام واجهات برمجة التطبيقات Aspose.Cells. تساعد هذه الميزة المطورين في تخزين معلومات مفيدة إلى جانب الملف، مثل متى تم استلام الملف ومعالجته وتسجيل الوقت وما إلى ذلك.

{{% alert color="primary" %}}

تكتب Aspose.Cells for .NET المعلومات مباشرة حول واجهة برمجة التطبيقات ورقم الإصدار في وثائق الإخراج. على سبيل المثال، عند تقديم المستند إلى PDF، يقوم Aspose.Cells for .NET بملء حقل **التطبيق** بالقيمة 'Aspose.Cells' وحقل **منتج PDF** بالقيمة، على سبيل المثال، 'Aspose.Cells v17.9'.

يرجى ملاحظة أنه لا يمكنك تعليم Aspose.Cells for .NET بتغيير أو إزالة هذه المعلومات من وثائق الإخراج.

{{% /alert %}}

### **كيفية الوصول إلى خصائص المستند**

تدعم واجهات برمجة التطبيقات Aspose.Cells كلا من أنواع خصائص المستند، المدمجة والمخصصة. يمثل [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) لـ Aspose.Cells ملف Excel و، مثل ملف Excel، يمكن أن يحتوي [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الفصول المتعددة، يمثل كل منها بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في حين أن مجموعة الفصول تمثل بواسطة فئة [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection).

استخدم [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) للوصول إلى خصائص المستند كما هو موضح أدناه.

- للوصول إلى خصائص المستند المدمجة، استخدم [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- للوصول إلى خصائص المستند المخصصة ، استخدم [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

كلا [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) و [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) يعيدان النسخة الفردية من [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). تحتوي هذه المجموعة على [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) كائن ، كل منها يمثل خاصية مستند مدمجة أو مخصصة واحدة.

من متطلبات التطبيق كيفية الوصول إلى الخاصية ، أي؛ باستخدام فهرس أو اسم الخاصية من [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) كما هو موضح في المثال أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

يتيح فئة [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) استرداد اسم وقيمة ونوع خاصية المستند:

- للحصول على اسم الخاصية ، استخدم [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- للحصول على قيمة الخاصية ، استخدم [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) يعيد القيمة ككائن.
- للحصول على نوع الخاصية ، استخدم [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type). تعيد هذه واحدة من قيم تعداد [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype). بعد الحصول على نوع الخاصية ، استخدم واحدة من طرق **DocumentProperty.ToXXX** للحصول على قيمة النوع المناسب بدلاً من استخدام [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). تم وصف طرق **DocumentProperty.ToXXX** في الجدول أدناه.

{{% alert color="primary" %}}

توفر فئة [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) أيضًا مجموعة من الطرق التي تعيد قيم أنواع بيانات أخرى.

{{% /alert %}}

|**اسم العضو**|**الوصف**|**طريقة ToXXX**|
| :- | :- | :- |
|Boolean| نوع البيانات الخاصية هو بوليان|ToBool|
|Date| نوع البيانات الخاصية هو التاريخ والوقت. لاحظ أن Microsoft Excel يخزن فقط <br> الجزء التاريخي ، لا يمكن تخزين الوقت في خاصية مخصصة من هذا النوع|ToDateTime|
|Float| نوع البيانات الخاصية هو Double|ToDouble|
|Number| نوع البيانات الخاصية هو Int32|ToInt|
|String| نوع البيانات الخاصية هو String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **كيفية إضافة أو إزالة خصائص المستند المخصصة**

كما وصفنا في وقت سابق في بداية هذا الموضوع ، لا يمكن للمطورين إضافة أو إزالة الخصائص المدمجة لأن هذه الخصائص محددة من النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها معرفة من قبل المستخدم.

### **كيفية إضافة الخصائص المخصصة**

قدمت واجهات برمجة التطبيقات Aspose.Cells الطريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) لفئة [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) من أجل إضافة خصائص مخصصة إلى المجموعة. تضيف طريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) الخاصية إلى ملف Excel وتعيد مرجعًا لخاصية المستند الجديدة ككائن [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **كيفية تكوين خاصية مخصصة مرتبطة بالمحتوى**

لإنشاء خاصية مخصصة مرتبطة بمحتوى نطاق محدد ، اتصل بالطريقة [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) وقم بتمرير اسم الخاصية والمصدر. يمكنك التحقق مما إذا كانت الخاصية مكونة كمرتبطة بالمحتوى باستخدام الخاصية [**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent). علاوة على ذلك ، من الممكن أيضًا الحصول على نطاق المصدر باستخدام الخاصية [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) من فئة [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

نحن نستخدم ملف نموذجي بسيط لبرنامج Microsoft Excel في المثال. يحتوي دفتر العمل على نطاق مسمى محدد يحمل التسمية **MyRange** والذي يشير إلى قيمة الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **كيفية إزالة الخصائص المخصصة**

لإزالة الخصائص المخصصة باستخدام Aspose.Cells، قم بالاتصال بالطريقة [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove) وقم بتمرير اسم خاصية المستند التي تريد إزالتها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **مواضيع متقدمة**
- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/net/adding-custom-properties-visible-inside-document-information-panel/)
- [ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة](/cells/ar/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة](/cells/ar/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند](/cells/ar/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="csharp" >}}
