---
title: العمل مع Cells GridWeb
type: docs
weight: 50
url: /ar/java/working-with-cells-gridweb/
---
## **الوصول إلى Cells في ورقة العمل**
يناقش هذا الموضوع الخلايا ، ويبحث في الميزة الأساسية لـ GridWeb: الوصول إلى الخلايا.

تحتوي كل ورقة عمل على كائن GridCells ، وهو مجموعة من كائنات GridCell. يمثل كائن GridCell خلية في Aspose.Cells.GridWeb. من الممكن الوصول إلى أي خلية باستخدام GridWeb. هناك طريقتان مفضلتان:

- [الوصول إلى الخلية بالاسم](/cells/ar/java/working-with-cells-gridweb/).
- [الوصول إلى الخلية عن طريق فهارس الصفوف والأعمدة](/cells/ar/java/working-with-cells-gridweb/).

أدناه ، تتم مناقشة كل نهج.
### **باستخدام Cell الاسم**
جميع الخلايا لها اسم فريد. على سبيل المثال ، A1 ، A2 ، B1 ، B2 ، إلخ. Aspose.Cells.GridWeb يسمح للمطورين بالوصول إلى أي خلية مرغوبة باستخدام اسم الخلية. ما عليك سوى تمرير اسم الخلية (كمؤشر) إلى مجموعة GridCells من GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **استخدام فهارس الصفوف والعمود**
يمكن أيضًا التعرف على الخلية من خلال موقعها من حيث فهارس الصفوف والأعمدة. ما عليك سوى تمرير فهارس الصفوف والأعمدة الخاصة بالخلية إلى مجموعة GridCells من GridWorksheet. هذا النهج أسرع من الأسلوب أعلاه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **الوصول إلى وتعديل قيمة Cell**
[الوصول إلى Cells في ورقة العمل](/cells/ar/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) ناقش الوصول إلى الخلايا. يوسع هذا الموضوع المناقشة لإظهار كيفية الوصول إلى قيم الخلايا وتعديلها باستخدام GridWeb API.
### **الوصول إلى قيمة Cell وتعديلها**
#### **قيم السلسلة**
 قبل الوصول إلى قيمة الخلية وتعديلها ، تحتاج إلى معرفة كيفية الوصول إلى الخلايا. للحصول على تفاصيل حول الأساليب المختلفة للوصول إلى الخلايا ، يرجى الرجوع إلى[الوصول إلى Cells في ورقة العمل](/cells/ar/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

تحتوي كل خلية على خاصية تسمى getStringValue (). بمجرد الوصول إلى الخلية ، يمكن للمطورين الوصول إلى طريقة getStringValue () للوصول إلى قيمة سلسلة الخلايا.

{{% alert color="primary" %}} 

هام: يمكن تخزين خمسة أنواع من القيم (Boolean و int و double و DateTime و string) في الخلايا ولكن لا يمكن استخدام طريقة (أساليب) getValue () / setValue () إلا للوصول إلى قيمة الكائن / تعديلها.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **جميع أنواع القيم**
Aspose.Cells.GridWeb يوفر أيضًا طريقة خاصة ، putValue ، لكل خلية. باستخدام هذه الطريقة ، من الممكن إدراج أو تعديل أي نوع من القيم (Boolean و int و double و DateTime و string) في خلية.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



هناك أيضًا نسخة محملة بشكل زائد من طريقة putValue يمكن أن تأخذ أي نوع من القيمة في تنسيق سلسلة وتحويلها إلى نوع بيانات مناسب تلقائيًا. لتحقيق ذلك ، مرر القيمة المنطقية "صواب" إلى معلمة أخرى لطريقة putValue كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **إضافة الصيغ إلى Cells**
الميزة الأكثر قيمة التي يقدمها Aspose.Cells.GridWeb هي دعم الصيغ أو الوظائف. Aspose.Cells.GridWeb له Formula Engine الخاص به الذي يحسب الصيغ في أوراق العمل. Aspose.Cells.GridWeb يدعم كلا من الوظائف أو الصيغ المضمنة والمعرفة من قبل المستخدم. يناقش هذا الموضوع إضافة الصيغ إلى الخلايا باستخدام Aspose.Cells.GridWeb API بالتفصيل.
### **كيف تضيف وتحسب صيغة؟**
 من الممكن إضافة الصيغ والوصول إليها وتعديلها في الخلايا باستخدام خاصية الصيغة للخلية. Aspose.Cells.GridWeb يدعم الصيغ المعرفة من قبل المستخدم والتي تتراوح من البسيط إلى المعقد. ومع ذلك ، يتم أيضًا توفير عدد كبير من الوظائف أو الصيغ المضمنة (على غرار Microsoft Excel) مع Aspose.Cells.GridWeb. للاطلاع على القائمة الكاملة للوظائف المضمنة ، يرجى الرجوع إلى هذا[قائمة الوظائف المدعومة.](/cells/ar/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

يجب أن يكون بناء جملة الصيغة متوافقًا مع بناء جملة Microsoft Excel. على سبيل المثال ، يجب أن تبدأ جميع الصيغ بعلامة يساوي (=).

لإضافة صيغة برمجيًا ، سيتعرف عليها Aspose.Cells.GridWeb كصيغة حتى إذا لم تستخدم علامة ** = ** ، ولكن إذا كان يجب على المستخدمين النهائيين الذين يعملون في واجهة المستخدم الرسومية استخدامها.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**تمت إضافة الصيغة إلى خلية B3 ولكن لم يتم حسابها بواسطة GridWeb** 

![ما يجب القيام به: image_بديل_نص](working-with-cells-gridweb_1.png)

في لقطة الشاشة أعلاه ، يمكنك أن ترى أنه تمت إضافة صيغة إلى B3 ولكن لم يتم حسابها بعد. لحساب جميع الصيغ ، قم باستدعاء أسلوب GridWorksheetCollection's calculateFormula الخاص بعنصر التحكم GridWeb بعد إضافة الصيغ إلى أوراق العمل كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

 يمكن للمستخدمين أيضًا حساب الصيغ بالنقر فوق**يُقدِّم**.

**النقر فوق الزر إرسال من GridWeb** 

![ما يجب القيام به: image_بديل_نص](working-with-cells-gridweb_2.png)

**الأهمية** : إذا قام المستخدم بالنقر فوق**يحفظ** أو**الغاء التحميل** الأزرار ، أو علامات تبويب الأوراق ، يتم حساب جميع الصيغ بواسطة GridWeb تلقائيًا.

**نتيجة الصيغة بعد الحساب** 

![ما يجب القيام به: image_بديل_نص](working-with-cells-gridweb_3.png)
### **الرجوع إلى Cells من أوراق العمل الأخرى**
باستخدام Aspose.Cells.GridWeb ، من الممكن الإشارة إلى القيم المخزنة في أوراق عمل مختلفة في صيغها ، وإنشاء صيغ معقدة.

بناء الجملة للإشارة إلى قيمة خلية من ورقة عمل مختلفة هو اسم الورقة! اسم الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **إنشاء التحقق من صحة البيانات في GridCell من GridWeb**
 Aspose.Cells.GridWeb يسمح لك بإضافة ملفات**تأكيد صحة البيانات** باستخدام طريقة GridWorksheet.getValidations (). add (). باستخدام هذه الطريقة ، يجب عليك تحديد**نطاق Cell** . ولكن إذا كنت ترغب في إنشاء التحقق من صحة البيانات في GridCell واحدة ، فيمكنك القيام بذلك مباشرةً باستخدام طريقة GridCell.createValidation (). وبالمثل ، يمكنك إزالة ملفات**تأكيد صحة البيانات** من GridCell باستخدام أسلوب GridCell.removeValidation ().

 يقوم نموذج التعليمات البرمجية التالي بإنشاء ملف**تأكيد صحة البيانات** في الخلية B3. إذا أدخلت أي قيمة ليست بين 20 و 40 ، فستظهر الخلية B3**خطئ في التحقق** في شكل**أحمر XXXX** كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **إنشاء أزرار أوامر مخصصة**
Aspose.Cells.GridWeb يحتوي على أزرار خاصة مثل إرسال وحفظ وتراجع. كل هذه الأزرار تؤدي مهام محددة لـ Aspose.Cells.GridWeb. من الممكن أيضًا إضافة أزرار مخصصة تؤدي مهامًا مخصصة. يشرح هذا الموضوع كيفية استخدام هذه الميزة.

يوضح نموذج التعليمات البرمجية التالي كيفية إنشاء زر أمر مخصص وكيفية معالجة حدث النقر الخاص به. يمكنك استخدام أي رمز لزر الأمر المخصص الخاص بك. لغرض التوضيح ، استخدمنا أيقونة الصورة هذه.

![ما يجب القيام به: image_بديل_نص](working-with-cells-gridweb_5.png)

 كما ترى في لقطة الشاشة التالية ، عندما ينقر المستخدم على زر الأمر المخصص ، فإنه يضيف نصًا في الخلية A1 يقول**"تم النقر فوق زر الأمر المخصص الخاص بي."**

![ما يجب القيام به: image_بديل_نص](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **معالجة الحدث لزر الأمر المخصص**
يشرح نموذج التعليمات البرمجية التالي كيفية تنفيذ معالجة الحدث لزر الأمر المخصص.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **تنسيق الخلايا لـ GridWeb**
### **سيناريوهات الاستخدام الممكنة**
يدعم GridWeb الآن المستخدمين لإدخال بيانات الخلية بتنسيق النسبة المئوية مثل 3٪ وسيتم تنسيق البيانات الموجودة في الخلية تلقائيًا كـ 3.00٪. ومع ذلك ، سيتعين عليك تعيين نمط الخلية إلى تنسيق النسبة المئوية وهو إما GridTableItemStyle.NumberType a 9 أو 10. سيتم تنسيق الرقم 9 3٪ كـ 3٪ ولكن الرقم 10 سيتم تنسيقه 3٪ كـ 3.00٪.

{{% alert color="primary" %}} 

إذا لم تقم بتعيين نمط الخلية على تنسيق النسبة المئوية ، فسيتم عرض بيانات الإدخال 3٪ على أنها 0.03.

{{% /alert %}} 
### **أدخل Cell بيانات ورقة عمل GridWeb بتنسيق النسبة المئوية**
يعين نموذج التعليمات البرمجية التالي الخلية A1 GridTableItemStyle.NumberType كـ 10 ، وبالتالي يتم تنسيق بيانات الإدخال 3٪ تلقائيًا كـ 3.00٪ كما هو موضح في لقطة الشاشة.

![ما يجب القيام به: image_بديل_نص](working-with-cells-gridweb_7.png)
### **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
