---
title: العمل مع خلايا GridWeb
type: docs
weight: 50
url: /ar/java/working-with-cells-gridweb/
---

## **الوصول إلى الخلايا في ورقة العمل**
تناول هذا الموضوع الخلايا، مع التركيز على الميزة الأساسية لـ GridWeb: الوصول إلى الخلايا.

تحتوي كل ورقة عمل على كائن GridCells، مجموعة من أجهزة GridCell. يمثل كائن GridCell خلية في Aspose.Cells.GridWeb. من الممكن الوصول إلى أي خلية باستخدام GridWeb. هناك طريقتان مفضلتان:

- [الوصول إلى الخلية عن طريق الاسم](/cells/ar/java/working-with-cells-gridweb/).
- [الوصول إلى الخلية عن طريق فهارس الصف والعمود](/cells/ar/java/working-with-cells-gridweb/).

أدناه موضوع كل نهج.
### **استخدام اسم الخلية**
تحتوي جميع الخلايا على اسم فريد. على سبيل المثال، A1، A2، B1، B2، إلخ. يسمح Aspose.Cells.GridWeb للمطورين بالوصول إلى أي خلية مطلوبة باستخدام اسم الخلية. ما عليك سوى تمرير اسم الخلية (كفهرس) إلى مجموعة GridCells لـ GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **استخدام فهرس الصف والعمود**
يمكن أيضًا التعرف على خلية من خلال موقعها من حيث فهارس الصف والعمود. ما عليك سوى تمرير فهارات الصف والعمود لخلية إلى مجموعة GridCells لـ GridWorksheet. هذا النهج أسرع من النهج الأول.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **الوصول وتعديل قيمة الخلية**
[وصول الخلايا في ورقة العمل](/cells/ar/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) ناقش وصول الخلايا. يوسع هذا الموضوع تلك النقاش ليظهر كيفية الوصول وتعديل قيم الخلايا باستخدام واجهة برمجة التطبيقات لـ GridWeb.
### **الوصول وتعديل قيمة الخلية**
#### **قيم السلاسل**
قبل الوصول وتعديل قيمة الخلية، تحتاج إلى معرفة كيفية الوصول إلى الخلايا. للحصول على تفاصيل حول النهج المختلفة للوصول إلى الخلايا، راجع [الوصول إلى الخلايا في ورقة العمل](/cells/ar/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

لكل خلية خاصية تسمى getStringValue(). بمجرد الوصول إلى خلية، يمكن للمطورين الوصول إلى طريقة getStringValue() للوصول إلى قيمة الخلية النصية.

{{% alert color="primary" %}} 

مهم: يمكن تخزين خمسة أنواع من القيم (Boolean, int, double, DateTime, and string) في الخلايا ولكن يمكن استخدام الطريقة(الطرق) getValue()/setValue() فقط للوصول/تعديل قيمة الكائن.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **جميع أنواع القيم**
توفر Aspose.Cells.GridWeb أيضًا طريقة خاصة، putValue، لكل خلية. باستخدام هذه الطريقة، من الممكن إدخال أو تعديل أي نوع من القيم (Boolean, int, double, DateTime, and string) في خلية.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



هناك أيضًا نسخة معبأة زائدة من طريقة putValue يمكنها أخذ أي نوع من القيم في تنسيق نصي وتحويلها إلى نوع بيانات صحيح تلقائيًا. للقيام بذلك، قم بتمرير قيمة Boolean true إلى معلمة أخرى من طريقة putValue كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **إضافة صيغ إلى الخلايا**
أهم الميزات التي يوفرها Aspose.Cells.GridWeb هي دعم الصيغ أو الوظائف. تحتوي Aspose.Cells.GridWeb على محرك الصيغ الخاص بها الذي يقوم بحساب الصيغ في أوراق العمل. يدعم Aspose.Cells.GridWeb الوظائف أو الصيغ الداخلية والمحددة من قبل المستخدمين. يناقش هذا الموضوع إضافة الصيغ إلى الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells.GridWeb بالتفصيل.
### **كيفية إضافة وحساب صيغة**
من الممكن إضافة، الوصول، وتعديل الصيغ في الخلايا باستخدام خاصية الصيغة للخلية. يدعم Aspose.Cells.GridWeb صيغ المعرفة من قبل المستخدم تتراوح بين البسيطة والمعقدة. ومع ذلك، يتم توفير عدد كبير من الدوال أو الصيغ المدمجة (مشابهة ل Microsoft Excel) أيضًا مع Aspose.Cells.GridWeb. لرؤية القائمة الكاملة للدوال المدمجة، يرجى الرجوع إلى [قائمة الدوال المدعمة.](/cells/ar/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

جب على بناء الصيغة أن تكون متوافقة مع بناء الصيغ في Microsoft Excel. على سبيل المثال، يجب أن تبدأ جميع الصيغ بعلامة يساوي (=).

لإضافة صيغة برمجياً، سيعترف Aspose.Cells.GridWeb بها كصيغة حتى إن لم تستخدم علامة '='، لكن إذا كان المستخدمين النهائيين يعملون على الواجهة الرسومية يجب عليهم استخدامها.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**تمت إضافة الصيغة إلى الخلية B3 ولكن لم يتم حسابها بواسطة GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

في اللقطة المتحركة أعلاه، يمكنك رؤية أن الصيغة قد تمت إضافتها إلى الخلية B3 ولم يتم حسابها بعد. لحساب جميع الصيغ، قم بنداء طريقة الحساب calculateFormula من مجموعة GridWorksheetCollection لعنصر تحكم GridWeb بعد إضافة الصيغ إلى ورق العمل كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

يمكن للمستخدمين أيضًا حساب الصيغ عن طريق النقر على **تقديم**.

**النقر على زر تقديم من GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**مهم**: إذا قام المستخدم بالنقر على **حفظ** أو **تراجع**, أو علامات علامات التبويب للصفحات، سيتم حساب جميع الصيغ تلقائيًا بواسطة GridWeb.

**نتيجة الصيغة بعد الحساب** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **الإشارة إلى الخلايا من أوراق عمل أخرى**
من خلال Aspose.Cells.GridWeb، يمكن الإشارة إلى القيم المخزنة في أوراق عمل مختلفة في صيغهم، مما يخلق صيغ معقدة.

الصيغة للإشارة إلى قيمة الخلية من ورقة عمل مختلفة هي اسم الورقة! اسم الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **إنشاء التحقق من البيانات في خلية من GridWeb**
يتيح Aspose.Cells.GridWeb لك إضافة 'التحقق من البيانات' باستخدام طريقة .add() GridWorksheet.getValidations(). باستخدام هذه الطريقة، يجب عليك تحديد 'نطاق الخلية'. ولكن إذا كنت ترغب في إنشاء التحقق من البيانات في خلية GridCell واحدة فقط يمكنك فعل ذلك مباشرة باستخدام طريقة GridCell.createValidation(). بالمثل، يمكنك إزالة 'التحقق من البيانات' من خلية الشبكة باستخدام طريقة GridCell.removeValidation().

الكود النموذجي التالي ينشئ **التحقق من البيانات** في خلية B3. إذا قمت بإدخال أي قيمة ليست بين 20 و 40، ستظهر خلية B3 **خطأ في التحقق** على شكل **XXXX أحمر** كما هو موضح في هذا اللقطة الشاشة.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **إنشاء أزرار أوامر مخصصة**
يحتوي Aspose.Cells.GridWeb على أزرار خاصة مثل 'إرسال'، 'حفظ'، و'تراجع'. كل هذه الأزرار تقوم بأداء مهام محددة لـ Aspose.Cells.GridWeb. كما أنه من الممكن إضافة أزرار مخصصة تقوم بأداء مهام مخصصة. يشرح هذا الموضوع كيفية استخدام هذه الميزة.

يشرح الكود المحدد أدناه كيفية إنشاء زر أمر مخصص وكيفية التعامل مع حدث النقر عليه. يمكنك استخدام أي رمز لأيقونتك المخصصة. لأغراض التوضيح، استخدمنا أيقونة الصورة هذه.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

كما ترون في اللقطة المتحركة التالية، عندما يقوم المستخدم بالنقر على زر الأمر المخصص، يتم إضافة نص في الخلية A1 قائلاً "لقد تم النقر على زر الأمر المخصص الخاص بي."

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **معالجة الأحداث لزر أمر مخصص**
يشرح الكود المحدد أدناه كيفية معالجة حدث زر الأمر المخصص.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **تهيئة الخلايا لـ GridWeb**
### **سيناريوهات الاستخدام المحتملة**
يدعم GridWeb الآن المستخدمين في إدخال بيانات الخلية بتنسيق النسبة مثل 3٪ وسيتم تنسيق البيانات في الخلية تلقائيًا كـ 3.00٪. ومع ذلك ، سيتعين عليك تعيين نمط الخلية إلى تنسيق النسبة وهو إما GridTableItemStyle.NumberType 9 أو 10. سيقوم الرقم 9 بتنسيق 3٪ كـ 3٪ ولكن الرقم 10 سيقوم بتنسيق 3٪ كـ 3.00٪.

{{% alert color="primary" %}} 

إذا لم تقم بتعيين نمط الخلية إلى تنسيق النسبة ، فسيتم عرض بيانات الإدخال 3٪ على أنه 0.03.

{{% /alert %}} 
### **إدخال بيانات الخلية لورقة العمل GridWeb بتنسيق النسبة**
الكود النموذجي التالي يضبط الخلية A1 GridTableItemStyle.NumberType كرقم 10، وبالتالي سيتم تنسيق بيانات الإدخال 3٪ تلقائياً كـ 3.00٪ كما هو موضح في اللقطة.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
