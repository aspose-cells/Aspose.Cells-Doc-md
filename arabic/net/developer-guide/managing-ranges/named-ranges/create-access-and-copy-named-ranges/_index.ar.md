---
title: إنشاء الوصول ونسخ النطاقات المسماة
type: docs
weight: 200
url: /ar/net/create-access-and-copy-named-ranges/
---
## **مقدمة**

عادةً ، تُستخدم تسميات الأعمدة والصفوف للإشارة إلى الخلايا الفردية. من الممكن إنشاء أسماء وصفية لتمثيل الخلايا أو نطاقات الخلايا أو الصيغ أو القيم الثابتة. الكلمة**اسم** قد يشير إلى سلسلة من الأحرف التي تمثل خلية أو نطاق من الخلايا أو صيغة أو قيمة ثابتة. يعني تعيين اسم لنطاق أنه يمكن الإشارة إلى هذا النطاق من الخلايا باسمه. استخدم أسماء سهلة الفهم ، مثل المنتجات ، للإشارة إلى نطاقات يصعب فهمها ، مثل Sales! C20: C30. يمكن استخدام التسميات في الصيغ التي تشير إلى البيانات الموجودة في نفس ورقة العمل ؛ إذا كنت تريد تمثيل نطاق في ورقة عمل أخرى ، فيمكنك استخدام اسم. * تعد النطاقات المسماة من بين أقوى ميزات Microsoft Excel ، خاصة عند استخدامها كنطاق مصدر لعناصر تحكم القائمة والجداول المحورية والمخططات وما إلى ذلك.

## **العمل مع النطاق المحدد باستخدام Microsoft Excel**

### **إنشاء نطاقات مسماة**

 تصف الخطوات التالية كيفية تسمية خلية أو نطاق من الخلايا باستخدام**مايكروسوفت اكسل** . تنطبق هذه الطريقة على**Microsoft Office Excel 2003**, **Microsoft إكسل 97**, **2000** و**2002**.

1. حدد الخلية ، نطاق الخلايا التي تريد تسميتها.
1.  انقر على**مربع الاسم** في الطرف الأيسر من شريط الصيغة.
1. اكتب اسم الخلايا.
1. اضغط دخول.

{{% alert color="primary" %}}

لا يمكنك تسمية خلية أثناء تغيير محتويات الخلية.

{{% /alert %}}

## **العمل مع النطاق المحدد باستخدام Aspose.Cells**

هنا ، نستخدم Aspose.Cells API للقيام بالمهمة.
 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة.

### **إنشاء نطاق مسمى**

 من الممكن إنشاء نطاق مسمى عن طريق استدعاء overloaded[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. نسخة نموذجية من[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) تأخذ الطريقة المعلمات التالية:

- اسم الخلية اليسرى العلوية ، اسم الخلية اليسرى العلوية في النطاق.
- اسم الخلية اليمنى السفلية ، اسم الخلية اليمنى السفلية في النطاق.

 عندما[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) يتم استدعاء الأسلوب ، ويعيد النطاق الذي تم إنشاؤه حديثًا كمثيل لـ[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) صف دراسي. استخدم هذا[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) كائن لتكوين النطاق المسمى. على سبيل المثال ، قم بتعيين اسم النطاق باستخدام[**اسم**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) خاصية. يوضح المثال التالي كيفية إنشاء نطاق مسمى من الخلايا يمتد عبر B4: G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **أدخل البيانات في Cells في النطاق المحدد**

يمكنك إدراج البيانات في الخلايا الفردية للنطاق باتباع النمط

- **C#**: النطاق [الصف ، العمود]
- **VB**: النطاق (الصف والعمود)

لنفترض أن لديك نطاقًا مسمى من الخلايا يمتد من A1 إلى C4. تجعل المصفوفة 4 * 3 = 12 خلية. يتم ترتيب خلايا النطاق الفردية بالتسلسل: النطاق [0،0] ، النطاق [0،1] ، النطاق [0،2] ، النطاق [1،0] ، النطاق [1،1] ، النطاق [1،2] ، النطاق [2،0] ، النطاق [2،1] ، النطاق [2،2] ، النطاق [3،0] ، النطاق [3،1] ، النطاق [3،2].

استخدم الخصائص التالية لتحديد الخلايا الموجودة في النطاق:

- يُرجع FirstRow فهرس الصف الأول في النطاق المسمى.
- يُرجع FirstColumn فهرس العمود الأول في النطاق المسمى.
- يُرجع RowCount العدد الإجمالي للصفوف في النطاق المسمى.
- ColumnCount بإرجاع العدد الإجمالي للأعمدة في النطاق المسمى.

يوضح المثال التالي كيفية إدخال بعض القيم في خلايا نطاق محدد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **حدد Cells في النطاق المحدد**

يمكنك إدراج البيانات في الخلايا الفردية للنطاق باتباع النمط:

- **C#**: النطاق [الصف ، العمود]
- **VB**: النطاق (الصف والعمود)

إذا كان لديك نطاق مسمى يمتد من A1: C4. تجعل المصفوفة 4 * 3 = 12 خلية. يتم ترتيب خلايا النطاق الفردية بالتسلسل: النطاق [0،0] ، النطاق [0،1] ، النطاق [0،2] ، النطاق [1،0] ، النطاق [1،1] ، النطاق [1،2] ، النطاق [2،0] ، النطاق [2،1] ، النطاق [2،2] ، النطاق [3،0] ، النطاق [3،1] ، النطاق [3،2].

استخدم الخصائص التالية لتحديد الخلايا الموجودة في النطاق:

- يُرجع FirstRow فهرس الصف الأول في النطاق المسمى.
- يُرجع FirstColumn فهرس العمود الأول في النطاق المسمى.
- يُرجع RowCount العدد الإجمالي للصفوف في النطاق المسمى.
- ColumnCount بإرجاع العدد الإجمالي للأعمدة في النطاق المسمى.

يوضح المثال التالي كيفية إدخال بعض القيم في خلايا نطاق محدد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **الوصول إلى النطاقات المسماة**

#### **الوصول إلى نطاق مسمى معين**

 اتصل ب[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) المجموعة[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) طريقة للحصول على نطاق بالاسم المحدد. نموذجي[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) يأخذ الأسلوب اسم النطاق المسمى ويعيد النطاق المسمى المحدد كمثيل لـ[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) صف دراسي. يوضح المثال التالي كيفية الوصول إلى نطاق محدد من خلال اسمه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **الوصول إلى جميع النطاقات المسماة في جدول بيانات**

 اتصل ب[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) المجموعة[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) طريقة للحصول على جميع النطاقات المسماة في جدول بيانات. ال[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) تقوم الطريقة بإرجاع مصفوفة من كافة نطاقات الأسماء في ملف[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) مجموعة.

يوضح المثال التالي كيفية الوصول إلى كافة النطاقات المسماة في مصنف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **نسخ النطاقات المسماة**

 يوفر Aspose.Cells[**المدى. نسخ ()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) طريقة لنسخ نطاق من الخلايا بتنسيق في نطاق آخر.

يوضح المثال التالي كيفية نسخ نطاق مصدر من الخلايا إلى نطاق مسمى آخر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
