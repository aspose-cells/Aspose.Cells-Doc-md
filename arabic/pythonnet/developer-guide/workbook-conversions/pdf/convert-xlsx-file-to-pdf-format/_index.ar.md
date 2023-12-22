---
title: تحويل ملف XLSX إلى تنسيق PDF
type: docs
weight: 30
url: /ar/python-net/convert-xlsx-file-to-pdf-format/
description: تعرف على كيفية تحويل ملف XLSX إلى تنسيق PDF باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---
{{% alert color="primary" %}}

يمثل PDF (تنسيق المستندات المحمولة) المستندات بشكل مستقل عن البرامج والأجهزة ونظام التشغيل المستخدم لإنشاء تلك المستندات. يمكن أن يكون الملف PDF عبارة عن مستندات تحتوي على أي مجموعة من النصوص والرسومات والصور بطريقة مستقلة عن الجهاز وعن الدقة. غالبًا ما تكون ملفات PDF مضغوطة، لذا فهي تشغل مساحة أقل من الملف الأصلي.

 في بعض الأحيان، تحتاج إلى تحويل ملف Excel Microsoft إلى PDF. ولهذا، تحتاج إلى حل سريع وآمن ودقيق وموثوق يتيح لك توزيع PDF مستندًا حول العالم. هناك العديد من أدوات التحويل التي يمكنها أداء هذه المهمة. ولكن عليك التأكد من الاحتفاظ بتخطيط مستند Excel الأصلي في ملف الإخراج PDF. يجب عرض الصور والمخططات والأشكال وتنسيق البيانات والخطوط والسمات والألوان وإعدادات إعداد الصفحة واتجاه النص والحدود والمخططات وما إلى ذلك بدقة ودقة.[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) يضمن تحويل عالي الدقة.

تم تصميم هذا المستند لتوفير فهم شامل لكيفية تحويل مستند Excel Microsoft (الذي يحتوي على صور ومخططات وتنسيقات وما إلى ذلك) إلى PDF. ولتحقيق هذه الغاية، يتم عرض كيفية إنشاء تطبيق وحدة تحكم بسيط في Visual Studio.Net يقوم بالتحويل ملف Excel إلى PDF باستخدام Aspose.Cells for Python via .NET API. يتم إجراء التحويل بدرجة عالية من الدقة والدقة.

{{% /alert %}}

##  **تحويل إكسل إلى PDF**

يستخدم هذا المثال ملف Excel (SampleInput.xlsx) كقالب. يحتوي المصنف على أوراق عمل تحتوي على مخططات وصور. تحتوي كل ورقة عمل على أنواع مختلفة من التنسيقات باستخدام الخطوط والسمات والألوان وتأثيرات التظليل والحدود. يوجد مخطط عمودي في ورقة العمل الأولى وصورة في الورقة الأخيرة.

###  **ملف قالب اكسل**

يحتوي ملف القالب على ثلاث أوراق عمل، بما في ذلك المخططات والصورة كوسائط. تحتوي ورقة العمل الأولى على مخططات، بينما تحتوي ورقة العمل الأخيرة على صورة كما هو موضح أدناه في لقطات الشاشة.

|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| ورقة العمل الأولى**(توقعات المبيعات)**| ورقة العمل الثانية**(تقرير المبيعات)**|
|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| ورقة العمل الثالثة**(ادخال بيانات)**| ورقة العمل الأخيرة**(صورة)**|

###  **عملية التحويل**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل الاتصال به[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) الطريقة مباشرة قبل تقديم جدول البيانات إلى PDF. ويضمن القيام بذلك إعادة حساب القيم التابعة للصيغة، ويتم عرض القيم الصحيحة في PDF.

{{% /alert %}}

###  **نتيجة**

عند تشغيل الكود أعلاه، يتم إنشاء ملف PDF في مجلد الملفات في دليل التطبيق الخاص بك.
تُظهر لقطات الشاشة التالية صفحات PDF. لاحظ أنه يتم أيضًا الاحتفاظ بالرؤوس والتذييلات في ملف الإخراج PDF.

|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| ورقة العمل الأولى**(توقعات المبيعات)**| ورقة العمل الثانية**(تقرير المبيعات)**|
|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![ما يجب القيام به:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| ورقة العمل الثالثة**(ادخال بيانات)**| ورقة العمل الأخيرة**(صورة)**|
