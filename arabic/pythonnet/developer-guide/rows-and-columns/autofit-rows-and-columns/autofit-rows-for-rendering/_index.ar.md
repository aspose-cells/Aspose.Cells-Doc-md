---
title: تحجيم الصفوف تلقائيًا للتقديم
type: docs
weight: 130
url: /ar/python-net/autofit-rows-for-rendering/
description: تعلم كيفية تكييف الصفوف للتقديم من خلال واجهة برمجة التطبيقات Aspose.Cells للبيثون via .NET.
keywords: مكتبة Excel للبيثون، تكييف الصفوف للتقديم بلغة البيثون، والتكييف التلقائي لارتفاع الصف عند فتح ملف Excel. 
---

عموما، عندما ترغب في عرض كامل النص في خلية، يمكنك تحجيم الصف في العرض العادي بنسبة تكبير 100% في Microsoft Excel. يسمح ذلك بظهور النص بشكل كامل في العرض العادي، وحتى عند الطباعة أو حفظ الملف كملف PDF، سيتم عرض النص بشكل صحيح.

ومع ذلك، في بعض الحالات، يعمل تحجيم الصف بشكل جيد في العرض العادي، ولكن عند التبديل إلى وضع الطباعة أو حفظ الملف كملف PDF، يتم قص النص. يرجى التحقق من ملف المصدر [Book1.xlsx](Book1.xlsx) واللقطات.

![تم قص النص في عرض الطباعة](text_clipped_in_printview.png)

إذا كنت ترغب في منع قص النص في ملف PDF المحفوظ، يمكنك تكييف الصف بخيار [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

الآن، لم يتم قص النص في ملف PDF الناتج.

![النص لم يتم قصه في ملف PDF المحفوظ](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="python-net" >}}
