---
title: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Alın
type: docs
weight: 240
url: /tr/net/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for .NET API si ile Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı Nasıl Öğrenilir.
keywords: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı, Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı Kurtarma, Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı Elde Etme
---

{{% alert color="primary" %}}

Aspose.Cells, hücrenin dize değerini herhangi bir biçimlendirmeyle veya olmaksızın almak için kullanılabilecek bir yöntem [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) sunar. Diyelim ki, 0.012345 değerinde bir hücreye sahipsiniz ve sadece iki ondalık basamak göstermek üzere biçimlendirdiniz. Excel'de 0.01 olarak görünecektir. [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) yöntemini kullanarak hem 0.01 olarak hem de 0.012345 olarak dize değerlerini alabilirsiniz. Parametre olarak aşağıdaki değerlere sahip olan [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı numaralı bir numara alır.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Aşağıdaki örnek kod, [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) yönteminin kullanımını açıklar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
