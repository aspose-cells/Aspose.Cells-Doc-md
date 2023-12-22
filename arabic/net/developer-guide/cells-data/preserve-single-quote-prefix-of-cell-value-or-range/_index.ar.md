---
title: احتفظ ببادئة الاقتباس المفردة ذات القيمة أو النطاق Cell
type: docs
weight: 310
url: /ar/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: تعرف على كيفية الحفاظ على بادئة الاقتباس المفردة للقيمة أو النطاق Cell من خلال Aspose.Cells for .NET API.
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---
##  **سيناريوهات الاستخدام المحتملة**

عندما تضع بعض القيمة داخل الخلية التي تحتوي على فاصلة عليا بادئة أو علامة اقتباس مفردة، فإن Microsoft يقوم Excel بإخفائها، ولكن عند تحديد الخلية، فإنها تعرض الفاصلة العليا البادئة أو علامة الاقتباس المفردة في شريط الصيغة كما هو موضح في لقطة الشاشة التالية.

![ما يجب القيام به:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells يخفي أيضًا الفاصلة العليا أو الاقتباس المفرد مثل Microsoft Excel ولكنه يعين[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) مثل**حقيقي** لتلك الخلية. إذا قمت بتعيين نمط فارغ للخلية، ثم[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) يصبح**خطأ شنيع** مرة أخرى. ولمعالجة هذه المشكلة يوفر Aspose.Cells[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) الممتلكات، عندما يتم تعيينها**false**، ثم لم يتم تحديث [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) على الإطلاق ويتم الاحتفاظ بقيمته القديمة . هذا يعني أنه إذا كانت القيمة القديمة لخاصية [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) **صحيحة**، فإنها سيبقى ** صحيحا** وإذا كانت القيمة القديمة *خطأ**، فستبقى *خطأ**.

##  **احتفظ ببادئة الاقتباس المفردة ذات القيمة أو النطاق Cell**

يشرح نموذج التعليمات البرمجية التالي استخدام[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)الممتلكات كما هو موضح سابقا. يرجى قراءة التعليقات الموجودة داخل الكود والاطلاع على مخرجات وحدة التحكم للكود الموضح أدناه للحصول على مزيد من المساعدة.

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

##  **إخراج وحدة التحكم**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
