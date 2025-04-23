---
title: ابحث ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة.
type: docs
weight: 270
url: /ar/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: تعلم كيفية البحث ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة من خلال Aspose.Cells for .NET API.
keywords: العثور على قيمة الخلية التي تبدأ بعلامة اقتباس واحدة، البحث عن قيمة الخلية التي تبدأ بعلامة اقتباس واحدة
---

{{% alert color="primary" %}}

Aspose.Cells الآن يوفر خاصية [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) للعثور على ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة. قبل هذه الخاصية، لم يكن هناك طريقة للتمييز بين سلاسل مثل عينة و 'عينة وما إلى ذلك.

{{% /alert %}}

الشيفرة العينية التالية تشرح أن السلاسل مثل عينة و 'عينة لا يمكن تمييزها باستخدام الخاصية [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue). لذلك يجب علينا استخدام الخاصية [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) للتمييز بينهما.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
{{< app/cells/assistant language="csharp" >}}
