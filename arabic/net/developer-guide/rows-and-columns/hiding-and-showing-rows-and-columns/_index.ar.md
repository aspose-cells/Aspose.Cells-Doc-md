---
title: إخفاء وعرض الصفوف والأعمدة
type: docs
weight: 60
url: /ar/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

في بعض الأحيان، من المنطقي إخفاء بعض الصفوف أو الأعمدة في ورقة عمل وعرضها لاحقًا. يوفر Microsoft Excel هذه الميزة وكذلك Aspose.Cells.

{{% /alert %}}

## **التحكم في رؤية الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) يسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. يتم مناقشة بعض هذه الأساليب أدناه.

### **إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء طرق [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) و[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) على التوالي. تأخذ كلا الطريقين فهم فهرس الصف والعمود كمعلمة لإخفاء الصف أو العمود المحدد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

### **عرض الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء طرق [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) و[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) على التوالي. تأخذ كلا الطريقين معلمتين:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

أثناء جعل العمود المخفي مرئيًا، إذا كنت بحاجة إلى استعادته إلى العرض المعين سابقًا أو إلى عرضه الأصلي، يرجى عرض العمود بعرض سلبي. على سبيل المثال: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **إخفاء عدة صفوف وأعمدة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء طرق [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) و[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) على التوالي. تأخذ كلا الطريقين فهرس الصف أو العمود البدء وعدد الصفوف أو الأعمدة التي يجب إخفاؤها كمعلمات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) و[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) فئة [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) لجعل عدة صفوف وأعمدة مرئية.

{{% /alert %}}
