---
title: Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable
type: docs
weight: 80
url: /sv/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ tillhandahåller [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)-egenskapen som du kan använda för att specificera om Pivottabell är kompatibel med Excel2003 vid uppdatering av pivottabellen. Om sant måste strängen vara kortare än eller lika med 255 tecken, så om strängen är längre än 255 tecken, kommer den att förkortas. Om **falsk**, kommer strängen inte att ha den nämnda restriktionen. Standardvärdet är **true**.

{{% /alert %}}

## **Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable**

Följande provkod förklarar användningen av egenskapen [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-). Den ursprungliga strängen är 383 tecken lång. Men när egenskapen [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) är inställd som **true** och pivottabellen uppdateras, avkortas datan i cell B5 i pivottabellen och blir 255 tecken lång. Men när egenskapen [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) är inställd som **false** och pivottabellen återigen uppdateras, avkortas inte datan i cell B5 i pivottabellen utan förblir 383 tecken lång. Vänligen läs kommentarerna inuti koden för att bättre förstå denna egenskap.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

