---
title: حفظ بادئة الاقتباس المفرد لقيّم الخلية أو النطاق باستخدام Golang عبر C++
linktitle: الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق
type: docs
weight: 310
url: /ar/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: تعلم كيفية الحفاظ على بادئة الاقتباس المفرد ل قيمة الخلية أو النطاق من خلال API Aspose.Cells for C++.
keywords: الحفاظ على بادئة علامة اقتباس واحدة لقيمة الخلية أو النطاق، إخفاء الرصاصة بادئة أو علامة اقتباس واحدة، إظهار الرصاصة بادئة أو علامة اقتباس واحدة
---

## **سيناريوهات الاستخدام المحتملة**

عندما تضع قيمة داخل الخلية وتحتوي على فاصلة بادئة أو علامة اقتباس مفردة، فإن مايكروسوفت إكسل يخفيها، ولكن عند تحديد الخلية، يعرض الفاصلة أو علامة الاقتباس المفردة في شريط الصيغة كما هو موضح في لقطة الشاشة التالية.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

كما يخفي Aspose.Cells الفاصلة أو علامة الاقتباس المفردة كما في مايكروسوفت إكسل، لكنه يضبط [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) على أنه **true** لتلك الخلية. إذا قمت بضبط نمط فارغ للخلية، يصبح [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) **false** مرة أخرى. للتعامل مع هذه المشكلة، يوفر Aspose.Cells الخاصية [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/)، عندما تتم ضبطها على **false**، فإن [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) لن يتم تحديثه على الإطلاق ويحتفظ بقيمته القديمة. هذا يعني أنه إذا كانت القيمة القديمة لخاصية [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) كانت **true**، فستظل **true**، وإذا كانت خاطئة، فستظل خاطئة.

## **الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق**

الشفرة النموذجية التالية تشرح كيفية استخدام الخاصية [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/) كما هو موضح سابقًا. يرجى قراءة التعليقات داخل الكود ومشاهدة خرج وحدة التحكم للرمز أدناه للمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **مخرجات الوحدة**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
