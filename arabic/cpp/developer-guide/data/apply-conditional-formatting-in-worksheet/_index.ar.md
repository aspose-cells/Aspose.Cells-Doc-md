---
title: تطبيق التنسيق الشرطي في ورقة العمل
type: docs
weight: 40
url: /ar/cpp/apply-conditional-formatting-in-worksheet/
---
## **سيناريو الاستخدام المحتمل**
 يسمح لك Aspose.Cells بإضافة جميع أنواع الصيغ الشرطية ، مثل الصيغة ، وفوق المتوسط ، ومقياس اللون ، وشريط البيانات ، ومجموعة الرموز ، و Top10 ، وما إلى ذلك.[IF FormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)فئة تحتوي على جميع الطرق اللازمة لتطبيق التنسيق الشرطي الذي تختاره. فيما يلي قائمة ببعض طرق Get.

- [GetIAboveAverage ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIColorScale ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDataBar ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [GetIIconSet ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITop10 ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **تطبيق التنسيق الشرطي في ورقة العمل**
 يُظهر نموذج التعليمات البرمجية التالي كيفية إضافة تنسيق شرطي لقيمة Cell على الخلايا A1 و B2. الرجاء مراجعة[ملف اكسل الناتج](23167004.xlsx) التي تم إنشاؤها بواسطة الكود ولقطة الشاشة التالية التي تشرح تأثير الكود على ملف[ملف اكسل الناتج](23167004.xlsx). إذا قمت بوضع قيمة أكبر من 100 في الخلية A2 و B2 ، فسيختفي لون التعبئة الأحمر من الخلية A1 و B2.

![ما يجب القيام به: image_بديل_نص](apply-conditional-formatting-in-worksheet_1.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
