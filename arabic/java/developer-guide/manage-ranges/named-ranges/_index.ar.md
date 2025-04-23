---
title: النطاقات المسماة
type: docs
weight: 40
url: /ar/java/named-ranges/
---

{{% alert color="primary" %}} 

عادةً ما يتم استخدام تسميات الأعمدة والصفوف للإشارة إلى الخلايا الفردية. من الممكن إنشاء أسماء وصفية لتمثيل الخلايا، أو نطاقات من الخلايا، أو الصيغ، أو القيم الثابتة. يمكن أن يشير كلمة 'اسم' إلى سلسلة من الأحرف التي تمثل خليةً، أو نطاقًا من الخلايا، أو صيغةً، أو قيمةً ثابتة. يعني تخصيص اسم لنطاق أن هذا النطاق من الخلايا يمكن الإشارة إليه بواسطة اسمه. استخدم أسماء سهلة الفهم، مثل المنتجات، للاشارة الى النطاقات الصعبة الفهم، مثل الإيرادات!C20:C30. يمكن استخدام العلامات في الصيغ التي تشير إلى البيانات على نفس ورقة العمل. إذا كنت تريد تمثيل نطاق في ورقة عمل أخرى، فيمكنك استخدام اسم. *النطاقات المسماة من بين أقوى الميزات في مايكروسوفت إكسل، خصوصًا عند استخدامها كنطاق المصدر لضوابط القوائم، الجداول المحورية، الرسوم البيانية وغيرها.*

{{% /alert %}} 
## **إنشاء نطاق مسمى**
### **استخدام Microsoft Excel**
تصف الخطوات التالية كيفية تسمية خلية أو نطاق من الخلايا باستخدام Microsoft Excel. هذه الطريقة تنطبق على برنامج Microsoft Office Excel 2003، و Microsoft Excel 97، 2000 و 2002.

1. حدد الخلية أو نطاق الخلايا الذي تريد تسميته.
1. انقر فوق مربع الاسم في الطرف الأيسر من شريط الصيغة.
1. اكتب اسم الخلايا.
1. اضغط على ENTER.

{{% alert color="primary" %}} 

لا يمكنك تسمية خلية أثناء تغيير محتويات الخلية.

{{% /alert %}} 
### **استخدام Aspose.Cells**
هنا، نستخدم واجهة برمجة التطبيقات Aspose.Cells للقيام بالمهمة.

توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يُمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

من الممكن إنشاء نطاق مسمى عن طريق استدعاء النسخة المحملة فوق من طريقة [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) من مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ نسخة [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) النموذجية المعاملات التالية:

- اسم الخلية العلوي الأيمن، اسم الخلية العلوي الأيسر في النطاق.
- اسم الخلية السفلي الأيمن، اسم الخلية السفلي الأيمن في النطاق.

عند استدعاء طريقة [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-), فهي تعود بنطاق مسمى جديد ككائن من نوع [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

يوضح المثال التالي كيفية إنشاء نطاق مسمى من الخلايا التي تمتد من B4 إلى G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **الوصول إلى جميع النطاقات المسماة في ورق عمل**
اتصل بطريقة [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) من مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) للحصول على جميع النطاقات المسماة في جدول البيانات. تعود طريقة [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) بمصفوفة من جميع النطاقات المسماة في مجموعة الأوراق.

يوضح المثال التالي كيفية الوصول إلى جميع النطاقات المسماة في ورق عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **الوصول إلى نطاق مسمى محدد**
اتصل بطريقة [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) من مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) للحصول على نطاق معين بالاسم. تأخذ طريقة [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) النموذجية اسم النطاق المسمى وتعيد النطاق المسمى المحدد ككائن من نوع [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

يظهر المثال التالي كيفية الوصول إلى نطاق محدد بواسطة اسمه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **تحديد الخلايا في نطاق مسمى**
باستخدام Aspose.Cells, يمكنك إدخال البيانات في الخلايا الفردية في النطاق. فلنفترض أن لديك نطاقًا مسمى للخلايا.أي، A1:C4. لذلك تجعل المصفوفة 4 * 3 = 12 خلية وترتب الخلايا في النطاق المسمى بشكل متسلسل. يوفر Aspose.Cells بعض الخصائص المفيدة لفئة [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) للوصول إلى الخلايا الفردية في النطاق. يمكنك استخدام الطرق التالية لتحديد الخلايا في النطاق:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) تعيد فهرس الصف الأول في النطاق المسمى.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) تعيد فهرس العمود الأول في النطاق المسمى.

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **إدخال البيانات في الخلايا في النطاق المسمى**
باستخدام Aspose.Cells, يمكنك إدخال البيانات في الخلايا الفردية في النطاق. فلنفترض أن لديك نطاقًا مسمى للخلايا أي، H1:J4. لذلك تجعل المصفوفة 4 * 3 = 12 خلية وترتب الخلايا في النطاق المسمى بشكل متسلسل. يوفر Aspose.Cells بعض الخصائص المفيدة لفئة [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) للوصول إلى الخلايا الفردية في النطاق. يمكنك استخدام الخصائص التالية لتحديد الخلايا في النطاق:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) تعيد فهرس الصف الأول في النطاق المسمى.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) تعيد فهرس العمود الأول في النطاق المسمى.

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **تنسيق النطاقات...إعداد لون الخلفية وسمات الخط لنطاق مسمى**
لتطبيق التنسيق، قم بتعريف [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) لتحديد إعدادات النمط وتطبيقه على [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

يظهر المثال التالي كيفية تعيين لون تعبئة صلب (لون الظل) مع إعدادات الخط إلى نطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **تنسيق النطاقات...إضافة حدود إلى نطاق مسمى**
من الممكن إضافة حدود لنطاق من الخلايا بدلاً من خلية واحدة فقط. يوفر كائن [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) طريقة [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) التي تأخذ المعاملات التالية لإضافة حد إلى نطاق الخلايا:

- نمط الحد: نوع الحد، محدد من تعداد [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- لون الحد: لون الخط للحد، محدد من تعداد [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

يظهر المثال التالي كيفية تعيين حد للنطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


سيتم توليد الإخراج التالي بعد تنفيذ الشفرة أعلاه: 

![todo:image_alt_text](named-ranges_1.png)
#### **تطبيق النمط الى الخلايا في مجموعة**
أحيانًا، تريد إنشاء وتطبيق نمط على خلايا [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range). للقيام بذلك، يمكنك التكرار على الخلايا في النطاق واستخدام طريقة [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) لتطبيق النمط على الخلية.

المثال التالي يوضح كيفية تطبيق الأنماط على الخلايا في مجموعة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **إزالة نطاق مسمى**
يوفر Aspose.Cells طريقة [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt-int-) لمسح اسم النطاق. لمسح محتويات النطاق، استخدم طريقة [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange-com.aspose.cells.CellArea-) الخاصة بـ Aspose.Cells.
المثال التالي يوضح كيفية إزالة نطاق مسمى مع محتوياته.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
{{< app/cells/assistant language="java" >}}
