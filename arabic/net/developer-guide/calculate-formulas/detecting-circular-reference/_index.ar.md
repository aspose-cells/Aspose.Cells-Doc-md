---
title: الكشف عن المرجع الدائري
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells للكشف عن المراجع الدائرية في Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الطريقة التي يوفرها Aspose.Cells للكشف عن المراجع الدائرية والحصول على النتائج. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /ar/net/detecting-circular-reference/
---
##  **مقدمة**

يمكن أن تحتوي المصنفات على مراجع دائرية وفي بعض الأحيان تكون هناك حاجة لاكتشاف ما إذا كانت المراجع الدائرية موجودة أم لا.

##  **المفهوم الكامن وراء الكشف عن المرجع الدائري**

لا يمكن اكتشاف المراجع الدائرية إلا عند حساب الصيغة لأن مراجع صيغة واحدة تعتمد عادةً على النتيجة المحسوبة لأجزاء أخرى أو صيغ أخرى. لذلك نقدم واجهات برمجة تطبيقات جديدة لهذا المطلب (لجمع الخلايا ذات المراجع الدائرية) في عملية حساب الصيغة:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): يمثل حساب البيانات ذات الصلة حول خلية واحدة يتم حسابها

[**AbstractCalculationMonitor.OnCircular(IEnumerator CircularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): سيتم استدعاؤه بواسطة محرك حساب الصيغة عند مواجهة مراجع دائرية، وهو العنصر الموجود في العداد[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) الكائنات التي تمثل جميع الخلايا في دائرة واحدة. تشير القيمة التي تم إرجاعها إلى ما إذا كان محرك الصيغة يحتاج إلى حساب تلك الخلايا بشكل دائري بعد هذا الاستدعاء.

 يجوز للمستخدم جمع تلك المراجع الدائرية في تنفيذ[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) طريقة.

يمكن تحميل ملف العينة المصدر من الرابط التالي:

[الصيغ الدائرية.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

تعريف ال*CircularMonitor* الطبقة التي تستمد من[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) الطبقة هي كما يلي:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
