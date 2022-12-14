---
title: تنسيق الجدول المحوري
type: docs
weight: 10
url: /ar/net/formatting-pivot-table/
---
## **مظهر الجدول المحوري**

يوضح كيفية إنشاء جدول محوري كيفية إنشاء جدول محوري بسيط. توضح هذه المقالة كيفية تخصيص مظهر الجدول المحوري عن طريق تعيين خصائص متنوعة:

- خيارات تنسيق الجدول المحوري
- خيارات تنسيق الحقول المحورية
- خيارات تنسيق حقل البيانات

### **تعيين خيارات تنسيق الجدول المحوري**

 ال[**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)يتحكم الفصل في الجدول المحوري الشامل ويمكن تنسيقه بعدة طرق.

#### **تعيين نوع التنسيق التلقائي**

يقدم Microsoft Excel عددًا من تنسيقات التقارير المختلفة المحددة مسبقًا. Aspose.Cells يدعم خيارات التنسيق هذه أيضًا. للوصول إليهم:

1.  تعيين[**PivotTable. تنسيق تلقائي**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) إلى**حقيقي**.
1.  قم بتعيين خيار تنسيق من ملف[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)تعداد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **ضبط خيارات التنسيق**

يوضح نموذج التعليمات البرمجية أدناه كيفية تنسيق الجدول المحوري لإظهار الإجماليات الكلية للصفوف والأعمدة ، وكيفية تعيين ترتيب حقل التقرير. كما يوضح كيفية تعيين سلسلة عميل للقيم الخالية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **تنسيق الشكل والمظهر يدويًا**

 لتنسيق شكل تقرير الجدول المحوري يدويًا ، بدلاً من استخدام تنسيقات التقارير المحددة مسبقًا ، استخدم تنسيق[**PivotTable.Format ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) و[**PivotTable.FormatAll ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)طُرق. قم بإنشاء كائن نمط للتنسيق الذي تريده ، على سبيل المثال:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **تعيين خيارات تنسيق الحقل المحوري**

 ال[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)يمثل class حقلاً في جدول محوري ويمكن تنسيقه بعدة طرق. يوضح نموذج التعليمات البرمجية أدناه كيفية:

- الوصول إلى حقول الصفوف.
- تحديد المجاميع الفرعية.
- ضبط الترتيب التلقائي.
- ضبط العرض التلقائي.

#### **ضبط تنسيق حقول الصف / العمود / الصفحة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **ضبط تنسيق حقول البيانات**

يوضح نموذج التعليمات البرمجية أدناه كيفية تعيين تنسيقات العرض وتنسيق الأرقام لحقول البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **مسح الحقول المحورية**

 ال[**مجموعة PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) طريقة اسمه[**صافي()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)يسمح لك بمسح الحقول المحورية. استخدمه عندما تريد مسح جميع الحقول المحورية في المناطق ، على سبيل المثال ، الصفحة أو العمود أو الصف أو البيانات.
يوضح نموذج التعليمات البرمجية أدناه كيفية مسح كافة الحقول المحورية في منطقة البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
