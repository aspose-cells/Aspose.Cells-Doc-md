---
title: تجميع الحقول المحورية في الجدول المحوري باستخدام Golang عبر C++
linktitle: تجميع الحقول المحورية في الجدول المحوري باستخدام Golang عبر C++
description: تعلم كيفية تجميع حقول الصفوف أو الأعمدة في الجدول المحوري إلى فترات مثل الشهور والأرباع، وإلى نطاقات رقمية، باستخدام PivotField.Group وPivotFieldGroupOptions في Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, جدول محوري, حقل محوري, تجميع الحقول المحورية, Group, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, تجميع التواريخ, نطاق رقمي, Go
type: docs
weight: 80
url: /ar/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يكون تجميع الحقول المحورية مفيدًا عندما يحتوي حقل صف أو عمود في جدول محوري على عدد كبير من العناصر المختلفة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على قيم متباعدة كثيرة. يدمج التجميع هذه العناصر في أقسام ذات معنى: التواريخ في شهور وأرباع وسنوات، والأرقام في نطاقات مثل 0-1 و2-3 و4-5. ويجعل هذا الجدول المحوري الكبير أكثر إحكامًا وأسهل في التحليل. تتيح Aspose.Cells هذه الإمكانية من خلال الطريقتين `PivotField.Group()` (للتجميع التلقائي حسب نوع البيانات) و`PivotField.Group(PivotFieldGroupOptions)` (لخيارات التجميع المخصصة).
- عند تجميع التواريخ، تُجمع التواريخ المفردة في فترات أكبر، مثل الأيام والشهور والأرباع والسنوات، ويُنشأ تسلسل هرمي زمني (مثل السنوات والأرباع والشهور). تصبح الاتجاهات عبر الزمن واضحة في لمحة، ويصبح كل مستوى من هذه الفترات حقلًا محوريًا مستقلًا في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- التجميع متاح فقط للحقول الموضوعة في منطقة `ROW` أو `COLUMN` داخل جدول محوري. لا يمكن تجميع حقل بيانات (قيمة) مباشرة. لتجميع هذا الحقل، يجب إضافته أولًا إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع الحقول المحورية تلقائيًا**
تتحقق الطريقة `PivotField.Group()` الخالية من المعاملات من نوع بيانات الحقل وتجمّعه تلقائيًا. الحقل الذي يحتوي على التواريخ فقط (والخلايا الفارغة) يُجمّع حسب الشهور. أما الحقل الذي يحتوي على الأرقام فقط (والخلايا الفارغة) فيُجمّع إلى نطاقات رقمية باستخدام فاصل رقمي تلقائي.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **تجميع الحقول المحورية باستخدام خيارات مخصصة**
توفر فئة `PivotFieldGroupOptions` إعدادات تجميع مخصصة. لحقول التاريخ، اضبط `StartDate` و`EndDate` و`GroupTypes` (تُمرَّر التواريخ كقيم من نوع `time.Time` في Go). للحقول الرقمية، اضبط `StartNumber` و`EndNumber` و`Interval`. يحدد سلوك `newPivotField` ما إذا كان التجميع ينشئ حقولًا محورية جديدة إلى جانب الحقل الأصلي (راجع قسم الملاحظة في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الشهور والأرباع**
يجمع المثال التالي حقل صف التاريخ في الجدول المحوري النموذجي حسب الشهور والأرباع، بين تاريخ بداية وتاريخ نهاية. يحمّل الرمز [ملف Excel النموذجي](sampleGroupPivotFieldsInPivotTable.xlsx)، ثم ينفذ التجميع، ويحسب بيانات الجدول المحوري، ثم يحفظ النتيجة المجمّعة. توضح لقطة الشاشة النتيجة: أصبح حقل صف التاريخ مجمّعًا الآن حسب الأرباع والشهور.
لاحظ أن ترتيب القيم في `GroupTypes` يُتجاهل. بغض النظر عن ترتيب أنواع التجميع المدرجة، تُعرض الحقول المجمّعة دائمًا من أكبر فترة زمنية إلى أصغرها: السنوات والأرباع والشهور والأيام والساعات والدقائق والثواني. في هذا المثال، وردت الشهور قبل الأرباع في `GroupTypes`، لكن تظهر الأرباع كمستوى خارجي وتظهر الشهور كمستوى داخلي.

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![جدول محوري مجمّع حسب الشهور والأرباع](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي إلى نطاقات**
يكون `FieldTwo` في الجدول المحوري النموذجي في الأصل حقل بيانات (قيمة). ولأن التجميع متاح فقط لحقول الصف والعمود، يستدعي الرمز أولًا `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، ثم يعيد تحديث الجدول المحوري، ثم يجمّع الحقل الرقمي إلى النطاقات 0-1 و2-3 و4-5 باستخدام `StartNumber = 0` و`EndNumber = 5` و`Interval = 2`.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **ملاحظة**

{{% alert color="primary" %}}
- تم إهمال الأحمال الزائدة لطريقة `PivotField.GroupBy()` وإزالتها من واجهة API. وتُستبدل بها الأحمال الزائدة للطريقة `PivotField.Group()` و`PivotField.Group(PivotFieldGroupOptions)`.
- في Microsoft Excel، يستبدل تجميع حقل رقمي الحقل المحوري الأصلي بالنطاقات المجمّعة، بينما ينشئ تجميع حقل تاريخ حقولًا محورية جديدة (حقلًا واحدًا لكل مستوى تجميع، مثل الأرباع والشهور) إلى جانب الحقل الأصلي. اعتبارًا من Aspose.Cells 26.10، تتبع طرائق `PivotField.Group()` السلوك نفسه في Excel.
- لا يسري `PivotFieldGroupOptions.Interval` إلا مع التجميع الرقمي أو تجميع التواريخ حسب الأيام (مثل تجميع التواريخ في فترات مدتها 7 أيام)، ويُتجاهل عند تجميع التواريخ حسب الشهور أو الأرباع أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [عرض أو تصفية أفضل 10 عناصر في الجدول المحوري](/cells/ar/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [عرض القيم كـ في الجدول المحوري](/cells/ar/go-cpp/show-values-as-in-pivot-table/)
- [تنسيق جزء من الجدول المحوري](/cells/ar/go-cpp/format-part-of-pivot-table/)
- [إضافة التنسيق الشرطي إلى الجدول المحوري](/cells/ar/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}