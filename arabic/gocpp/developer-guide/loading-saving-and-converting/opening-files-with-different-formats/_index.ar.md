---
title: فتح الملفات بتنسيقات مختلفة
type: docs
weight: 30
url: /ar/go-cpp/opening-files-with-different-formats/

description: تتيح لك واجهة برمجة التطبيقات Aspose.Cells for .NET فتح/قراءة تنسيقات مختلفة مثل XLSX، HTML، CSV، ODS، TSV، SXC، FODS، إلخ.
keywords: فتح ملفات xlsx، فتح ملفات html، قراءة ملفات fods، قراءة ملفات ods، قراءة ملفات sxc، فتح ملفات csv، ملفات قيم منفصلة بواسطة الفاصلة، صيغة SpreadsheetML، tsv، mhtml
---

{{% alert color="primary" %}}

باستخدام Aspose.Cells، يمكنك فتح ملفات بصيغ مختلفة. يمكن لـ **Aspose.Cells** فتح مجموعة من صيغ الملفات مثل جداول بيانات Microsoft Excel (XLS، XLSX، XLSM، XLSB)، SpreadsheetML، قيم مفصولة بفواصل (CSV)، ملفات مرفوضة بواسطة جدول، ملفات مفصولة بواسطة علامات التبويب (TSV)، وغير ذلك.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة، يرجى الرجوع إلى الصفحات التالية:
[تنسيقات الملفات المدعومة](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **فتح الملفات بتنسيقات مختلفة**

يسمح Aspose.Cells للمطورين بفتح ملفات جدول بيانات بصيغ مختلفة مثل SpreadsheetML، القيم المفصولة بفواصل (CSV)، القيم المفصولة بواسطة علامات التبويب (TSV)، وملفات ODS. لفتح مثل هذه الملفات، يمكن للمطورين استخدام نفس المنهجية كما هو الحال لفتح ملفات بإصدارات مختلفة من Microsoft Excel.

### **فتح ملفات SpreadsheetML**

ملفات SpreadsheetML هي تمثيلات XML لجداول البيانات، تتضمن كل المعلومات عنها، مثل التنسيق، الصيغ، وغير ذلك. منذ إصدار Microsoft Excel XP، تمت إضافة خيار تصدير XML إلى Microsoft Excel يصدر جداول البيانات إلى ملفات SpreadsheetML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **فتح ملفات HTML**

تتيح Aspose.Cells لفتح ملف HTML في كائن Workbook. يجب أن يكون ملف HTML موجهًا لـ Microsoft Excel أي يجب أن تكون MS-Excel قادرة على فتحه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **فتح ملفات CSV**

ملفات قيم مفصولة بفواصل (CSV) تحتوي على سجلات حيث تكون القيم مفصولة بفواصل. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود بحرف الفاصلة وتقوم بتقديمه بواسطة الرمز التنصيصي من خلال الرمز مزدوج التنصيص. إذا كانت قيمة الحقل تحتوي على رمز تنصيصي مزدوج فإنه يتم الخروج منها بزوج من الرموز المزدوجة للتنصيص. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

#### **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**

في Excel ، عند فتح ملف CSV الذي يحتوي على أحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بالشيء نفسه بواسطة واجهة برمجة التطبيقات Aspose.Cells والتي يتم توضيحها في مثال الشيفرة المعطى أدناه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFileAndReplaceInvalidCharacters.go" >}}

يمكن تنزيل ملف المصدر العيني من الروابط التالية لاختبار هذه الميزة.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **فتح ملفات النصوص بفاصل مخصص**

تُستخدم ملفات النصوص لاحتواء البيانات الجدولية بدون تنسيق. هذا النوع من الملفات هو نوعٌ من ملفات النصوص البسيطة، وقد تحتوي على بعض محددات التجزئة المخصصة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

يمكن تنزيل ملفات المصدر النموذجية من الروابط التالية لاختبار هذه الميزة.

[CustomSeparator.txt](CustomSeparator.txt)

### **فتح ملفات النصوص المفصولة بواسطة الألسنة**

ملف القيم المفصولة بواسطة علامات التبويب (Text) يحتوي على بيانات جدول البيانات ولكن بدون أي تنسيق. يتم تنظيم البيانات في صفوف وأعمدة كما في الجداول وجداول البيانات. بشكل أساسي، ملف مفصول بواسطة علامة التبويب هو نوع خاص من ملفات النص العادي مع فاصلة علامات التبويب بين كل عمود.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**

ملف القيم المفصولة بواسطة علامات التبويب (TSV) يحتوي على بيانات جدول البيانات ولكن بدون أي تنسيق. هو نفس الملف المفصول بواسطة علامة التبويب حيث يتم تنظيم البيانات في صفوف وأعمدة كما في الجداول وجداول البيانات.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **فتح ملفات SXC**

StarOffice Calc مشابه لMicrosoft Excel ويدعم الصيغ والمخططات والوظائف والماكرو. يتم حفظ جداول البيانات التي تم إنشاؤها باستخدام هذا البرنامج بامتداد SXC. يُستخدم ملف SXC أيضًا لملفات جدول البيانات OpenOffice.org Calc. يمكن لـ Aspose.Cells قراءة ملفات SXC ، كما يتضح من عينة الكود التالية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **فتح ملفات FODS**

ملف FODS هو جدول بيانات محفوظ بتنسيق OpenDocument XML بدون ضغط. يمكن لـ Aspose.Cells قراءة ملفات FODS ، كما يتضح من عينة الكود التالية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
