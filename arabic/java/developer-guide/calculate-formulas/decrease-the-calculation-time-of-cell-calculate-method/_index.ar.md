---
title: تقليل وقت حساب أسلوب Cell.Calculate
type: docs
weight: 860
url: /ar/java/decrease-the-calculation-time-of-cell-calculate-method/
---


سيناريوهات الاستخدام المحتملة

عادةً، نوصي المستخدمين باستدعاء طريقة [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. لكن أحيانًا، لا يرغب المستخدمون في حساب كامل دفتر العمل. إنهم يريدون فقط حساب خلية واحدة. توفر Aspose.Cells الخاصية [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) والتي يمكنك تعيينها إلى **false** وسيقلل ذلك بشكل كبير من وقت حساب الخلية الفردية. لأنه عندما يتم تعيين الخاصية التكرارية إلى **true**، يتم إعادة حساب جميع المعتمدين على كل استدعاء. ولكن عندما يتم تعيين الخاصية إلى **false**، يتم حساب الخلايا المعتمدة مرة واحدة فقط ولا تُعاد حسابها على الاستدعاءات التالية.
## **تخفيض وقت حساب الخلية لوسيلة (.Calculate())**
يوضح الرمز النموذجي التالي استخدام خاصية [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive). يرجى تنفيذ هذا الرمز مع [ملف إكسل عينة محدد](5472288.xlsx) والتحقق من الناتج في وحدة التحكم. ستجد أن تعيين الخاصية التكرارية على **false** قلل وقت الحساب بشكل ملحوظ. يرجى أيضًا قراءة التعليقات لفهم أفضل لهذه الخاصية.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **مخرجات الوحدة**
هذا هو ناتج وحدة التحكم من الرمز النموذجي أعلاه عند تنفيذه مع [ملف إكسل عينة محدد](5472288.xlsx) على جهازنا. يرجى ملاحظة، قد تختلف الناتج ولكن سيكون الوقت المنقضي بعد تعيين الخاصية التكرارية على **false** دائمًا أقل من تعيينها على **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
