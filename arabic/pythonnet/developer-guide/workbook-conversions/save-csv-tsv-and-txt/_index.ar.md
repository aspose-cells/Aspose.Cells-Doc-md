---
title: تحويل إكسل إلى CSV، TSV و Txt
linktitle: حفظ كملف CSV، TSV و Txt
type: docs
weight: 40
url: /ar/python-net/convert-excel-to-csv-tsv-and-txt/
description: تحويل Excel إلى CSV وTSV وTxt باستخدام Aspose.Cells لـ Python via .NET API.
keywords: تحويل Excel إلى CSV وTSV وTxt باستخدام Python ، تحويل Excel إلى CSV وTSV وTxt بلغة Python via NET ، تحويل دفتر العمل إلى CSV وTSV وTxt بلغة Python.
---

{{% alert color="primary" %}}

تتيح Aspose.Cells لـ Python via .NET تحويل ملفات Excel و ods و json وغيرها من التنسيقات إلى CSV و TSV وTXT.

{{% /alert %}}

## **حفظ دفتر العمل إلى تنسيق نصي أو CSV**

في بعض الأحيان ، ترغب في تحويل أو حفظ دفتر عمل يحتوي على أوراق عمل متعددة إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT ، TabDelim ، CSV ، وما إلى ذلك) ، فإن Microsoft Excel و Aspose.Cells لـ Python via .NET يحفظان افتراضيًا محتويات ورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك إلى CSV. بشكل افتراضي، [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) هو الفاصلة، لذا لا تحدد فاصلًا عند حفظ التنسيق إلى CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **حفظ ملفات النص بفاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **مواضيع متقدمة**
- [الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
