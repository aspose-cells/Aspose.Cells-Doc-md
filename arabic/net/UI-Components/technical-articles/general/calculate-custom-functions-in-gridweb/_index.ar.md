---
title: حساب وظائف مخصصة في GridWeb
type: docs
weight: 90
url: /ar/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: يقدم هذا المقال ميزات الوظائف المخصصة في GridWeb.
---


## **سيناريوهات الاستخدام المحتملة**
يدعم Aspose.Cells.GridWeb حساب الوظائف المخصصة باستخدام خاصية GridWeb.CustomCalculationEngine. تأخذ هذه الخاصية مثيلًا لواجهة GridAbstractCalculationEngine. يرجى تنفيذ واجهة GridAbstractCalculationEngine وحساب الوظائف المخصصة الخاصة بك باستخدام منطقك الخاص.
## **حساب الوظائف المخصصة في GridWeb**
يضيف الكود المعاين التالي وظيفة مخصصة بالاسم MYTESTFUNC() في الخلية B3. ثم نحسب قيمة هذه الوظيفة عن طريق تنفيذ واجهة GridAbstractCalculationEngine. نحسب MYTESTFUNC() بطريقة تضرب معاملها بمقدار 2 ونعيد النتيجة. لذلك، إذا كان معاملها 9، سترجع 2*9 = 18.
### **الكود المثالي**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
