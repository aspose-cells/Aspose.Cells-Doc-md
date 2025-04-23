---
title: تعيين صيغة مشتركة باستخدام Node.js عبر C++
linktitle: ضبط الصيغ المشتركة
type: docs
weight: 10
url: /ar/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

إذا كنت ترغب في إضافة وظيفة في ورقة عمل تقوم ببعض الحسابات، يشرح هذا المقال كيفية تحقيق ذلك باستخدام Aspose.Cells for Node.js via C++.

{{% /alert %}}

## تعيين صيغة مشتركة باستخدام Aspose.Cells for Node.js via C++

من المفترض أن يكون لديك ورقة عمل مليئة بالبيانات بتنسيق يبدو مثل الورقة العمل النموذجية التالية.

|**ملف الإدخال مع عمود واحد من البيانات**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

ترغب في إضافة وظيفة في B2 التي ستقوم بحساب ضريبة المبيعات للصف الأول من البيانات. الضريبة **9%**. الصيغة التي تحسب ضريبة المبيعات هي: **"=A2*0.09"**. يشرح هذا المقال كيفية تطبيق هذه الصيغة باستخدام Aspose.Cells.

يتيح لك Aspose.Cells تحديد صيغة باستخدام الخاصية [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--). هناك خياران لإضافة الصيغ إلى الخلايا الأخرى (B3 و B4 و B5، وهلم جرا.) في العمود.

إما أن تفعل ما فعلته للخلية الأولى، بحيث تقوم بشكل فعال بتعيين الصيغة لكل خلية، مع تحديث مرجع الخلية وفقًا لذلك (A3*0.09، A4*0.09، A5*0.09 وهكذا). يتطلب هذا تحديث مراجع الخلايا لكل صف. كما يتطلب أن يقوم Aspose.Cells بتحليل كل صيغة بشكل فردي، مما قد يكون مكلفًا من حيث الوقت لأوراق عمل كبيرة وصيغ معقدة. كما يضيف الكود خطوطًا إضافية على الرغم من أن الحلقات يمكن أن تقصرها بعض الشيء.

وهجاهدًا عبارة عن استخدام **صيغة مشتركة**. مع الصيغة المشتركة، تُحدث الصيغ تلقائيًا لمراجع الخلية في كل صف بحيث تُحسب الضريبة بشكل صحيح. الأسلوب [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) أكثر كفاءة من الأسلوب الأول.

تُظهر المثال التالي كيفية استخدامه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
