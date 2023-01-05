---
title: إخفاء وإظهار الصفوف والأعمدة
type: docs
weight: 60
url: /ar/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يكون من المنطقي إخفاء صفوف أو أعمدة معينة في ورقة عمل وعرضها لاحقًا. يوفر Microsoft Excel هذه الميزة وكذلك يفعل Aspose.Cells.

{{% /alert %}}

## **التحكم في رؤية الصفوف والأعمدة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) يسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة تمثل جميع الخلايا في ورقة العمل. ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. تمت مناقشة القليل من هذه أدناه.

### **إخفاء الصفوف والأعمدة**

 يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) و[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)جمع على التوالي. تأخذ كلتا الطريقتين فهرس الصف والعمود كمعامل لإخفاء الصف أو العمود المحدد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق ضبط ارتفاع الصف أو عرض العمود على 0 على التوالي.

{{% /alert %}}

### **إظهار الصفوف والأعمدة**

 يمكن للمطورين إظهار أي صف أو عمود مخفي عن طريق استدعاء[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) و[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)جمع على التوالي. تأخذ كلتا الطريقتين معلمتين:

- **فهرس الصف أو العمود** - فهرس صف أو عمود يُستخدم لإظهار الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المخصص للصف أو العمود بعد الإخفاء.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

أثناء جعل عمود مخفي مرئيًا ، إذا كنت بحاجة إلى استعادته إلى العرض المعين مسبقًا أو عرضه الأصلي ، فيرجى إظهار العمود بعرض سلبي. على سبيل المثال: ورقة عمل .Cells.UnhideColumn (5، -1)

{{% /alert %}}

### **إخفاء صفوف وأعمدة متعددة**

 يمكن للمطورين إخفاء صفوف أو أعمدة متعددة مرة واحدة عن طريق استدعاء[**إخفاء الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) و[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)جمع على التوالي. تأخذ كلتا الطريقتين صف البداية أو فهرس العمود وعدد الصفوف أو الأعمدة التي يجب إخفاؤها كمعلمات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 من الممكن أيضًا استخدام ملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) صف دراسي'[**إظهار الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) و[**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)طرق لإظهار العديد من الصفوف والأعمدة.

{{% /alert %}}
