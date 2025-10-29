---
title: طرق مختلفة لحفظ الملفات مع Golang عبر C++
linktitle: حفظ الملفات
type: docs
weight: 40
url: /ar/go-cpp/different-ways-to-save-files/
description: يستطيع Aspose.Cells for C++ حفظ الملفات إلى تنسيقات مختلفة. حفظ الملفات كملف PDF. حفظ الملفات كملف HTML. حفظ الملفات كملف DOCX. حفظ الملفات كملف PPTX. حفظ الملفات كملف JSON. حفظ الملفات كملف MHTML.
keywords: Aspose.Cells حفظ إكسل إلى PDF، HTML، JSON، CSV، TXT، XML، DOCX، PPTX، MHT، MHTML وغيرها باستخدام C++، حفظ أو تحويل دفتر العمل إلى PDF HTML JSON TXT SQL في C++.
---

{{% alert color="primary" %}}

‏تجعل Aspose.Cells من الممكن إنشاء الملفات وحفظها. يشرح هذا المقال الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)، التي تمثل ملف Microsoft Excel وتوفر الخصائص والطرق الضرورية للعمل مع ملفات Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) طريقة [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) المستخدمة لحفظ ملفات Excel. تحتوي الطريقة [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) على العديد من الأوزان المستخدمة لحفظ الملفات بطرق مختلفة.

يتم تقرير تنسيق الملف الذي يتم حفظ الملف إليه بواسطة تعداد [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/).

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

لحفظ الملفات في موقع تخزين، حدد اسم الملف (مع المسار التخزيني الكامل) وتنسيق الملف المطلوب (من تعداد [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/)) عند استدعاء طريقة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) للكائن [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles.go" >}}
## **كيفية حفظ الكتاب الدراسي إلى صيغة PDF**
صيغة ملف الـ PDF هي نوع من المستندات التي تم إنشاؤها من قبل Adobe في تسعينيات القرن الماضي. الغرض من هذه الصيغة كان تقديم معيار لتمثيل المستندات والمواد المرجعية الأخرى في صيغة مستقلة من البرامج التطبيقية والأجهزة وكذلك نظام التشغيل. تحتوي صيغة ملف الـ PDF بالكامل على القدرة على استيعاب معلومات مثل النصوص والصور والروابط الفائقة وحقول النماذج ووسائط غنية والتواقيع الرقمية والمرفقات والبيانات الوصفية والميزات الجغرافية والأجسام ثلاثية الأبعاد التي يمكن أن تصبح جزءًا من المستند المصدر

تظهر الأكواد التالية كيفية حفظ الكتاب الدراسي كملف PDF باستخدام Aspose.Cells
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-1.go" >}}
## **كيفية حفظ الكتاب الدراسي إلى تنسيق نصي أو CSV**

في بعض الأحيان ، تريد تحويل أو حفظ دفتر عمل بعدة ورقات عمل إلى تنسيق نصي. بالنسبة لتنسيقات النص (مثل TXT، TabDelim، CSV، إلخ) ، يحفظ كل من Microsoft Excel وAspose.Cells افتراضيًا محتويات الورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل المثال نفسه لحفظ الملف بصيغة CSV. بشكل افتراضي، [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) هو فاصلة، لذا لا تحدد فاصل إذا كنت تحفظ بصيغة CSV. يرجى ملاحظة: إذا كنت تستخدم النسخة التقييمية وحتى تم تعيين خاصية [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) إلى true، فإن البرنامج سيصدر ورقة عمل واحدة فقط.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-2.go" >}}
## **كيفية حفظ ملف إلى ملفات نصية مع فاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-3.go" >}}
## **كيفية حفظ ملف إلى تيار**

لحفظ الملفات في تيار، أنشئ كائن *MemoryStream* أو *FileStream* واحفظ الملف في ذلك الكائن تيار عن طريق استدعاء طريقة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) للكائن [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/). حدد تنسيق الملف المطلوب باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) عند استدعاء الطريقة [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-4.go" >}}
## **كيفية حفظ ملف إكسل إلى ملفات Html و Mht**
يمكن لـ Aspose.Cells ببساطة حفظ ملف إكسل، JSON، CSV أو ملفات أخرى التي يمكن تحميلها بواسطة Aspose.Cells كملفات .html و .mht.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-5.go" >}} 

## **كيفية حفظ ملف إكسل إلى OpenOffice (ODS, SXC, FODS, OTS)**
يمكننا حفظ الملفات في تنسيق مفتوح المكتب: ODS, SXC, FODS, OTS وغيرها.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-6.go" >}}
## **كيفية حفظ ملف إكسل إلى JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف مفتوح المعايير لمشاركة البيانات التي تستخدم النص القابل للقراءة من قبل الإنسان لتخزين ونقل البيانات. يتم تخزين ملفات JSON باستخدام الامتداد .json. يتطلب JSON تنسيقًا أقل وهو بديل جيد لـ XML. يتم استخلاص JSON من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. تدعم العديد من لغات البرمجة الحديثة مولد وتجزئة JSON. application/json هو نوع الوسائط المستخدم لـ JSON.

تدعم Aspose.Cells حفظ الملفات في JSON أو XML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-7.go" >}}

## **مواضيع متقدمة**
- [ضبط مستوى ضغط الورقة العمل](/cells/ar/cpp/adjust-workbook-compression-level/)
- [حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم](/cells/ar/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [حفظ الملف في كائن الاستجابة](/cells/ar/cpp/saving-file-to-response-object/)
