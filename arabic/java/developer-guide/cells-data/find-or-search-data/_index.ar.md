---
title: البحث عن البيانات أو البحث
type: docs
weight: 120
url: /ar/java/find-or-search-data/
---

{{% alert color="primary" %}} 

في Microsoft Excel، يمكن للمستخدمين البحث عن الخلايا التي تحتوي على بيانات محددة. على سبيل المثال، بالنقر على **تحرير** ثم **العثور** يفتح مربع البحث. يدخل المستخدم قيمة وينقر على **موافق** للبحث عنها. يقوم Excel بتحديد الحقول المطابقة.

**استخدام مربع البحث للعثور على الخلايا التي تحتوي على قيمة معينة** 

![todo:image_alt_text](find-or-search-data_1.png)

في هذا المثال، قيمة البحث هي "البرتقال".

تسمح Aspose.Cells للمطورين بالبحث من خلال الخلايا في ورقة العمل للعثور على تلك التي تحتوي على قيمة معينة.

{{% /alert %}} 
## **العثور على الخلايا التي تحتوي على بيانات محددة**
توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، التي تمثل ملف Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)، وهي مجموعة تسمح بالوصول إلى كل ورقة العمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)، مجموعة تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) العديد من الأساليب للعثور على الخلايا في ورقة العمل التي تحتوي على بيانات تحددها المستخدم. يتم مناقشة بعض هذه الأساليب أدناه بتفصيل أكثر.

تُرجع جميع أساليب البحث مراجع الخلايا التي تحتوي على قيمة البحث المحددة.
## **البحث عن تحتوي على صيغة**
يمكن للمطورين العثور على صيغة محددة في ورقة العمل عن طريق استدعاء [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة البحث's [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))، ضبط [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) إلى [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) وتمريرها كمعلمة إلى الطريق [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)).

عادةً، تقبل طريق [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) معلمتين أو أكثر:

- الكائن المطلوب البحث عنه: يمثل كائنًا مطلوب العثور عليه في ورقة العمل.
- الخلية السابقة: تمثل الخلية السابقة بنفس الصيغة. يمكن تعيين هذا المعلمة على قيمة الفراغ عند البحث من البداية.
- خيارات البحث: تمثل معايير البحث. في الأمثلة أدناه ، يتم استخدام بيانات ورق العمل التالية لممارسة طرق البحث:

**بيانات ورق العمل العينة** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **البحث عن السلاسل**
البحث عن الخلايا التي تحتوي على قيمة نصية سهل ومرن. هناك طرق مختلفة للبحث ، على سبيل المثال ، البحث عن الخلايا التي تحتوي على سلاسل تبدأ بحرف معين أو مجموعة من الأحرف.
### **البحث عن السلاسل التي تبدأ بأحرف معينة**
للبحث عن الحرف الأول في سلسلة ، ادعوا مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) لل[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) الأسلوب ، ثم ضبط [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) إلى [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH) وتمريرها كمعلمة إلى [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) الأسلوب.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **البحث عن السلاسل التي تنتهي بأحرف محددة**
Aspose.Cells يمكن أيضًا العثور على السلاسل التي تنتهي بأحرف محددة. للبحث عن الأحرف الأخيرة في سلسلة ، ادعوا مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) لل[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) الأسلوب ، ثم ضبط [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) إلى [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH) وتمريرها كمعلمة إلى [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) الأسلوب.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **البحث بتعابير منتظمة: ميزة RegEx**
توفر التعبير المنتظم وسيلة موجزة ومرنة لمطابقة (تحديد واعتراف) سلاسل نصية ، مثل الأحرف الخاصة أو الكلمات أو الأنماط.

على سبيل المثال ، يطابق نمط التعبير المنتظم abc-*~~xyz~~ السلاسل "abc-123-xyz" ، "abc-985-xyz" و "abc-pony-xyz". العلامة * هي بطاقة وبالتالي يتطابق النمط مع أي سلاسل تبدأ بـ "abc" وتنتهي بـ "-xyz" ، بغض النظر عما إذا كانت الأحرف هي في الوسط.

Aspose.Cells تتيح لك البحث باستخدام التعابير المنتظمة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **مواضيع متقدمة**
- [العثور على الخلايا ذات النمط المحدد](/cells/ar/java/find-cells-with-specific-style/)
- [البحث عن البيانات باستخدام القيم الأصلية](/cells/ar/java/search-data-using-original-values/)
