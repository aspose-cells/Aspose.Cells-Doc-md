---
title: تشكيل الجدول المحوري باستخدام Golang عبر C++
linktitle: تنسيق جدول الدوران
type: docs
weight: 10
url: /ar/go-cpp/formatting-pivot-table/
description: تعلم كيف تخصص مظهر الجداول المحورية باستخدام Aspose.Cells for C++.
---

## **مظهر جدول الدوران**

كيفية إنشاء جدول دوران يشرح كيفية إنشاء جدول دوران بسيط. يوضح هذا المقال كيفية تخصيص مظهر جدول الدوران عن طريق تعيين مختلف الخصائص:

- خيارات تنسيق جدول الدوران
- خيارات تنسيق حقول الجدول الدوران
- خيارات تنسيق حقل البيانات

### **تعيين خيارات تنسيق جدول الدوران**

تتحكم فئة [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) في الجدول الدوري الكلي ويمكن تهيئتها بعدة طرق.

#### **تعيين نوع التنسيق التلقائي**

 تقدم Microsoft Excel العديد من تنسيقات التقارير المحددة مسبقًا. يدعم Aspose.Cells أيضًا خيارات التنسيق هذه. للوصول إليها:

1. قم بتعيين [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) إلى **صحيح**.
1. قم بتعيين خيار التنسيق من تعداد [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/) .

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **ضبط خيارات التنسيق**

 يوضح المثال التالي كيفية تنسيق الجدول المحوري لإظهار الإجماليات الكبرى للصفوف والأعمدة، وكيفية ضبط ترتيب الحقول في التقرير. كما يوضح كيفية تعيين سلسلة مخصصة للقيم الفارغة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **تنسيق المظهر يدويًا**

 لتنسيق مظهر تقرير الجدول المحوري يدويًا، بدلًا من استخدام تنسيقات التقرير المحددة مسبقًا، استخدم الطرق [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) و [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). أنشئ كائن نمط للتنسيق المطلوب، على سبيل المثال:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **ضبط خيارات تنسيق حقل الدوري**

تمثل فئة [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) حقلًا في جدول دور ، ويمكن تهيئته بعدة طرق. تُظهر العينة البرمجية أدناه كيفية:

- الوصول إلى حقول الصفوف.
- ضبط المجاميع الفرعية.
- ضبط الترتيب التلقائي.
- ضبط الإظهار التلقائي.

#### **ضبط تنسيق حقول الصف/العمود/الصفحة**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **ضبط تنسيق حقول البيانات**

تُظهر العينة البرمجية أدناه كيفية تعيين تنسيقات العرض وتنسيق الأرقام لحقول البيانات.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **مسح حقول Pivot**

تحتوي فئة [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) على طريقة تسمى [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) تتيح لك مسح حقول الجدول الدوري. استخدمها عندما ترغب في مسح جميع حقول الجدول الدوري في المناطق، على سبيل المثال، الصفحة، العمود، الصف أو البيانات.
يظهر الكود العيني أدناه كيفية مسح جميع حقول الجدول المفصلي في مجال البيانات.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
