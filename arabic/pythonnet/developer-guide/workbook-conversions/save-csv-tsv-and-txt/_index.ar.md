---
title: تحويل Excel إلى CSV,TSV وTxt
linktitle: احفظ باسم CSV,TSV و Txt
type: docs
weight: 40
url: /ar/python-net/convert-excel-to-csv-tsv-and-txt/
description: قم بتحويل Excel إلى CSV,TSV وTxt باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET يجعل من الممكن تحويل ملفات Excel و ods و json وملفات التنسيق الأخرى إلى CSV و TSV و TXT.

{{% /alert %}}

##  **حفظ المصنف إلى نص أو تنسيق CSV**

في بعض الأحيان، قد ترغب في تحويل مصنف يحتوي على أوراق عمل متعددة أو حفظه إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT، TabDelim، CSV، وما إلى ذلك)، بشكل افتراضي، يقوم كل من Microsoft Excel وAspose.Cells for Python via .NET بحفظ محتويات ورقة العمل النشطة فقط.

يشرح مثال التعليمات البرمجية التالي كيفية حفظ مصنف بأكمله بتنسيق نصي. قم بتحميل المصنف المصدر الذي يمكن أن يكون أي ملف جدول بيانات Excel أو OpenOffice Microsoft (مثل XLS، XLSX، XLSM، XLSB، ODS وما إلى ذلك) مع أي عدد من أوراق العمل.

عند تنفيذ التعليمات البرمجية، فإنه يحول بيانات كافة الأوراق في المصنف إلى تنسيق TXT.

 يمكنك تعديل نفس المثال لحفظ الملف الخاص بك إلى CSV. بشكل افتراضي،**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**هي فاصلة، لذلك لا تحدد فاصلًا في حالة الحفظ بتنسيق CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **حفظ الملفات النصية باستخدام فاصل مخصص**

تحتوي الملفات النصية على بيانات جدول بيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **مواضيع متقدمة**
- [احتفظ بفواصل الصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [اقتطاع الصفوف والأعمدة الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
