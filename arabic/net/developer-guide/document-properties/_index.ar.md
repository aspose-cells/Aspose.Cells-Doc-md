---
title: إدارة خصائص الوثيقة
linktitle: خصائص المستند
type: docs
weight: 80
url: /ar/net/managing-document-properties/
description: إدارة خصائص المستندات لملفات جداول البيانات.
---
## **مقدمة**

يوفر Microsoft Excel إمكانية إضافة خصائص إلى ملفات جداول البيانات. توفر خصائص المستند هذه معلومات مفيدة وهي مقسمة إلى فئتين كما هو مفصل أدناه.

- الخصائص المحددة من قبل النظام (المضمنة): تحتوي الخصائص المضمنة على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المعرفة من قبل المستخدم (المخصصة): الخصائص المخصصة التي يحددها المستخدم النهائي في شكل زوج الاسم والقيمة.

{{% alert color="primary" %}}

أهم نقطة يجب معرفتها حول الخصائص المضمنة والمخصصة هي أنه يمكن الوصول إلى الخصائص المضمنة وتعديلها ، ولكن لا يتم إنشاؤها أو إزالتها. ومع ذلك ، يمكن إنشاء الخصائص المخصصة وإدارتها.

{{% /alert %}}

## **إدارة خصائص الوثيقة باستخدام Microsoft Excel**

 Microsoft يسمح لك Excel بإدارة خصائص الوثيقة لملفات Excel بطريقة WYSIWYG. يرجى اتباع الخطوات التالية لفتح ملف**ملكيات** الحوار في Excel 2016.

1.  من**ملف** القائمة ، حدد**معلومات**.

|**اختيار قائمة المعلومات**|
|:- |
|![ما يجب القيام به: image_بديل_نص](managing-document-properties_1.png)|
1.  انقر فوق**ملكيات**العنوان وحدد "خصائص متقدمة".

|**النقر فوق تحديد الخصائص المتقدمة**|
|:- |
|![ما يجب القيام به: image_بديل_نص](managing-document-properties_2.png)|
1. إدارة خصائص وثيقة الملف.

|**حوار الخصائص**|
|:- |
|![ما يجب القيام به: image_بديل_نص](managing-document-properties_3.png)|
في مربع حوار الخصائص ، توجد علامات تبويب مختلفة ، مثل عام ، وملخص ، وإحصاءات ، ومحتويات ، وعادات. تساعد كل علامة تبويب في تكوين أنواع مختلفة من المعلومات المتعلقة بالملف. يتم استخدام علامة التبويب "مخصص" لإدارة الخصائص المخصصة.

## **التعامل مع خصائص الوثيقة باستخدام Aspose.Cells**

يمكن للمطورين إدارة خصائص الوثيقة ديناميكيًا باستخدام Aspose.Cells APIs. تساعد هذه الميزة المطورين على تخزين المعلومات المفيدة مع الملف ، مثل وقت استلام الملف ومعالجته وختمه بالوقت وما إلى ذلك.

{{% alert color="primary" %}}

 Aspose.Cells for .NET يكتب مباشرة المعلومات حول API ورقم الإصدار في وثائق المخرجات. على سبيل المثال ، عند تقديم المستند إلى PDF ، يتم تعبئة Aspose.Cells for .NET**تطبيق** حقل بقيمة "Aspose.Cells" و**PDF منتج** حقل بالقيمة ، على سبيل المثال "Aspose.Cells v17.9".

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for .NET لتغيير أو إزالة هذه المعلومات من مستندات الإخراج.

{{% /alert %}}

### **الوصول إلى خصائص المستند**

تدعم واجهات برمجة التطبيقات Aspose.Cells كلا نوعي خصائص المستند المضمنة والمخصصة. Aspose.Cells '[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل class ملف Excel ، ومثل ملف Excel ، فإن ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمكن أن تحتوي الفئة على أوراق عمل متعددة ، يمثل كل منها ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class بينما يتم تمثيل مجموعة أوراق العمل بواسطة[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)صف دراسي.

 استخدم ال[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)للوصول إلى خصائص مستند الملف كما هو موضح أدناه.

-  للوصول إلى خصائص المستند المضمنة ، استخدم[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  للوصول إلى خصائص المستند المخصصة ، استخدم[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 كلا ال[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) و[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) إرجاع مثيل[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). هذه المجموعة تحتوي على[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)كائنات ، يمثل كل منها خاصية واحدة مضمنة أو مخصصة للمستند.

 الأمر متروك لمتطلبات التطبيق في كيفية الوصول إلى الممتلكات ، أي ؛ باستخدام فهرس أو اسم الخاصية من[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)كما هو موضح في المثال أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 ال[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)تسمح class باسترداد اسم وقيمة ونوع خاصية المستند:

-  للحصول على اسم الخاصية ، استخدم[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  للحصول على قيمة العقار ، استخدم[**الوثيقة القيمة**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**الوثيقة القيمة**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)تُرجع القيمة ككائن.
-  للحصول على نوع الخاصية ، استخدم[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . هذا يعيد واحد من[**نوع الملكية**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) قيم التعداد. بعد الحصول على نوع الخاصية ، استخدم أحد ملفات**الوثيقة الملكية. إلى XXX** طرق للحصول على قيمة النوع المناسب بدلاً من استخدام[**الوثيقة القيمة**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . ال**الوثيقة الملكية. إلى XXX**الطرق موضحة في الجدول أدناه.

{{% alert color="primary" %}}

 ال[**وثيقة الملكية**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)يوفر class أيضًا مجموعة من الطرق التي تُرجع قيم أنواع البيانات الأخرى.

{{% /alert %}}

|**اسم عضو**|**وصف**|**طريقة ToXXX**|
|:- |:- |:- |
|قيمة منطقية|نوع بيانات الخاصية منطقي|ToBool|
|تاريخ|نوع بيانات الخاصية هو DateTime. لاحظ أن Microsoft يخزن Excel فقط<br>جزء التاريخ ، لا يمكن تخزين أي وقت في خاصية مخصصة من هذا النوع|ToDateTime|
|تطفو|نوع بيانات الخاصية هو مزدوج|للمضاعفة|
|عدد|نوع بيانات الخاصية هو Int32|ToInt|
|سلسلة|نوع بيانات الخاصية هو String|إلى سلسلة|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **إضافة أو إزالة خصائص المستند المخصصة**

كما أوضحنا سابقًا في بداية هذا الموضوع ، لا يمكن للمطورين إضافة أو إزالة الخصائص المضمنة لأن هذه الخصائص محددة من قبل النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها محددة من قبل المستخدم.

### **إضافة خصائص مخصصة**

 كشفت واجهات برمجة التطبيقات Aspose.Cells ملف[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) طريقة ل[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) class لإضافة خصائص مخصصة إلى المجموعة. ال[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) أسلوب إضافة الخاصية إلى ملف Excel وإرجاع مرجع لخاصية المستند الجديدة كملف[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)موضوع.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **تكوين خاصية مخصصة "ارتباط بالمحتوى"**

 لإنشاء خاصية مخصصة مرتبطة بمحتوى نطاق معين ، قم باستدعاء[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) طريقة واسم الملكية والمصدر. يمكنك التحقق مما إذا كانت الخاصية قد تم تكوينها على أنها مرتبطة بالمحتوى باستخدام[**DocumentProperty.SLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) خاصية. علاوة على ذلك ، من الممكن أيضًا الحصول على نطاق المصدر باستخدام[**مصدر**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) ممتلكات[**وثيقة الملكية**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)صف دراسي.

 نستخدم ملف إكسل Microsoft قالب بسيط في المثال. يحتوي المصنف على نطاق مسمى محدد يسمى**MyRange** الذي يشير إلى قيمة الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **إزالة الخصائص المخصصة**

 لإزالة الخصائص المهيأة باستخدام Aspose.Cells ، قم باستدعاء[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)الطريقة وتمرير اسم خاصية المستند المراد إزالتها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **موضوعات مسبقة**
- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند](/cells/ar/net/adding-custom-properties-visible-inside-document-information-panel/)
- [إعداد خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة](/cells/ar/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [حدد إصدار المستند لملف Excel باستخدام خصائص المستند المضمنة](/cells/ar/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [حدد لغة ملف Excel باستخدام خصائص المستند المضمنة](/cells/ar/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
