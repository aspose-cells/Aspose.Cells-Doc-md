---
title: إدارة خصائص المستند باستخدام Node.js عبر C++
linktitle: خصائص المستند
type: docs
weight: 80
url: /ar/nodejs-cpp/managing-document-properties/
description: تعلم كيفية إدارة خصائص المستند من خلال واجهات برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: كيفية إدارة خصائص المستند في Node.js عبر C++، الحصول أو تعيين خصائص المستند باستخدام Node.js عبر C++، إضافة أو حذف خصائص المستند عبر Node.js عبر C++، إدراج أو إزالة خصائص المستند باستخدام Node.js عبر C++، كيفية الوصول إلى خصائص المستند باستخدام واجهات برمجة تطبيقات Aspose.Cells for Node.js via C++.
---


## **مقدمة**

يوفر Microsoft Excel القدرة على إضافة خصائص إلى ملفات جداول البيانات. توفر هذه الخصائص المستندية معلومات مفيدة وتنقسم إلى فئتين كما هو موضح أدناه.

- الخصائص المعرفة مسبقًا (المدمجة): الخصائص المدمجة تحتوي على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المخصصة (المخصصة): الخصائص المخصصة المحددة من قبل المستخدم النهائي في شكل زوج اسم-قيمة.

{{% alert color="primary" %}}

أهم نقطة لمعرفتها حول الخصائص المدمجة والمخصصة هي أنه يمكن الوصول إلى الخصائص المدمجة وتعديلها، ولكن لا يمكن إنشاؤها أو إزالتها. ومع ذلك، يمكن إنشاء الخصائص المخصصة وإدارتها.

{{% /alert %}}

## **كيفية إدارة خصائص المستند باستخدام Microsoft Excel**

تمكنك Microsoft Excel من إدارة خصائص المستندات لملفات Excel بطريقة WYSIWYG. يرجى اتباع الخطوات أدناه لفتح مربع الحوار **الخصائص** في Excel 2016.

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

يكتب Aspose.Cells for Node.js via C++ مباشرة المعلومات حول API ورقم الإصدار في المستندات المخرجة. على سبيل المثال، عند تصيير المستند إلى PDF، يقوم Aspose.Cells for Node.js via C++ بملء حقل **التطبيق** بالقيمة 'Aspose.Cells' وحقل **منتج PDF** بالقيمة مثل 'Aspose.Cells v17.9'.

يرجى ملاحظة أنك لا تستطيع إيعاز Aspose.Cells for Node.js via C++ لتغيير أو إزالة هذه المعلومات من المستندات المخرجة.

{{% /alert %}}

### **كيفية الوصول إلى خصائص المستند**

تدعم واجهات برمجة تطبيقات Aspose.Cells كلا نوعي خصائص المستند، المدمجة والخصائص المخصصة. Class [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) من Aspose.Cells يمثل ملف إكسل، ومثل ملف إكسل، يمكن لـ [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) أن يحتوي على عدة ورقات عمل، كل منها يُمثل بواسطة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)، في حين تُمثل مجموعة ورقات العمل بواسطة [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).

استخدم [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) للوصول إلى خصائص المستند للملف كما هو موضح أدناه.

- للوصول إلى خصائص المستند المدمجة، استخدم [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- للوصول إلى خصائص المستند المخصصة ، استخدم [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

كل من [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) و [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) تُرجع مثيل [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/)، الذي يحتوي على [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) من الكائنات، كل منها يمثل خاصية مستند مدمجة أو مخصصة.

يعتمد الأمر على متطلبات التطبيق على كيفية الوصول إلى الخاصية، سواء باستخدام الفهرس أو الاسم من [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) كما هو موضح في المثال أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

يسمح لك [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) باسترجاع اسم، قيمة، ونوع الخاصية المستند:

- للحصول على اسم الخاصية ، استخدم [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- للحصول على قيمة الخاصية، استخدم [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) يُرجع القيمة ككائن.
- للحصول على نوع الخاصية، استخدم [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). يُرجع أحد قيم التعداد [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/). بعد الحصول على نوع الخاصية، استخدم واحدة من طرق **DocumentProperty.ToXXX** للحصول على قيمة النوع المناسب بدلاً من استخدام [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). يتم وصف طرق **DocumentProperty.ToXXX** في الجدول أدناه.

{{% alert color="primary" %}}

يوفر [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) أيضًا مجموعة من الطرق التي ترجع قيم الأنواع الأخرى من البيانات.

{{% /alert %}}

|**اسم العضو**|**الوصف**|**طريقة ToXXX**|
| :- | :- | :- |
|Boolean| نوع البيانات الخاصية هو بوليان|ToBool|
|Date| نوع البيانات الخاصية هو التاريخ والوقت. لاحظ أن Microsoft Excel يخزن فقط <br> الجزء التاريخي ، لا يمكن تخزين الوقت في خاصية مخصصة من هذا النوع|ToDateTime|
|Float| نوع البيانات الخاصية هو Double|ToDouble|
|Number| نوع البيانات الخاصية هو Int32|ToInt|
|String| نوع بيانات الخاصية هو string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **كيفية إضافة أو إزالة خصائص المستند المخصصة**

كما وصفنا في وقت سابق في بداية هذا الموضوع ، لا يمكن للمطورين إضافة أو إزالة الخصائص المدمجة لأن هذه الخصائص محددة من النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها معرفة من قبل المستخدم.

### **كيفية إضافة الخصائص المخصصة**

واجهت واجهات برمجة تطبيقات Aspose.Cells الطريقة [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) للفئة [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) لإضافة خصائص مخصصة للمجموعة. تضيف طريقة [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) الخاصية إلى ملف إكسل وتُعيد مرجعًا لخاصية المستند الجديدة ككائن [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **كيفية تكوين خاصية مخصصة مرتبطة بالمحتوى**

لإنشاء خاصية مخصصة مرتبطة بمحتوى نطاق معين، استدعِ طريقة [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) ومرر اسم الخاصية والمصدر. يمكنك التحقق مما إذا كانت الخاصية مهيأة على أنها مرتبطة بالمحتوى باستخدام الخاصية [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--). علاوة على ذلك، من الممكن أيضًا الحصول على نطاق المصدر باستخدام الخاصية [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) من فئة [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

نحن نستخدم ملف نموذجي بسيط لبرنامج Microsoft Excel في المثال. يحتوي دفتر العمل على نطاق مسمى محدد يحمل التسمية **MyRange** والذي يشير إلى قيمة الخلية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **كيفية إزالة الخصائص المخصصة**

لإزالة الخصائص المخصصة باستخدام Aspose.Cells، استدعي طريقة [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) ومرر اسم الخاصية الخاصة بالمستند المراد إزالته.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **مواضيع متقدمة**
- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة](/cells/ar/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة](/cells/ar/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند](/cells/ar/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
