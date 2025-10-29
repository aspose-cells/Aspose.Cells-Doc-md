---
title: إعدادات الخط مع Golang عبر C++
linktitle: إعدادات الخط
type: docs
weight: 30
url: /ar/go-cpp/cells-font-settings/
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جدول البيانات. تدعم تعيين إعدادات الخط للخلايا، مما يتيح للمستخدمين تخصيص نمط وخصائص الخطوط. ستوضح هذه المقالة كيف تستخدم مكتبة Aspose.Cells لضبط إعدادات الخطوط في الخلايا.
keywords: Aspose.Cells، Cells، Font Settings، Styles، Properties
---

{{% alert color="primary" %}}

يمكن التحكم في مظهر النص وشكله عن طريق تغيير إعدادات الخط. قد تشمل إعدادات الخط الاسم، النمط، الحجم، اللون، وتأثيرات أخرى للخطوط. تمامًا كبرنامج Microsoft Excel، يدعم Aspose.Cells أيضًا تكوين إعدادات الخطوط للخلايا.

{{% /alert %}}

## **تكوين إعدادات الخط**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورق عمل في ملف Excel. يمثل ورق العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). كل عنصر في مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) يمثل كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

توفر Aspose.Cells فئة [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) وطرق [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) و [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/) تُستخدم للحصول على وتعيين نمط تنسيق الخلية. توفر الفئة [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) خصائص لتكوين إعدادات الخط.

### **تعيين اسم الخط**

يمكن للمطورين تطبيق أي خط على النص داخل خلية باستخدام خاصية [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **تعيين نمط الخط إلى عريض**

يمكن للمطورين جعل النص عريضًا عن طريق ضبط خاصية [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) من كائن [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) على **صحيح**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **تعيين حجم الخط**

قم بتعيين حجم الخط باستخدام خاصية [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **تعيين لون الخط**

استخدم خاصية [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) لضبط لون الخط. اختر أي لون من التعداد اللوني (جزء من إطار عمل C++) وقم بتعيينه للخاصية [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **تعيين نوع تسطير الخط**

استخدم خاصية [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) لتسطير النص. تقدم Aspose.Cells مجموعة من أنواع تسطير الخط المحددة مسبقًا في تعداد [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)

|**أنواع تسطير الخط**|**الوصف**|
| :- | :- |
|Accounting|تسطير واحد للحساب|
|Double|تسطير مزدوج|
|DoubleAccounting|تسطير حسابي مزدوج|
|None|بدون تسطير|
|Single|تسطير واحد|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **ضبط تأثير شطب**

تطبيق تأثير الشطب عن طريق ضبط خاصية [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) إلى **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **ضبط تأثير الرمز الفرعي**

تطبيق الرمز الفرعي عن طريق ضبط خاصية [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) إلى **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **ضبط تأثير الرمز العلوي على الخط**

يمكن للمطورين تطبيق تأثير الرمز العلوي على الخط عن طريق ضبط خاصية [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) إلى **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **مواضيع متقدمة**
- [تطبيق تأثيرات الرمز العلوي والرمز السفلي على الخطوط](/cells/ar/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل](/cells/ar/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
