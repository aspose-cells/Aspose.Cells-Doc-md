---
title: استخدام ميزة ICustomFunction
type: docs
weight: 20
url: /ar/cpp/using-icustomfunction-feature/
---
## **مقدمة**
تقدم هذه المقالة فهمًا لكيفية استخدام ميزة ICustomFunction لتنفيذ وظائف مخصصة مع واجهات برمجة التطبيقات Aspose.Cells.

تتيح لك واجهة ICustomFunction إضافة وظائف حساب الصيغة المخصصة لتوسيع محرك الحساب الأساسي Aspose.Cells من أجل تلبية متطلبات معينة. هذه الميزة مفيدة لتحديد وظائف مخصصة (محددة من قبل المستخدم) في ملف قالب أو في رمز حيث يمكن تنفيذ الوظيفة المخصصة وتقييمها باستخدام واجهات برمجة تطبيقات Aspose.Cells مثل أي وظيفة إكسل Microsoft افتراضية أخرى.
## **استخدام ميزة ICustomFunction**
يقوم نموذج التعليمات البرمجية التالي بتنفيذ واجهة ICustomFunction التي تقوم بتقييم وإرجاع قيم الوظيفتين المخصصتين مثل MySampleFunc () و YourSampleFunc (). توجد هذه الوظائف المخصصة داخل الخلايا A1 و A2 على التوالي. ثم تقوم باستدعاء طريقة IWorkbook.CalculateFormula (false، ICustomFunction) لاستدعاء تنفيذ طريقة ICustomFunction.CalculateCustomFunction (). بعد ذلك ، يقوم بطباعة قيم A1 و A2 على وحدة التحكم والتي هي في الواقع القيم التي تم إرجاعها بواسطة ICustomFunction.CalculateCustomFunction (). الرجاء مراجعة إخراج وحدة التحكم لنموذج التعليمات البرمجية أدناه للحصول على مزيد من المساعدة.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **إخراج وحدة التحكم**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
