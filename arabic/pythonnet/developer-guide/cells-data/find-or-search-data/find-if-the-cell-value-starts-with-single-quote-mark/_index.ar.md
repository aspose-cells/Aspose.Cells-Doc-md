---
title: ابحث ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة.
type: docs
weight: 270
url: /ar/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: تعلم كيفية معرفة ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة من خلال Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel ، البحث عن قيمة الخلية التي تبدأ بعلامة اقتباس مفردة في Python ، البحث عن قيمة الخلية التي تبدأ بعلامة اقتباس مفردة في Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET يوفر الآن الخاصية [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) للعثور عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة. قبل هذه الخاصية ، لم يكن هناك طريقة للتمييز بين السلاسل مثل عينة و 'عينة'، وما إلى ذلك.

{{% /alert %}}

الشيفرة العينية التالية تشرح أن السلاسل مثل عينة و 'عينة لا يمكن تمييزها باستخدام الخاصية [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/). لذلك يجب علينا استخدام الخاصية [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) للتمييز بينهما.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
