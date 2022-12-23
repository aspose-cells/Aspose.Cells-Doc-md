---
title: إدارة خصائص الوثيقة
type: docs
weight: 10
url: /ar/java/managing-document-properties/
---
## **مقدمة**

يوفر Microsoft Excel إمكانية إضافة خصائص إلى ملفات جداول البيانات. توفر خصائص المستند هذه معلومات مفيدة وهي مقسمة إلى فئتين كما هو مفصل أدناه.

- الخصائص المحددة من قبل النظام (المضمنة): تحتوي الخصائص المضمنة على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المعرفة من قبل المستخدم (المخصصة): الخصائص المخصصة التي يحددها المستخدم النهائي في شكل زوج الاسم والقيمة.

{{% alert color="primary" %}}

أهم نقطة يجب معرفتها حول الخصائص المضمنة والمخصصة هي أنه يمكن الوصول إلى الخصائص المضمنة وتعديلها ، ولكن لا يمكن إنشاؤها أو إزالتها ، ومع ذلك ، يمكن إنشاء خصائص المستند المخصصة وإدارتها.

{{% /alert %}}

## **إدارة خصائص الوثيقة باستخدام Microsoft Excel**

 Microsoft يسمح Excel بإدارة خصائص المستندات لملفات Excel بطريقة WYSIWYG. يرجى اتباع الخطوات التالية لفتح ملف**ملكيات** الحوار في Excel 2016.

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

 Aspose.Cells for Java يكتب مباشرة المعلومات حول API ورقم الإصدار في وثائق المخرجات. على سبيل المثال ، عند تقديم المستند إلى PDF ، يتم تعبئة Aspose.Cells for Java**تطبيق** حقل بقيمة "Aspose.Cells" و**PDF منتج** الحقل بالقيمة ، على سبيل المثال "Aspose.Cells for Java v17.9".

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for Java لتغيير أو إزالة هذه المعلومات من مستندات الإخراج.

{{% /alert %}}

### **الوصول إلى خصائص المستند**

تدعم واجهات برمجة التطبيقات Aspose.Cells كلا نوعي خصائص المستند المضمنة والمخصصة. Aspose.Cells '[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل class ملف Excel ، ومثل ملف Excel ، فإن ملف[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمكن أن تحتوي الفئة على أوراق عمل متعددة ، يمثل كل منها ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class بينما يتم تمثيل مجموعة أوراق العمل بواسطة[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)صف دراسي.

 استخدم ال[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)للوصول إلى خصائص مستند الملف كما هو موضح أدناه.

-  للوصول إلى خصائص المستند المضمنة ، استخدم[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  للوصول إلى خصائص المستند المخصصة ، استخدم ملحق[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 كلا ال[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) و[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) إرجاع مثيل[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . هذه المجموعة تحتوي على[**وثيقة الملكية**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)كائنات ، يمثل كل منها خاصية واحدة مضمنة أو مخصصة للمستند.

 الأمر متروك لمتطلبات التطبيق في كيفية الوصول إلى الممتلكات ، أي ؛ باستخدام فهرس أو اسم الخاصية من[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)كما هو موضح في المثال أدناه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

 ال[**وثيقة الملكية**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)تسمح class باسترداد اسم وقيمة ونوع خاصية المستند:

-  للحصول على اسم الخاصية ، استخدم[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  للحصول على قيمة العقار ، استخدم[**الوثيقة القيمة**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**الوثيقة القيمة**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)تُرجع القيمة ككائن.
-  للحصول على نوع الخاصية ، استخدم[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . هذا يعيد واحد من[**نوع الملكية**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)قيم التعداد.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **إضافة أو إزالة خصائص المستند المخصصة**

كما أوضحنا سابقًا في بداية هذا الموضوع ، لا يمكن للمطورين إضافة أو إزالة الخصائص المضمنة لأن هذه الخصائص محددة من قبل النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها محددة من قبل المستخدم.

### **إضافة خصائص مخصصة**

 كشفت واجهات برمجة التطبيقات Aspose.Cells ملف[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) طريقة لـ[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) class لإضافة خصائص مخصصة إلى المجموعة. ال[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) يضيف الأسلوب الخاصية إلى ملف Excel ويعيد مرجعًا لخاصية المستند الجديدة كملف[**وثيقة الملكية**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)موضوع.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **تكوين خاصية مخصصة "ارتباط بالمحتوى"**

 لإنشاء خاصية مخصصة مرتبطة بمحتوى نطاق معين ، قم باستدعاء[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) ) طريقة واسم خاصية المرور والمصدر. يمكنك التحقق مما إذا كانت الخاصية قد تم تكوينها على أنها مرتبطة بالمحتوى باستخدام[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) خاصية. علاوة على ذلك ، من الممكن أيضًا الحصول على نطاق المصدر باستخدام[**مصدر**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) ممتلكات[**وثيقة الملكية**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)صف دراسي.

 نستخدم ملف إكسل Microsoft قالب بسيط في المثال. يحتوي المصنف على نطاق مسمى محدد يسمى**MyRange** الذي يشير إلى قيمة الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **إزالة الخصائص المخصصة**

 لإزالة الخصائص المهيأة باستخدام Aspose.Cells ، قم باستدعاء[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) وتمرير اسم خاصية المستند المراد إزالتها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
