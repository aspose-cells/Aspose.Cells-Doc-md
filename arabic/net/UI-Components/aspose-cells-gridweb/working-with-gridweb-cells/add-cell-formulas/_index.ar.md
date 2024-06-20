---
title: إضافة صيغ الخلية
type: docs
weight: 30
url: /ar/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb، صيغة
description: يقدم هذا المقال كيفية إضافة صيغة في الخلية في GridWeb.
---

{{% alert color="primary" %}} 

أهم الميزات التي يوفرها Aspose.Cells.GridWeb هي دعم الصيغ أو الوظائف. تحتوي Aspose.Cells.GridWeb على محرك الصيغ الخاص بها الذي يقوم بحساب الصيغ في أوراق العمل. يدعم Aspose.Cells.GridWeb الوظائف أو الصيغ الداخلية والمحددة من قبل المستخدمين. يناقش هذا الموضوع إضافة الصيغ إلى الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells.GridWeb بالتفصيل.

{{% /alert %}} 
## **إضافة الصيغ إلى الخلايا**
### **كيفية إضافة وحساب صيغة**
من الممكن إضافة والوصول وتعديل الصيغ في الخلايا عن طريق استخدام خاصية الصيغة الخلوية. تدعم Aspose.Cells.GridWeb الصيغ المحددة من قبل المستخدمين تتراوح من البسيطة إلى العقد. ومع ذلك، يتم تزويد Aspose.Cells.GridWeb بعدد كبير من الوظائف أو الصيغ المدمجة (مشابهة لـ Microsoft Excel). لرؤية القائمة الكاملة للوظائف المدمجة، يرجى الرجوع إلى هذه [القائمة بالوظائف المدعومة.](/cells/ar/net/aspose-cells-gridweb/list-of-supported-functions/)

{{% alert color="primary" %}} 

جب على بناء الصيغة أن تكون متوافقة مع بناء الصيغ في Microsoft Excel. على سبيل المثال، يجب أن تبدأ جميع الصيغ بعلامة يساوي (=).

لإضافة صيغة ديناميكية، سيتعرف Aspose.Cells.GridWeb عليها كصيغة حتى لو لم تستخدم علامة **=**، ولكن إذا كان المستخدمون النهائيون يعملون في واجهة المستخدم الرسومية، يجب عليهم استخدام علامة "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**تمت إضافة الصيغة إلى الخلية B3 ولكن لم يتم حسابها بواسطة GridWeb** 

![todo:image_alt_text](add-cell-formulas_1.png)

في لقطة الشاشة أعلاه، يمكنك رؤية أن تمت إضافة صيغة إلى خلية B3 ولكن لم يتم حسابها بعد. لحساب جميع الصيغ، قم بالاستدعاء GridWeb control's GridWorksheetCollection's CalculateFormula method بعد إضافة الصيغ إلى أوراق العمل كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

يمكن للمستخدمين أيضًا حساب الصيغ عن طريق النقر على **تقديم**.

**النقر على زر تقديم من GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**مهم**: إذا قام المستخدم بالنقر على **حفظ** أو **تراجع**, أو علامات علامات التبويب للصفحات، سيتم حساب جميع الصيغ تلقائيًا بواسطة GridWeb.

**نتيجة الصيغة بعد الحساب** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **الإشارة إلى الخلايا من أوراق عمل أخرى**
من خلال Aspose.Cells.GridWeb، يمكن الإشارة إلى القيم المخزنة في أوراق عمل مختلفة في صيغهم، مما يخلق صيغ معقدة.

الصيغة للإشارة إلى قيمة الخلية من ورقة عمل مختلفة هي اسم الورقة! اسم الخلية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
