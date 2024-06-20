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
أبسط نهج لتحديد عرض وارتفاع الصف هو استدعاء أسلوب [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) في صف العمل [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). يأخذ أسلوب [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) مؤشر الصف (الذي سيتم تغيير حجمه) كمعامل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **تحديد الصف تلقائيًا في مجموعة من الخلايا**
يتألف الصف من العديد من الأعمدة. تسمح Aspose.Cells للمطورين بتحديد عرض الصف تلقائيًا بناءً على المحتوى في مجموعة من الخلايا ضمن الصف من خلال استدعاء الإصدارة المالإدلوجة لأسلوب [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)). يأخذ الأسلوب المالإدلوجي الباراميترات التالية:

- **فهرس الصف**, فهرس الصف المراد ضبطه تلقائياً.
- **فهرس العمود الأول**, فهرس العمود الأول للصف.
- **فهرس العمود الأخير**, فهرس العمود الأخير للصف.

يقوم الأسلوب [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) بفحص محتويات جميع الأعمدة في الصف ثم يلائم الصف تلقائيًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **تلائم العمود تلقائيًا - بسيط**
أسهل طريقة لتغيير حجم عرض وارتفاع العمود هي استدعاء الأسلوب [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). يأخذ الأسلوب [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) فهرس العمود (الذي سيتم تغيير حجمه) كمعلمة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **تلائم العمود في مجموعة من الخلايا**
يتكون العمود من العديد من الصفوف. من الممكن تلائم العمود تلقائيًا بناءً على المحتوى في مجموعة من الخلايا في العمود باستدعاء الإصدار المكدس من الأسلوب [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) الذي يأخذ المعلمات التالية:

- **فهرس العمود**, يمثل فهرس العمود الذي تحتاج محتوياته إلى التكيف تلقائيًا
- **فهرس الصف الأول**, يمثل فهرس الصف الأول للعمود
- **فهرس الصف الأخير**, يمثل فهرس الصف الأخير للعمود

يقوم الأسلوب [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) بفحص محتويات كافة الصفوف في العمود ثم يلائم العمود تلقائيًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **تلائم حجم الصفوف للخلايا المدمجة**
مع Aspose.Cells من الممكن تلائم الصفوف تلقائيًا حتى للخلايا التي تم دمجها باستخدام واجهة برمجة التطبيقات [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). يوفر فئة [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) الخاصية [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) التي يمكن استخدامها لتلائم الصفوف للخلايا المدمجة. تقبل [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) عضوًا قابلاً للتعداد [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) الذي يحتوي على الأعضاء التالية.

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): تجاهل الخلايا المدمجة.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): توسيع ارتفاع الصف الأول فقط.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): توسيع ارتفاع الصف الأخير فقط.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): توسيع ارتفاع كل صف على حدة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

يمكنك أيضًا استخدام الإصدارات المكدسة لأساليب [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) و [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) التي تقبل مجموعة من الصفوف/أعمدة ومثيلًا لـ [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) لتلائم الصفوف/أعمدة المحددة بتفاصيل [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) المطلوبة وفقًا لذلك.

توقيعات الأساليب المذكورة أعلاه كما يلي:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **مهم معرفته**
{{% alert color="primary" %}} 

إذا تم دمج الخلية, فإن طرق *AutoFit* لن يتم تطبيقها, وهذا هو نفس السلوك كما في Microsoft Excel. علاوة على ذلك, إذا كان النص في الخلية ملفوفا, فإن طريقة [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) لن يتم تطبيقها أيضا. شيء آخر يجب أن تعرفه هو أن طرق *AutoFit* تستغرق وقتا طويلا. لذلك, يجب أن تقوم بالاتصال بهذه الطرق بأقل قدر ممكن لضمان كفاءة تطبيقك.

{{% /alert %}}
