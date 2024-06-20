---
title: الدوائر والتبعيات
type: docs
weight: 230
url: /ar/java/precedents-and-dependents/
---

{{% alert color="primary" %}} 

ورق العمل المالي المعقد، خصوصًا تلك التي تم تطويرها بالتعاون، يمكن أن تخفي الأخطاء الأكثر إحراجًا. فحص الصيغ لضمان الدقة والعثور على مصدر الخطأ يمكن أن يكون صعبًا عندما تستخدم الصيغ خلايا سابقة وخلايا معولة.

{{% /alert %}} 
## **مقدمة**
- **الخلايا المسبقة** هي الخلايا التي يشير إليها صيغة في خلية أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن الخلية B5 هي مسبقة للخلية D10.
- ** الخلايا التابعة** تحتوي الخلايا على صيغ تشير إلى خلايا أخرى. على سبيل المثال ، إذا احتوت الخلية D10 على الصيغة = B5 ، فإن الخلية D10 هي تابعة للخلية B5.

لجعل ورق العمل سهل القراءة، قد ترغب في إظهار بشكل واضح الخلايا المستخدمة في صيغة. بالمثل، قد ترغب في استخراج الخلايا المعولة لخلايا أخرى.

تتيح Aspose.Cells لك تتبع الخلايا ومعرفة الخلايا المرتبطة.
## **تتبع خلايا السابقة والتابعة: مايكروسوفت إكسل**
قد تتغير الصيغ استنادًا إلى التعديلات التي قام بها العميل. على سبيل المثال ، إذا كانت الخلية C1 معتمدة على C3 و C4 التي تحتوي على صيغة ، وتم تغيير C1 (بحيث يتم تجاوز الصيغة) ، فيجب تغيير C3 و C4 ، أو غيرها من الخلايا ، لتوازن الجدول الخماسي استنادًا إلى قواعد الأعمال.

بالمثل ، فلنفترض أن C1 تحتوي على الصيغة "=(B1*22)/(M2*N32)". أريد أن أجد الخلايا التي يعتمد C1 عليها ، أي الخلايا السابقة B1 و M2 و N32.

قد تحتاج إلى تتبع التبعية لخلية معينة إلى خلايا أخرى. إذا تم تضمين قواعد الأعمال في الصيغ ، نود معرفة التبعيات وتنفيذ بعض القواعد استنادًا إليها. بالمثل ، إذا تم تعديل قيمة خلية معينة ، فأي الخلايا في ورقة العمل يتأثر بتلك التغيير؟

تسمح مايكروسوفت إكسل للمستخدمين بتتبع الخلايا السابقة والتابعة.

1. في شريط الأدوات **View Toolbar** ، حدد **Formula Auditing**. سيتم عرض مربع حوار Formula Auditing.
1. تتبع السابقين:
   1. حدد الخلية التي تحتوي الصيغة التي تريد العثور على الخلايا السابقة لها.
   1. لعرض السهم التتبع إلى كل خلية توفر بيانات مباشرة للخلية النشطة، انقر على **تتبع السابقين** على شريط أدوات **تدقيق الصيغ**.
1. تتبع الصيغ التي تشير إلى خلية معينة (التوابع)
   1. حدد الخلية التي تريد تحديد الخلايا التابعة لها.
   1. لعرض السهم التتبع إلى كل خلية تعتمد على الخلية النشطة، انقر على تتبع التوابع على شريط أدوات تدقيق الصيغ.
## **تتبع خلايا السابقة والتابعة: Aspose.Cells**
### **تتبع السابقين**
يسهل Aspose.Cells الحصول على الخلايا المسبقة. يمكن لها ألا تسترد الخلايا التي تقدم البيانات للسلف المبسط فحسب بل تجد أيضًا الخلايا التي تقدم البيانات للسلف المعقد مع النطاقات المسماة.

في المثال أدناه، يتم استخدام ملف إكسل نموذجي، Book1.xls. يحتوي جدول البيانات على بيانات وصيغ على ورقة العمل الأولى.

توفر Aspose.Cells [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) [GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents--) طريقة الفئة لتتبع الخلايا السابقة. تعيد [ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection). كما يمكنك رؤية أعلاه، في Book1.xls، تحتوي الخلية B7 على الصيغة "=SUM(A1:A3)". لذا فإن الخلايا A1:A3 هي الخلايا السابقة للخلية B7. يوضح المثال التالي ميزة تتبع الخلايا السابقة باستخدام ملف النموذج Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **تتبع المعتمدين**
يتيح لك Aspose.Cells الحصول على الخلايا المعتمدة في أوراق العمل. ليست Aspose.Cells قادرة فقط على استرداد الخلايا التي تقدم بيانات بشأن صيغة بسيطة بل تجد أيضًا الخلايا التي تقدم بيانات لمعتمدي صيغة معقدة باستخدام النطاقات المسماة.

توفر Aspose.Cells فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) وطريقة [GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)) التي يمكن استخدامها لتتبع المتابعين لخلية. على سبيل المثال، في Book1.xlsx هناك صيغ: "=A1+20" و "=A1+30" في الخلايا B2 و C2 على التوالي. يوضح الأمثلة التالية كيفية تتبع المتابعين للخلية A1 باستخدام ملف القالب Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **تتبع الخلايا المسبقة والمعتمدة وفقًا لسلسلة الحساب**
تعتبر واجهات برمجة التطبيقات السالفة لتتبع السالفة والتابعة وفقا لتعبير الصيغة نفسها. إنها توفر ببساطة وسيلة مريحة للمستخدم لتتبع التبعيات المتبادلة لعدد قليل من الصيغ. إذا كان هناك عدد كبير من الصيغ في دفتر العمل ويحتاج المستخدم إلى تتبع السالفة والتابعة لكل خلية، فإنها ستوفر أداءً سيئًا. في مثل هذه الحالة، يجب على المستخدم النظر في استخدام الطرق [GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation--) و [GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean)/). تتبع هاتان الطريقتان التبعيات وفقًا لسلسلة الحساب. لاستخدامهما، يجب أولاً تمكين سلسلة الحساب عن طريق [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain). بعد ذلك يجب القيام بحساب كامل لدفتر العمل عن طريق [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). بعد ذلك، يمكنك تتبع السالفة أو التابعة لكل تلك الخلايا التي تحتاجها.

بالنسبة لبعض الصيغ، قد تكون المسبقات الناتجة مختلفة بالنسبة لـ GetPrecedents و GetPrecedentsInCalculation، وقد تكون المعتمدون الناتجة مختلفة بالنسبة لـ GetDependents و GetDependentsInCalculation. على سبيل المثال، إذا كانت صيغة الخلية A1 هي "=IF(TRUE,B2,C3)"، فستوفر GetPrecedents B2 و C3 كمسبقات لـ A1. وفي هذا السياق، يحمل كل من B2 و C3 المعتمد A1 عند التحقق بواسطة GetDependents. ومع ذلك، بالنسبة لحساب هذه الصيغة، من الواضح أنه يمكن لـ B2 فقط التأثير على النتيجة المحسوبة. لذا فإن GetPrecedentsInCalculation لن تقدم C3 لـ A1، ولن تقدم GetDependentsInCalculation A1 لـ C3. في بعض الأحيان قد يكون لدى المستخدم مجرد متطلبات تتبع تلك الترابطات التي تؤثر فعليًا على النتيجة المحسوبة لصيغ استنادًا إلى البيانات الحالية لورقة العمل، فيجب عليهم أيضًا استخدام GetDependentsInCalculation/GetPrecedentsInCalculation بدلاً من GetDependents/GetPrecedents.

يوضح المثال التالي كيفية تتبع المسبقات والمعتمدين وفقًا لسلسلة الحساب للخلايا:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
