---
title: Ange om pivottabellen är kompatibel för Excel2003 medan du uppdaterar pivottabellen
type: docs
weight: 80
url: /sv/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**Pivottabell.IsExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)egenskap som du kan använda för att ange om pivottabellen är kompatibel med Excel2003 medan du uppdaterar pivottabellen. Om sant måste en sträng vara mindre än eller lika med 255 tecken, så om strängen är större än 255 tecken kommer den att trunkeras. Om**falsk** , kommer en sträng inte att ha den ovannämnda begränsningen. Standardvärdet är**Sann**.

{{% /alert %}}

## **Ange om pivottabellen är kompatibel för Excel2003 medan du uppdaterar pivottabellen**

 Följande exempelkod förklarar användningen av[**Pivottabell.IsExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) fast egendom. Den ursprungliga strängen är 383 tecken lång. Men när[**Pivottabell.IsExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) egenskapen är inställd**Sann** och pivottabellen uppdateras, trunkeras data i cell B5 i pivottabellen och den blir 255 tecken lång. Men när[**Pivottabell.IsExcel2003kompatibel**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) egenskapen är inställd**falsk** och pivottabellen uppdateras igen, trunkeras inte data i cell B5 i pivottabellen och förblir 383 tecken långa. Vänligen läs kommentarerna i koden för bättre förståelse av den här egenskapen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
