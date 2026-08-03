---
title: حقول القيم في Aspose.Cells for C++
linktitle: حقول القيم في Aspose.Cells for C++
description: تعلّم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيم على محور الصفوف أو الأعمدة في Aspose.Cells for C++.
keywords: Aspose.Cells, C++, جدول محوري, حقل القيم, PivotField, PivotField.Function, حقل البيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعدّ إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يعرض Aspose.Cells `PivotTable.AddFieldToArea(PivotFieldType, string)`، وهي صيغة محمّلة تقبل الثابت `PivotFieldType.Data` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، تعرضه واجهة البرمجة من خلال مجموعة `PivotTable.DataFields` بالترتيب الذي أُضيفت به الحقول. افتراضيًا، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.Sum`، بينما يكون العمود غير الرقمي افتراضيًا `Count`.
## تغيير دالة التلخيص
يتم تغليف كل حقل موضوع في منطقة البيانات داخليًا كنسخة من `PivotField`، وتُعيد خاصية `Function` الخاصة به قيمة من تعداد `ConsolidationFunction`. يتيح لك مُعيِّن `Function` ذاته التنقل بين التجمّعات المتاحة، بما في ذلك `Sum` و `Count` و `Average` و `Max` و `Min` و `Product` و `StdDev` و `StdDevp` و `Var` و `Varp`.
{{% alert color="primary" %}}
تغيير `Function` يؤثر فقط على التجمّع، ولا يتغير عمود المصدر.
{{% /alert %}}
لذا يمكنك ترك حقل بيانات واحد كـ `Sum` بينما تُضيف حقل بيانات ثانٍ يستهدف عمود المصدر نفسه لكنه يستخدم `Count` أو `Average`، وكل ذلك في جدول محوري واحد.
## رسم حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلين من البيانات أو أكثر، يعرض Aspose.Cells حقلًا افتراضيًا إضافيًا يُسمى `PivotTable.ValuesField`. يمثّل هذا الحقل الافتراضي تجمّع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة كحقل محوري أساسي، وهو أمر مفيد لعرض مقاييس متعددة جنبًا إلى جنب.
{{% alert color="primary" %}}
لا يعمل `PivotTable.ValuesField` إذا لم يكن هناك حقل قيم أو كان هناك حقل قيم واحد فقط.
{{% /alert %}}
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة توضح كل قدرة موصوفة أعلاه على نفس بنية الجدول المحوري.
## السيناريو 1 — سحب حقل أساسي إلى منطقة القيم
يوضح هذا السيناريو كيفية وضع حقل أساسي واحد (`Amount`) في منطقة البيانات بجدول محوري موجود. تضع بنية الجدول المحوري المشتركة `Category` و `Item` على محور الصفوف و `Year` على محور الأعمدة. بعد العملية، يظهر `Amount` في منطقة البيانات ويُحسب افتراضيًا كـ `Sum` لـ `Amount`.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Aspose::Cells::Startup();

 Workbook workbook;
 Worksheet worksheet = workbook.GetWorksheets().Get(0);
 worksheet.SetName(u"Data");

 Cells cells = worksheet.GetCells();

 // العناوين في A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // صفوف البيانات A2:D9 باستخدام حلقات متداخلة متفرعة على j
 for (int i = 1; i <= 8; i++)
 {
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
 break;
 case 1:
 if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
 else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
 else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
 else cells.Get(i, j).PutValue(U16String("Daikon"));
 break;
 case 2:
 cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) cells.Get(i, j).PutValue(100);
 else if (i == 2) cells.Get(i, j).PutValue(150);
 else if (i == 3) cells.Get(i, j).PutValue(80);
 else if (i == 4) cells.Get(i, j).PutValue(90);
 else if (i == 5) cells.Get(i, j).PutValue(50);
 else if (i == 6) cells.Get(i, j).PutValue(60);
 else if (i == 7) cells.Get(i, j).PutValue(40);
 else cells.Get(i, j).PutValue(45);
 break;
 }
 }
 }

 // إضافة جدول محوري في F3 باسم PivotTable1
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // تخطيط الجدول المحوري: Category و Item في الصف، Year في العمود، Amount كحقل بيانات
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");

 Aspose::Cells::Cleanup();
 return 0;
}
```
## السيناريو 2 — تغيير دالة التلخيص
يبدأ هذا السيناريو من نفس بنية الجدول المحوري كالسيناريو 1، لكنه يُضيف حقل `Amount` إلى منطقة البيانات مرتين. يشير كلا حقلي البيانات إلى عمود المصدر نفسه، ومع ذلك يُعدَّل الحقل الثاني باستخدام أداة التعيين `PivotField.Function` ليصبح `Count` بدلاً من `Sum` الافتراضي.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 Vector<String> headers{ "Category", "Item", "Year", "Amount" };
 for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

 Vector<Vector<Object*>> data;
 // ملء البيانات ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 PivotField countField = pivotTable.GetDataFields().Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```
## السيناريو 3 — رسم حقول القيم على محور الصفوف أو الأعمدة
مع وجود حقلين من البيانات في موضعهما، يصبح `PivotTable.ValuesField` قابلاً للاستخدام. يسحب هذا السيناريو ذلك الحقل الافتراضي التجميعي إلى منطقة الأعمدة بحيث يظهر كل مقياس في منطقة البيانات ككتلة عمود خاصة به بجوار `Year`.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 // ... بناء البيانات ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType::Column, pivotTable->GetValuesField()->GetName());
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```
معًا، تغطي هذه السيناريوهات الثلاثة كل جانب من جوانب معالجة حقول القيم في Aspose.Cells for C++، بدءًا من حقل بيانات واحد مع `Sum` الافتراضي وحتى جدول محوري متعدد المقاييس يتحكم فيه `ValuesField` الافتراضي في التخطيط على محور الصفوف أو الأعمدة.

{{< app/cells/assistant language="cpp" >}}
