---
title: Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable
type: docs
weight: 80
url: /sv/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) som du kan använda för att ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable. Om sant måste en sträng vara mindre än eller lika med 255 tecken, så om strängen är större än 255 tecken kommer den att bli avkortad. Om **falskt** kommer en sträng inte att ha den tidigare nämnda begränsningen. Standardvärdet är **true**.

{{% /alert %}}

## **Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable**

Följande provkod förklarar användningen av egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible). Den ursprungliga strängen är 383 tecken lång. Men när egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) är inställd som **true** och pivottabellen uppdateras, avkortas datan i cell B5 i pivottabellen och blir 255 tecken lång. Men när egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) är inställd som **false** och pivottabellen återigen uppdateras, avkortas inte datan i cell B5 i pivottabellen utan förblir 383 tecken lång. Vänligen läs kommentarerna inuti koden för att bättre förstå denna egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
