---
title: نسخ بيانات النطاق بالنمط
type: docs
weight: 610
url: /ar/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[نسخ بيانات النطاق فقط](/cells/ar/net/copy-range-data-only/) شرح كيفية نسخ البيانات من نطاق من الخلايا إلى نطاق آخر. على وجه التحديد ، طبقت العملية مجموعة جديدة من الأنماط على الخلايا المنسوخة. يمكن Aspose.Cells أيضًا نسخ نطاق كامل بالتنسيق. يشرح هذا المقال كيف.

{{% /alert %}}

يوفر Aspose.Cells مجموعة من الفئات والطرق للعمل مع النطاقات ، على سبيل المثال ،[**CreateRange ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**النمط**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) و[**تطبيق ستايل ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

هذا المثال:

1. يقوم بإنشاء مصنف.
1. يملأ عددًا من الخلايا في ورقة العمل الأولى بالبيانات.
1.  يخلق أ[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  يخلق أ[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) كائن بسمات تنسيق محددة.
1. يطبق النمط على نطاق البيانات.
1. ينشئ نطاقًا ثانيًا من الخلايا.
1. ينسخ البيانات بالتنسيق من النطاق الأول إلى النطاق الثاني.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
