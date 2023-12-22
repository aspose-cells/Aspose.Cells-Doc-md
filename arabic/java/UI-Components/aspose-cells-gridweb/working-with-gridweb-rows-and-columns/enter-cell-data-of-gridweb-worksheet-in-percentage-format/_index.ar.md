---
title: أدخل Cell بيانات ورقة عمل GridWeb بتنسيق النسبة المئوية
type: docs
weight: 1010
url: /ar/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **سيناريوهات الاستخدام المحتملة**
يدعم GridWeb الآن المستخدمين لإدخال بيانات الخلية بتنسيق النسبة المئوية مثل 3% وسيتم تنسيق البيانات الموجودة في الخلية تلقائيًا على أنها 3.00%. ومع ذلك، سيتعين عليك تعيين نمط الخلية على تنسيق النسبة المئوية والذي يكون إما GridTableItemStyle.NumberType a 9 أو 10. سيتم تنسيق الرقم 9 3% كـ 3% ولكن الرقم 10 سيتم تنسيقه 3% كـ 3.00%.

{{% alert color="primary" %}} 

إذا لم تقم بتعيين نمط الخلية على تنسيق النسبة المئوية، فسيتم عرض البيانات المدخلة 3% على أنها 0.03.

{{% /alert %}} 
##  **أدخل Cell بيانات ورقة عمل GridWeb بتنسيق النسبة المئوية**
يقوم نموذج التعليمة البرمجية التالي بتعيين الخلية A1 GridTableItemStyle.NumberType على القيمة 10، وبالتالي يتم تنسيق بيانات الإدخال 3% تلقائيًا على أنها 3.00% كما هو موضح في لقطة الشاشة.

![ما يجب القيام به:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **عينة من الرموز**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






