---
title: وظيفة التوحيد
type: docs
weight: 20
url: /ar/net/consolidation-function/
---

## **وظيفة التوحيد**

يمكن استخدام Aspose.Cells لتطبيق وظيفة التوحيد على حقول البيانات (أو حقول القيم) لجدول Pivot. في Microsoft Excel، يمكنك نقر بزر الماوس الأيمن على حقل القيم ومن ثم تحديد اختيار **إعدادات حقل القيم...** ثم تحديد علامة **تلخيص القيم بواسطة**. من هناك، يمكنك تحديد أي وظيفة توحيد تفضل مثل Sum، Count، Average، Max، Min، Product، Distinct Count، إلخ.

يوفر Aspose.Cells تعدادًا [**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) لدعم وظائف التوحيد التالية.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

### **تطبيق وظيفة التوحيد على حقول البيانات لجدول الإحصائيات**

يطبق الكود التالي وظيفة تجميع **المتوسط** على الحقل الأول من البيانات (أو حقل القيمة) ووظيفة تجميع **عدد فريد** على الحقل الثاني من البيانات (أو حقل القيمة).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

دعم وظيفة تجميع العدد المميز من قبل Microsoft Excel 2013 فقط.

{{% /alert %}}
