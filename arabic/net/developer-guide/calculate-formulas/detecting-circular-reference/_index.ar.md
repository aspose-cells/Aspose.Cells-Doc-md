---
title: كشف الإشارة المرجعية الدائرية
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لكشف الإشارات المرجعية الدائرية في Microsoft Excel. من خلال تحميل ملف Excel القائم أو إنشاء واحد جديد، يمكننا استخدام الطريقة المقدمة من Aspose.Cells لكشف الإشارات المرجعية الدائرية والحصول على النتائج. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، إشارات مرجعية دائرية، كشف
type: docs
weight: 70
url: /ar/net/detecting-circular-reference/
---

## **مقدمة**

يمكن أن تحتوي الدفاتر على إشارات مرجعية دائرية وأحيانًا هناك حاجة للكشف عما إذا كانت هناك إشارات مرجعية دائرية أم لا.

## **المفهوم الكامن وراء كشف الإشارة المرجعية الدائرية**

يمكن فقط كشف الإشارات المرجعية الدائرية عند حساب الصيغة لأن الإشارات في صيغة واحدة تعتمد عادة على النتيجة المحسوبة لأجزاء أخرى أو صيغ أخرى. لذا نحن نوفر واجهات برمجة تطبيقات جديدة لهذا الاحتياج (لجمع الخلايا ذات الإشارات المرجعية الدائرية) في عملية حساب الصيغة:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): يمثل حساب البيانات ذات الصلة حول خلية تتم حسابها

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): سيتم استدعاؤها بواسطة محرك حساب الصيغ عند مواجهة الإشارات المرجعية، العنصر في عنصر التعداد هو [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) كائنات تمثل جميع الخلايا في دائرة واحدة. القيمة المُرجَعة تُحدد ما إذا كان محرك الصيغ يحتاج إلى حساب تلك الخلايا في الدائرة بعد هذا الاستدعاء.

يمكن للمستخدم جمع تلك الإشارات المرجعية في تنفيذ الطريقة [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular).

يمكن تحميل ملف العينة المصدر من الرابط التالي:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

تعريف فئة *CircularMonitor* المشتقة من [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) على النحو التالي:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
