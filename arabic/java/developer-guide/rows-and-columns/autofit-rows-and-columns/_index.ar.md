---
title: احتواء تلقائي للصفوف والأعمدة
type: docs
weight: 20
url: /ar/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

يوفر Microsoft Excel ميزة جيدة لتغيير الحجم التلقائي لعرض الخلية وارتفاعها وفقًا لمحتواها. هذه الميزة متاحة أيضًا لمستخدمي Aspose.Cells مع قوة التحجيم التلقائي لأبعاد الخلية في وقت التشغيل.

{{% /alert %}} 
## **تركيب تلقائي**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. تبحث هذه المقالة في استخدام[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)فئة للاحتواء التلقائي للصفوف أو الأعمدة.
### **صف الاحتواء التلقائي - بسيط**
 تتمثل الطريقة الأكثر مباشرة في تغيير حجم عرض الصف وارتفاعه تلقائيًا في استدعاء[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي'[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) طريقة. ال[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) تأخذ الطريقة فهرس الصف (للصف الذي سيتم تغيير حجمه) كمعامل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **صف الاحتواء التلقائي في نطاق Cells**
 يتكون الصف من عدة أعمدة. يسمح Aspose.Cells للمطورين بملاءمة صف تلقائيًا استنادًا إلى المحتوى في نطاق من الخلايا داخل الصف عن طريق استدعاء نسخة محملة بشكل زائد من[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) طريقة. يأخذ المعلمات التالية:

- **فهرس الصف**، فهرس الصف الذي سيتم تركيبه تلقائيًا.
- **فهرس العمود الأول**، فهرس العمود الأول للصف.
- **فهرس العمود الأخير**، فهرس العمود الأخير للصف.

 ال[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) يتحقق من محتويات جميع الأعمدة في الصف ثم يقوم تلقائيًا بملاءمة الصف.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **عمود الاحتواء التلقائي - بسيط**
 أسهل طريقة لتغيير حجم عرض العمود وارتفاعه تلقائيًا هي استدعاء ملف[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي'[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) طريقة. ال[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)الأسلوب يأخذ فهرس العمود (للعمود على وشك تغيير حجمه) كمعامل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **عمود الاحتواء التلقائي في نطاق Cells**
 يتكون العمود من عدة صفوف. من الممكن أن يتم احتواء عمود تلقائيًا استنادًا إلى المحتوى الموجود في نطاق من الخلايا في العمود عن طريق استدعاء نسخة محملة بشكل زائد من[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) الطريقة التي تأخذ المعلمات التالية:

- **فهرس العمود**، يمثل فهرس العمود الذي تحتاج محتوياته إلى الضبط التلقائي
- **فهرس الصف الأول**، يمثل فهرس الصف الأول من العمود
- **فهرس الصف الأخير**، يمثل فهرس الصف الأخير من العمود

 ال[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) يتحقق الأسلوب من محتويات جميع الصفوف في العمود ثم يقوم تلقائيًا بملاءمة العمود.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **صفوف AutoFit للدمج Cells**
مع Aspose.Cells ، من الممكن احتواء الصفوف تلقائيًا حتى للخلايا التي تم دمجها باستخدام[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)فئة تقدم[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)الخاصية التي يمكن استخدامها للاحتواء التلقائي للصفوف للخلايا المدمجة.[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)يقبل[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)معدود يضم الأعضاء التالية أسماؤهم.

- [لا أحد](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): تجاهل الخلايا المدمجة.
- [السطر الأول](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): يوسع ارتفاع الصف الأول فقط.
- [الخط الأخير](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): يوسع ارتفاع الصف الأخير فقط.
- [كل خط](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): يوسع ارتفاع كل صف فقط.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 يمكنك أيضًا استخدام الإصدارات المحملة بشكل زائد من[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [الأعمدة التلقائية](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) توابع تقبل نطاقًا من الصفوف / الأعمدة ومثيلًا لـ[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) لملاءمة الصفوف / الأعمدة المحددة تلقائيًا بالملف المطلوب[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)وفقاً لذلك.

تواقيع الطرق المذكورة هي كما يلي:

1.  autoFitRows (int startRow، int endRow،[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)والخيارات)
1.  autoFitColumns (int firstColumn ، int lastColumn ،[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)والخيارات)
## **من المهم أن تعرف**
{{% alert color="primary" %}} 

 إذا تم دمج خلية ثم*احتواء تلقائي* لن يتم تطبيق الأساليب ، وهو نفس السلوك كما في Microsoft Excel. علاوة على ذلك ، إذا تم التفاف النص الموجود في الخلية ، فسيتم تغليف ملف[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) لن يتم تطبيق الطريقة أيضًا. شيء آخر تحتاج إلى معرفته هو أن ملف*احتواء تلقائي*الأساليب تستغرق وقتًا طويلاً. لذلك ، يجب أن تسمي هذه الطرق نادرًا ما يكون ذلك ممكنًا لضمان كفاءة تطبيقك.

{{% /alert %}}
