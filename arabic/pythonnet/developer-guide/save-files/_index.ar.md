---
title: طرق مختلفة لحفظ الملفات
linktitle: حفظ الملفات
type: docs
weight: 40
url: /ar/python-net/different-ways-to-save-files/
description: يمكن لـ Aspose.Cells for Python via .NET حفظ الملفات إلى تنسيقات مختلفة. حفظ الملفات إلى PDF. حفظ الملفات إلى HTML. حفظ الملفات إلى DOCX. حفظ الملفات إلى PPTX. حفظ الملفات إلى JSON. حفظ الملفات إلى MHTML.
keywords: Aspose.Cells للبايثون via .NET حفظ إكسل إلى PDF و HTML و JSON و CSV و TXT و XML و DOCX و PPTX و MHT و MHTML وغيرها باستخدام C#، حفظ أو تحويل مصنف إلى PDF HTML JSON TXT SQL باستخدام C#.
---

{{% alert color="primary" %}}

يجعل Aspose.Cells for Python via .NET من الممكن إنشاء وحفظ الملفات. تشرح هذه المقالة الطرق المختلفة التي يمكن من خلالها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

يوفر Aspose.Cells for Python via .NET الخاصية [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Excel من مايكروسوفت وتوفر الخصائص والطرق اللازمة للعمل مع ملفات Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) الطريقة [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) المستخدمة لحفظ ملفات Excel. تحتوي طريقة [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) على العديد من الأحمال الزائدة المستخدمة لحفظ الملفات بطرق مختلفة.

يتم تقرير تنسيق الملف الذي يتم حفظ الملف إليه بواسطة تعداد [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat).

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

لحفظ الملفات في موقع تخزين، حدد اسم الملف (مع المسار التخزيني الكامل) وتنسيق الملف المطلوب (من تعداد [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)) عند استدعاء طريقة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) للكائن [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SavingFiletoSomeLocation-1.py" >}}

## **كيفية حفظ الكتاب الدراسي إلى صيغة PDF**
صيغة ملف الـ PDF هي نوع من المستندات التي تم إنشاؤها من قبل Adobe في تسعينيات القرن الماضي. الغرض من هذه الصيغة كان تقديم معيار لتمثيل المستندات والمواد المرجعية الأخرى في صيغة مستقلة من البرامج التطبيقية والأجهزة وكذلك نظام التشغيل. تحتوي صيغة ملف الـ PDF بالكامل على القدرة على استيعاب معلومات مثل النصوص والصور والروابط الفائقة وحقول النماذج ووسائط غنية والتواقيع الرقمية والمرفقات والبيانات الوصفية والميزات الجغرافية والأجسام ثلاثية الأبعاد التي يمكن أن تصبح جزءًا من المستند المصدر

يوضح الرمزان التاليان كيفية حفظ كتاب العمل كملف PDF باستخدام Aspose.Cells for Python via .NET:
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Save-As-Pdf.py" >}}

## **كيفية حفظ الكتاب الدراسي إلى تنسيق نصي أو CSV**

في بعض الأحيان ، ترغب في تحويل أو حفظ دفتر عمل يحتوي على أوراق عمل متعددة إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT ، TabDelim ، CSV ، وما إلى ذلك) ، فإن Microsoft Excel و Aspose.Cells لـ Python via .NET يحفظان افتراضيًا محتويات ورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل المثال نفسه لحفظ الملف بصيغة CSV. بشكل افتراضي، [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator) هو فاصلة، لذا لا تحدد فاصل إذا كنت تحفظ بصيغة CSV. يرجى ملاحظة: إذا كنت تستخدم النسخة التقييمية وحتى تم تعيين خاصية [**TxtSaveOptions.export_all_sheets**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/export_all_sheets/) إلى true، فإن البرنامج سيصدر ورقة عمل واحدة فقط.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToTextCSVFormat-1.py" >}}

## **كيفية حفظ ملف إلى ملفات نصية مع فاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-OpeningTextFilewithCustomSeparator-1.py" >}}


## **كيفية حفظ ملف إكسل إلى ملفات Html و Mht**
يمكن لـ Aspose.Cells for Python via .NET حفظ ملف Excel و JSON و CSV أو ملفات أخرى يمكن تحميلها بواسطة Aspose.Cells for Python via .NET كملفات .html و .mht بسهولة.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-MHTML.py" >}}


## **كيفية حفظ ملف إكسل إلى OpenOffice (ODS, SXC, FODS, OTS)**
يمكننا حفظ الملفات في تنسيق مفتوح المكتب: ODS, SXC, FODS, OTS وغيرها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-ODS.py" >}}

## **كيفية حفظ ملف إكسل إلى JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف مفتوح المعايير لمشاركة البيانات التي تستخدم النص القابل للقراءة من قبل الإنسان لتخزين ونقل البيانات. يتم تخزين ملفات JSON باستخدام الامتداد .json. يتطلب JSON تنسيقًا أقل وهو بديل جيد لـ XML. يتم استخلاص JSON من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. تدعم العديد من لغات البرمجة الحديثة مولد وتجزئة JSON. application/json هو نوع الوسائط المستخدم لـ JSON.

يدعم Aspose.Cells for Python via .NET حفظ الملفات إلى JSON أو XML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-JSON.py" >}}


## **مواضيع متقدمة**
- [ضبط مستوى ضغط الورقة العمل](/cells/ar/python-net/adjust-workbook-compression-level/)
- [حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم](/cells/ar/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/)

