---
title: الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق
type: docs
weight: 1900
url: /ar/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **سيناريوهات الاستخدام المحتملة**

عندما تضع قيمة ما داخل الخلية التي تحتوي على رمز تأشيرة أو علامة اقتباس أحادية في البداية، يخفي Microsoft Excel ذلك، ولكن عند تحديد الخلية، يعرض الرمز التأشيري أو الاقتباس الأحادي في شريط الصيغة كما هو مبين في لقطة الشاشة التالية.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

تخفي Aspose.Cells أيضًا العلامة اقتباس رئيسية أو علامة اقتباس واحدة مثل Microsoft Excel ولكنها تعين الـ [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) كـ **صحيحة** لتلك الخلية. إذا قمت بتعيين نمط فارغ للخلية، فإن [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) تصبح **false** مرة أخرى. من أجل التعامل مع هذه المشكلة، توفر Aspose.Cells خاصية [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)، عندما يتم تعيين **false**، فإن [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) لا يُحدث على الإطلاق ويتم الاحتفاظ بقيمته القديمة. يعني إذا كانت القيمة القديمة لخاصية [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) كانت **صحيحة**، فستظل صحيحة وإذا كانت القيمة القديمة كانت خاطئة، فستظل خاطئة.

## **الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق**

يشرح الكود النموذجي التالي استخدام الخاصية [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) كما هو موضح سابقًا. يُرجى قراءة التعليقات داخل الكود ورؤية الإخراج الموجود في وحدة التحكم للكود المعطى أدناه للحصول على مزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
