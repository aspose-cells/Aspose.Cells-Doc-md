---
title: تحميل أو استيراد ملف CSV مع الصيغ
type: docs
weight: 350
url: /ar/python-net/load-or-import-csv-file-with-formulas/
description: تحميل أو استيراد ملف CSV مع الصيغ باستخدام Aspose.Cells لواجهة برمجة التطبيقات لـ Python via .NET API.
keywords: تحميل ملف CSV أو استيراده مع الصيغ في Python via NET، تحويل ملف CSV مع الصيغ إلى Excel في Python، تحويل ملف CSV مع الصيغ إلى xlsx، تحميل ملف CSV مع الصيغ إلى ملف Excel.
---

{{% alert color="primary" %}} 

يحتوي ملف CSV بشكل أساسي على بيانات نصية ولا يحتوي على أي صيغ. ومع ذلك، في بعض الأحيان يحدث أن ملفات CSV تحتوي أيضًا على صيغ. يجب تحميل مثل هؤلاء ملفات CSV عن طريق ضبط [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) ك **true**. بمجرد ضبط هذا الخاصية **true**، سوف لا تعامل Aspose.Cells الصيغ كنص بسيط. سيتم معالجتها كصيغة وسوف يقوم محرك حساب الصيغ في Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 

يوضح الكود التالي كيف يمكنك تحميل واستيراد ملف CSV بالصيغ. يمكنك استخدام أي ملف CSV. لأغراض التوضيح، سنستخدم [ملف csv بسيط](5115034.csv) الذي يحتوي على هذه البيانات. كما ترون، يحتوي على صيغة.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



يقوم الكود أولاً بتحميل ملف CSV، ثم استيراده مرة أخرى في الخلية D4. وأخيرًا، يقوم بحفظ كائن الورقة في تنسيق XSLX. [يبدو الملف XLSX الناتج](5115052.xlsx) مثل هذا. كما ترون، تحتوي الخلية C3 و F4 على صيغة ونتيجتها 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

