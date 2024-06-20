---
title: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير أوراق الجدول إلى تنسيق CSV
type: docs
weight: 160
url: /ar/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**

توفر Aspose.Cells القدرة على الاحتفاظ بفواصل الخطوط أثناء تحويل جداول البيانات إلى تنسيق CSV. لهذا الغرض، يمكنك استخدام الخاصية [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) في فئة [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions). الخاصية [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) هي خاصية بوليانية. للاحتفاظ بفواصل الأسطر الفارغة أثناء تحويل ملف الإكسيل إلى CSV، ضبط الخاصية [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) على **true**.

الكود النموذجي التالي يقوم بتحميل [ملف الإكسيل المصدر](84378743.xlsx)، ويضبط الخاصية [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) على **true** ويحفظه بصيغة [output.csv](84378744.csv). توضح اللقطة المقارنة بين ملف الإكسيل المصدر، الإخراج الافتراضي الذي تم إنشاؤه أثناء تحويل جدول البيانات إلى CSV والإخراج الذي تم إنشاؤه بضبط [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) على **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
