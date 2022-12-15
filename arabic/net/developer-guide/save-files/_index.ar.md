---
title: طرق مختلفة لحفظ الملفات
linktitle: احفظ الملفات
type: docs
weight: 40
url: /ar/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells يجعل من الممكن تكوين وحفظ الملفات. تشرح هذه المقالة الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

 يوفر Aspose.Cells ملف**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** والذي يمثل ملف Excel Microsoft ويوفر الخصائص والأساليب اللازمة للعمل مع ملفات Excel. ال**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** فئة توفر**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** الطريقة المستخدمة لحفظ ملفات Excel. ال**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**الأسلوب يحتوي على العديد من التحميلات الزائدة التي تُستخدم لحفظ الملفات بطرق مختلفة.

 يتم تحديد تنسيق الملف الذي تم حفظ الملف به بواسطة ملف**[SaveFormat] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**تعداد

|**أنواع تنسيق الملف**|**وصف**|
|:- |:- |
|CSV|يمثل ملف CSV|
|إكسل 97 إلى 2003|يمثل ملف Excel 97 - 2003|
|xlsx|يمثل ملف Excel 2007 XLSX|
|Xlsm|يمثل ملف Excel 2007 XLSM|
|Xltx|يمثل ملف Excel 2007 نموذج XLTX|
|Xltm|يمثل ملف XLTM ممكّن للماكرو في Excel 2007|
|Xlsb|يمثل ملف Excel 2007 ثنائي XLSB|
|SpreadsheetML|يمثل ملف جدول بيانات XML|
|ملف TSV|يمثل ملف قيم مفصولة بعلامات جدولة|
|علامة التبويب محدد|يمثل ملفًا نصيًا محددًا بعلامات جدولة|
|المواد المستنفدة للأوزون|يمثل ملف ODS|
|لغة البرمجة|يمثل ملف (ملفات) HTML|
|هتمل|يمثل ملف (ملفات) MHTML|
|بي دي إف|يمثل ملف PDF|
|XPS|يمثل مستند XPS|
|شجار|يمثل تنسيق ملف الصور ذي العلامات (TIFF)|

## **حفظ الملف كتنسيقات مختلفة**

 لحفظ الملفات في موقع تخزين ، حدد اسم الملف (مكتمل بمسار التخزين) وتنسيق الملف المطلوب (من ملف**[SaveFormat] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**تعداد) عند استدعاء**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** أشياء**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **حفظ المصنف كملف PDF**
تنسيق المستندات المحمولة (PDF) هو نوع من المستندات التي أنشأتها Adobe في التسعينيات. كان الغرض من تنسيق الملف هذا هو تقديم معيار لتمثيل المستندات والمواد المرجعية الأخرى بتنسيق مستقل عن برامج التطبيقات والأجهزة وكذلك نظام التشغيل. يتمتع تنسيق ملف PDF بالقدرة الكاملة على احتواء معلومات مثل النصوص والصور والارتباطات التشعبية وحقول النموذج والوسائط الغنية والتوقيعات الرقمية والمرفقات والبيانات الوصفية والميزات الجغرافية المكانية والكائنات ثلاثية الأبعاد الموجودة فيه والتي يمكن أن تصبح جزءًا من المستند المصدر.

توضح الرموز التالية كيفية حفظ workboook كملف pdf باستخدام Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **حفظ المصنف إلى نص أو تنسيق CSV**

في بعض الأحيان ، تريد تحويل مصنف أو حفظه باستخدام أوراق عمل متعددة إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT ، TabDelim ، CSV ، إلخ) ، افتراضيًا ، يتم حفظ محتويات ورقة العمل النشطة فقط Microsoft Excel و Aspose.Cells.

يوضح المثال التالي من التعليمات البرمجية كيفية حفظ مصنف بأكمله في تنسيق نصي. قم بتحميل المصنف المصدر الذي يمكن أن يكون أي ملف جدول بيانات Microsoft Excel أو OpenOffice (مثل XLS و XLSX و XLSM و XLSB و ODS وما إلى ذلك) بأي عدد من أوراق العمل.

عندما يتم تنفيذ الكود ، فإنه يحول بيانات جميع الأوراق في المصنف إلى تنسيق TXT.

 يمكنك تعديل نفس المثال لحفظ ملفك في CSV. بشكل افتراضي،**[TxtSaveOptions.Separator] (https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**هي فاصلة ، لذلك لا تحدد فاصلًا في حالة الحفظ بتنسيق CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **حفظ الملفات النصية باستخدام فاصل مخصص**

تحتوي الملفات النصية على بيانات جدول بيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **حفظ الملف في دفق**

 لحفظ الملفات في تدفق ، قم بإنشاء ملف*MemoryStream* أو*تيار ملف* الكائن وحفظ الملف إلى كائن الدفق هذا عن طريق استدعاء**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** أشياء**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** طريقة. حدد تنسيق الملف المطلوب باستخدام امتداد**[SaveFormat] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)** التعداد عند استدعاء**[حفظ] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **حفظ الملفات كملفات Html و Mht**
يمكن لـ Aspose.Cells ببساطة حفظ ملف Excel أو JSON أو CSV أو ملفات أخرى يمكن تحميلها بواسطة Aspose.Cells كملفات .html و .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **حفظ باسم OpenOffice (ODS، SXC، FODS، OTS)**
يمكننا حفظ الملفات على هيئة تنسيق مفتوح: ODS و SXC و FODS و OTS وما إلى ذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **حفظ ملف Excel بصيغة JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف قياسي مفتوح لمشاركة البيانات التي تستخدم نصًا يمكن للبشر قراءته لتخزين البيانات ونقلها. يتم تخزين ملفات JSON بامتداد .json. يتطلب JSON تنسيقًا أقل وهو بديل جيد لـ XML. JSON مشتق من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. يتم دعم إنشاء وتحليل JSON من قبل العديد من لغات البرمجة الحديثة. application / json هو نوع الوسائط المستخدم لـ JSON.

يدعم Aspose.Cells حفظ الملفات في JSON أو XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **موضوعات مسبقة**
- [ضبط مستوى ضغط المصنف](/cells/ar/net/adjust-workbook-compression-level/)
- [حفظ المصنف لتقييد تنسيق جدول بيانات XML المفتوح](/cells/ar/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [حفظ الملف إلى كائن الاستجابة](/cells/ar/net/saving-file-to-response-object/)
