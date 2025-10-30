---
title: Hücre değerinin tek tek tırnak işaretiyle başlayıp başlamadığını bul
type: docs
weight: 270
url: /tr/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Hücre değeri tek tırnak işaretiyle başlıyorsa Aspose.Cells for Node.js via C++ API si aracılığıyla nasıl bulunacağını öğrenin.
keywords: Node.js üzerinden C++ ile hücre değeri tek tırnak işaretiyle başlıyor mu onu bulun, C++ ile Node.js üzerinden tek tırnak işaretiyle başlıyorsa hücre değeri arayın
---

{{% alert color="primary" %}}

Aspose.Cells artık hücre değeri tek tırnak işaretiyle başlıyorsa bunu bulmak için [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) yöntemini sağlar. Bu özelliğin öncesinde, sample ve 'sample' gibi dizeleri ayırt etmek için bir yol yoktu.

{{% /alert %}}

Aşağıdaki örnek kod, sample ve 'sample' gibi dizelerin [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) yöntemiyle ayırt edilemeyeceğini açıklar. Bu nedenle, onları ayırt etmek için [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) yöntemini kullanmalıyız.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
