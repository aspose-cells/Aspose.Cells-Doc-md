---
title: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Alın
type: docs
weight: 240
url: /tr/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for Node.js via C++ API si aracılığıyla hücre dizgesi değerlerini biçimlendirmeden ve biçimlendirmeyle alma yollarını öğrenin.
keywords: İçeriğe ve biçimlendirmeye göre hücre dizge değeri alın Node.js C++ kullanarak, biçimlendirmeden hücre dizge değeri alın Node.js C++ ile, biçimlendirmeden hücre dizge değeri edin Node.js C++ aracılığıyla
---

{{% alert color="primary" %}}

Aspose.Cells, [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) metodunu sağlar, bu metod, hücrenin biçimlendirmesi olup olmamasına bakmaksızın dizge değerini alabilir. Diyelim ki, hücrede 0.012345 değeri var ve sadece iki ondalık basamağı göstermek için biçimlendirilmiş. Excel'de bu 0.01 olarak görünür. Hem 0.01 hem de 0.012345 biçiminde dizge değerleri almak için [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) metodunu kullanabilirsiniz. Parametre olarak aşağıdaki enum değerleri alan [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) parametresi vardır.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Aşağıdaki örnek kod [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) metodunun kullanımını açıklar.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

