---
title: PivotTable'ı yenilerken PivotTable'ın Excel2003 için uyumlu olup olmadığını belirtin
type: docs
weight: 80
url: /tr/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

 Aspose.Cells şunları sağlar:[**PivotTable.IsExcel2003Uyumlu**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)PivotTable'ı yenilerken PivotTable'ın Excel2003 ile uyumlu olup olmadığını belirtmek için kullanabileceğiniz özellik. true ise, bir dize 255 karakterden küçük veya buna eşit olmalıdır, bu nedenle dize 255 karakterden büyükse kesilecektir. Eğer**YANLIŞ** , bir dize yukarıda belirtilen kısıtlamaya sahip olmayacaktır. varsayılan değer**doğru**.

{{% /alert %}}

## **PivotTable'ı yenilerken PivotTable'ın Excel2003 için uyumlu olup olmadığını belirtin**

 Aşağıdaki örnek kod, kullanımını açıklar[**PivotTable.IsExcel2003Uyumlu**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) Emlak. Orijinal dize 383 karakter uzunluğundadır. Ama ne zaman[**PivotTable.IsExcel2003Uyumlu**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) özellik ayarlandı**doğru** ve pivot tablo yenilendiğinde, pivot tablonun B5 hücresinin verileri kesilir ve 255 karakter uzunluğunda olur. Ancak, ne zaman[**PivotTable.IsExcel2003Uyumlu**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) özellik ayarlandı**YANLIŞ** ve pivot tablo tekrar yenilendiğinde, pivot tablonun B5 hücresinin verileri kesilmez ve 383 karakter uzunluğunda kalır. Bu özelliği daha iyi anlamak için lütfen kodun içindeki açıklamaları okuyun.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
