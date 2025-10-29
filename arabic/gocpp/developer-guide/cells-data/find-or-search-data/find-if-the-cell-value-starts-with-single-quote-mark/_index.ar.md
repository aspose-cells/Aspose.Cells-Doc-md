---
title: اعثر إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة باستخدام Golang عبر C++
linktitle: ابحث ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة.
type: docs
weight: 270
url: /ar/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: تعلم كيفية البحث عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة عبر واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: العثور على قيمة الخلية التي تبدأ بعلامة اقتباس واحدة، البحث عن قيمة الخلية التي تبدأ بعلامة اقتباس واحدة
---

{{% alert color="primary" %}}

Aspose.Cells الآن يوفر خاصية [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) للعثور على ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة. قبل هذه الخاصية، لم يكن هناك طريقة للتمييز بين سلاسل مثل عينة و 'عينة وما إلى ذلك.

{{% /alert %}}

الشيفرة العينية التالية تشرح أن السلاسل مثل عينة و 'عينة لا يمكن تمييزها باستخدام الخاصية [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). لذلك يجب علينا استخدام الخاصية [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) للتمييز بينهما.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
