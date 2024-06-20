---
title: استخدام ميزة AbstractCalculationEngine
type: docs
weight: 20
url: /ar/cpp/using-abstractcalculationengine-feature/
---

## لا تزال الميزات تحت التطوير، فترقبوا المزيد.


## **مقدمة**
يوفر هذا المقال فهمًا لكيفية استخدام ميزة [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) لتنفيذ الوظائف المخصصة باستخدام واجهات برمجة التطبيقات Aspose.Cells.

<!--

تتيح واجهة AbstractCalculationEngine إمكانية إضافة وظائف حسابية مخصصة لتوسيع محرك حسابي النواة في Aspose.Cells لتلبية متطلبات معينة. تعتبر هذه الميزة مفيدة لتحديد الوظائف المخصصة في ملف قالب أو في كود حيث يمكن تنفيذ الوظيفة المخصصة وتقييمها باستخدام واجهات برمجة التطبيقات Aspose.Cells مثل أي وظيفة أخرى افتراضية في Microsoft Excel.
## **استخدام ميزة AbstractCalculationEngine**
يقوم الشيفرة المرفقة بتنفيذ واجهة AbstractCalculationEngine التي تقوم بتقييم وإرجاع قيم الوظائف المخصصة الاثنتين، وهي MySampleFunc() و YourSampleFunc(). توجد هذه الوظائف المخصصة داخل الخلايا A1 و A2 على التوالي. ثم، تستدعي طريقة Workbook.CalculateFormula(const CalculationOptions& options) لاستدعاء تنفيذ واجهة AbstractCalculationEngine.Calculate(CalculationData& data). بعد ذلك، يتم طباعة قيم A1 و A2 على الوحدة النمطية. يرجى الرجوع إلى مخرجات الوحدة النمطية للشيفرة المرفقة بالأسفل للمزيد من المساعدة.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature-new.cpp" >}}


## **مخرجات الوحدة**
{{< highlight java >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
-->
