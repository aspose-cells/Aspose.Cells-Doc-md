---
title: Ange om Pivottabellen är kompatibel med Excel 2003 vid uppdatering av Pivottabellen med Golang via C++
linktitle: Ange kompatibilitet för Excel2003 i PivotTable
type: docs
weight: 80
url: /sv/go-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Lär dig hur du anger PivotTable kompatibilitet för Excel2003 med hjälp av Aspose.Cells for C++ när du uppdaterar PivotTable.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) som du kan använda för att ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable. Om sant måste en sträng vara mindre än eller lika med 255 tecken, så om strängen är större än 255 tecken kommer den att bli avkortad. Om **falskt** kommer en sträng inte att ha den tidigare nämnda begränsningen. Standardvärdet är **true**.

{{% /alert %}}

## **Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable**

Följande provkod förklarar användningen av egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/). Den ursprungliga strängen är 383 tecken lång. Men när egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) är inställd som **true** och pivottabellen uppdateras, avkortas datan i cell B5 i pivottabellen och blir 255 tecken lång. Men när egenskapen [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) är inställd som **false** och pivottabellen återigen uppdateras, avkortas inte datan i cell B5 i pivottabellen utan förblir 383 tecken lång. Vänligen läs kommentarerna inuti koden för att bättre förstå denna egenskap.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyWhetherThePivottableIsCompatibleForExcel2003WhileRefreshingPivottable.go" >}}
