---
title: فتح ملفات بتنسيقات مختلفة
type: docs
weight: 30
url: /ar/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API يسمح لك بفتح / قراءة تنسيقات مختلفة مثل XLSX ، HTML ، CSV ، ODS ، TSV ، SXC ، FODS ، إلخ.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 باستخدام Aspose.Cells يمكنك فتح الملفات بتنسيقات مختلفة.**Aspose.Cells** يمكن فتح مجموعة من تنسيقات الملفات مثل Microsoft جداول بيانات Excel (XLS ، XLSX ، XLSM ، XLSB) ، SpreadsheetML ، قيم مفصولة بفواصل (CSV) ، ملفات مفصولة بعلامات جدولة أو ملفات مفصولة بعلامات جدولة (TSV) إلخ.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة ، فيرجى الرجوع إلى الصفحات التالية:
[تنسيقات الملفات المدعومة](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **فتح ملفات بتنسيقات مختلفة**

Aspose.Cells يسمح للمطورين بفتح ملفات جداول البيانات بتنسيقات مختلفة مثل SpreadsheetML ، قيم مفصولة بفواصل (CSV) ، قيم مفصولة بعلامات جدولة أو قيم مفصولة بعلامات جدولة (TSV) ، ملفات ODS. لفتح مثل هذه الملفات ، يمكن للمطورين استخدام نفس المنهجية التي يستخدمونها لفتح ملفات مختلفة من إصدارات Microsoft Excel.

### **فتح SpreadsheetML الملفات**

ملفات SpreadsheetML عبارة عن تمثيلات XML لجداول البيانات بما في ذلك جميع المعلومات المتعلقة بها ، مثل التنسيق والصيغ وما إلى ذلك. منذ Microsoft Excel XP ، تمت إضافة خيار تصدير XML إلى Microsoft Excel الذي يقوم بتصدير جداول البيانات الخاصة بك إلى ملفات SpreadsheetML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **فتح HTML الملفات**

Aspose.Cells يسمح لك بفتح ملف HTML في كائن المصنف. يجب أن يكون الملف HTML موجهًا إلى Microsoft Excel ، أي يجب أن يكون MS-Excel قادرًا على فتحه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **فتح CSV الملفات**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات حيث يتم فصل القيم بفاصلات. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود عن طريق الفاصلة ويتم اقتباسها بحرف اقتباس مزدوج. إذا احتوت قيمة الحقل على علامة اقتباس مزدوجة ، يتم تخطيها بزوج من علامات الاقتباس المزدوجة. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **فتح CSV الملفات واستبدال الحروف غير الصالحة**

في Excel ، عند فتح ملف CSV بأحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بنفس الشيء بواسطة Aspose.Cells API والذي هو موضح في مثال الكود الموضح أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **استخدام المحلل اللغوي المفضل**

هذا ليس ضروريًا دائمًا لاستخدام إعدادات المحلل اللغوي الافتراضية لفتح ملفات CSV. في بعض الأحيان ، لا يؤدي استيراد ملف CSV إلى إنشاء الإخراج المتوقع مثل تنسيق التاريخ ليس كما هو متوقع أو يتم التعامل مع الحقول الفارغة بشكل مختلف. لهذا الغرض**TxtLoadOptions.PreferredParsers**متاح لتوفير المحلل اللغوي المفضل لتحليل أنواع البيانات المختلفة حسب المتطلبات. يوضح نموذج التعليمات البرمجية التالي استخدام المحلل اللغوي المفضل.

يمكن تنزيل نموذج ملف المصدر وملفات الإخراج من الروابط التالية لاختبار هذه الميزة.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **فتح ملفات نصية باستخدام فاصل مخصص**

تُستخدم الملفات النصية للاحتفاظ ببيانات جدول البيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **فتح ملفات محدده بعلامات تبويب**

يحتوي الملف المحدد بعلامات جدولة (نص) على بيانات جدول بيانات ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات. بشكل أساسي ، الملف المحدد بعلامات جدولة هو نوع خاص من ملفات النص العادي مع علامة تبويب بين كل عمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **فتح ملفات قيم مفصولة بعلامات جدولة (TSV)**

يحتوي ملف القيم المفصولة بعلامات جدولة (TSV) على بيانات جدول بيانات ولكن بدون أي تنسيق. هو نفسه مع ملف محدد بعلامات جدولة حيث يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}

### **فتح SXC الملفات**

StarOffice Calc مشابه لـ Microsoft Excel ويدعم الصيغ والمخططات والوظائف ووحدات الماكرو. يتم حفظ جداول البيانات التي تم إنشاؤها باستخدام هذا البرنامج بالملحق SXC. يتم استخدام ملف SXC أيضًا لملفات جداول بيانات OpenOffice.org Calc. يمكن Aspose.Cells قراءة ملفات SXC كما هو موضح في نموذج التعليمات البرمجية التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **فتح FODS الملفات**

الملف FODS هو جدول بيانات محفوظ في OpenDocument XML بدون أي ضغط. يمكن لـ Aspose.Cells قراءة ملفات FODS كما هو موضح في نموذج التعليمات البرمجية التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

