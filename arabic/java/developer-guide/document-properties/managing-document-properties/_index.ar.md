---
title: إدارة خصائص المستند
type: docs
weight: 10
url: /ar/java/managing-document-properties/
---

## **مقدمة**

يوفر Microsoft Excel القدرة على إضافة خصائص إلى ملفات جداول البيانات. توفر هذه الخصائص المستندية معلومات مفيدة وتنقسم إلى فئتين كما هو موضح أدناه.

- الخصائص المعرفة مسبقًا (المدمجة): الخصائص المدمجة تحتوي على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المخصصة (المخصصة): الخصائص المخصصة المحددة من قبل المستخدم النهائي في شكل زوج اسم-قيمة.

{{% alert color="primary" %}}

أهم نقطة لمعرفته حول الخصائص المدمجة والمخصصة هي أنه يمكن الوصول إلى الخصائص المدمجة وتعديلها، ولكن لا يمكن إنشاؤها أو إزالتها، على عكس الخصائص المخصصة للمستند والتي يمكن إنشاؤها وإدارتها.

{{% /alert %}}

## **إدارة خصائص المستند باستخدام Microsoft Excel**

يتيح Microsoft Excel إدارة خصائص المستند في ملفات Excel بطريقة WYSIWYG. يرجى اتباع الخطوات التالية لفتح حوار **Properties** في Excel 2016.

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

## **العمل مع خصائص المستند باستخدام Aspose.Cells**

يمكن للمطورين إدارة خصائص الوثيقة بشكل ديناميكي باستخدام واجهات برمجة التطبيقات Aspose.Cells. تساعد هذه الميزة المطورين في تخزين معلومات مفيدة إلى جانب الملف، مثل متى تم استلام الملف ومعالجته وتسجيل الوقت وما إلى ذلك.

{{% alert color="primary" %}}

يكتب Aspose.Cells for Java مباشرة المعلومات حول واجهة برمجة التطبيقات ورقم الإصدار في المستندات الناتجة. على سبيل المثال، عند تحويل المستند إلى ملف PDF، يملأ Aspose.Cells for Java حقل **التطبيق** بالقيمة 'Aspose.Cells' وحقل **منتج PDF** بالقيمة، على سبيل المثال 'Aspose.Cells for Java v17.9'.

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for Java لتغيير أو إزالة هذه المعلومات من المستندات الناتجة.

{{% /alert %}}

### **الوصول إلى خصائص المستند**

تدعم واجهات برمجة التطبيقات Aspose.Cells كلا من أنواع خصائص المستند، المدمجة والمخصصة. يمثل [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) لـ Aspose.Cells ملف Excel و، مثل ملف Excel، يمكن أن يحتوي [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) الفصول المتعددة، يمثل كل منها بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) في حين أن مجموعة الفصول تمثل بواسطة فئة [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).

استخدم [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) للوصول إلى خصائص المستند كما هو موضح أدناه.

- للوصول إلى خصائص المستند المدمجة، استخدم [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- للوصول إلى خصائص المستند المخصصة، استخدم [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

كل من [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) و[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) تعيد نموذجًا من صنف [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection). تحتوي هذه المجموعة على [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) كائن، كل منها يُمثل خاصية مستند مدمجة أو مخصصة واحدة.

من متطلبات التطبيق كيفية الوصول إلى الخاصية ، أي؛ باستخدام فهرس أو اسم الخاصية من [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) كما هو موضح في المثال أدناه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

يتيح فئة [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) استرداد اسم وقيمة ونوع خاصية المستند:

- للحصول على اسم الخاصية ، استخدم [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- للحصول على قيمة الخاصية ، استخدم [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) يعيد القيمة ككائن.
- للحصول على نوع الخاصية، استخدم [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). يعيد هذا واحدة من قيم تعددات [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **إضافة أو إزالة الخصائص المخصصة للمستند**

كما وصفنا في وقت سابق في بداية هذا الموضوع ، لا يمكن للمطورين إضافة أو إزالة الخصائص المدمجة لأن هذه الخصائص محددة من النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها معرفة من قبل المستخدم.

### **إضافة الخصائص المخصصة**

قدمت واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells الطريقة [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) لفئة [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) من أجل إضافة خصائص مخصصة إلى المجموعة. تقوم الطريقة [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) بإضافة الخاصية إلى ملف Excel وتُرجع مرجعًا لخاصية المستند الجديدة ككائن [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **تكوين خاصية مخصصة "ربط بالمحتوى"**

لإنشاء خاصية مخصصة مرتبطة بمحتوى نطاق محدد ، اتصل بالطريقة [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String)) وقم بتمرير اسم الخاصية والمصدر. يمكنك التحقق مما إذا كانت الخاصية مكونة كمرتبطة بالمحتوى باستخدام الخاصية [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent). علاوة على ذلك ، من الممكن أيضًا الحصول على نطاق المصدر باستخدام الخاصية [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) من فئة [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

نحن نستخدم ملف نموذجي بسيط لبرنامج Microsoft Excel في المثال. يحتوي دفتر العمل على نطاق مسمى محدد يحمل التسمية **MyRange** والذي يشير إلى قيمة الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **إزالة الخصائص المخصصة**

لإزالة الخصائص المخصصة باستخدام Aspose.Cells، قم بالاتصال بالطريقة [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) وقم بتمرير اسم خاصية المستند التي تريد إزالتها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
