---
title: تحويل ملفات Excel إلى CSV و TSV و Txt
linktitle: حفظ بتنسيق CSV و TSV و Txt
type: docs
weight: 40
url: /ar/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

يتيح Aspose.Cells تحويل ملفات Excel و ods و json وملفات التنسيقات الأخرى إلى CSV و TSV و TXT.

{{% /alert %}}

## **حفظ المصنف إلى نص أو تنسيق CSV**

في بعض الأحيان ، تريد تحويل مصنف أو حفظه باستخدام أوراق عمل متعددة إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT ، TabDelim ، CSV ، إلخ) ، افتراضيًا ، يتم حفظ محتويات ورقة العمل النشطة فقط Microsoft Excel و Aspose.Cells.

يوضح المثال التالي من التعليمات البرمجية كيفية حفظ مصنف بأكمله في تنسيق نصي. قم بتحميل المصنف المصدر الذي يمكن أن يكون أي ملف جدول بيانات Microsoft Excel أو OpenOffice (مثل XLS و XLSX و XLSM و XLSB و ODS وما إلى ذلك) بأي عدد من أوراق العمل.

عندما يتم تنفيذ الكود ، فإنه يحول بيانات جميع الأوراق في المصنف إلى تنسيق TXT.

 يمكنك تعديل نفس المثال لحفظ ملفك في CSV. بشكل افتراضي،**[TxtSaveOptions.Separator] (https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**هي فاصلة ، لذلك لا تحدد فاصلًا في حالة الحفظ بتنسيق CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **حفظ الملفات النصية باستخدام فاصل مخصص**

تحتوي الملفات النصية على بيانات جدول بيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **موضوعات مسبقة**
- [احتفظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تقليم الصفوف والأعمدة الفارغة البادئة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
