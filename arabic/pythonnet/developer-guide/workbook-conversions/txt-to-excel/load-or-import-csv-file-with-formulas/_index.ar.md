---
title: قم بتحميل أو استيراد ملف CSV باستخدام الصيغ
type: docs
weight: 350
url: /ar/python-net/load-or-import-csv-file-with-formulas/
description: قم بتحميل أو استيراد ملف CSV مع الصيغ باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 يحتوي الملف CSV في الغالب على بيانات نصية ولا يحتوي على أي صيغ. ومع ذلك، في بعض الأحيان يحدث أن تحتوي الملفات CSV أيضًا على صيغ. يجب تحميل ملفات CSV هذه عن طريق تعيين ملف[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) كما * صحيح **. بمجرد تعيين هذه الخاصية *صحيحة**، لن يتعامل Aspose.Cells مع الصيغة كنص بسيط. سيتم التعامل معها كصيغة وسيقوم محرك حساب الصيغة Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 

 يوضح التعليمة البرمجية التالية كيف يمكنك تحميل ملف CSV بالإضافة إلى استيراده باستخدام الصيغ. يمكنك استخدام أي ملف CSV. لغرض التوضيح، نستخدم[ملف CSV بسيط](5115034.csv)الذي يحتوي على هذه البيانات. كما ترون أنه يحتوي على صيغة.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 يقوم الكود أولاً بتحميل الملف CSV، ثم استيراده مرة أخرى في الخلية D4. وأخيرًا، يقوم بحفظ كائن المصنف بتنسيق XSLX. ال[ملف الإخراج XLSX](5115052.xlsx) يشبه هذا. كما ترى تحتوي الخلية C3 وF4 على الصيغة ونتيجتها 800.

|![ما يجب القيام به:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

