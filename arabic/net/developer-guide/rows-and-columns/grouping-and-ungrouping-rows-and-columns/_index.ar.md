---
title: تجميع الصفوف والأعمدة وإلغاء تجميعها
type: docs
weight: 50
url: /ar/net/grouping-and-ungrouping-rows-and-columns/
---
## **مقدمة**

في ملف Excel Microsoft ، يمكنك إنشاء مخطط تفصيلي للبيانات للسماح لك بإظهار مستويات التفاصيل وإخفائها بنقرة واحدة بالماوس.

 انقر على**رموز المخطط التفصيلي**، 1 ، 2 ، 3 ، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل فقط بسرعة ، أو يمكنك استخدام الرموز لمشاهدة التفاصيل ضمن ملخص فردي أو عنوان كما هو موضح أدناه في الشكل :

|**تجميع الصفوف والأعمدة.**|
|:- |
|![ما يجب القيام به: image_بديل_نص](grouping-and-ungrouping-rows-and-columns_1.png)|

## **إدارة المجموعة للصفوف والأعمدة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف إكسل Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل ، وقد تمت مناقشة القليل منها أدناه بمزيد من التفصيل.

### **تجميع الصفوف والأعمدة**

 من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء[**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) و[**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. تأخذ كلتا الطريقتين المعلمات التالية:

- أول صف / فهرس العمود ، أول صف أو عمود في المجموعة.
- فهرس الصف / العمود الأخير ، الصف أو العمود الأخير في المجموعة.
- مخفي ، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف / الأعمدة بعد التجميع أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **إعدادات المجموعة**

Microsoft يسمح لك Excel بتكوين إعدادات المجموعة لعرض:

- صفوف التلخيص أدناه التفاصيل.
- أعمدة التلخيص على يمين التفاصيل.

 يمكن للمطورين تكوين إعدادات المجموعة هذه باستخدام ملف[**الخطوط العريضة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي.

### **صفوف الملخص إلى أسفل التفاصيل**

 من الممكن التحكم في عرض صفوف التلخيص أدناه بالتفصيل عن طريق تعيين[**الخطوط العريضة**](https://reference.aspose.com/cells/net/aspose.cells/outline) صف دراسي'[**ملخص**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) الملكية ل**حقيقي** أو**خاطئة**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **أعمدة التلخيص إلى يمين التفاصيل**

 يمكن للمطورين أيضًا التحكم في عرض أعمدة الملخص على يمين التفاصيل عن طريق تعيين[**ملخص العمود**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) ممتلكات[**الخطوط العريضة**](https://reference.aspose.com/cells/net/aspose.cells/outline) الفئة الى**حقيقي** أو**خاطئة**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **فك تجميع الصفوف والأعمدة**

 لفك تجميع أي صفوف أو أعمدة مجمعة ، قم باستدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) و[**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)طُرق. تأخذ كلتا الطريقتين معلمتين:

- الصف الأول أو فهرس العمود ، الصف / العمود الأول المراد فك تجميعه.
- فهرس الصف أو العمود الأخير ، الصف / العمود الأخير المراد فك تجميعه.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) يحتوي على حمل زائد يأخذ المعلمة المنطقية الثالثة. ضبطه على**حقيقي**يزيل كافة المعلومات المجمعة. خلاف ذلك ، تتم إزالة معلومات المجموعة الخارجية فقط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
