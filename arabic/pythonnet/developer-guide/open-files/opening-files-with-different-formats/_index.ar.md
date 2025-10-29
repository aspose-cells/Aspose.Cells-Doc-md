---
title: فتح الملفات بتنسيقات مختلفة
type: docs
weight: 30
url: /ar/python-net/opening-files-with-different-formats/
description: يتيح لك API الخاص بـ Aspose.Cells لـ Python via .NET فتح/قراءة تنسيقات مختلفة مثل XLSX، HTML، CSV، ODS، TSV، SXC، FODS، وغيرها.
keywords: فتح ملفات xlsx، فتح ملفات html، قراءة ملفات fods، قراءة ملفات ods، قراءة ملفات sxc، فتح ملفات csv، ملفات قيم منفصلة بواسطة الفاصلة، صيغة SpreadsheetML، tsv، mhtml
---

{{% alert color="primary" %}}

 باستخدام Aspose.Cells لـ Python via .NET يمكنك فتح ملفات بتنسيقات مختلفة. يدعم Aspose.Cells لـ Python via .NET مجموعة من تنسيقات الملفات مثل جداول بيانات إكسل (XLS، XLSX، XLSM، XLSB)، SpreadsheetML، قيم مفصولة بفواصل (CSV)، ملفات مفصولة بواسطة علامات تبويب (TSV) وغيرها.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة، يرجى الرجوع إلى الصفحات التالية:
[تنسيقات الملفات المدعومة](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **فتح الملفات بتنسيقات مختلفة**

 يسمح Aspose.Cells لـ Python via .NET للمطورين بفتح ملفات جداول البيانات بأشكال مختلفة مثل SpreadsheetML، قيم مفصولة بفواصل (CSV)، فواصل علامات التبويب أو قيم مفصولة بفواصل (TSV)، ملفات ODS. لفتح مثل هذه الملفات، يمكن للمطورين استخدام نفس المنهجية التي يستخدمونها لفتح ملفات إصدارات مختلفة من Microsoft Excel.

### **فتح ملفات SpreadsheetML**

ملفات SpreadsheetML هي تمثيلات XML لجداول البيانات تشمل جميع المعلومات حولها، مثل التنسيق، المعادلات إلخ. منذ Microsoft Excel XP تمت إضافة خيار تصدير XML إلى Microsoft Excel الذي يصدر جداول البيانات إلى ملفات SpreadsheetML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **فتح ملفات HTML**

 يسمح Aspose.Cells لـ Python via .NET لك بفتح ملف HTML وتحويله إلى كائن Workbook. يجب أن يكون ملف HTML موجهًا لبرنامج إكسل، بمعنى أن MS-Excel يجب أن يكون قادرًا على فتحه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **فتح ملفات CSV**

ملفات قيم مفصولة بفواصل (CSV) تحتوي على سجلات حيث تكون القيم مفصولة بفواصل. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود بحرف الفاصلة وتقوم بتقديمه بواسطة الرمز التنصيصي من خلال الرمز مزدوج التنصيص. إذا كانت قيمة الحقل تحتوي على رمز تنصيصي مزدوج فإنه يتم الخروج منها بزوج من الرموز المزدوجة للتنصيص. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **فتح ملفات CSV واستبدال الأحرف غير الصحيحة**

عند فتح ملف CSV في إكسل يحتوي على أحرف خاصة، يتم استبدال الأحرف تلقائيًا. يتم ذلك أيضًا بواسطة API الخاص بـ Aspose.Cells لـ Python via .NET والذي يظهر في المثال البرمجي أدناه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **فتح ملفات النصوص المفصولة بواسطة الألسنة**

يحتوي ملف النص المفصول بواسطة الألسنة على بيانات جدولية بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة مثلما يحدث في الجداول والأوراق الجدولية. بشكل أساسي، يعد ملف النص المفصول بواسطة الألسنة نوعًا خاصًا من ملفات النص البسيطة مع وجود فراغ بين كل عمود.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**

يحتوي ملف القيم المفصولة بواسطة الألسنة على بيانات جدولية بدون أي تنسيق. وهو نفس الشيء مع ملف النص المفصول بواسطة الألسنة، حيث تتم ترتيب البيانات في صفوف وأعمدة مثلما يحدث في الجداول والأوراق الجدولية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **فتح ملفات SXC**

 ستار أوفيس كالك مشابه لبرنامج إكسل من مايكروسوفت ويدعم الصيغ، والمخططات، والوظائف، والماكرو. تُحفظ جداول البيانات التي يتم إنشاؤها بهذا البرنامج بامتداد SXC. يُستخدم ملف SXC أيضًا لملفات جدول بيانات OpenOffice.org Calc. يمكن لـ Aspose.Cells لـ Python via .NET قراءة ملفات SXC كما هو موضح في عينة الكود التالية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **فتح ملفات FODS**

ملف FODS هو جدول بيانات محفوظ بصيغة OpenDocument XML بدون ضغط. يمكن لـ Aspose.Cells لـ Python via .NET قراءة ملفات FODS كما هو موضح في العينة التالية من الكود.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
