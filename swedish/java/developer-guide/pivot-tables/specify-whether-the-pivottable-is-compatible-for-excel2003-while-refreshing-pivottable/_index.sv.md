---
title: Ange om pivottabellen är kompatibel för Excel2003 medan du uppdaterar pivottabellen
type: docs
weight: 880
url: /sv/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 Aspose.Cells tillhandahåller[Pivottabell.IsExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)egenskap som du kan använda för att ange om pivottabellen är kompatibel med Excel2003 medan du uppdaterar pivottabellen. Om**Sann** , en sträng måste vara mindre än eller lika med 255 tecken, så om strängen är större än 255 tecken kommer den att trunkeras. Om**falsk** , kommer en sträng inte att ha den ovannämnda begränsningen. Standardvärdet är**Sann**.

{{% /alert %}} 
## **Ange om pivottabellen är kompatibel för Excel2003 medan du uppdaterar pivottabellen**
 Följande exempelkod förklarar användningen av[Pivottabell.IsExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) fast egendom. Den ursprungliga strängen är 383 tecken lång. Men när[Pivottabell.IsExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) egenskapen är inställd på**Sann** och pivottabellen uppdateras, trunkeras data i cell B5 i pivottabellen och den blir 255 tecken lång. Men när[Pivottabell.IsExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) egenskapen är inställd**falsk** och pivottabellen uppdateras igen, trunkeras inte data i cell B5 i pivottabellen och förblir 383 tecken långa. Vänligen ladda ner[exempel på excel-fil](5472558.xlsx) används i den här koden,[output excel-fil](5472557.xlsx) genereras av den och dess konsolutgång för din referens. Vänligen läs även kommentarerna i koden för bättre förståelse av den här egenskapen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Konsolutgång**
Här är konsolutgången för ovanstående exempelkod när den exekveras med den givna[exempel på excel-fil](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
