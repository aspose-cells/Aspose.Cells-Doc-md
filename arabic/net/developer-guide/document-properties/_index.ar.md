---
title: إدارة خصائص الوثيقة
linktitle: خصائص المستند
type: docs
weight: 80
url: /ar/net/managing-document-properties/
description: تعرف على كيفية إدارة خصائص المستند من خلال Aspose.Cells لواجهات برمجة التطبيقات NET.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **مقدمة**

Microsoft يوفر Excel القدرة على إضافة خصائص إلى ملفات جداول البيانات. توفر خصائص المستند هذه معلومات مفيدة وتنقسم إلى فئتين كما هو مفصل أدناه.

- الخصائص المحددة بواسطة النظام (المضمنة): تحتوي الخصائص المضمنة على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المحددة من قبل المستخدم (المخصصة): الخصائص المخصصة التي يحددها المستخدم النهائي في شكل زوج من الاسم والقيمة.

{{% alert color="primary" %}}

أهم نقطة يجب معرفتها حول الخصائص المضمنة والمخصصة هي أنه يمكن الوصول إلى الخصائص المضمنة وتعديلها، ولكن لا يمكن إنشاؤها أو إزالتها. ومع ذلك، يمكن إنشاء الخصائص المخصصة وإدارتها.

{{% /alert %}}

##  **كيفية إدارة خصائص المستند باستخدام Microsoft إكسل**

 Microsoft يتيح لك Excel إدارة خصائص المستند لملفات Excel بطريقة WYSIWYG. يرجى اتباع الخطوات التالية لفتح**ملكيات** الحوار في Excel 2016

1.  من**ملف** من القائمة، حدد *معلومات**.

|**اختيار قائمة المعلومات**|
| :- |
|![ما يجب القيام به:image_alt_text](managing-document-properties_1.png)|
1.  انقر فوق**ملكيات** العنوان وحدد "الخصائص المتقدمة".

|**النقر فوق تحديد الخصائص المتقدمة**|
| :- |
|![ما يجب القيام به:image_alt_text](managing-document-properties_2.png)|
1. إدارة خصائص وثيقة الملف.

|**حوار الخصائص**|
| :- |
|![ما يجب القيام به:image_alt_text](managing-document-properties_3.png)|
في مربع الحوار "خصائص"، توجد علامات تبويب مختلفة، مثل "عام" و"الملخص" و"الإحصائيات" و"المحتويات" و"الجمارك". تساعد كل علامة تبويب في تكوين أنواع مختلفة من المعلومات المتعلقة بالملف. يتم استخدام علامة التبويب "مخصص" لإدارة الخصائص المخصصة.

##  **كيفية العمل مع خصائص المستند باستخدام Aspose.Cells**

يمكن للمطورين إدارة خصائص المستند ديناميكيًا باستخدام واجهات برمجة التطبيقات Aspose.Cells. تساعد هذه الميزة المطورين على تخزين معلومات مفيدة مع الملف، مثل وقت استلام الملف ومعالجته وختمه بالوقت وما إلى ذلك.

{{% alert color="primary" %}}

 Aspose.Cells for .NET يكتب مباشرة المعلومات حول API ورقم الإصدار في مستندات الإخراج. على سبيل المثال، عند تقديم المستند إلى PDF، تتم تعبئة Aspose.Cells for .NET**طلب** الحقل بقيمة "Aspose.Cells" و**PDF منتج** الحقل بالقيمة، على سبيل المثال "Aspose.Cells v17.9".

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for .NET لتغيير هذه المعلومات أو إزالتها من المستندات الناتجة.

{{% /alert %}}

###  **كيفية الوصول إلى خصائص الوثيقة**

 تدعم واجهات برمجة التطبيقات Aspose.Cells كلا النوعين من خصائص المستند، المضمنة والمخصصة. Aspose.Cells'[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل class ملف Excel، ومثل ملف Excel، فإن ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمكن أن يحتوي الفصل على أوراق عمل متعددة، يتم تمثيل كل منها بواسطة ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة بينما يتم تمثيل مجموعة أوراق العمل بواسطة[**مجموعة أوراق العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)فصل.

 استخدم ال[**مجموعة أوراق العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)للوصول إلى خصائص مستند الملف كما هو موضح أدناه.

- للوصول إلى خصائص المستند المضمنة، استخدم[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  للوصول إلى خصائص المستند المخصصة، استخدم[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 كلا ال[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) و[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) إرجاع مثيل[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). تحتوي هذه المجموعة على[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)كائنات، يمثل كل منها خاصية مستند واحدة مضمنة أو مخصصة.

 الأمر متروك لمتطلبات التطبيق حول كيفية الوصول إلى العقار، أي؛ باستخدام الفهرس أو اسم الخاصية من[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)كما هو موضح في المثال أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 ال[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)تسمح الفئة باسترداد اسم وقيمة ونوع خاصية المستند:

-  للحصول على اسم الخاصية، استخدم[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  للحصول على قيمة العقار استخدم[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)ترجع القيمة ككائن.
-  للحصول على نوع الخاصية، استخدم[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . يؤدي هذا إلى إرجاع أحد[**نوع الملكية**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)قيم التعداد. بعد حصولك على نوع الخاصية، استخدم أحد**DocumentProperty.ToXXX** طرق للحصول على قيمة النوع المناسب بدلا من استخدامه[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . ال**DocumentProperty.ToXXX**تم وصف الطرق في الجدول أدناه.

{{% alert color="primary" %}}

 ال[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)يوفر class أيضًا مجموعة من الأساليب التي تُرجع قيم أنواع البيانات الأخرى.

{{% /alert %}}

|**اسم عضو**|**وصف**|**طريقة تو XXX**|
| :- | :- | :- |
|منطقية|نوع بيانات الخاصية هو منطقي|ToBool|
|تاريخ| نوع بيانات الخاصية هو DateTime. لاحظ أن Microsoft يخزن Excel فقط<br>جزء التاريخ، لا يمكن تخزين أي وقت في خاصية مخصصة من هذا النوع|إلىDateTime|
|يطفو|نوع بيانات الخاصية مزدوج|للمضاعفة|
|رقم|نوع بيانات الخاصية هو Int32|ToInt|
|String|نوع بيانات الخاصية هو سلسلة|إلى سلسلة|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **كيفية إضافة أو إزالة خصائص المستند المخصصة**

كما وصفنا سابقًا في بداية هذا الموضوع، لا يمكن للمطورين إضافة أو إزالة الخصائص المضمنة لأن هذه الخصائص معرفة من قبل النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها معرفة من قبل المستخدم.

###  **كيفية إضافة خصائص مخصصة**

 Aspose.Cells كشفت واجهات برمجة التطبيقات (APIs) عن[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) طريقة ل[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) class لإضافة خصائص مخصصة إلى المجموعة. ال[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) تضيف الطريقة الخاصية إلى ملف Excel وتقوم بإرجاع مرجع لخاصية المستند الجديد كملف[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)هدف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **كيفية تكوين خاصية "الارتباط بالمحتوى" المخصصة**

 لإنشاء خاصية مخصصة مرتبطة بمحتوى نطاق معين، قم باستدعاء[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) طريقة وتمرير اسم الخاصية والمصدر. يمكنك التحقق مما إذا تم تكوين الخاصية على أنها مرتبطة بالمحتوى باستخدام[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) ملكية. علاوة على ذلك، من الممكن أيضًا الحصول على نطاق المصدر باستخدام[**مصدر**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) ملكية[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)فصل.

نستخدم قالب Excel بسيطًا Microsoft في المثال. يحتوي المصنف على نطاق مسمى محدد يسمى**MyRange** والذي يشير إلى قيمة الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **كيفية إزالة الخصائص المخصصة**

 لإزالة الخصائص المخصصة باستخدام Aspose.Cells، اتصل بالرقم[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)الطريقة وتمرير اسم خاصية المستند المراد إزالتها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **مواضيع متقدمة**
- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند](/cells/ar/net/adding-custom-properties-visible-inside-document-information-panel/)
- [ضبط خصائص ScaleCrop وLinksUpToDate لخصائص المستند المضمنة](/cells/ar/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [حدد إصدار المستند لملف Excel باستخدام خصائص المستند المضمنة](/cells/ar/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [حدد لغة ملف Excel باستخدام خصائص المستند المضمنة](/cells/ar/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
