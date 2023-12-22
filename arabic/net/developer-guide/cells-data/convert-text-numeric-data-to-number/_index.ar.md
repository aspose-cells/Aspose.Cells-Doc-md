---
title: تحويل البيانات الرقمية النصية إلى رقم
type: docs
weight: 900
url: /ar/net/convert-text-numeric-data-to-number/
description: تعرف على كيفية تحويل الأرقام المخزنة كنص في Excel إلى أرقام باستخدام Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
##  **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، تريد تحويل البيانات الرقمية المدخلة كنص إلى أرقام. يمكنك إدخال أرقام كنص في برنامج Excel Microsoft عن طريق وضع فاصلة عليا قبل الرقم، على سبيل المثال *'12345**. ثم يعامل Excel الرقم كسلسلة. Aspose.Cells يسمح لك بتحويل السلاسل إلى أرقام.


##  كيفية تحويل الأرقام المخزنة كنص إلى أرقام في إكسيل
يمكنك تحويل الأرقام المخزنة كنص إلى أرقام باتباع بعض الخطوات البسيطة.
1. حدد أي خلية مفردة أو نطاق من الخلايا يحتوي على مؤشر خطأ في الزاوية العلوية اليسرى.
1.  بجوار الخلية المحددة أو نطاق الخلايا المحدد، انقر فوق زر الخطأ الذي يظهر. في القائمة، انقر فوق تحويل إلى رقم.
<br>
<img src="4.png" width=70% />
1. إذا لم يكن زر التنبيه متوفرًا، فحدد عمودًا يحتوي على هذه المشكلة. إذا كنت لا تريد تحويل العمود بأكمله، فيمكنك تحديد خلية واحدة أو أكثر بدلاً من ذلك. فقط تأكد من أن الخلايا التي تحددها موجودة في نفس العمود، وإلا فلن تنجح هذه العملية. يُستخدم زر النص إلى أعمدة عادةً لتقسيم عمود، ولكن يمكن استخدامه أيضًا لتحويل عمود واحد من النص إلى أرقام. في علامة التبويب بيانات، انقر فوق تحويل النص إلى أعمدة.
<br>
<img src="1.png" width=70% />
1. انقر فوق الزر "إنهاء" في المربع المنبثق.
<br>
<img src="2.png" width=70% />
1. يتم تحويل الأرقام المخزنة كنص إلى أرقام.
<br>
<img src="3.png" width=70% />

## كيفية تحويل الأرقام المخزنة كنص إلى أرقام باستخدام Aspose.Cells for .NET
Aspose.Cells يوفر[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)الطريقة التي يمكن استخدامها لتحويل جميع البيانات الرقمية النصية أو النصية إلى أرقام.

تعرض لقطة الشاشة التالية أرقام السلسلة في الخلايا *A1:A17**. تتم محاذاة أرقام السلسلة إلى اليسار.
<br>
<img src="5.png" width=70% />

 تم تحويل أرقام السلسلة هذه إلى أرقام باستخدام[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)في لقطة الشاشة التالية. كما ترون، فهي الآن محاذاة إلى اليمين.
<br>
<img src="6.png" width=70% />

##  كود C# لتحويل البيانات الرقمية إلى أرقام فعلية

يوضح نموذج التعليمات البرمجية التالي كيفية تحويل كافة البيانات الرقمية سلسلة إلى أرقام فعلية في كافة أوراق العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
