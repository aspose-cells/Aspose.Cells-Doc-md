---
title: تناسب الصفوف والأعمدة تلقائيًا
type: docs
weight: 20
url: /ar/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

توفر Microsoft Excel ميزة جيدة لتحديد تلقائي لعرض وارتفاع الخلية وفقًا لمحتواها. يتوفر هذه الميزة أيضًا لمستخدمي Aspose.Cells مع قوة تحديد الأبعاد للخلية أثناء التشغيل.

{{% /alert %}} 
## **ضبط تلقائي**
توفر Aspose.Cells صفًا من الصفوف [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) تمثل ملف Microsoft Excel. يحتوي صف [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة الصف [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). يوفر صف [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة كبيرة من الخصائص والأساليب لإدارة ورقة العمل. يتناول هذا المقال استخدام صف [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) لتحديد تلقائي للصفوف أو الأعمدة.
### **ضبط تلقائي للصف - بسيط**
أبسط طريقة لضبط تلقائي لعرض وارتفاع الصف هي استدعاء طريقة [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) من فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). تأخذ طريقة [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) فهرس الصف (للصف الذي سيتم تغيير حجمه) كمعامل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **تحديد الصف تلقائيًا في مجموعة من الخلايا**
يتألف الصف من العديد من الأعمدة. يتيح Aspose.Cells للمطورين ضبط تلقائي لصف واحد استنادًا إلى المحتوى في نطاق من الخلايا داخل الصف عن طريق استدعاء نسخة محملة فوق من طريقة [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-). تأخذ هذه الطريقة المعاملات التالية:

- **فهرس الصف**, فهرس الصف المراد ضبطه تلقائياً.
- **فهرس العمود الأول**, فهرس العمود الأول للصف.
- **فهرس العمود الأخير**, فهرس العمود الأخير للصف.

تتحقق طريقة [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) من محتويات جميع الأعمدة في الصف ثم تقوم بضبط حجمه تلقائيًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **تلائم العمود تلقائيًا - بسيط**
أسهل طريقة لضبط تلقائي لعرض وارتفاع عمود هي استدعاء طريقة [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) من فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). تأخذ هذه الطريقة فهرس العمود (للعمود الذي سيتم تغيير حجمه) كمعامل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **تلائم العمود في مجموعة من الخلايا**
العمود يتكون من العديد من الصفوف. من الممكن ضبط تلقائي لعمود استنادًا إلى المحتوى في نطاق من الخلايا في العمود عن طريق استدعاء نسخة محملة فوق من طريقة [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) التي تأخذ المعاملات التالية:

- **فهرس العمود**, يمثل فهرس العمود الذي تحتاج محتوياته إلى التكيف تلقائيًا
- **فهرس الصف الأول**, يمثل فهرس الصف الأول للعمود
- **فهرس الصف الأخير**, يمثل فهرس الصف الأخير للعمود

تتحقق طريقة [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) من محتويات جميع الصفوف في العمود ثم تقوم بضبط عرضه تلقائيًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **تلائم حجم الصفوف للخلايا المدمجة**
مع Aspose.Cells من الممكن تلائم الصفوف تلقائيًا حتى للخلايا التي تم دمجها باستخدام واجهة برمجة التطبيقات [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). يوفر فئة [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) الخاصية [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) التي يمكن استخدامها لتلائم الصفوف للخلايا المدمجة. تقبل [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) عضوًا قابلاً للتعداد [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) الذي يحتوي على الأعضاء التالية.

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): تجاهل الخلايا المدمجة.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE): يوسع ارتفاع الصف الأول فقط.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE): يوسع ارتفاع الصف الأخير فقط.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE): يوسع ارتفاع كل صف فقط.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

يمكنك أيضًا استخدام النسخ الزائد من طرق [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) و [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--) التي تقبل نطاق الصفوف/الأعمدة ونسخة من [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) لضبط تلقائي للصفوف/الأعمدة المختارة مع خيارات [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) المرغوب فيها.

توقيعات الأساليب المذكورة أعلاه كما يلي:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **مهم معرفته**
{{% alert color="primary" %}} 

إذا تم دمج خلية، فلن يتم تطبيق طرق *AutoFit*، وهو نفس السلوك في Microsoft Excel. علاوة على ذلك، إذا كانت النص في خلية ملتفة، فلن يتم تطبيق طريقة [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-). شيء آخر عليك معرفته هو أن طرق *AutoFit* تستغرق وقتًا. لذلك، يجب استدعاؤها بأقل قدر ممكن لضمان كفاءة تطبيقك.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
