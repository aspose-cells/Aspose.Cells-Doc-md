---
title: تحويل ملفات CSV، TSV و TXT إلى Excel
type: docs
weight: 50
url: /ar/java/convert-csv-tsv-and-txt-to-excel/
---

## **فتح ملفات CSV**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات يتم فصل قيمها أو تقسيمها بواسطة فواصل. في ملفات CSV، يتم تخزين البيانات في تنسيق جدولي يحتوي على حقول مفصولة بحرف الفاصلة ومحاطة بحرف الاقتباس المزدوج. إذا احتوت قيمة الحقل على حرف الاقتباس المزدوج فيجب تهريبها بزوج من أحرف الاقتباس المزدوج. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات الخاصة بك إلى ملف CSV.

لفتح ملفات CSV، استخدم فئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وحدد قيمة [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) المحددة مسبقًا في فئة التعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**

في Excel، عند فتح ملف CSV مع أحرف خاصة، يتم استبدال الأحرف تلقائيًا. ويتم نفس الأمر بواسطة واجهة برمجة التطبيقات Aspose.Cells التي يتم توضيحها في المثال البرمجي المعطى أدناه.

#### **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **فتح ملفات CSV باستخدام محلل الجاري التفضيلي**

غالبًا ما ليس من الضروري استخدام إعدادات محلل افتراضية لفتح ملفات CSV. في بعض الأحيان، قد لا ينتج استيراد ملف CSV الإخراج المتوقع مثل عدم تطابق تنسيق التاريخ المتوقع أو معالجة الحقول الفارغة بشكل مختلف. لهذا الغرض، تتاح فئة [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) لتوفير محلل مفضل لتوصيل مختلف أنواع البيانات حسب الحاجة. يوضح الكود عينة التالي استخدام المحلل المفضل.  

يمكن تنزيل ملف الشفرة المصدري وملفات الإخراج التجريبية من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **فتح ملفات TSV (مفصولة بالألسنة)**

تحتوي ملفات TSV على بيانات جدولية ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة مثل الجداول وأوراق العمل. بإيجاز، ملف TSV هو نوع خاص من ملف نصي عادي مع علامة تبويب بين كل عمود في النص.

لفتح ملفات مقسمة بواسطة العلامات، يجب على المطورين استخدام الفئة [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) وحدد القيمة [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) المحددة مسبقًا في فئة التعداد [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **مثال**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **مواضيع متقدمة**
- [تحميل أو استيراد ملف CSV بالصيغ](/cells/ar/java/load-or-import-csv-file-with-formulas/)
- [تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

