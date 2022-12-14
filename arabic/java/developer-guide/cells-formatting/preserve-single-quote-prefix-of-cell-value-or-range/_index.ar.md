---
title: احتفظ ببادئة اقتباس فردية بقيمة Cell أو نطاق
type: docs
weight: 1900
url: /ar/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تضع بعض القيمة داخل الخلية التي تحتوي على فاصلة عليا أو علامة اقتباس مفردة ، فإن Microsoft يقوم Excel بإخفائها ، ولكن عند تحديد الخلية ، فإنها تعرض الفاصلة العليا أو علامة الاقتباس الفردية في شريط الصيغة كما هو موضح في لقطة الشاشة التالية.

![ما يجب القيام به: image_بديل_نص](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

يخفي Aspose.Cells أيضًا الفاصلة العليا أو الاقتباس الفردي مثل Microsoft Excel ولكنه يحدد[**النمط**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) كما**حقيقي** لتلك الخلية. إذا قمت بتعيين نمط فارغ للخلية ، فحينئذٍ[**النمط**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) يصبح**خاطئة** تكرارا. من أجل التعامل مع هذه المشكلة ، يوفر Aspose.Cells[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) الملكية ، عندما يتم تعيينها**خاطئة**، ومن بعد[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)لم يتم تحديثه على الإطلاق ويتم الاحتفاظ بقيمته القديمة. هذا يعني إذا كانت القيمة القديمة[**النمط**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)كانت الممتلكات**حقيقي**، سيبقى صحيحًا وإذا كانت القيمة القديمة خاطئة ، فستظل خاطئة.

## **احتفظ ببادئة اقتباس فردية بقيمة Cell أو نطاق**

يشرح نموذج التعليمات البرمجية التالي استخدام[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)الخاصية كما هو موضح سابقًا. يرجى قراءة التعليقات الموجودة داخل الكود والاطلاع على إخراج وحدة التحكم للرمز الوارد أدناه للحصول على مزيد من المساعدة.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
