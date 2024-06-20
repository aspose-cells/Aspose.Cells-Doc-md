---
title: كشف الإشارة المرجعية الدائرية
type: docs
weight: 70
url: /ar/java/detecting-circular-reference/
---

## **مقدمة**

يمكن أن تحتوي الدفاتر على إشارات مرجعية دائرية وأحيانًا هناك حاجة للكشف عما إذا كانت هناك إشارات مرجعية دائرية أم لا.

## **المفهوم الكامن وراء كشف الإشارة المرجعية الدائرية**

يمكن فقط كشف الإشارات المرجعية الدائرية عند حساب الصيغة لأن الإشارات في صيغة واحدة تعتمد عادة على النتيجة المحسوبة لأجزاء أخرى أو صيغ أخرى. لذا نحن نوفر واجهات برمجة تطبيقات جديدة لهذا الاحتياج (لجمع الخلايا ذات الإشارات المرجعية الدائرية) في عملية حساب الصيغة:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): يمثل حساب البيانات ذات الصلة حول خلية تتم حسابها

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)): سيتم استدعاؤها بواسطة محرك حساب الصيغ عند مواجهة الإشارات المرجعية، العنصر في عنصر التعداد هو [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) كائنات تمثل جميع الخلايا في دائرة واحدة. القيمة المُرجَعة تُحدد ما إذا كان محرك الصيغ يحتاج إلى حساب تلك الخلايا في الدائرة بعد هذا الاستدعاء.

يمكن للمستخدم جمع تلك الإشارات المرجعية في تنفيذ الطريقة [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)).

يمكن تحميل ملف العينة المصدر من الرابط التالي:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

تعريف فئة *CircularMonitor* المشتقة من [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) على النحو التالي:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
