---
title: أدخل Cell بيانات ورقة عمل GridWeb بتنسيق النسبة المئوية
type: docs
weight: 1010
url: /ar/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **سيناريوهات الاستخدام الممكنة**
يدعم GridWeb الآن المستخدمين لإدخال بيانات الخلية بتنسيق النسبة المئوية مثل 3٪ وسيتم تنسيق البيانات الموجودة في الخلية تلقائيًا كـ 3.00٪. ومع ذلك ، سيتعين عليك تعيين نمط الخلية إلى تنسيق النسبة المئوية وهو إما GridTableItemStyle.NumberType a 9 أو 10. سيتم تنسيق الرقم 9 3٪ كـ 3٪ ولكن الرقم 10 سيتم تنسيقه 3٪ كـ 3.00٪.

{{% alert color="primary" %}} 

إذا لم تقم بتعيين نمط الخلية على تنسيق النسبة المئوية ، فسيتم عرض بيانات الإدخال 3٪ على أنها 0.03.

{{% /alert %}} 
## **أدخل Cell بيانات ورقة عمل GridWeb بتنسيق النسبة المئوية**
يعين نموذج التعليمات البرمجية التالي الخلية A1 GridTableItemStyle.NumberType كـ 10 ، وبالتالي يتم تنسيق بيانات الإدخال 3٪ تلقائيًا كـ 3.00٪ كما هو موضح في لقطة الشاشة.

![ما يجب القيام به: image_بديل_نص](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **عينة من الرموز**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






