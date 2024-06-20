---
title: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير أوراق الجدول إلى تنسيق CSV
type: docs
weight: 160
url: /ar/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: الحفاظ على الفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام API Aspose.Cells للبايثون via .NET.
keywords: الحفاظ على الفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام Python، إبقاء الفواصل للصفوف الفارغة أثناء حفظ جداول البيانات بتنسيق CSV في Python via NET، الحفاظ على الفواصل للصفوف الفارغة عند تصدير جدول البيانات من Excel إلى تنسيق CSV بواسطة Python.
---

## **الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**

توفر Aspose.Cells for Python via .NET القدرة على الاحتفاظ بفواصل الأسطر أثناء تحويل جداول البيانات إلى تنسيق CSV. لهذا، يُمكنك استخدام الخاصية [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) من الفئة [**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/). [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) هي خاصية منطقية. للحفاظ على الفواصل للأسطر الفارغة أثناء تحويل ملف الإكسيل إلى CSV، يُرجى ضبط الخاصية [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) إلى **true**.

الكود النموذجي التالي يقوم بتحميل [ملف الإكسيل المصدر](84378743.xlsx)، ويضبط الخاصية [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) على **true** ويحفظه بصيغة [output.csv](84378744.csv). توضح اللقطة المقارنة بين ملف الإكسيل المصدر، الإخراج الافتراضي الذي تم إنشاؤه أثناء تحويل جدول البيانات إلى CSV والإخراج الذي تم إنشاؤه بضبط [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) على **true**.

![todo:image_alt_text](result.jpg)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
