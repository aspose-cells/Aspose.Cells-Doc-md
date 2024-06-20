---
title: Biçim Stratejisi ile Hücre Dize Değerini Alma
type: docs
weight: 240
url: /tr/python-net/get-cell-string-value-with-format-strategy/
description: Aspose.Cells for Python via .NET API üzerinden Hücre Dize Değerini Biçimlendirme ile Almayı ve Biçimsiz Almayı Nasıl Yapacağınızı Öğrenin.
keywords: Python Excel Kütüphanesi, Python da Biçimlendirme ile ve Biçimsiz Hücre Dize Değerini Alma, Python da Biçimlendirme ile ve Biçimsiz Hücre Dize Değerini Almak, Python da Biçimlendirme ile ve Biçimsiz Hücre Dize Değerini Almak, Python da Hücre Dize Değeri Elde Etme
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, herhangi bir biçimlendirme olmadan veya herhangi bir biçimlendirmeyle hücrenin dize değerini almak için kullanılabilecek bir yöntem [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) sağlar. Varsayalım ki, değeri 0.012345 olan bir hücreyi sadece iki ondalık basamak göstermek üzere biçimlendirdiniz. Bu durumda Excel'de 0.01 olarak görünecektir. [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) yöntemini kullanarak hem 0.01 hem de 0.012345 olarak dize değerlerini alabilirsiniz. Parametre olarak [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) numaralı enumu alır, bu enumun aşağıdaki değerleri vardır.

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

Aşağıdaki örnek kod, [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) yönteminin kullanımını açıklar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
