---
title: الحصول على التحذيرات عند تحميل ملف Excel باستخدام Node.js عبر C++
linktitle: الحصول على تحذيرات أثناء تحميل ملف إكسل
type: docs
weight: 110
url: /ar/nodejs-cpp/get-warnings-while-loading-excel-file/
description: تعلم كيفية التقاط التحذيرات أثناء تحميل ملف Excel باستخدام Aspose.Cells for Node.js via C++. تعامل مع دفاتر العمل المعطوبة ولكن القابلة للتحميل بشكل فعال.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، يحاول المستخدم تحميل دفتر عمل يكون معطوبًا بعض الشيء ولكنه قابل للتحميل. في مثل هذه الحالات، يرمي Aspose.Cells تحذيرات أثناء تحميل دفتر العمل. يمكنك التقاط هذه التحذيرات من خلال تنفيذ واجهة [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) وتعيين الخاصية [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--).

## **الحصول على تحذيرات أثناء تحميل ملف إكسل**

يشرح الكود النموذجي التالي كيفية الحصول على التحذيرات أثناء تحميل ملف Excel. يقوم الكود بتحميل [ملف Excel النموذجي](sampleDuplicateDefinedName.xlsx) الذي يرمي تحذير [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype) عند التحميل. ثم يتم التقاط هذا التحذير بواسطة طريقة [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-) التي تطبع رسائل التحذير على وحدة التحكم. ثم يحفظ الكود دفتر العمل كـ [ملف Excel الناتج](outputDuplicateDefinedName.xlsx). إذا فتحت ملف Excel النموذجي في Microsoft Excel، فستعرض أيضًا هذا التحذير كما هو موضح في الصورة. يرجى أيضًا التحقق من إخراج وحدة التحكم للرمز أدناه لمزيد من الفهم.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **مخرجات الوحدة**

إليك مخرجات وحدة التحكم للكود أعلاه عند تنفيذه مع [ملف إكسل عيني](sampleDuplicateDefinedName.xlsx) المقدم.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
