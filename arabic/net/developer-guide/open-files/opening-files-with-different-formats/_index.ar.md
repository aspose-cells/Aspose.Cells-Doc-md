---
title: فتح الملفات بتنسيقات مختلفة
type: docs
weight: 30
url: /ar/net/opening-files-with-different-formats/
description: تتيح لك واجهة برمجة التطبيقات Aspose.Cells for .NET فتح/قراءة تنسيقات مختلفة مثل XLSX، HTML، CSV، ODS، TSV، SXC، FODS، إلخ.
keywords: فتح ملفات xlsx، فتح ملفات html، قراءة ملفات fods، قراءة ملفات ods، قراءة ملفات sxc، فتح ملفات csv، ملفات قيم منفصلة بواسطة الفاصلة، صيغة SpreadsheetML، tsv، mhtml
---

{{% alert color="primary" %}}

باستخدام Aspose.Cells يمكنك فتح الملفات بتنسيقات مختلفة. Aspose.Cells يمكنها فتح مجموعة من تنسيقات الملفات مثل جداول بيانات Microsoft Excel (XLS، XLSX، XLSM، XLSB)، SpreadsheetML، قيم منفصلة بواسطة الفاصلة (CSV)، قيم منفصلة بواسطة الفاصلة أو الفواصل (TSV)، وغيرها إلخ.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة، يرجى الرجوع إلى الصفحات التالية:
[تنسيقات الملفات المدعومة](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **فتح الملفات بتنسيقات مختلفة**

تتيح Aspose.Cells للمطورين فتح ملفات جداول بيانات بتنسيقات مختلفة مثل SpreadsheetML، قيم منفصلة بواسطة الفاصلة (CSV)، قيم منفصلة بواسطة الفاصلة أو الفواصل (TSV)، ملفات ODS. يمكن للمطورين استخدام نفس المنهجية التي يستخدمونها لفتح ملفات إصدارات مختلفة من Microsoft Excel لفتح مثل تلك الملفات.

### **فتح ملفات SpreadsheetML**

ملفات SpreadsheetML هي تمثيلات XML لجداول البيانات تشمل جميع المعلومات حولها، مثل التنسيق، المعادلات إلخ. منذ Microsoft Excel XP تمت إضافة خيار تصدير XML إلى Microsoft Excel الذي يصدر جداول البيانات إلى ملفات SpreadsheetML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **فتح ملفات HTML**

تتيح Aspose.Cells لفتح ملف HTML في كائن Workbook. يجب أن يكون ملف HTML موجهًا لـ Microsoft Excel أي يجب أن تكون MS-Excel قادرة على فتحه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **فتح ملفات CSV**

ملفات قيم مفصولة بفواصل (CSV) تحتوي على سجلات حيث تكون القيم مفصولة بفواصل. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود بحرف الفاصلة وتقوم بتقديمه بواسطة الرمز التنصيصي من خلال الرمز مزدوج التنصيص. إذا كانت قيمة الحقل تحتوي على رمز تنصيصي مزدوج فإنه يتم الخروج منها بزوج من الرموز المزدوجة للتنصيص. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**

في Excel ، عند فتح ملف CSV الذي يحتوي على أحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بالشيء نفسه بواسطة واجهة برمجة التطبيقات Aspose.Cells والتي يتم توضيحها في مثال الشيفرة المعطى أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **استخدام محلل مفضل**

ليس من الضروري دائمًا استخدام إعدادات المحلل الافتراضية لفتح ملفات CSV. في بعض الأحيان ، لا ينشأ استيراد ملف CSV الإخراج المتوقع مثل تنسيق التاريخ ليس كما هو متوقع أو يتم التعامل بشكل مختلف مع الحقول الفارغة. يتوفر لهذا الغرض **TxtLoadOptions.PreferredParsers** لتوفير محلل مفضل خاص لتحليل أنواع بيانات مختلفة وفقًا للمتطلبات. يوضح الشيفرة التالية عينة عن استخدام المحلل المفضل.  

يمكن تنزيل ملف الشفرة المصدري وملفات الإخراج التجريبية من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **فتح ملفات النصوص بفاصل مخصص**

تُستخدم ملفات النصوص لاحتواء البيانات الجدولية بدون تنسيق. هذا النوع من الملفات هو نوعٌ من ملفات النصوص البسيطة، وقد تحتوي على بعض محددات التجزئة المخصصة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **فتح ملفات النصوص المفصولة بواسطة الألسنة**

يحتوي ملف النص المفصول بواسطة الألسنة على بيانات جدولية بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة مثلما يحدث في الجداول والأوراق الجدولية. بشكل أساسي، يعد ملف النص المفصول بواسطة الألسنة نوعًا خاصًا من ملفات النص البسيطة مع وجود فراغ بين كل عمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**

يحتوي ملف القيم المفصولة بواسطة الألسنة على بيانات جدولية بدون أي تنسيق. وهو نفس الشيء مع ملف النص المفصول بواسطة الألسنة، حيث تتم ترتيب البيانات في صفوف وأعمدة مثلما يحدث في الجداول والأوراق الجدولية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}

### **فتح ملفات SXC**

StarOffice Calc مماثل لـ Microsoft Excel ويدعم الصيغ والرسوم البيانية والوظائف والتوابع والماكرو. الجداول التي تم إنشاؤها باستخدام هذا البرنامج يتم حفظها بامتداد SXC.يُستخدم ملف SXC أيضاً لملفات جدول البيانات في OpenOffice.org Calc. يمكن لـ Aspose.Cells قراءة ملفات SXC كما هو موضح في الكود العيني التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **فتح ملفات FODS**

ملف FODS هو جدول بيانات محفوظ في تنسيق OpenDocument XML دون أي ضغط. يمكن لـ Aspose.Cells قراءة ملفات FODS كما هو موضح في الكود العيني التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
