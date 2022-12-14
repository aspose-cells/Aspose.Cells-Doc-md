---
title: فتح ملفات بتنسيقات مختلفة
type: docs
weight: 30
url: /ar/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API يسمح لك بفتح / قراءة تنسيقات مختلفة مثل XLSX ، HTML ، CSV ، ODS ، TSV ، SXC ، FODS ، إلخ.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 باستخدام Aspose.Cells يمكنك فتح الملفات بتنسيقات مختلفة.**Aspose.Cells** يمكن فتح مجموعة من تنسيقات الملفات مثل Microsoft جداول بيانات Excel (XLS ، و XLSX ، و XLSM ، و XLSB) ، و SpreadsheetML ، والقيم المفصولة بفواصل (CSV) ، أو ملفات مفصولة بعلامات جدولة أو قيم مفصولة بعلامات جدولة (TSV) وما إلى ذلك.

إذا كنت بحاجة إلى معرفة جميع تنسيقات الملفات المدعومة ، فيرجى الرجوع إلى الصفحات التالية:
[تنسيقات الملفات المدعومة](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **فتح ملفات بتنسيقات مختلفة**

يسمح Aspose.Cells للمطورين بفتح ملفات جداول البيانات بتنسيقات مختلفة مثل SpreadsheetML أو قيم مفصولة بفواصل (CSV) أو قيم مفصولة بعلامات جدولة أو قيم مفصولة بعلامات جدولة (TSV) أو ملفات ODS. لفتح مثل هذه الملفات ، يمكن للمطورين استخدام نفس المنهجية التي يستخدمونها لفتح ملفات إصدارات Excel Microsoft المختلفة.

### **فتح ملفات SpreadsheetML**

ملفات SpreadsheetML هي تمثيلات XML لجداول البيانات بما في ذلك جميع المعلومات عنها ، مثل التنسيق والصيغ وما إلى ذلك. منذ Microsoft Excel XP ، تمت إضافة خيار تصدير XML إلى Microsoft Excel الذي يقوم بتصدير جداول البيانات الخاصة بك إلى ملفات SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile.cpp" >}}

### **فتح ملفات HTML**

Aspose.Cells يسمح لك بفتح ملف HTML في كائن المصنف. يجب أن يكون ملف HTML Microsoft موجهًا لبرنامج Excel ، أي يجب أن يكون MS-Excel قادرًا على فتحه.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile.cpp" >}}

### **فتح ملفات CSV**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات حيث يتم فصل القيم بفاصلات. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود عن طريق الفاصلة ويتم اقتباسها بحرف اقتباس مزدوج. إذا احتوت قيمة الحقل على علامة اقتباس مزدوجة ، يتم تخطيها بزوج من علامات الاقتباس المزدوجة. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile.cpp" >}}

#### **فتح ملفات CSV واستبدال الأحرف غير الصالحة**

في Excel ، عند فتح ملف CSV بأحرف خاصة ، يتم استبدال الأحرف تلقائيًا. يتم القيام بنفس الشيء عن طريق Aspose.Cells API وهو موضح في مثال الكود الموضح أدناه.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters.cpp" >}}

يمكن تنزيل نموذج ملف المصدر من الروابط التالية لاختبار هذه الميزة.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **فتح ملفات نصية باستخدام فاصل مخصص**

تُستخدم الملفات النصية للاحتفاظ ببيانات جدول البيانات بدون تنسيق. الملف عبارة عن ملف نصي عادي يمكن أن يحتوي على بعض المحددات المخصصة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator.cpp" >}}

يمكن تنزيل نموذج ملف المصدر من الروابط التالية لاختبار هذه الميزة.

[CustomSeparator.txt](CustomSeparator.txt)

### **فتح ملفات محدده بعلامات تبويب**

يحتوي الملف المحدد بعلامات جدولة (نص) على بيانات جدول بيانات ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات. بشكل أساسي ، الملف المحدد بعلامات جدولة هو نوع خاص من ملفات النص العادي مع علامة تبويب بين كل عمود.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile.cpp" >}}

### **فتح ملفات قيم مفصولة بعلامات جدولة (TSV)**

يحتوي ملف القيم المفصولة بعلامات جدولة (TSV) على بيانات جدول بيانات ولكن بدون أي تنسيق. هو نفسه مع ملف محدد بعلامات جدولة حيث يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile.cpp" >}}

### **فتح ملفات SXC**

StarOffice Calc مشابه لـ Microsoft Excel ويدعم الصيغ والمخططات والوظائف ووحدات الماكرو. يتم حفظ جداول البيانات التي تم إنشاؤها باستخدام هذا البرنامج بامتداد SXC. يتم استخدام ملف SXC أيضًا لملفات جداول بيانات OpenOffice.org Calc. يمكن Aspose.Cells قراءة ملفات SXC كما هو موضح في نموذج التعليمات البرمجية التالي.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile.cpp" >}}

### **فتح ملفات FODS**

ملف FODS هو جدول بيانات محفوظ في OpenDocument XML دون أي ضغط. يمكن Aspose.Cells قراءة ملفات FODS كما هو موضح في نموذج التعليمات البرمجية التالي.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile.cpp" >}}
