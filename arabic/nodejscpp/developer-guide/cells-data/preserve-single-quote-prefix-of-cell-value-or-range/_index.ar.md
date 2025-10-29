---
title: الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق
type: docs
weight: 310
url: /ar/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: تعرف على كيفية الحفاظ على بادئة الاقتباس الأحادي لقيمة أو نطاق الخلية من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: الحفاظ على بادئة الاقتباس الأحادي لقيمة أو نطاق الخلية Node.js عبر C++، إخفاء الفاصلة العليا أو علامة الاقتباس الأحاديه في البداية Node.js عبر C++، إظهار الفاصلة العليا أو علامة الاقتباس الأحاديه في البداية Node.js عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

عندما تضع قيمة ما داخل الخلية التي تحتوي على رمز تأشيرة أو علامة اقتباس أحادية في البداية، يخفي Microsoft Excel ذلك، ولكن عند تحديد الخلية، يعرض الرمز التأشيري أو الاقتباس الأحادي في شريط الصيغة كما هو مبين في لقطة الشاشة التالية.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

 يختفي Aspose.Cells for Node.js via C++ أيضًا الفاصلة العليا أو علامة الاقتباس الأحاديه مثل Microsoft Excel ولكنه يضبط [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) على **true** لتلك الخلية. إذا قمت بضبط نمط فارغ للخلية، فإن [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) يعود ليصبح **false** مرة أخرى. للتعامل مع هذه المسألة، يوفر Aspose.Cells for Node.js via C++ طريقة [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)، عند ضبطها على **false**، لا يتم تحديث [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) على الإطلاق ويحتفظ بقيمته القديمة. وهذا يعني إذا كانت القيمة القديمة لـ [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) كانت **true**، فسوف تظل **true**، وإذا كانت **false**، فستظل **false**.

## **الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق**

يوضح الكود التجريبي التالي كيفية استخدام طريقة [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) كما هو موضح سابقًا. يرجى قراءة التعليقات داخل الكود ورؤية إخراج الوحدة في الأسفل للمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **مخرجات الوحدة**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
