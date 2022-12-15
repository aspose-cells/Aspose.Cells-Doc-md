---
title: كشف المرجع الدائري
type: docs
weight: 70
url: /ar/net/detecting-circular-reference/
---
## **مقدمة**

يمكن أن تحتوي المصنفات على مراجع دائرية وفي بعض الأحيان تكون هناك حاجة لاكتشاف ما إذا كانت المراجع الدائرية موجودة أم لا.

## **المفهوم الكامن وراء الكشف عن المرجع الدائري**

لا يمكن اكتشاف المراجع الدائرية إلا عند حساب الصيغة لأن مراجع إحدى الصيغ تعتمد بشكل عام على النتيجة المحسوبة للأجزاء الأخرى أو الصيغ الأخرى. لذلك نحن نقدم واجهات برمجة تطبيقات جديدة لهذا المطلب (لتجميع الخلايا ذات المراجع الدائرية) في عملية حساب الصيغة:

[**حساب الخلية**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): يمثل حساب البيانات ذات الصلة حول خلية واحدة يتم حسابها

[**AbstractCalculationMonitor.onCircular (IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): سيتم استدعاؤه بواسطة محرك حساب الصيغة عند مواجهة مراجع دائرية ، يكون العنصر الموجود في العداد[**حساب الخلية**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) كائنات تمثل جميع الخلايا في دائرة واحدة. تشير القيمة التي تم إرجاعها إلى ما إذا كان محرك الصيغة يحتاج إلى حساب تلك الخلايا بشكل دائري بعد هذا الاستدعاء.

 يجوز للمستخدم جمع تلك المراجع المعممة في تنفيذ[**AbstractCalculationMonitor.onCircular ()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) طريقة.

يمكن تنزيل ملف العينة المصدر من الرابط التالي:

[معاد الصيغ. xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

تعريف ال*CircularMonitor* فئة مشتقة من[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) الطبقة على النحو التالي:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
