---
title: أضف Cell الصيغ
type: docs
weight: 30
url: /ar/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

الميزة الأكثر قيمة التي يقدمها Aspose.Cells.GridWeb هي دعم الصيغ أو الوظائف. Aspose.Cells.GridWeb له Formula Engine الخاص به الذي يحسب الصيغ في أوراق العمل. Aspose.Cells.GridWeb يدعم كلا من الوظائف أو الصيغ المضمنة والمعرفة من قبل المستخدم. يناقش هذا الموضوع إضافة الصيغ إلى الخلايا باستخدام Aspose.Cells.GridWeb API بالتفصيل.

{{% /alert %}} 
## **إضافة الصيغ إلى Cells**
### **كيف تضيف وتحسب صيغة؟**
 من الممكن إضافة الصيغ والوصول إليها وتعديلها في الخلايا باستخدام خاصية الصيغة للخلية. Aspose.Cells.GridWeb يدعم الصيغ المعرفة من قبل المستخدم والتي تتراوح من البسيط إلى المعقد. ومع ذلك ، يتم أيضًا توفير عدد كبير من الوظائف أو الصيغ المضمنة (على غرار Microsoft Excel) مع Aspose.Cells.GridWeb. للاطلاع على القائمة الكاملة للوظائف المضمنة ، يرجى الرجوع إلى هذا[قائمة الوظائف المدعومة.](/cells/ar/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

يجب أن يكون بناء جملة الصيغة متوافقًا مع بناء جملة Microsoft Excel. على سبيل المثال ، يجب أن تبدأ جميع الصيغ بعلامة يساوي (=).

لإضافة صيغة ديناميكيًا ، سيتعرف عليها Aspose.Cells.GridWeb كصيغة حتى إذا لم تستخدم علامة ** = ** ، ولكن إذا كان المستخدمون النهائيون يعملون في واجهة المستخدم الرسومية ، فيجب عليه استخدام علامة "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**تمت إضافة الصيغة إلى خلية B3 ولكن لم يتم حسابها بواسطة GridWeb** 

![ما يجب القيام به: image_بديل_نص](add-cell-formulas_1.png)

في لقطة الشاشة أعلاه ، يمكنك أن ترى أنه تمت إضافة صيغة إلى B3 ولكن لم يتم حسابها بعد. لحساب جميع الصيغ ، قم باستدعاء أسلوب GridWorksheetCollection's CalculateFormula الخاص بعنصر التحكم GridWeb بعد إضافة الصيغ إلى أوراق العمل كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

 يمكن للمستخدمين أيضًا حساب الصيغ بالنقر فوق**يُقدِّم**.

**النقر فوق الزر إرسال من GridWeb** 

![ما يجب القيام به: image_بديل_نص](add-cell-formulas_2.png)

**الأهمية** : إذا قام المستخدم بالنقر فوق**يحفظ** أو**الغاء التحميل** الأزرار ، أو علامات تبويب الأوراق ، يتم حساب جميع الصيغ بواسطة GridWeb تلقائيًا.

**نتيجة الصيغة بعد الحساب** 

![ما يجب القيام به: image_بديل_نص](add-cell-formulas_3.png)

{{% /alert %}} 
### **الرجوع إلى Cells من أوراق العمل الأخرى**
باستخدام Aspose.Cells.GridWeb ، من الممكن الإشارة إلى القيم المخزنة في أوراق عمل مختلفة في صيغها ، وإنشاء صيغ معقدة.

بناء الجملة للإشارة إلى قيمة خلية من ورقة عمل مختلفة هو اسم الورقة! اسم الخلية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
