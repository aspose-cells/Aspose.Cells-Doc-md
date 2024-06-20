---
title: Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable
type: docs
weight: 880
url: /sv/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller egenskapen [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) som du kan använda för att ange om PivotTable är kompatibelt för Excel2003 vid uppdatering av PivotTable. Om **true**, måste en sträng vara mindre än eller lika med 255 tecken, så om strängen är längre än 255 tecken kommer den att avkortas. Om **false**, kommer en sträng inte ha den tidigare nämnda begränsningen. Standardvärdet är **true**.

{{% /alert %}} 
## **Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable**
Följande exempelkod förklarar användningen av egenskapen [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible). Den ursprungliga strängen är 383 tecken lång. Men när [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)-egenskapen är inställd på **true** och pivot-tabellen uppdateras, avkortas datan i cellen B5 i pivot-tabellen och blir 255 tecken lång. Men när [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)-egenskapen är inställd på **false** och pivot-tabellen återigen uppdateras, avkortas datan i cellen B5 i pivot-tabellen inte och förblir 383 tecken lång. Vänligen ladda ner den [exempel på Excel-fil](5472558.xlsx) som används i denna kod, [utdata Excel-fil](5472557.xlsx) genererad av den och dess konsoloutput för din referens. Läs även kommentarerna inne i koden för bättre förståelse av denna egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Konsoloutput**
Här är konsoloutputen av ovanstående exempelkod när den körs med den angivna [exempel på Excel-fil](5472558.xlsx).



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
