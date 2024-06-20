---
title: تحويل ملفات CSV، TSV و TXT إلى Excel
type: docs
weight: 30
url: /ar/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

من خلال Aspose.Cells ، يمكنك تحويل ملف CSV إلى Excel ، OpenOffice ، Pdf ، Json والعديد من التنسيقات المختلفة.

{{% /alert %}}


## **فتح ملفات CSV**

ملفات قيم مفصولة بفواصل (CSV) تحتوي على سجلات حيث تكون القيم مفصولة بفواصل. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود بحرف الفاصلة وتقوم بتقديمه بواسطة الرمز التنصيصي من خلال الرمز مزدوج التنصيص. إذا كانت قيمة الحقل تحتوي على رمز تنصيصي مزدوج فإنه يتم الخروج منها بزوج من الرموز المزدوجة للتنصيص. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**

في Excel ، عند فتح ملف CSV الذي يحتوي على أحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بالشيء نفسه بواسطة واجهة برمجة التطبيقات Aspose.Cells والتي يتم توضيحها في مثال الشيفرة المعطى أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **استخدام محلل مفضل**

ليس من الضروري دائمًا استخدام إعدادات المحلل الافتراضية لفتح ملفات CSV. في بعض الأحيان ، لا ينشأ استيراد ملف CSV الإخراج المتوقع مثل تنسيق التاريخ ليس كما هو متوقع أو يتم التعامل بشكل مختلف مع الحقول الفارغة. يتوفر لهذا الغرض **TxtLoadOptions.PreferredParsers** لتوفير محلل مفضل خاص لتحليل أنواع بيانات مختلفة وفقًا للمتطلبات. يوضح الشيفرة التالية عينة عن استخدام المحلل المفضل.  

يمكن تنزيل ملف الشفرة المصدري وملفات الإخراج التجريبية من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **فتح ملفات النصوص بفاصل مخصص**

تُستخدم ملفات النصوص لاحتواء البيانات الجدولية بدون تنسيق. هذا النوع من الملفات هو نوعٌ من ملفات النصوص البسيطة، وقد تحتوي على بعض محددات التجزئة المخصصة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **فتح ملفات النصوص المفصولة بواسطة الألسنة**

يحتوي ملف النص المفصول بواسطة الألسنة على بيانات جدولية بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة مثلما يحدث في الجداول والأوراق الجدولية. بشكل أساسي، يعد ملف النص المفصول بواسطة الألسنة نوعًا خاصًا من ملفات النص البسيطة مع وجود فراغ بين كل عمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**

يحتوي ملف القيم المفصولة بواسطة الألسنة على بيانات جدولية بدون أي تنسيق. وهو نفس الشيء مع ملف النص المفصول بواسطة الألسنة، حيث تتم ترتيب البيانات في صفوف وأعمدة مثلما يحدث في الجداول والأوراق الجدولية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **مواضيع متقدمة**
- [تحميل أو استيراد ملف CSV بالصيغ](/cells/ar/net/load-or-import-csv-file-with-formulas/)
- [قراءة ملف CSV بعدة ترميزات](/cells/ar/net/reading-csv-file-with-multiple-encodings/)

