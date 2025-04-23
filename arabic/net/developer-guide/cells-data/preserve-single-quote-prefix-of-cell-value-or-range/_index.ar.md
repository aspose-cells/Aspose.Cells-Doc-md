---
title: الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق
type: docs
weight: 310
url: /ar/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: تعلم كيفية الحفاظ على بادئة علامة اقتباس واحدة لقيمة الخلية أو النطاق من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: الحفاظ على بادئة علامة اقتباس واحدة لقيمة الخلية أو النطاق، إخفاء الرصاصة بادئة أو علامة اقتباس واحدة، إظهار الرصاصة بادئة أو علامة اقتباس واحدة
---

## **سيناريوهات الاستخدام المحتملة**

عندما تضع قيمة ما داخل الخلية التي تحتوي على رمز تأشيرة أو علامة اقتباس أحادية في البداية، يخفي Microsoft Excel ذلك، ولكن عند تحديد الخلية، يعرض الرمز التأشيري أو الاقتباس الأحادي في شريط الصيغة كما هو مبين في لقطة الشاشة التالية.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

تخفي Aspose.Cells أيضًا بادئة الرصاصة الأو علامة اقتباس واحدة مثل Microsoft Excel ولكنها تضبط [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) لتلك الخلية على **صحيح**. إذا قمت بتعيين نمط فارغ للخلية، فإن [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) تصبح **خاطئة** مرة أخرى. من أجل التعامل مع هذه المشكلة، توفر Aspose.Cells خاصية [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)، عندما يتم تعيينها **خاطئة**، فإن [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) لا يتم تحديثها على الإطلاق ويتم الاحتفاظ بقيمتها القديمة. وهذا يعني إذا كانت القيمة القديمة للخاصية [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) كانت **صحيحة**، فإنها ستظل **صحيحة**، وإذا كانت القيمة القديمة كانت **خاطئة**، فإنها ستظل **خاطئة**.

## **الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق**

يشرح رمز العينة التالي استخدام الخاصية [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) كما هو موضح سابقا. يرجى قراءة التعليقات داخل الكود ورؤية نتائج الكونسول للكود المعطى أدناه لمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
