---
title: حساب الوظائف المخصصة في GridWeb
type: docs
weight: 90
url: /ar/net/calculate-custom-functions-in-gridweb/
---
## **سيناريوهات الاستخدام الممكنة**
Aspose.Cells.GridWeb يدعم حساب الوظائف المخصصة بواسطة خاصية GridWeb.CustomCalculationEngine. تأخذ هذه الخاصية مثيل واجهة GridAbstractCalculationEngine. يرجى تنفيذ واجهة GridAbstractCalculationEngine وحساب وظائفك المخصصة بمنطقك الخاص.
## **حساب الوظائف المخصصة في GridWeb**
يضيف نموذج التعليمات البرمجية التالي دالة مخصصة تسمى MYTESTFUNC () في الخلية B3. ثم نحسب قيمة هذه الوظيفة من خلال تنفيذ واجهة GridAbstractCalculationEngine. نحسب MYTESTFUNC () بطريقة تضرب المعلمة مع 2 وتعيد النتيجة. لذلك إذا كانت المعلمة 9 ، فستعيد 2 * 9 = 18.
### **عينة من الرموز**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
