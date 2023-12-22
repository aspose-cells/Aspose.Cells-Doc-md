---
title: طرق مختلفة لحفظ الملفات
linktitle: احفظ الملفات
type: docs
weight: 40
url: /ar/net/different-ways-to-save-files/
description: Aspose.Cells for .NET يمكنه حفظ الملفات بتنسيقات مختلفة. احفظ الملفات في PDF. احفظ الملفات في HTML. احفظ الملفات في DOCX. احفظ الملفات في PPTX. احفظ الملفات في JSON. احفظ الملفات في MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells يجعل من الممكن إنشاء وحفظ الملفات. تشرح هذه المقالة الطرق المختلفة التي يمكن من خلالها حفظ الملفات.

{{% /alert %}}

##  **طرق مختلفة لحفظ الملفات**

 Aspose.Cells يوفر**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)** والذي يمثل ملف Excel Microsoft ويوفر الخصائص والأساليب اللازمة للعمل مع ملفات Excel. ال**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)** يوفر الفصل**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** الطريقة المستخدمة لحفظ ملفات Excel. ال**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**تحتوي الطريقة على العديد من الأحمال الزائدة التي تستخدم لحفظ الملفات بطرق مختلفة.

 يتم تحديد تنسيق الملف الذي يتم حفظ الملف فيه بواسطة**[حفظ التنسيق](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**تعداد

|**أنواع تنسيقات الملفات**|**وصف**|
| :- | :- |
|CSV|يمثل ملف CSV|
|Excel97To2003|يمثل ملف Excel 97 - 2003|
|XLSX|يمثل ملف Excel 2007 XLSX|
|XLSM|يمثل ملف Excel 2007 XLSM|
|XLTX|يمثل ملف قالب Excel 2007 رقم XLTX|
|XLTM|يمثل ملف Excel 2007 الممكّن بماكرو XLTM|
|XLSB|يمثل ملف Excel 2007 الثنائي XLSB|
|SpreadsheetML|يمثل ملف جدول بيانات XML|
|TSV|يمثل ملف قيم مفصولة بعلامات جدولة|
|TabDelimited|يمثل ملف نصي محدد بعلامات جدولة|
|ODS|يمثل ملف ODS|
|لغة البرمجة|يمثل HTML ملف (ملفات)|
|أتش تي أم أل|يمثل ملف (ملفات) MHTML|
|بي دي إف|يمثل ملف PDF|
|XPS|يمثل وثيقة XPS|
|TIFF|يمثل تنسيق ملف الصور الموسوم (TIFF)|

##  **كيفية حفظ الملف بتنسيقات مختلفة**

لحفظ الملفات في موقع تخزين، حدد اسم الملف (مكتملًا بمسار التخزين) وتنسيق الملف المطلوب (من ملف**[حفظ التنسيق](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** التعداد) عند استدعاء**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)** أشياء**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **كيفية حفظ المصنف إلى PDF**
تنسيق المستندات المحمولة (PDF) هو نوع من المستندات تم إنشاؤه بواسطة Adobe في التسعينيات. كان الغرض من تنسيق الملف هذا هو تقديم معيار لتمثيل المستندات والمواد المرجعية الأخرى بتنسيق مستقل عن البرامج التطبيقية والأجهزة بالإضافة إلى نظام التشغيل. يتمتع تنسيق الملف PDF بقدرة كاملة على احتواء معلومات مثل النصوص والصور والارتباطات التشعبية وحقول النماذج والوسائط الغنية والتوقيعات الرقمية والمرفقات وبيانات التعريف والميزات الجغرافية المكانية والكائنات ثلاثية الأبعاد التي يمكن أن تصبح جزءًا من المستند المصدر.

الكود التالي يوضح كيفية حفظ المصنف كملف pdf مع Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **كيفية حفظ المصنف إلى نص أو تنسيق CSV**

في بعض الأحيان، قد ترغب في تحويل مصنف يحتوي على أوراق عمل متعددة أو حفظه إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT، TabDelim، CSV، وما إلى ذلك)، بشكل افتراضي، يقوم كل من Microsoft Excel وAspose.Cells بحفظ محتويات ورقة العمل النشطة فقط.

يشرح مثال التعليمات البرمجية التالي كيفية حفظ مصنف بأكمله بتنسيق نصي. قم بتحميل المصنف المصدر الذي يمكن أن يكون أي ملف جدول بيانات Excel أو OpenOffice Microsoft (مثل XLS، XLSX، XLSM، XLSB، ODS وما إلى ذلك) مع أي عدد من أوراق العمل.

عند تنفيذ التعليمات البرمجية، فإنه يحول بيانات كافة الأوراق في المصنف إلى تنسيق TXT.

 يمكنك تعديل نفس المثال لحفظ الملف الخاص بك إلى CSV. بشكل افتراضي،**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**هي فاصلة، لذلك لا تحدد فاصلًا في حالة الحفظ بتنسيق CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **كيفية حفظ الملف إلى ملفات نصية باستخدام فاصل مخصص**

تحتوي الملفات النصية على بيانات جدول بيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **كيفية حفظ الملف في الدفق**

 لحفظ الملفات في دفق، قم بإنشاء ملف*دفق الذاكرة* أو*تيار ملف*كائن واحفظ الملف في كائن الدفق هذا عن طريق استدعاء ملف**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)** أشياء**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** طريقة. حدد تنسيق الملف المطلوب باستخدام**[حفظ التنسيق](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** التعداد عند استدعاء**[حفظ](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **كيفية حفظ ملف Excel إلى ملفات Html وMht**
يمكن لـ Aspose.Cells ببساطة حفظ ملف Excel أو JSON أو CSV أو ملفات أخرى يمكن تحميلها بواسطة Aspose.Cells كملفات .html و.mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **كيفية حفظ ملف Excel في OpenOffice (ODS، SXC، FODS، OTS)**
يمكننا حفظ الملفات بتنسيق open offce: ODS، SXC، FODS، OTS إلخ.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **كيفية حفظ ملف Excel إلى JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف قياسي مفتوح لمشاركة البيانات يستخدم نصًا يمكن قراءته بواسطة الإنسان لتخزين البيانات ونقلها. يتم تخزين الملفات JSON بامتداد .json. يتطلب JSON تنسيقًا أقل ويعتبر بديلاً جيدًا لـ XML. JSON مشتق من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. توليد وتحليل JSON مدعوم بالعديد من لغات البرمجة الحديثة. application/json هو نوع الوسائط المستخدم لـ JSON.

Aspose.Cells يدعم حفظ الملفات إلى JSON أو XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **مواضيع متقدمة**
- [ضبط مستوى ضغط المصنف](/cells/ar/net/adjust-workbook-compression-level/)
- [احفظ المصنف في تنسيق جدول بيانات XML المفتوح الصارم](/cells/ar/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [حفظ الملف إلى كائن الاستجابة](/cells/ar/net/saving-file-to-response-object/)
