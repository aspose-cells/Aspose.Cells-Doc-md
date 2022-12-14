---
title: إنقاص وقت الحساب إلى Cell.Calculate طريقة
type: docs
weight: 860
url: /ar/java/decrease-the-calculation-time-of-cell-calculate-method/
---
سيناريوهات الاستخدام الممكنة

 عادة ، نوصي المستخدمين بالاتصال[المصنف .CalculateFormula ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) مرة واحدة ثم احصل على القيم المحسوبة للخلايا الفردية. لكن في بعض الأحيان ، لا يرغب المستخدمون في حساب المصنف بأكمله. إنهم يريدون فقط حساب خلية واحدة. يوفر Aspose.Cells[خيارات الحساب](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) الممتلكات التي يمكنك تعيينها**خاطئة**وسيقلل من وقت الحساب للخلية الفردية بشكل كبير. لأنه عند تعيين الخاصية العودية إلى**حقيقي**، ثم يتم إعادة حساب جميع المعالين من الخلايا في كل مكالمة. ولكن عندما يتم تعيين الخاصية العودية على**خاطئة**، ثم يتم حساب الخلايا التابعة مرة واحدة فقط ولا يتم حسابها مرة أخرى في المكالمات اللاحقة.
## **إنقاص وقت الحساب لـ Cell.Calculate () طريقة**
 يوضح نموذج التعليمات البرمجية التالي استخدام[خيارات الحساب](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) منشأه. يرجى تنفيذ هذا الرمز مع المعطى[نموذج ملف اكسل](5472288.xlsx) وتحقق من إخراج وحدة التحكم الخاصة به. ستجد أن تعيين الخاصية العودية إلى**خاطئة**قلل من وقت الحساب بشكل كبير. يرجى أيضًا قراءة التعليقات من أجل فهم أفضل لهذه الخاصية.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **إخراج وحدة التحكم**
 هذا هو إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه عند تنفيذه مع المعطى[نموذج ملف اكسل](5472288.xlsx) على أجهزتنا. يرجى ملاحظة ، قد يختلف الإخراج الخاص بك ولكن الوقت المنقضي بعد تعيين الخاصية العودية إلى**خاطئة** سيكون دائمًا أقل من تعيينه على**حقيقي**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
