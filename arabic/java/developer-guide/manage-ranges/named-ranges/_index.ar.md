---
title: النطاقات المسماة
type: docs
weight: 40
url: /ar/java/named-ranges/
---
{{% alert color="primary" %}} 

عادةً ما يتم استخدام تسميات الأعمدة والصفوف للإشارة إلى الخلايا الفردية. من الممكن إنشاء أسماء وصفية لتمثيل الخلايا أو نطاقات الخلايا أو الصيغ أو القيم الثابتة. الكلمة**اسم** قد يشير إلى سلسلة من الأحرف التي تمثل خلية أو نطاق من الخلايا أو صيغة أو قيمة ثابتة. يعني تعيين اسم لنطاق أنه يمكن الإشارة إلى هذا النطاق من الخلايا باسمه. استخدم أسماء سهلة الفهم ، مثل المنتجات ، للإشارة إلى نطاقات يصعب فهمها ، مثل Sales! C20: C30. يمكن استخدام التسميات في الصيغ التي تشير إلى البيانات الموجودة في نفس ورقة العمل ؛ إذا كنت تريد تمثيل نطاق في ورقة عمل أخرى ، فيمكنك استخدام اسم. * تعد النطاقات المسماة من بين أقوى ميزات Microsoft Excel ، خاصة عند استخدامها كنطاق مصدر لعناصر تحكم القائمة والجداول المحورية والمخططات وما إلى ذلك.

{{% /alert %}} 
## **إنشاء نطاق مسمى**
### **باستخدام Microsoft إكسل**
تصف الخطوات التالية كيفية تسمية خلية أو نطاق من الخلايا باستخدام Microsoft Excel. تنطبق هذه الطريقة على Microsoft Office Excel 2003 و Microsoft Excel 97 و 2000 و 2002.

1. حدد الخلية ، نطاق الخلايا التي تريد تسميتها.
1. انقر فوق مربع الاسم في الطرف الأيسر من شريط الصيغة.
1. اكتب اسم الخلايا.
1. اضغط دخول.

{{% alert color="primary" %}} 

لا يمكنك تسمية خلية أثناء تغيير محتويات الخلية.

{{% /alert %}} 
### **باستخدام Aspose.Cells**
هنا ، نستخدم Aspose.Cells API للقيام بالمهمة.

 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة.

 من الممكن إنشاء نطاق مسمى عن طريق استدعاء overloaded[إنشاء المدى](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. نسخة نموذجية من[إنشاء المدى](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) تأخذ الطريقة المعلمات التالية:

- اسم الخلية العلوية اليمنى ، اسم الخلية العلوية اليسرى في النطاق.
- اسم الخلية اليمنى السفلية ، اسم الخلية اليمنى السفلية في النطاق.

 عندما[إنشاء المدى](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) ، تقوم بإرجاع النطاق المسمى الذي تم إنشاؤه حديثًا كمثيل لـ[نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/range) صف دراسي.

يوضح المثال التالي كيفية إنشاء نطاق مسمى من الخلايا يمتد عبر B4: G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **الوصول إلى كافة النطاقات المسماة في جدول بيانات**
 اتصل ب[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) طريقة ال[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) للحصول على جميع النطاقات المسماة في جدول بيانات. ال[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) يقوم الأسلوب بإرجاع مصفوفة من كافة النطاقات المسماة في ملف[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

يوضح المثال التالي كيفية الوصول إلى كافة النطاقات المسماة في مصنف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **الوصول إلى نطاق مسمى معين**
 اتصل ب[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) المجموعة[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) للحصول على نطاق محدد بالاسم. نموذجي[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) اسم النطاق المسمى ويعيد النطاق المسمى المحدد كمثيل لـ[نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/range)صف دراسي.

يوضح المثال التالي كيفية الوصول إلى نطاق محدد من خلال اسمه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **حدد Cells في نطاق مسمى**
باستخدام Aspose.Cells ، يمكنك ادراج البيانات في الخلايا الفردية للنطاق. افترض أن لديك نطاق مسمى من الخلايا ، a1: C4. لذا فإن المصفوفة ستجعل 4 * 3 = 12 خلية ويتم ترتيب خلايا النطاق الفردية بالتتابع. يوفر لك Aspose.Cells بعض الخصائص المفيدة لفئة [النطاق] (https://reference.aspose.com/cells/java/com.aspose.cells/range) للوصول إلى الخلايا الفردية في النطاق. يمكنك استخدام الطرق التالية لتحديد الخلايا في النطاق:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) إرجاع فهرس الصف الأول في النطاق المسمى.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)إرجاع فهرس العمود الأول في النطاق المسمى.

يوضح المثال التالي كيفية إدخال بعض القيم في خلايا نطاق محدد.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **أدخل البيانات في Cells في النطاق المحدد**
باستخدام Aspose.Cells ، يمكنك ادراج البيانات في الخلايا الفردية للنطاق. لنفترض أن لديك نطاقًا مسمى من الخلايا ، مثل H1: J4. لذا فإن المصفوفة ستجعل 4 * 3 = 12 خلية ويتم ترتيب خلايا النطاق الفردية بالتتابع. يوفر لك Aspose.Cells بعض الخصائص المفيدة لفئة [النطاق] (https://reference.aspose.com/cells/java/com.aspose.cells/range) للوصول إلى الخلايا الفردية في النطاق. يمكنك استخدام الخصائص التالية لتحديد الخلايا في النطاق:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)إرجاع فهرس الصف الأول في النطاق المسمى.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)إرجاع فهرس العمود الأول في النطاق المسمى.

يوضح المثال التالي كيفية إدخال بعض القيم في خلايا نطاق محدد.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **نطاقات التنسيق ... تعيين لون الخلفية وخصائص الخط إلى نطاق مسمى**
 لتطبيق التنسيق ، حدد ملف[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) لتحديد إعدادات النمط وتطبيقه على ملف[نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/range)هدف.

يوضح المثال التالي كيفية تعيين لون تعبئة خالص (لون التظليل) باستخدام إعدادات الخط إلى نطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **تنسيق النطاقات ... إضافة حدود إلى نطاق مسمى**
 من الممكن إضافة حدود إلى نطاق من الخلايا بدلاً من خلية واحدة فقط. ال[نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/range) كائن يوفر[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)طريقة تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:

-  borderStyle: نوع الحد المحدد من ملف[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)تعداد.
-  borderColor: لون خط الحد المحدد من ملف[اللون](https://reference.aspose.com/cells/java/com.aspose.cells/Color) تعداد.

يوضح المثال التالي كيفية تعيين حد مخطط إلى نطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 سيتم إنشاء المخرجات التالية بعد تنفيذ الكود أعلاه:

![ما يجب القيام به: image_بديل_نص](named-ranges_1.png)
#### **تطبيق النمط على الخلايا في نطاق**
في بعض الأحيان ، تريد إنشاء تطبيق نمط على الخلايا في ملف[نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/range) . لهذا ، يمكنك التكرار عبر الخلايا الموجودة في النطاق واستخدام الامتداد[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) طريقة لتطبيق النمط على الخلية.

يوضح المثال التالي كيفية تطبيق الأنماط على الخلايا في نطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **إزالة نطاق مسمى**
 يوفر Aspose.Cells ملف[NameCollection.RemoveAt ()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) طريقة لمسح اسم النطاق. لمسح محتويات النطاق ، استخدم[Cells. ClearRange ()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) طريقة.
يوضح المثال التالي كيفية إزالة نطاق مسمى بمحتوياته.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


ألوان الحدود
