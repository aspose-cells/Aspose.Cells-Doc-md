---  
title: الكشف عن أوراق العمل الفارغة باستخدام Node.js عبر C++  
linktitle: كشف الأوراق العمل الفارغة  
type: docs  
weight: 410  
url: /ar/nodejs-cpp/detecting-empty-worksheets/  
description: توضح هذه المقالة رمزًا يشرح كيفية الكشف برمجياً عن أوراق العمل الفارغة في مصنفات إكسل باستخدام واجهة برمجة تطبيقات Node.js مع مكتبة C++.  
keywords: الكشف عن ورقة عمل فارغة باستخدام Node.js عبر C++، العثور على ورقة عمل إكسل فارغة باستخدام Node.js عبر C++  
---  

## **فحص الخلايا المعبأة**

يمكن أن تحتوي أوراق العمل على خلية واحدة أو أكثر مملوءة بقيم، حيث يمكن أن تكون القيمة بسيطة (نص، رقم، تاريخ/وقت) أو صيغة أو قيمة تستند إلى صيغة. في مثل هذه الحالة، من السهل الكشف عما إذا كانت ورقة العمل فارغة أم لا. كل ما علينا التحقق منه هو الخاصيتان [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) أو [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--). إذا أعادت الخاصيتان المذكورتان أصلاً قيمًا صفرية أو إيجابية، فهذا يعني أن خلية واحدة أو أكثر قد تم ملؤها؛ ومع ذلك، إذا أعادت أي من هاتين الخاصيتين -1، فهذا يدل على عدم وجود خلايا مملوءة في ورقة العمل المعطاة.

{{% alert color="primary" %}}

تحتوي مجموعتا الصفوف والأعمدة على مؤشرات تبدأ بالصفر؛ لذلك، تعني الخلية عند الصف 0 والعمود 0 أول خلية في ورقة العمل، وهي A1.

{{% /alert %}}

## **فحص الخلايا المهيأة الفارغة**

يتم تهيئة جميع الخلايا التي تحتوي على قيم تلقائيًا؛ ومع ذلك، هناك احتمال أن تحتوي ورقة العمل على خلايا تحتوي فقط على تنسيق مطبق. في مثل هذا السيناريو، ستعيد الخاصيتان [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) أو [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) -1، مما يشير إلى غياب القيم المعبأة، لكن الخلايا المهيأة بسبب تنسيق الخلية لا يمكن اكتشافها باستخدام هذا النهج. للتحقق مما إذا كانت لدى ورقة العمل خلايا مهيأة فارغة، يُنصح باستخدام طريقة `Enumerator.MoveNext` على المُعدّاد الذي تم الحصول عليه من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). إذا أعادت `Enumerator.MoveNext` **true**، فهذا يعني أن هناك خلية مهيأة واحدة أو أكثر في ورقة العمل المعطاة.

## **فحص الأشكال**

من الممكن ألا تحتوي ورقة العمل المعطاة على خلايا مملوءة؛ ومع ذلك، قد تحتوي على أشكال وكائنات مثل الضوابط والمخططات والصور، وما إلى ذلك. إذا كنا بحاجة للتحقق مما إذا كانت تحتوي على أي شكل، يمكننا ذلك عن طريق فحص الخاصية [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--). تشير أي قيمة إيجابية إلى وجود شكل (أشكال) في ورقة العمل.

## **نموذج برمجة**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
