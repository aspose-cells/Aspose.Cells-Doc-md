---
title: صفوف الاحتواء التلقائي للعرض
type: docs
weight: 130
url: /ar/net/autofit-rows-for-rendering/
---
بشكل عام، عندما تريد عرض كل النص في خلية، يمكنك احتواء الصف تلقائيًا في العرض العادي مع تكبير بنسبة 100% في Microsoft Excel. يتيح ذلك أن يكون النص مرئيًا بالكامل في العرض العادي، وحتى عند طباعة الملف أو حفظه كـ PDF، سيتم عرض النص بشكل صحيح.

 ومع ذلك، في بعض الحالات، يعمل صف الاحتواء التلقائي بشكل جيد في العرض العادي، ولكن عند التبديل إلى عرض الطباعة أو حفظ الملف كـ PDF، يتم قص النص. يرجى التحقق من الملف المصدر[Book1.xlsx](Book1.xlsx) ولقطات الشاشة.

![يتم قص النص في طريقة عرض الطباعة](text_clipped_in_printview.png)

إذا كنت تريد منع قص النص في الملف المحفوظ PDF، فيمكنك ضبط الصف تلقائيًا باستخدام[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/forrendering/) خيار.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Autofit-AutofitRowsForRendering.cs" >}}

الآن، لم يتم قص النص في ملف الإخراج PDF.

![لا يتم قص النص في ملف pdf المحفوظ](text_not_clipped_in_saved_pdf.png)