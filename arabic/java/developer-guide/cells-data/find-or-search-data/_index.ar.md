---
title: البحث عن البيانات أو البحث عنها
type: docs
weight: 120
url: /ar/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 في Microsoft Excel ، يمكن للمستخدمين البحث عن الخلايا التي تحتوي على بيانات محددة. على سبيل المثال ، النقر فوق**يحرر** وثم**تجد** يفتح مربع حوار البحث. يقوم المستخدمون بإدخال قيمة والنقرات**نعم** للبحث عنه. يبرز Excel الحقول المتطابقة.

**استخدام مربع الحوار "بحث" للعثور على الخلايا التي تحتوي على قيمة محددة** 

![ما يجب القيام به: image_بديل_نص](find-or-search-data_1.png)

في هذا المثال ، قيمة البحث هي "Oranges".

Aspose.Cells يسمح للمطورين بالبحث خلال الخلايا في ورقة العمل للعثور على تلك التي تحتوي على قيمة معينة.

{{% /alert %}} 
## **ايجاد Cells الذي يحتوي على بيانات محددة**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) ، يمثل ملف Excel. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) ، مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي.

 ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة تقدم[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) ، مجموعة تمثل جميع الخلايا في ورقة العمل[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)توفر المجموعة عدة طرق للبحث عن الخلايا في ورقة عمل تحتوي على بيانات محددة من قبل المستخدم. تتم مناقشة عدد قليل من هذه الأساليب أدناه بمزيد من التفصيل.

تُرجع جميع طرق البحث مراجع الخلايا لأي خلايا تحتوي على قيمة البحث المحددة.
## **البحث عن صيغة**
 يمكن للمطورين العثور على صيغة محددة في ورقة العمل عن طريق استدعاء[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[تجد](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) ) طريقة تحديد[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) إلى[LookInType.FormULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)وتمريره كمعامل إلى[تجد](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) طريقة.

 عادةً ما يكون ملف[تجد](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) يقبل الأسلوب معلمتين أو أكثر:

- كائن للبحث: يمثل كائنًا مطلوبًا للبحث عنه في ورقة العمل.
- Cell السابق: يمثل الخلية السابقة بنفس الصيغة. يمكن ضبط هذه المعلمة على قيمة خالية عند البحث من البداية.
- خيارات البحث: تمثل معايير البحث. في الأمثلة أدناه ، تُستخدم بيانات ورقة العمل التالية لممارسة طرق البحث:

**نموذج بيانات ورقة العمل** 

![ما يجب القيام به: image_بديل_نص](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **البحث عن سلاسل**
يعد البحث عن الخلايا التي تحتوي على قيمة سلسلة أمرًا سهلاً ومرنًا. توجد طرق مختلفة للبحث ، على سبيل المثال ، البحث عن الخلايا التي تحتوي على سلاسل تبدأ بحرف معين أو مجموعة من الأحرف.
### **البحث عن سلاسل تبدأ بأحرف معينة**
 للبحث عن الحرف الأول في السلسلة ، قم باستدعاء[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[تجد](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) الطريقة ، اضبط ملف[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) إلى[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)وتمريره كمعامل إلى[تجد](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **البحث عن سلاسل تنتهي بأحرف معينة**
 يمكن أن يقوم Aspose.Cells أيضًا بإيجاد سلاسل تنتهي بحروف معينة. للبحث عن الأحرف الأخيرة في السلسلة ، قم باستدعاء[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[تجد](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) الطريقة ، اضبط ملف[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) إلى[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)وتمريره كمعامل إلى[تجد](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **البحث باستخدام التعبيرات العادية: ميزة RegEx**
يوفر التعبير العادي وسيلة موجزة ومرنة لمطابقة (تحديد والتعرف على) سلاسل النص ، مثل أحرف أو كلمات أو أنماط معينة.

على سبيل المثال ، نمط التعبير العادي abc-* ~~ xyz ~~ تطابق السلاسل "abc-123-xyz" و "abc-985-xyz" و "abc-pony-xyz".* هي حرف بدل لذا فإن النمط يطابق أي سلاسل تبدأ بـ "abc" وتنتهي بـ "-xyz" ، بغض النظر عن الأحرف الموجودة في المنتصف.

يسمح لك Aspose.Cells بالبحث باستخدام التعابير النمطية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **موضوعات مسبقة**
- [ابحث عن خلايا ذات نمط محدد](/cells/ar/java/find-cells-with-specific-style/)
- [البحث في البيانات باستخدام القيم الأصلية](/cells/ar/java/search-data-using-original-values/)
