---
title: إخفاء وعرض الصفوف والأعمدة
type: docs
weight: 50
url: /ar/java/hiding-and-showing-rows-and-columns/
---

## **مقدمة**
في بعض الأحيان، قد يكون من الضروري للمستخدمين إخفاء صفوف أو أعمدة معينة في ورقة العمل ثم عرضها لاحقًا. يوفر Microsoft Excel هذه الميزة وكذلك Aspose.Cells.
## **التحكم في رؤية الصفوف والأعمدة**
يوفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. يتم مناقشة بعض هذه الطرق أدناه.
### **إخفاء الصفوف أو الأعمدة**
يمكن للمطورين إخفاء صف أو عمود من خلال استدعاء طرق [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) و [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). كلا الطريقتين تأخذ مؤشر الصف أو العمود كمعامل لإخفاء الصف أو العمود المحدد.

{{% alert color="primary" %}} 

ملاحظة: من الممكن أيضًا إخفاء صف أو عمود إذا قمنا بتعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **عرض الصفوف والأعمدة**
يمكن للمطورين إلغاء إخفاء أي صف أو عمود مخفي عن طريق استدعاء طرق [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) و [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). كلا الطريقتين تأخذان معلمتين:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المخصص للصف أو العمود بعد عرضه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

أثناء جعل عمود/صف مخفي مرئيًا، إذا كنت بحاجة لاستعادته إلى العرض أو الارتفاع المخصص سابقًا، أو عرض العرض أو الارتفاع الأصلي، يرجى إظهار العمود أو الصف بعرض أو ارتفاع سلبي. على سبيل المثال، worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
