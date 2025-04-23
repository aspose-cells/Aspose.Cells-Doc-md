---
title: الوصول وتحديث أجزاء النص الغني للخلية
linktitle: تنسيق النص الغني
type: docs
weight: 440
url: /ar/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

يسمح Aspose.Cells لك بالوصول وتحديث أجزاء النص الغني للخلية. لهذا الغرض، يمكنك استخدام الطرق Cell.getCharacters() و Cell.setCharacters(). ستعيد وتقبل هذه الطرق مصفوفة من كائنات FontSetting التي يمكنك استخدامها للوصول وتحديث مختلف خصائص الخط مثل اسم الخط، لون الخط، والعراجيّة وما إلى ذلك.

{{% /alert %}} 
## **الوصول إلى وتحديث أجزاء النص الغني للخلية**
يوضح الكود التالي استخدام الطرق Cell.getCharacters() و Cell.setCharacters() باستخدام [ملف الإكسل المصدر](5472937.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يحتوي ملف الإكسل المصدر على نص غني في الخلية A1. يحتوي على 3 أجزاء وكل جزء له خط مختلف. سنوصل إلى هذه الأجزاء ونحدث الجزء الأول باسم خط جديد. في النهاية، يقوم بحفظ دفتر العمل باسم [ملف الإكسل الناتج](5472930.xlsx). عند فتحه، ستجد أن خط الجزء الأول من النص قد تغير إلى **"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **مخرجات الوحدة**
فيما يلي مخرجات الكونسول للكود العينة أعلاه باستخدام [ملف الإكسل المصدر](5472937.xlsx).

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
