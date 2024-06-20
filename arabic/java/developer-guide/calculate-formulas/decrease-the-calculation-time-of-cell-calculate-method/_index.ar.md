---
title: تقليل وقت حساب أسلوب Cell.Calculate
type: docs
weight: 860
url: /ar/java/decrease-the-calculation-time-of-cell-calculate-method/
---


سيناريوهات الاستخدام المحتملة

عادةً ما نوصي المستخدمين بالاتصال بالطريقة [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. ولكن في بعض الأحيان، قد لا يكون المستخدمون يريدون حساب كامل الدفتر. إنهم يريدون فقط حساب خلية واحدة. توفر Aspose.Cells خاصية [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) يمكنك تعيينها على **false** وسوف تقلل من وقت حساب الخلية الفردية بشكل كبير. لأنه عندما يتم تعيين الخاصية التكرارية على **true**، يتم إعادة حساب جميع الخلايا التالية على كل مكالمة. ولكن عندما يتم تعيين الخاصية التكرارية على **false**، يتم حساب الخلايا التالية مرة واحدة فقط ولا يتم إعادة حسابها مجددًا في المكالمات التالية.
## **تخفيض وقت حساب الخلية لوسيلة (.Calculate())**
يوضح الرمز النموذجي التالي استخدام خاصية [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive). يرجى تنفيذ هذا الرمز مع [ملف إكسل عينة محدد](5472288.xlsx) والتحقق من الناتج في وحدة التحكم. ستجد أن تعيين الخاصية التكرارية على **false** قلل وقت الحساب بشكل ملحوظ. يرجى أيضًا قراءة التعليقات لفهم أفضل لهذه الخاصية.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **مخرجات الوحدة**
هذا هو ناتج وحدة التحكم من الرمز النموذجي أعلاه عند تنفيذه مع [ملف إكسل عينة محدد](5472288.xlsx) على جهازنا. يرجى ملاحظة، قد تختلف الناتج ولكن سيكون الوقت المنقضي بعد تعيين الخاصية التكرارية على **false** دائمًا أقل من تعيينها على **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
