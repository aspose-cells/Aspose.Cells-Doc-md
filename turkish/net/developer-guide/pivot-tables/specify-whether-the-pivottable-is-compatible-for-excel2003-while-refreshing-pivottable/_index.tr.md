---
title: PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin
type: docs
weight: 80
url: /tr/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtebileceğiniz [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) özelliğini sağlar. Eğer true ise, bir dize 255 karakterden az veya eşit olmalıdır, bu nedenle eğer dize 255 karakterden büyükse kısaltılacaktır. Eğer **false** ise, bir dize yukarıda bahsedilen kısıtlamayı taşımayacaktır. Varsayılan değer **true** dur.

{{% /alert %}}

## **PivotTable, PivotTable yeniden tazelenirken Excel2003 için uyumlu olup olmadığını belirtin**

Aşağıdaki örnek kod, [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) özelliğinin kullanımını açıklar. Orijinal dize 383 karakter uzunluğundadır. Fakat [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) özelliği **true** olarak ayarlandığında ve pivot tablosu yeniden tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılır ve 255 karakter uzunluğuna gelir. Ancak [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) özelliği **false** olarak ayarlandığında ve pivot tablosu tekrar tazelendiğinde, pivot tablosunun B5 hücresinin verisi kısaltılmaz ve 383 karakter uzunluğunda kalır. Bu özelliğin daha iyi anlaşılması için kod içindeki yorumları okuyun lütfen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
