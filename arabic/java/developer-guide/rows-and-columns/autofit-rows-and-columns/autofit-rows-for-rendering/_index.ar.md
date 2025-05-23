---
title: تحجيم الصفوف تلقائيًا للتقديم
type: docs
weight: 130
url: /ar/java/autofit-rows-for-rendering/
---

عموما، عندما ترغب في عرض كامل النص في خلية، يمكنك تحجيم الصف في العرض العادي بنسبة تكبير 100% في Microsoft Excel. يسمح ذلك بظهور النص بشكل كامل في العرض العادي، وحتى عند الطباعة أو حفظ الملف كملف PDF، سيتم عرض النص بشكل صحيح.

ومع ذلك، في بعض الحالات، يعمل تحجيم الصف بشكل جيد في العرض العادي، ولكن عند التبديل إلى وضع الطباعة أو حفظ الملف كملف PDF، يتم قص النص. يرجى التحقق من ملف المصدر [Book1.xlsx](Book1.xlsx) واللقطات.

![تم قص النص في عرض الطباعة](text_clipped_in_printview.png)

إذا كنت ترغب في منع قص النص في ملف PDF المحفوظ، يمكنك تحجيم الصف مع خيار [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

الآن، لم يتم قص النص في ملف PDF الناتج.

![النص لم يتم قصه في ملف PDF المحفوظ](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="java" >}}
