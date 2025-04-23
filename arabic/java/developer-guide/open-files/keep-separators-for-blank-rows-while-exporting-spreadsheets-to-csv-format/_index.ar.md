---
title: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير أوراق الجدول إلى تنسيق CSV
type: docs
weight: 110
url: /ar/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**

توفر Aspose.Cells القدرة على الاحتفاظ بفواصل الخطوط أثناء تحويل جداول البيانات إلى تنسيق CSV. لهذا الغرض، يمكنك استخدام الخاصية [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) في فئة [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions). الخاصية [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) هي خاصية بوليانية. للاحتفاظ بفواصل الأسطر الفارغة أثناء تحويل ملف الإكسيل إلى CSV، ضبط الخاصية [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) على **true**.

يحمل الكود العيني التالي [ملف Excel المصدر](KeepSeparatorsForBlankRow.xlsx). يقوم بتعيين خاصية [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) إلى **صحيح** ويحفظه بصيغة [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). يُظهر التقاط الشاشة المقارنة بين ملف Excel المصدر، الإخراج الافتراضي المُنشأ أثناء تحويل الجدول الزمني إلى CSV والإخراج الناتج عن تعيين [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) إلى **صحيح**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
{{< app/cells/assistant language="java" >}}
