---
title: العمل مع Cells GridWeb
type: docs
weight: 50
url: /ar/java/working-with-cells-gridweb/
---
##  **الوصول إلى Cells في ورقة العمل**
يناقش هذا الموضوع الخلايا، وينظر إلى الميزة الأساسية لـ GridWeb: الوصول إلى الخلايا.

تحتوي كل ورقة عمل على كائن GridCells، وهو عبارة عن مجموعة من كائنات GridCell. يمثل كائن GridCell خلية في Aspose.Cells.GridWeb. من الممكن الوصول إلى أي خلية باستخدام GridWeb. هناك طريقتان مفضلتان:

- [الوصول إلى الخلية بالاسم](/cells/ar/java/working-with-cells-gridweb/).
- [الوصول إلى الخلية عن طريق فهارس الصفوف والأعمدة](/cells/ar/java/working-with-cells-gridweb/).

أدناه، تتم مناقشة كل نهج.
###  **باستخدام Cell الاسم**
جميع الخلايا لها اسم فريد. على سبيل المثال، A1، A2، B1، B2، إلخ. Aspose.Cells.GridWeb يسمح للمطورين بالوصول إلى أي خلية مطلوبة باستخدام اسم الخلية. ما عليك سوى تمرير اسم الخلية (كفهرس) إلى مجموعة GridCells في GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


###  **استخدام فهارس الصفوف والأعمدة**
يمكن أيضًا التعرف على الخلية من خلال موقعها من حيث مؤشرات الصفوف والأعمدة. ما عليك سوى تمرير فهارس الصفوف والأعمدة الخاصة بالخلية إلى مجموعة GridCells في ورقة GridWorksheet. هذا النهج أسرع من النهج المذكور أعلاه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
##  **الوصول وتعديل قيمة Cell**
[الوصول إلى Cells في ورقة العمل](/cells/ar/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) ناقش الوصول إلى الخلايا. يوسع هذا الموضوع تلك المناقشة لإظهار كيفية الوصول إلى قيم الخلايا وتعديلها باستخدام GridWeb API.
###  **الوصول إلى قيمة Cell وتعديلها**
####  **قيم السلسلة**
 قبل الوصول إلى قيمة الخلية وتعديلها، عليك معرفة كيفية الوصول إلى الخلايا. للحصول على تفاصيل حول الأساليب المختلفة للوصول إلى الخلايا، راجع[الوصول إلى Cells في ورقة العمل](/cells/ar/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

تحتوي كل خلية على خاصية تسمى getStringValue(). بمجرد الوصول إلى الخلية، يمكن للمطورين الوصول إلى طريقة getStringValue() للوصول إلى قيمة سلسلة الخلايا.

{{% alert color="primary" %}} 

هام: يمكن تخزين خمسة أنواع من القيم (Boolean وint وdouble وDateTime وstring) في الخلايا ولكن لا يمكن استخدام طريقة (طرق) getValue()/setValue() إلا للوصول إلى/تعديل قيمة الكائن.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
####  **جميع أنواع القيم**
Aspose.Cells.GridWeb يوفر أيضًا طريقة خاصة، putValue، لكل خلية. باستخدام هذه الطريقة، من الممكن إدراج أو تعديل أي نوع من القيم (Boolean وint وdouble وDateTime وstring) في الخلية.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



هناك أيضًا إصدار مثقل من طريقة putValue يمكنه أخذ أي نوع من القيمة بتنسيق سلسلة وتحويله إلى نوع بيانات مناسب تلقائيًا. لتحقيق ذلك، قم بتمرير القيمة المنطقية الحقيقية إلى معلمة أخرى من طريقة putValue كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
##  **إضافة الصيغ إلى Cells**
الميزة الأكثر قيمة التي يقدمها Aspose.Cells.GridWeb هي دعم الصيغ أو الوظائف. Aspose.Cells.GridWeb لديه محرك الصيغة الخاص به الذي يحسب الصيغ في أوراق العمل. Aspose.Cells.GridWeb يدعم كلاً من الوظائف أو الصيغ المضمنة والمحددة من قبل المستخدم. يناقش هذا الموضوع إضافة الصيغ إلى الخلايا باستخدام Aspose.Cells.GridWeb API بالتفصيل.
###  **كيفية إضافة وحساب الصيغة؟**
 من الممكن إضافة الصيغ والوصول إليها وتعديلها في الخلايا باستخدام خاصية الصيغة الخاصة بالخلية. Aspose.Cells.GridWeb يدعم الصيغ المعرفة من قبل المستخدم والتي تتراوح من البسيطة إلى المعقدة. ومع ذلك، يتم أيضًا توفير عدد كبير من الوظائف أو الصيغ المضمنة (المشابهة لـ Microsoft Excel) مع Aspose.Cells.GridWeb. للاطلاع على القائمة الكاملة للوظائف المضمنة، يرجى الرجوع إلى هذا[قائمة الوظائف المدعومة.](/cells/ar/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

يجب أن يكون بناء جملة الصيغة متوافقًا مع بناء جملة Excel Microsoft. على سبيل المثال، يجب أن تبدأ كافة الصيغ بعلامة التساوي (=).

لإضافة صيغة برمجيًا، سيتعرف Aspose.Cells.GridWeb عليها كصيغة حتى إذا كنت لا تستخدم علامة *=*، ولكن إذا كان المستخدمون النهائيون الذين يعملون في واجهة المستخدم الرسومية يجب عليهم استخدامها.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**تمت إضافة الصيغة إلى الخلية B3 ولكن لم يتم حسابها بواسطة GridWeb** 

![ما يجب القيام به:image_alt_text](working-with-cells-gridweb_1.png)

في لقطة الشاشة أعلاه، يمكنك أن ترى أنه تمت إضافة صيغة إلى B3 ولكن لم يتم حسابها بعد. لحساب كافة الصيغ، قم باستدعاء أسلوب accountFormula الخاص بعنصر تحكم GridWeb GridWorksheetCollection بعد إضافة الصيغ إلى أوراق العمل كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

يمكن للمستخدمين أيضًا حساب الصيغ بالنقر فوق *إرسال**.

**النقر على زر إرسال من GridWeb** 

![ما يجب القيام به:image_alt_text](working-with-cells-gridweb_2.png)

**هام**: إذا قام المستخدم بالنقر فوق **حفظ** أو**الغاء التحميل** الأزرار، أو علامات تبويب الورقة، يتم حساب جميع الصيغ بواسطة GridWeb تلقائيًا.

**نتيجة الصيغة بعد الحساب** 

![ما يجب القيام به:image_alt_text](working-with-cells-gridweb_3.png)
###  **الرجوع إلى Cells من أوراق العمل الأخرى**
باستخدام Aspose.Cells.GridWeb، من الممكن الإشارة إلى القيم المخزنة في أوراق عمل مختلفة في صيغها، مما يؤدي إلى إنشاء صيغ معقدة.

بناء الجملة للإشارة إلى قيمة خلية من ورقة عمل مختلفة هو SheetName!CellName.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
##  **إنشاء التحقق من صحة البيانات في GridCell من GridWeb**
 Aspose.Cells.GridWeb يسمح لك بالإضافة**تأكيد صحة البيانات** باستخدام طريقة GridWorksheet.getValidations().add(). باستخدام هذه الطريقة، يجب عليك تحديد**Cell المدى**. ولكن إذا كنت تريد إنشاء التحقق من صحة البيانات في GridCell واحد، فيمكنك القيام بذلك مباشرة باستخدام طريقة GridCell.createValidation(). وبالمثل، يمكنك إزالة ** التحقق من صحة البيانات** من GridCell باستخدام أسلوب GridCell.removeValidation().

 ينشئ نموذج التعليمات البرمجية التالي**تأكيد صحة البيانات** في الخلية B3. إذا قمت بإدخال أي قيمة لا تتراوح بين 20 و40، ستظهر الخلية B3**خطئ في التحقق** في شكل**أحمر XXXX** كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
##  **إنشاء أزرار الأوامر المخصصة**
Aspose.Cells.GridWeb يحتوي على أزرار خاصة مثل الإرسال والحفظ والتراجع. تؤدي كل هذه الأزرار مهامًا محددة لـ Aspose.Cells.GridWeb. من الممكن أيضًا إضافة أزرار مخصصة تؤدي مهام مخصصة. يشرح هذا الموضوع كيفية استخدام هذه الميزة.

يشرح نموذج التعليمات البرمجية التالي كيفية إنشاء زر أمر مخصص وكيفية التعامل مع حدث النقر الخاص به. يمكنك استخدام أي رمز لزر الأمر المخصص الخاص بك. ولأغراض التوضيح، استخدمنا أيقونة الصورة هذه.

![ما يجب القيام به:image_alt_text](working-with-cells-gridweb_5.png)

 كما ترون في لقطة الشاشة التالية، عندما ينقر المستخدم على زر الأمر المخصص، فإنه يضيف نصًا في الخلية A1 يقول**"تم النقر على زر الأمر المخصص الخاص بي."**

![ما يجب القيام به:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
###  **التعامل مع الأحداث من زر الأمر المخصص**
يشرح نموذج التعليمات البرمجية التالي كيفية تنفيذ معالجة الحدث لزر الأمر المخصص.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
##  **تنسيق الخلايا لـ GridWeb**
###  **سيناريوهات الاستخدام المحتملة**
يدعم GridWeb الآن المستخدمين لإدخال بيانات الخلية بتنسيق النسبة المئوية مثل 3% وسيتم تنسيق البيانات الموجودة في الخلية تلقائيًا على أنها 3.00%. ومع ذلك، سيتعين عليك تعيين نمط الخلية على تنسيق النسبة المئوية والذي يكون إما GridTableItemStyle.NumberType a 9 أو 10. سيتم تنسيق الرقم 9 3% كـ 3% ولكن الرقم 10 سيتم تنسيقه 3% كـ 3.00%.

{{% alert color="primary" %}} 

إذا لم تقم بتعيين نمط الخلية على تنسيق النسبة المئوية، فسيتم عرض البيانات المدخلة 3% على أنها 0.03.

{{% /alert %}} 
###  **أدخل Cell بيانات ورقة عمل GridWeb بتنسيق النسبة المئوية**
يقوم نموذج التعليمة البرمجية التالي بتعيين الخلية A1 GridTableItemStyle.NumberType على القيمة 10، وبالتالي يتم تنسيق بيانات الإدخال 3% تلقائيًا على أنها 3.00% كما هو موضح في لقطة الشاشة.

![ما يجب القيام به:image_alt_text](working-with-cells-gridweb_7.png)
###  **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
