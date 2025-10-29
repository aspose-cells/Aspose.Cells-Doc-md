---
title: تحويل إكسل إلى CSV و TSV و Txt مع Golang عبر C++
linktitle: حفظ كملف CSV، TSV و Txt
type: docs
weight: 40
url: /ar/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: تحويل ملفات إكسل إلى تنسيقات CSV و TSV و TXT بسهولة باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

يجعل Aspose.Cells من الممكن تحويل ملفات Excel و ODS و JSON والتنسيقات الأخرى إلى CSV و TSV و TXT.

{{% /alert %}}

## **حفظ دفتر العمل إلى تنسيق نصي أو CSV**

في بعض الأحيان ، تريد تحويل أو حفظ دفتر عمل بعدة ورقات عمل إلى تنسيق نصي. بالنسبة لتنسيقات النص (مثل TXT، TabDelim، CSV، إلخ) ، يحفظ كل من Microsoft Excel وAspose.Cells افتراضيًا محتويات الورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك بصيغة CSV. بشكل افتراضي، [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) هو فاصلة، لذا لا تحدد فاصل عند الحفظ بصيغة CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **حفظ ملفات النص بفاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **مواضيع متقدمة**
- [الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
