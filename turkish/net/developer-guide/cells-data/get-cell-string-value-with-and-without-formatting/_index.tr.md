---
title: Biçimlendirmeli ve Biçimlendirmesiz Cell Dize Değeri Alın
type: docs
weight: 240
url: /tr/net/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for .NET API aracılığıyla Biçimlendirmeli ve Biçimlendirmesiz Cell Dize Değerinin nasıl alınacağını öğrenin.
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
---
{{% alert color="primary" %}}

 Aspose.Cells bir yöntem sunuyor[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)herhangi bir biçimlendirmeyle veya biçimlendirme olmadan hücrenin dize değerini elde etmek için kullanılabilir. 0,012345 değerine sahip bir hücreniz olduğunu ve onu yalnızca iki ondalık basamağı görüntüleyecek şekilde biçimlendirdiğinizi varsayalım. Daha sonra Excel'de 0,01 olarak görüntülenecektir. Dize değerlerini hem 0,01 hem de 0,012345 olarak alabilirsiniz.[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) yöntem. Alır[**CellValueFormatStrateji**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)aşağıdaki değerlere sahip bir parametre olarak enum

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 Aşağıdaki örnek kod, kullanımını açıklamaktadır.[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
