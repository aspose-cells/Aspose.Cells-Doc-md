---
title: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام Golang عبر C++
linktitle: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير أوراق الجدول إلى تنسيق CSV
type: docs
weight: 160
url: /ar/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: تعلم كيفية الاحتفاظ بالفواصل للصفوف الفارغة عند تصدير جداول البيانات إلى تنسيق CSV باستخدام Aspose.Cells مع Golang عبر C++.
---

## **الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**

توفر Aspose.Cells القدرة على الاحتفاظ بفواصل الأسطر أثناء تحويل جداول البيانات إلى تنسيق CSV. لهذا، يمكنك استخدام خاصية [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) من فئة [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) هي خاصية من نوع boolean. للحفاظ على الفواصل للفقرات الفارغة أثناء تحويل ملف Excel إلى CSV، اضبط الخاصية [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) على **true**.

يعرض الرمز النموذجي التالي تحميل ملف Excel [المصدر](84378743.xlsx). حيث يضبط الخاصية [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) على **true** ويحفظه كـ [ملف CSV الناتج](84378744.csv). تظهر الصورة المجمعة المقارنة بين ملف Excel المصدر، والناتج الافتراضي عند تحويل ورقة العمل إلى CSV، والناتج الناتج عن ضبط [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) على **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
