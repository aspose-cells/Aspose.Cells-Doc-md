---
title: احتفظ ببادئة اقتباس فردية بقيمة Cell أو نطاق
type: docs
weight: 310
url: /ar/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تضع بعض القيمة داخل الخلية التي تحتوي على فاصلة عليا أو علامة اقتباس مفردة ، فإن Microsoft يقوم Excel بإخفائها ، ولكن عند تحديد الخلية ، فإنها تعرض الفاصلة العليا أو علامة الاقتباس الفردية في شريط الصيغة كما هو موضح في لقطة الشاشة التالية.

![ما يجب القيام به: image_بديل_نص](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

يخفي Aspose.Cells أيضًا الفاصلة العليا أو الاقتباس الفردي مثل Microsoft Excel ولكنه يحدد[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) كما**حقيقي** لتلك الخلية. إذا قمت بتعيين نمط فارغ للخلية ، فحينئذٍ[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) يصبح**خاطئة** تكرارا. من أجل التعامل مع هذه المشكلة ، يوفر Aspose.Cells[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) الملكية ، عندما يتم تعيينها**خاطئة** ، ومن بعد[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)لم يتم تحديثه على الإطلاق ويتم الاحتفاظ بقيمته القديمة. هذا يعني إذا كانت القيمة القديمة[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)كانت الممتلكات**حقيقي** ، ستبقى**حقيقي** وإذا كانت القيمة القديمة**خاطئة** ، ستبقى**خاطئة**.

## **احتفظ ببادئة اقتباس فردية بقيمة Cell أو نطاق**

 يشرح نموذج التعليمات البرمجية التالي استخدام[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)الخاصية كما هو موضح سابقًا. يرجى قراءة التعليقات الموجودة داخل الكود والاطلاع على إخراج وحدة التحكم للرمز الوارد أدناه للحصول على مزيد من المساعدة.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
