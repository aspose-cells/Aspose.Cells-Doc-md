---
title: إدخال بيانات الخلية لورقة عمل GridWeb بتنسيق النسبة المئوية
type: docs
weight: 80
url: /ar/net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: يقدم هذا المقال إدخال بيانات الخلية بتنسيق النسبة المئوية في GridWeb.
---


## **سيناريوهات الاستخدام المحتملة**
يدعم GridWeb الآن المستخدمين في إدخال بيانات الخلية بتنسيق النسبة مثل 3٪ وسيتم تنسيق البيانات في الخلية تلقائيًا كـ 3.00٪. ومع ذلك ، سيتعين عليك تعيين نمط الخلية إلى تنسيق النسبة وهو إما GridTableItemStyle.NumberType 9 أو 10. سيقوم الرقم 9 بتنسيق 3٪ كـ 3٪ ولكن الرقم 10 سيقوم بتنسيق 3٪ كـ 3.00٪.

{{% alert color="primary" %}} 

إذا لم تقم بتعيين نمط الخلية إلى تنسيق النسبة ، فسيتم عرض بيانات الإدخال 3٪ على أنه 0.03.

{{% /alert %}} 
## **إدخال بيانات الخلية لورقة العمل GridWeb بتنسيق النسبة**
الكود النموذجي التالي يضبط الخلية A1 GridTableItemStyle.NumberType كرقم 10، وبالتالي سيتم تنسيق بيانات الإدخال 3٪ تلقائياً كـ 3.00٪ كما هو موضح في اللقطة.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **الكود المثالي**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
