---
title: Biçimlendirmeli ve Biçimlendirmesiz Cell Dize Değerini Alın
type: docs
weight: 240
url: /tr/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells bir yöntem sağlar[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) herhangi bir biçimlendirme olsun veya olmasın hücrenin dize değerini almak için kullanılabilir. 0.012345 değerine sahip bir hücreniz olduğunu ve onu yalnızca iki ondalık basamak gösterecek şekilde biçimlendirdiğinizi varsayalım. Daha sonra Excel'de 0.01 olarak görüntülenecektir. Dize değerlerini hem 0.01 hem de 0.012345 olarak alabilirsiniz.[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) yöntem. Alır[**CellValueFormatStrateji**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum aşağıdaki değerlere sahip bir parametre olarak

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 Aşağıdaki örnek kod, kullanımını açıklar[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
