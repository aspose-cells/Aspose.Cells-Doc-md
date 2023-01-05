---
title: قم بتحويل CSV و TSV و TXT إلى Excel
type: docs
weight: 50
url: /ar/java/convert-csv-tsv-and-txt-to-excel/
---
## **فتح CSV الملفات**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات محددة قيمها أو مفصولة بفواصل. في ملفات CSV ، يتم تخزين البيانات في تنسيق جدولي يحتوي على حقول مفصولة بفاصلة ويتم اقتباسها بحرف اقتباس مزدوج. إذا احتوت قيمة الحقل على علامة اقتباس مزدوجة ، يتم تخطيها بزوج من علامات الاقتباس المزدوجة. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى ملف CSV.

لفتح CSV ملفات ، استخدم امتداد**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** فئة واختيار**[CSV] (https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** القيمة المحددة مسبقًا في**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

## **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **فتح CSV الملفات واستبدال الحروف غير الصالحة**

في Excel ، عند فتح ملف CSV بأحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بنفس الشيء بواسطة Aspose.Cells API والذي هو موضح في مثال الكود الموضح أدناه.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **فتح CSV الملفات باستخدام المحلل اللغوي المفضل**

هذا ليس ضروريًا دائمًا لاستخدام إعدادات المحلل اللغوي الافتراضية لفتح ملفات CSV. في بعض الأحيان ، لا يؤدي استيراد ملف CSV إلى إنشاء الإخراج المتوقع مثل تنسيق التاريخ ليس كما هو متوقع أو يتم التعامل مع الحقول الفارغة بشكل مختلف. لهذا الغرض**[TxtLoadOptions.PreferredParsers] (https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**متاح لتوفير المحلل اللغوي المفضل لتحليل أنواع البيانات المختلفة حسب المتطلبات. يوضح نموذج التعليمات البرمجية التالي استخدام المحلل اللغوي المفضل.

يمكن تنزيل نموذج ملف المصدر وملفات الإخراج من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **فتح ملفات TSV (محدد بعلامات جدولة)**

تحتوي الملفات المحددة بعلامات جدولة على بيانات جدول بيانات ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة مثل الجداول وجداول البيانات. باختصار ، الملف المحدد بعلامات جدولة هو نوع خاص من ملفات النص العادي بعلامة جدولة بين كل عمود في النص.

لفتح ملفات محددة بعلامات جدولة ، يجب على المطورين استخدام الامتداد**[LoadOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** فئة واختيار**[TSV] (https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** القيمة المحددة مسبقًا في**[LoadFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**تعداد.

## **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **موضوعات مسبقة**
- [قم بتحميل أو استيراد ملف CSV باستخدام الصيغ](/cells/ar/java/load-or-import-csv-file-with-formulas/)
- [تقليم الصفوف والأعمدة الفارغة البادئة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

