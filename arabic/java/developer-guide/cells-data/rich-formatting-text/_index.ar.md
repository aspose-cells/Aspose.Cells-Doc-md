---
title: قم بالوصول إلى أجزاء النص المنسق وتحديثها في Cell
linktitle: نص منسق
type: docs
weight: 440
url: /ar/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells يسمح لك بالتوصل وتحديث أجزاء النص المنسق للخانة. لهذا الغرض ، يمكنك استخدام أساليب Cell.getCharacters () و Cell.setCharacters (). ستعود هذه الطرق وتقبل مصفوفة كائنات FontSetting التي يمكنك استخدامها للوصول إلى الخصائص المختلفة للخط وتحديثها مثل اسم الخط ولون الخط والجرأة وما إلى ذلك.

{{% /alert %}} 
## **قم بالوصول إلى أجزاء النص المنسق وتحديثها في Cell**
 يوضح الكود التالي استخدام الأسلوبين Cell.getCharacters () و Cell.setCharacters () باستخدام[ملف اكسل المصدر](5472937.xlsx) والتي يمكنك تنزيلها من الرابط المقدم. يحتوي ملف Excel المصدر على نص منسق في الخلية A1. يحتوي على 3 أجزاء ولكل جزء خط مختلف. سنصل إلى هذه الأجزاء ونحدث الجزء الأول باسم خط جديد. أخيرًا ، يحفظ المصنف باسم[ملف اكسل الناتج](5472930.xlsx) . عندما تفتحه ، ستجد أن خط الجزء الأول من النص قد تغير إلى**"اريال"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **إخراج وحدة التحكم**
 هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه باستخدام[ملف اكسل المصدر](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
