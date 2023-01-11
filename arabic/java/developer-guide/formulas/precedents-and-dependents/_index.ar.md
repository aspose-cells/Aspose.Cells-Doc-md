﻿---
title: السوابق والمعالون
type: docs
weight: 230
url: /ar/java/precedents-and-dependents/
---
{{% alert color="primary" %}} 

أوراق العمل المالية المعقدة ، خاصة تلك التي تم تطويرها بالتعاون ، يمكن أن تخفي الأخطاء الأكثر إحراجًا. قد يكون التحقق من الصيغ للتأكد من دقتها وإيجاد مصدر الخطأ أمرًا صعبًا عندما تستخدم الصيغة خلايا سابقة وخلايا تابعة.

{{% /alert %}} 
## **مقدمة**
- **الخلايا السابقة** هي الخلايا المشار إليها بواسطة صيغة أخرى في Cell. على سبيل المثال ، إذا كانت الخلية D10 تحتوي على الصيغة = B5 ، فإن الخلية B5 هي سابقة للخلية D10.
- **الخلايا التابعة** تحتوي على صيغ تشير إلى خلايا أخرى. على سبيل المثال ، إذا كانت الخلية D10 تحتوي على الصيغة = B5 ، فإن الخلية D10 تكون تابعة للخلية B5.

لتسهيل قراءة جدول البيانات ، قد ترغب في إظهار الخلايا الموجودة في جدول البيانات والمستخدمة في الصيغة بوضوح. وبالمثل ، قد ترغب في استخراج الخلايا التابعة للخلايا الأخرى.

Aspose.Cells يسمح لك بتتبع الخلايا ومعرفة أي منها مرتبطة.
## **تتبع السوابق والمعالين Cells: Microsoft Excel**
قد تتغير الصيغ بناءً على التعديلات التي يجريها العميل. على سبيل المثال ، إذا كانت الخلية C1 تعتمد على C3 و C4 التي تحتوي على صيغة ، وتم تغيير C1 (بحيث يتم تجاوز الصيغة) ، أو C3 و C4 ، أو خلايا أخرى ، فيجب تغييرها لموازنة جدول البيانات استنادًا إلى قواعد العمل.

وبالمثل ، افترض أن C1 تحتوي على الصيغة "= (B1*22) / (م 2*N32) ". أريد العثور على الخلايا التي تعتمد عليها C1 ، وهي الخلايا السابقة B1 و M2 و N32.

قد تحتاج إلى تتبع تبعية خلية معينة إلى خلايا أخرى. إذا تم تضمين قواعد العمل في الصيغ ، فنحن نرغب في معرفة التبعية وتنفيذ بعض القواعد بناءً عليها. وبالمثل ، إذا تم تعديل قيمة خلية معينة ، فأي الخلايا في ورقة العمل ستتأثر بهذا التغيير؟

Microsoft Excel يسمح للمستخدمين بتتبع السوابق والتابعين.

1.  على ال**عرض شريط الأدوات** ، تحديد**تدقيق الصيغة**. سيتم عرض مربع حوار تدقيق الصيغة.
1. تتبع السوابق:
1. حدد الخلية التي تحتوي على الصيغة التي تريد البحث عن الخلايا السابقة لها.
 1. لعرض سهم التتبع لكل خلية توفر بيانات مباشرة إلى الخلية النشطة ، انقر فوق**تتبع السوابق** على ال**تدقيق الصيغة** شريط الأدوات.
1. تتبع الصيغ التي تشير إلى خلية معينة (التابعين)
 1. حدد الخلية التي تريد تحديد الخلايا التابعة لها.
 1. لعرض سهم التتبع لكل خلية تعتمد على الخلية النشطة ، انقر فوق تتبع التابعين على شريط أدوات تدقيق الصيغة.
## **تتبع السوابق والمعالين Cells: Aspose.Cells**
### **تتبع السوابق**
يسهل Aspose.Cells الحصول على الخلايا السابقة. لا يمكنها فقط استرداد الخلايا التي توفر بيانات لسوابق الصيغ البسيطة ولكن أيضًا العثور على الخلايا التي توفر بيانات لسوابق الصيغ المعقدة ذات النطاقات المسماة.

في المثال أدناه ، يتم استخدام ملف Excel نموذجي ، Book1.xls. يحتوي جدول البيانات على بيانات وصيغ في ورقة العمل الأولى.

 يوفر Aspose.Cells ملف[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) صف دراسي'[GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents() ) الطريقة المستخدمة لتتبع سوابق الخلية. تقوم بإرجاع ملف[ريفريداريكوليكشن](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection)كما ترى أعلاه ، في Book1.xls ، تحتوي الخلية B7 على صيغة "= SUM (A1: A3)". لذا فإن الخلايا A1: A3 هي الخلايا السابقة للخلية B7. يوضح المثال التالي ميزة سوابق التتبع باستخدام ملف القالب Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **تتبع المعالين**
يتيح لك Aspose.Cells الحصول على خلايا تابعة في جداول البيانات. لا يمكن لـ Aspose.Cells استرداد الخلايا التي توفر بيانات تتعلق بصيغة بسيطة فحسب ، بل يمكن أيضًا العثور على الخلايا التي توفر البيانات إلى المعتمدين على صيغة معقدة ذات نطاقات مسماة.

 يوفر Aspose.Cells ملف[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) صف دراسي'[GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)) الطريقة المستخدمة لتتبع التابعين للخلية. على سبيل المثال ، في Book1.xlsx توجد صيغ: "= A1 + 20" و "= A1 + 30" في الخلايا B2 و C2 على التوالي. يوضح المثال التالي كيفية تتبع التابعين لخلية A1 باستخدام ملف القالب Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **تتبع الخلايا السابقة والتابعة وفقًا لسلسلة الحساب**
أعلى نقطة من تتبع السوابق والمعالين وفقًا لتعبير الصيغة نفسها. إنها ببساطة توفر طريقة ملائمة للمستخدم لتتبع التبعيات لبعض الصيغ. إذا كان هناك قدر كبير من الصيغ في المصنف ويحتاج المستخدم إلى تتبع السابقات والعناصر التابعة لكل خلية ، فسوف ينتج عنها أداء ضعيف. لمثل هذه الحالة ، يجب على المستخدم النظر في استخدام[GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation() /) و[GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean) /) أساليب. تتبع هاتان الطريقتان التبعيات وفقًا لسلسلة الحساب. لذلك ، لاستخدامها ، تحتاج أولاً إلى تمكين سلسلة الحساب من خلال[المصنف ، الإعدادات ، إعدادات الصيغ ، التمكين ، السلسلة الحسابية](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain) . ثم يجب عليك إجراء الحساب الكامل للمصنف بواسطة[المصنف .CalculateFormula ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). بعد ذلك ، يمكنك تتبع السوابق أو التابعين لكل تلك الخلايا التي تحتاجها.

بالنسبة لبعض الصيغ ، قد تكون السابقات الناتجة مختلفة لـ GetPrecedents و GetPrecedentsInCalculation ، وقد تختلف المعالون الناتجة عن GetDependents و GetDependentsInCalculation. على سبيل المثال ، إذا كانت صيغة الخلية A1 هي "= IF (TRUE، B2، C3)" ، فإن GetPrecedents سيوفر B2 و C3 كسابقة A1. وفقًا لذلك ، يحتوي كل من B2 و C3 على A1 التابع عند التحقق بواسطة GetDependents. ومع ذلك ، لحساب هذه الصيغة ، من الواضح أن B2 فقط هي التي يمكن أن تؤثر على النتيجة المحسوبة. لذلك لن يوفر GetPrecedentsInCalculation C3 لـ A1 ، ولن يوفر GetDependentsInCalculation A1 لـ C3. في بعض الأحيان ، قد يكون لدى المستخدم فقط متطلبات تتبع تلك التبعيات التي تؤثر بالفعل على النتيجة المحسوبة للصيغ بناءً على البيانات الحالية للمصنف ، ثم يحتاجون أيضًا إلى استخدام GetDependentsInCalculation / GetPrecedentsInCalculation بدلاً من GetDependents / GetPrecedents.

يوضح المثال التالي كيفية تتبع السوابق والمعالين وفقًا لسلسلة الحساب للخلايا:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}