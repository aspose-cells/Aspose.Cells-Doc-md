---
title: تحويل CSV، TSV، و TXT إلى إكسل باستخدام Golang عبر C++
linktitle: تحويل CSV و TSV و TXT إلى Excel
type: docs
weight: 30
url: /ar/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: تعلم كيفية تحويل ملفات CSV و TSV و TXT إلى Excel باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 باستخدام Aspose.Cells for C++، يمكنك تحويل ملفات CSV إلى Excel، OpenOffice، PDF، JSON، والعديد من التنسيقات الأخرى.

{{% /alert %}}

## **فتح ملفات CSV**

ملفات القيم المفصولة بفواصل (CSV) تحتوي على سجلات تفصل بين القيم بواسطة الفاصلة. تُخزن البيانات في جدول حيث يتم فصل كل عمود بواسطة الحرف الفاصلة ويوضع بين علامتي اقتباس مزدوجتين. إذا احتوى حقل على علامة اقتباس مزدوجة، يتم الهروب منها بمزوج من علامتي اقتباس مزدوجتين. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات الجدول إلى CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **فتح ملفات CSV واستبدال الأحرف غير الصالحة**

عند فتح ملف CSV في Excel، يتم استبدال الأحرف تلقائيًا. يتم هذا بواسطة API الخاص بـ Aspose.Cells أيضًا، كما هو موضح في المثال البرمجي أدناه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **باستخدام القارئ المفضل**

ليس من الضروري دائمًا استخدام إعدادات القارئ الافتراضية لفتح ملفات CSV. أحيانًا، استيراد ملف CSV لا يخلق الناتج المتوقع، مثل عندما يكون تنسيق التاريخ غير متوقع أو يتم التعامل مع الحقول الفارغة بشكل مختلف. لهذا الغرض، تتوفر خاصية **TxtLoadOptions.PreferredParsers** لتوفير قاريء مفضل خاص بك لتحليل أنواع البيانات المختلفة حسب متطلباتك. يوضح المثال التالي استخدام قارئ مفضل.

يمكن تنزيل ملف الشفرة المصدري وملفات الإخراج التجريبية من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **فتح ملفات النصوص بفاصل مخصص**

تُستخدم ملفات النصوص لاحتواء البيانات الجدولية بدون تنسيق. هذا النوع من الملفات هو نوعٌ من ملفات النصوص البسيطة، وقد تحتوي على بعض محددات التجزئة المخصصة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **فتح ملفات ذات فاصل علامات التبويب**

ملفات النص المفصولة بعلامات التبويب (TSV) تحتوي على بيانات جداول بيانات ولكن بدون تنسيق. تكون البيانات مرتبة في صفوف وأعمدة كما في الجداول وبرمجيات الجدول. بشكل أساسي، فإن ملف TSV هو نوع خاص من ملفات النص العادي مع فصل بين كل عمود بعلامة تبويب.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**

ملفات القيم المفصولة بعلامة تبويب (TSV) تحتوي على بيانات جداول بيانات ولكن بدون تنسيق. إنها نفس نوع ملف المفصولة بعلامة تبويب حيث يتم ترتيب البيانات في صفوف وأعمدة كما في الجداول وبرمجيات الجدول.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **مواضيع متقدمة**
- [تحميل أو استيراد ملف CSV مع صيغ](/cells/ar/cpp/load-or-import-csv-file-with-formulas/)
- [قراءة ملف CSV بعدة ترميزات](/cells/ar/cpp/reading-csv-file-with-multiple-encodings/)
