---
title: ضبط ارتفاع الصف وعرض العمود
type: docs
weight: 10
url: /ar/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

عند العمل مع أوراق العمل وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج أحيانًا إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. أحيانًا، تعني تطبيق التنسيق على الصفوف أو الأعمدة أن ارتفاع الصف الحالي أو عرض العمود بحاجة إلى تغيير لعرض البيانات. عادةً ما يقوم المستخدمون بضبط ارتفاع الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام مايكروسوفت إكسل. ولكن مع Aspose.Cells، يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.

{{% /alert %}}

## **العمل مع الصفوف**

### **ضبط ارتفاع الصف**

يوفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Excel من Microsoft. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) تمكنك من الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. بعض هذه الطرق يُناقش أدناه بمزيد من التفصيل.

#### **تعيين ارتفاع الصف**

من الممكن تعيين ارتفاع صف واحد عن طريق استدعاء طريقة [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تأخذ طريقة [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) المعاملات التالية كما يلي:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **تعيين ارتفاع جميع الصفوف في ورقة العمل**

إذا كان المطورون بحاجة إلى تعيين ارتفاع الصف نفسه لجميع الصفوف في ورقة العمل، يمكنهم فعل ذلك باستخدام طريقة [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **العمل مع الأعمدة**

### **ضبط عرض العمود**

حدد عرض العمود عن طريق استدعاء طريقة [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تأخذ طريقة [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) المعاملات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, العرض المطلوب للعمود.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **تعيين عرض جميع الأعمدة في ورقة العمل**

لتعيين نفس عرض العمود لجميع الأعمدة في ورقة العمل، استخدم طريقة [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
