---
title: ابحث ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة.
type: docs
weight: 270
url: /ar/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: تعلم كيفية معرفة ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: البحث عن قيمة خلية تبدأ بعلامة اقتباس مفردة Node.js عبر C++، البحث عن قيمة خلية تبدأ بعلامة اقتباس مفردة Node.js عبر C++.
---

{{% alert color="primary" %}}

يقدم Aspose.Cells الآن طريقة [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) لمعرفة ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة. قبل وجود هذه الخاصية، لم يكن هناك وسيلة لتمييز بين سلاسل مثل sample و 'sample' وغيرها.

{{% /alert %}}

يشرح الكود التالي أن السلاسل مثل sample و 'sample' لا يمكن التمييز بينهم باستخدام طريقة [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). لذلك، يجب علينا استخدام طريقة [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) لتمييزهم.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
