---
title: إدراج جدول محوري
linktitle: إدراج جدول محوري
description: إنشاء الجداول المحورية وتنسيقها باستخدام Aspose.Cells for Node.js via C++.
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري.
type: docs
weight: 160
url: /ar/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ما هو الجدول المحوري؟**
الجدول المحوري هو تقرير ملخص تفاعلي: يختصر مجموعة كبيرة من البيانات الخام المرتبة صفًا بصف في مصفوفة موجزة، دون الحاجة إلى استخدام أي صيغة. أنت تحدد أي الأعمدة ستصبح تسميات للصفوف، وأيها ستصبح تسميات للأعمدة، وأيها سيتم تجميعه كقيم، بينما يتولى الجدول المحوري عملية التجميع والحساب:
- **تلخيص** — إجمالي المبيعات لكل منتج أو منطقة أو ربع، بدلاً من سلاسل الصيغ الطويلة.
- **مقارنة** — إدراج الفئات في الصفوف والفترات في الأعمدة يحوّل قائمة مسطحة إلى تقرير متقاطع تكشف فيه الاتجاهات بوضوح في لمحة.
- **الانتقال إلى التفاصيل** — انقر نقرًا مزدوجًا على أي قيمة ملخص لاستعراض الصفوف المصدرية التي تقف خلفها.
- **تحديث** — عند تغيير بيانات المصدر، تكفي عملية تحديث واحدة لإعادة حساب التقرير بالكامل.
تشمل السيناريوهات المعتادة لوحات معلومات المبيعات، وتفصيل المصروفات، وتحليل المخزون، وكذلك الإجابة عن أسئلة من نوع "كيف تتفصل هذه الأرقام حسب الفئة والوقت؟". يبني Aspose.Cells for Node.js via C++ الجداول المحورية نفسها برمجيًا، لذا يمكن للمصنفات التي ينشئها تطبيقك أن تتضمن تقارير جاهزة بدلًا من البيانات الخام وحدها.

### **نموذج كائنات الجدول المحوري**
يوفر Aspose.Cells for Node.js via C++ مجموعة خاصة من الفئات تُستخدم لإنشاء الجداول المحورية والتحكم فيها. تُستخدم هذه الفئات لإنشاء كائنات [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) وضبطها، وهي العناصر الأساسية التي يتكون منها الجدول المحوري. وتتمثل هذه الكائنات في:
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) يمثل حقلًا في [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) يمثل مجموعة جميع كائنات [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) يمثل جدولًا محوريًا في ورقة عمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) يمثل مجموعة جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) في ورقة عمل.

### **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**
يتطلب إنشاء جدول محوري ثلاث خطوات: كتابة بيانات المصدر في خلايا ورقة العمل، وإضافة الجدول المحوري في موقع الوجهة، ووضع حقول الجدول المحوري في مناطق الصفوف والأعمدة والبيانات.
1. أضف البيانات إلى ورقة العمل باستخدام طريقة [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) الخاصة بكائن [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). ستُستخدم هذه البيانات كمصدر بيانات للجدول المحوري.
2. أضف جدولًا محوريًا إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) الخاصة بمجموعة [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection): `add(sourceData, row, column)`. يمثل `sourceData` نطاق المصدر (على سبيل المثال، "A1:C8")؛ وتحدد `row` و`column` إحداثيات خلية الوجهة وفق نظام ترقيم يبدأ من 0 عند الركن العلوي الأيسر للجدول المحوري (تعني الخلية E3 الصف 2 والعمود 4). يعيد الأسلوب كائن [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) الجديد مباشرةً.
3. ضع حقول الجدول المحوري باستخدام أسلوب `addFieldToArea` الخاص بكائن [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable): يوضع اسم الحقل في منطقة الصفوف (`PivotFieldType.Row`)، أو منطقة الأعمدة (`PivotFieldType.Column`)، أو منطقة البيانات (`PivotFieldType.Data`).
4. احفظ المصنف — يُكتب الجدول المحوري في الملف المحفوظ.
بعد تنفيذ رمز المثال، تتم إضافة جدول محوري إلى ورقة العمل.

```javascript
const AsposeCells = require("aspose.cells.node");

// إنشاء مصنف جديد والحصول على ورقة العمل الأولى
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// كتابة البيانات المصدرية: المبيعات حسب الرياضة والربع
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// إضافة جدول محوري في خلية الوجهة E3، باستخدام A1:C8 كمصدر
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// تعيين حقول الجدول المحوري: الرياضة إلى الصفوف، الربع إلى الأعمدة، المبيعات إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// حفظ المصنف
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر بيانات، يجب أن يمتد النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" صالح، في حين "C3:A1" غير صالح.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}