---
title: فتح الملفات بتنسيقات مختلفة
type: docs
weight: 30
url: /ar/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API يسمح لك بفتح/قراءة صيغ مختلفة مثل XLSX، HTML، CSV، ODS، TSV، SXC، FODS، إلخ.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 باستخدام Aspose.Cells يمكنك فتح الملفات بتنسيقات مختلفة.**Aspose.Cells** يمكنه فتح مجموعة من تنسيقات الملفات مثل Microsoft جداول بيانات Excel (XLS، XLSX، XLSM، XLSB)، SpreadsheetML، قيم مفصولة بفواصل (CSV)، ملفات محددة بعلامات جدولة أو قيم مفصولة بعلامات جدولة (TSV) وما إلى ذلك.

إذا كنت تريد معرفة جميع تنسيقات الملفات المدعومة، فيرجى الرجوع إلى الصفحات التالية:
[تنسيقات الملفات المدعومة](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **فتح الملفات بتنسيقات مختلفة**

Aspose.Cells يسمح للمطورين بفتح ملفات جداول البيانات بتنسيقات مختلفة مثل SpreadsheetML، قيم مفصولة بفواصل (CSV)، قيم مفصولة بعلامات جدولة أو مفصولة بعلامات جدولة (TSV)، ملفات ODS. لفتح مثل هذه الملفات، يمكن للمطورين استخدام نفس المنهجية التي يستخدمونها لفتح ملفات إصدارات Excel المختلفة Microsoft.

###  **فتح SpreadsheetML الملفات**

ملفات SpreadsheetML هي تمثيلات XML لجداول البيانات بما في ذلك جميع المعلومات المتعلقة بها، مثل التنسيق والصيغ وما إلى ذلك. منذ Microsoft Excel XP، تمت إضافة خيار تصدير XML إلى Microsoft Excel الذي يصدر جداول البيانات الخاصة بك إلى SpreadsheetML ملفًا.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **فتح HTML الملفات**

Aspose.Cells يسمح لك بفتح ملف HTML في كائن المصنف. يجب أن يكون الملف HTML موجهًا لـ Excel، أي يجب أن يكون MS-Excel قادرًا على فتحه.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **فتح CSV الملفات**

تحتوي ملفات القيم المفصولة بفواصل (CSV) على سجلات يتم فيها فصل القيم بفواصل. يتم تخزين البيانات كجدول حيث يتم فصل كل عمود بحرف الفاصلة ويتم اقتباسه بواسطة حرف الاقتباس المزدوج. إذا كانت قيمة الحقل تحتوي على حرف اقتباس مزدوج، فسيتم تجاوزه بزوج من أحرف الاقتباس المزدوجة. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات جدول البيانات إلى CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **فتح ملفات CSV واستبدال الأحرف غير الصالحة**

في Excel، عند فتح ملف CSV بأحرف خاصة، يتم استبدال الأحرف تلقائيًا. ويتم نفس الشيء عن طريق Aspose.Cells API وهو موضح في مثال الكود الموضح أدناه.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

يمكن تنزيل نموذج الملف المصدر من الروابط التالية لاختبار هذه الميزة.

[InvalidCharacters.csv](InvalidCharacters.csv)

###  **فتح الملفات النصية باستخدام فاصل مخصص**

تُستخدم الملفات النصية للاحتفاظ ببيانات جدول البيانات بدون تنسيق. الملف هو نوع من الملفات النصية العادية التي يمكن أن تحتوي على بعض المحددات المخصصة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

يمكن تنزيل نموذج الملف المصدر من الروابط التالية لاختبار هذه الميزة.

[CustomSeparator.txt](CustomSeparator.txt)

###  **فتح الملفات المحددة بعلامات التبويب**

يحتوي الملف (النص) المحدد بعلامات جدولة على بيانات جدول بيانات ولكن بدون أي تنسيق. يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات. في الأساس، الملف المحدد بعلامات جدولة هو نوع خاص من الملفات النصية العادية مع وجود علامة تبويب بين كل عمود.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **فتح ملفات القيم المفصولة بعلامات التبويب (TSV).**

يحتوي ملف القيم المفصولة بعلامات جدولة (TSV) على بيانات جدول البيانات ولكن بدون أي تنسيق. إنه نفس الشيء مع ملف Tab Delimited حيث يتم ترتيب البيانات في صفوف وأعمدة كما هو الحال في الجداول وجداول البيانات.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **فتح SXC الملفات**

يشبه StarOffice Calc برنامج Excel Microsoft ويدعم الصيغ والمخططات والوظائف ووحدات الماكرو. يتم حفظ جداول البيانات التي تم إنشاؤها باستخدام هذا البرنامج بالملحق SXC. يتم استخدام الملف SXC أيضًا لملفات جداول بيانات OpenOffice.org Calc. يمكن لـ Aspose.Cells قراءة ملفات SXC كما هو موضح في نموذج التعليمات البرمجية التالي.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **فتح FODS الملفات**

الملف FODS هو جدول بيانات محفوظ في OpenDocument XML دون أي ضغط. يمكن لـ Aspose.Cells قراءة ملفات FODS كما هو موضح في نموذج التعليمات البرمجية التالي.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
