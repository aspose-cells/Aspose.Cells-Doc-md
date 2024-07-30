---
title: طرق مختلفة لحفظ الملفات
linktitle: حفظ الملفات
type: docs
weight: 40
url: /ar/net/different-ways-to-save-files/
description: يمكن لـAspose.Cells for .NET حفظ الملفات بتنسيقات مختلفة. حفظ الملفات إلى PDF. حفظ الملفات إلى HTML. حفظ الملفات إلى DOCX. حفظ الملفات إلى PPTX. حفظ الملفات إلى JSON. حفظ الملفات إلى MHTML.
keywords: ‏Aspose.Cells Save Excel إلى PDF، HTML، JSON، CSV، TXT، XML، DOCX، PPTX،‏ MHT، MHTML، وغيرها باستخدام C#، حفظ أو تحويلسجل عمل إلى PDF‏ HTML‏ JSON‏ TXT‏ SQL في C#.
---

{{% alert color="primary" %}}

‏تجعل Aspose.Cells من الممكن إنشاء الملفات وحفظها. يشرح هذا المقال الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel وتوفر الخصائص والطرق الضرورية للعمل مع ملفات Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) طريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) المستخدمة لحفظ ملفات Excel. تحتوي الطريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) على العديد من الأوزان المستخدمة لحفظ الملفات بطرق مختلفة.

يتم تقرير تنسيق الملف الذي يتم حفظ الملف إليه بواسطة تعداد [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat).

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|CSV|يمثل ملف CSV|
|Excel97To2003| يمثل ملف Excel 97-2003|
||Xlsx| يمثل ملف Excel 2007 XLSX|
||Xlsm| يمثل ملف Excel 2007 XLSM|
||Xltx| يمثل قالب Excel 2007 XLTX|
||Xltm| يمثل ملف Excel 2007 الممكن للتشغيل الآلي XLTM|
|Xlsb| يمثل ملف XLSB بتنسيق Excel 2007 الثنائي
|SpreadsheetML| يمثل ملف XML لجدول بيانات
|TSV|يمثل ملف قيم مفصولة بعلامة التبويب|
|TabDelimited|يمثل ملف نصي بقيم مفصولة بواسطة علامة التبويب|
|ODS|يمثل ملف ODS|
|Html| يمثل ملف HTML
|MHtml| يمثل ملف MHTML
|Pdf| يمثل ملف PDF
|XPS| يمثل مستند XPS
|TIFF| يمثل ملف TIFF

## **كيفية حفظ الملف بتنسيقات مختلفة**

لحفظ الملفات في موقع تخزين، حدد اسم الملف (مع المسار التخزيني الكامل) وتنسيق الملف المطلوب (من تعداد [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)) عند استدعاء طريقة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) للكائن [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **كيفية حفظ الكتاب الدراسي إلى صيغة PDF**
صيغة ملف الـ PDF هي نوع من المستندات التي تم إنشاؤها من قبل Adobe في تسعينيات القرن الماضي. الغرض من هذه الصيغة كان تقديم معيار لتمثيل المستندات والمواد المرجعية الأخرى في صيغة مستقلة من البرامج التطبيقية والأجهزة وكذلك نظام التشغيل. تحتوي صيغة ملف الـ PDF بالكامل على القدرة على استيعاب معلومات مثل النصوص والصور والروابط الفائقة وحقول النماذج ووسائط غنية والتواقيع الرقمية والمرفقات والبيانات الوصفية والميزات الجغرافية والأجسام ثلاثية الأبعاد التي يمكن أن تصبح جزءًا من المستند المصدر

تظهر الأكواد التالية كيفية حفظ الكتاب الدراسي كملف PDF باستخدام Aspose.Cells
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **كيفية حفظ الكتاب الدراسي إلى تنسيق نصي أو CSV**

في بعض الأحيان ، تريد تحويل أو حفظ دفتر عمل بعدة ورقات عمل إلى تنسيق نصي. بالنسبة لتنسيقات النص (مثل TXT، TabDelim، CSV، إلخ) ، يحفظ كل من Microsoft Excel وAspose.Cells افتراضيًا محتويات الورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك إلى CSV. افتراضيًا، [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) هي فاصلة، لذا لا تحدد فاصلة عند الحفظ بتنسيق CSV. يرجى ملاحظة: إذا كنت تستخدم النسخة التقييمية وحتى إذا تم تعيين خاصية [**TxtSaveOptions.ExportAllSheets**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/exportallsheets/) على القيمة true، فإن البرنامج سيقوم فقط بتصدير ورقة عمل واحدة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **كيفية حفظ ملف إلى ملفات نصية مع فاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **كيفية حفظ ملف إلى تيار**

لحفظ الملفات في تيار، أنشئ كائن *MemoryStream* أو *FileStream* واحفظ الملف في ذلك الكائن تيار عن طريق استدعاء طريقة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) للكائن [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index). حدد تنسيق الملف المطلوب باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) عند استدعاء الطريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **كيفية حفظ ملف إكسل إلى ملفات Html و Mht**
يمكن لـ Aspose.Cells ببساطة حفظ ملف إكسل، JSON، CSV أو ملفات أخرى التي يمكن تحميلها بواسطة Aspose.Cells كملفات .html و .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **كيفية حفظ ملف إكسل إلى OpenOffice (ODS, SXC, FODS, OTS)**
يمكننا حفظ الملفات في تنسيق مفتوح المكتب: ODS, SXC, FODS, OTS وغيرها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **كيفية حفظ ملف إكسل إلى JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف مفتوح المعايير لمشاركة البيانات التي تستخدم النص القابل للقراءة من قبل الإنسان لتخزين ونقل البيانات. يتم تخزين ملفات JSON باستخدام الامتداد .json. يتطلب JSON تنسيقًا أقل وهو بديل جيد لـ XML. يتم استخلاص JSON من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. تدعم العديد من لغات البرمجة الحديثة مولد وتجزئة JSON. application/json هو نوع الوسائط المستخدم لـ JSON.

تدعم Aspose.Cells حفظ الملفات في JSON أو XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **مواضيع متقدمة**
- [ضبط مستوى ضغط الورقة العمل](/cells/ar/net/adjust-workbook-compression-level/)
- [حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم](/cells/ar/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [حفظ الملف في كائن الاستجابة](/cells/ar/net/saving-file-to-response-object/)
