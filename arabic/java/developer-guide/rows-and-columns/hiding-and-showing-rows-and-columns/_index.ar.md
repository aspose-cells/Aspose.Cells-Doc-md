---
title: إخفاء وإظهار الصفوف والأعمدة
type: docs
weight: 50
url: /ar/java/hiding-and-showing-rows-and-columns/
---
## **مقدمة**
في بعض الأحيان ، قد يطلب المستخدمون أيضًا إخفاء صفوف أو أعمدة معينة من ورقة العمل ثم عرضها لاحقًا. يوفر Microsoft Excel هذه الميزة وكذلك Aspose.Cells.
## **التحكم في رؤية الصفوف والأعمدة**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة تمثل جميع الخلايا في ورقة العمل. ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. تمت مناقشة بعض هذه أدناه.
### **إخفاء الصفوف أو الأعمدة**
 يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء[HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) و[HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) طرق[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)جمع على التوالي. تأخذ كلتا الطريقتين فهرس الصف / العمود كمعامل لإخفاء الصف أو العمود المحدد.

{{% alert color="primary" %}} 

ملاحظة: من الممكن أيضًا إخفاء صف أو عمود إذا قمنا بتعيين ارتفاع الصف أو عرض العمود على 0 على التوالي.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **إظهار الصفوف والأعمدة**
 يمكن للمطورين إظهار أي صف أو عمود مخفي عن طريق استدعاء[UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) و[UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) طرق[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)جمع على التوالي. تأخذ كلتا الطريقتين معلمتين:

- **فهرس الصف أو العمود** - فهرس صف أو عمود يُستخدم لإظهار الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المخصص للصف أو العمود بعد عرضهما.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

أثناء جعل عمود / صف مخفي مرئيًا ، إذا كنت بحاجة إلى استعادته إلى العرض أو الارتفاع المعين مسبقًا ، أو عرضه أو ارتفاعه الأصليين ، فيرجى إظهار العمود أو الصف ذي العرض أو الارتفاع السالب. على سبيل المثال ، workheet.getCells (). unhideColumn (5، -1)

{{% /alert %}}
