---
title: Hücre değerinin tek tek tırnak işaretiyle başlayıp başlamadığını bul
type: docs
weight: 270
url: /tr/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for Python via .NET API si aracılığıyla hücre değerinin tek tırnak işareti ile başlayıp başlamadığını bulmayı öğrenin.
keywords: Python Excel Kütüphanesi, Hücre değerinin tek tırnak işareti ile başlayıp başlamadığını bul, Tek tırnak işareti ile başlayan hücre değerini bul
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET artık hücre değerinin tek tırnak işareti ile başlayıp başlamadığını bulmak için [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) özelliğini sağlar. Bu özelden önce, örnek olarak sample ve 'sample gibi diziler arasında ayırım yapmanın bir yolu yoktu.

{{% /alert %}}

Aşağıdaki örnek kod, örnek ve 'örnek gibi dizilerin [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/) özelliği ile ayırt edilemeyeceğini açıklar. Bu nedenle onları ayırt etmek için [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) özelliğini kullanmamız gerekir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
