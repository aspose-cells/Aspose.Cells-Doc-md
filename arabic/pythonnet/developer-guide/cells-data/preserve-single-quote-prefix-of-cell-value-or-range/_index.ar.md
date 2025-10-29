---
title: الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق
type: docs
weight: 310
url: /ar/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: تعلم كيفية الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق من خلال Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel ، الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق في Python ، إخفاء الفواصل الآولية أو علامة الاقتباس الفردية في Python ، إظهار الفواصل الآولية أو علامة الاقتباس الفردية في Python
---

## **سيناريوهات الاستخدام المحتملة**

عندما تضع قيمة ما داخل الخلية التي تحتوي على رمز تأشيرة أو علامة اقتباس أحادية في البداية، يخفي Microsoft Excel ذلك، ولكن عند تحديد الخلية، يعرض الرمز التأشيري أو الاقتباس الأحادي في شريط الصيغة كما هو مبين في لقطة الشاشة التالية.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

يخفي Aspose.Cells for Python via .NET أيضا الرمز التأشيري أو الاقتباس الأحادي مثل Microsoft Excel ولكنه يضبط [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) على **صحيح** لهذه الخلية. إذا قمت بضبط نمط فارغ للخلية، فإن [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) تصبح **خاطئة** مرة أخرى. من أجل التعامل مع هذه المشكلة، يوفر Aspose.Cells for Python via .NET خاصية [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)، عندما تكون مضبوطة **خاطئة**، ثم [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) لا يتم تحديثه على الإطلاق ويتم الاحتفاظ بقيمته القديمة. هذا يعني إذا كانت القيمة القديمة لخاصية [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) كانت **صحيحة**، فإنها ستظل **صحيحة** وإذا كانت القيمة القديمة كانت **خاطئة**، فإنها ستظل **خاطئة**.

## **الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق**

يشرح رمز العينة التالي استخدام الخاصية [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) كما هو موضح سابقا. يرجى قراءة التعليقات داخل الكود ورؤية نتائج الكونسول للكود المعطى أدناه لمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
