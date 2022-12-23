---
title: قم بتحويل CSV و TSV و TXT إلى Excel
type: docs
weight: 30
url: /ar/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

باستخدام Aspose.Cells ، يمكنك تحويل ملف CSV إلى Excel و OpenOffice و Pdf و Json والعديد من التنسيقات المختلفة.

{{% /alert %}}


## **فتح CSV الملفات**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات حيث يتم فصل القيم بفاصلات. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود عن طريق الفاصلة ويتم اقتباسها بحرف اقتباس مزدوج. إذا احتوت قيمة الحقل على علامة اقتباس مزدوجة ، يتم تخطيها بزوج من علامات الاقتباس المزدوجة. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **فتح CSV الملفات واستبدال الحروف غير الصالحة**

في Excel ، عند فتح ملف CSV بأحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بنفس الشيء بواسطة Aspose.Cells API والذي هو موضح في مثال الكود الموضح أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **استخدام المحلل اللغوي المفضل**

هذا ليس ضروريًا دائمًا لاستخدام إعدادات المحلل اللغوي الافتراضية لفتح ملفات CSV. في بعض الأحيان ، لا يؤدي استيراد ملف CSV إلى إنشاء الإخراج المتوقع مثل تنسيق التاريخ ليس كما هو متوقع أو يتم التعامل مع الحقول الفارغة بشكل مختلف. لهذا الغرض**TxtLoadOptions.PreferredParsers**متاح لتوفير المحلل اللغوي المفضل لتحليل أنواع البيانات المختلفة حسب المتطلبات. يوضح نموذج التعليمات البرمجية التالي استخدام المحلل اللغوي المفضل.

يمكن تنزيل نموذج ملف المصدر وملفات الإخراج من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **فتح ملفات نصية باستخدام فاصل مخصص**

تُستخدم الملفات النصية للاحتفاظ ببيانات جدول البيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **فتح ملفات محدده بعلامات تبويب**

يحتوي الملف المحدد بعلامات جدولة (نص) على بيانات جدول بيانات ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات. بشكل أساسي ، الملف المحدد بعلامات جدولة هو نوع خاص من ملفات النص العادي مع علامة تبويب بين كل عمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **فتح ملفات قيم مفصولة بعلامات جدولة (TSV)**

يحتوي ملف القيم المفصولة بعلامات جدولة (TSV) على بيانات جدول بيانات ولكن بدون أي تنسيق. هو نفسه مع ملف محدد بعلامات جدولة حيث يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **موضوعات مسبقة**
- [قم بتحميل أو استيراد ملف CSV باستخدام الصيغ](/cells/ar/net/load-or-import-csv-file-with-formulas/)
- [قراءة CSV ملف ذو ترميزات متعددة](/cells/ar/net/reading-csv-file-with-multiple-encodings/)

