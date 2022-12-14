---
title: Konvertera text till kolumner med Aspose.Cells
type: docs
weight: 30
url: /sv/net/convert-text-to-columns-using-aspose-cells/
---
## **Möjliga användningsscenarier**

Du kan konvertera din text till kolumner med Microsoft Excel. Denna funktion är tillgänglig från*Dataverktyg* under*Data* flik. För att dela upp innehållet i en kolumn i flera kolumner bör data innehålla en specifik avgränsare som ett kommatecken (eller något annat tecken) baserat på vilket Microsoft Excel delar upp innehållet i en cell till flera celler. Aspose.Cells tillhandahåller också denna funktion via[**Arbetsblad.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)metod.

## **Konvertera text till kolumner med Aspose.Cells**

 Följande exempelkod förklarar användningen av[**Arbetsblad.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metod. Koden lägger först till några personers namn i kolumn A i det första kalkylbladet. För- och efternamn separeras med mellanslag. Då gäller det[**Arbetsblad.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metod i kolumn A och spara den som utdata Excel-fil. Om du öppnar[output excel-fil](25395213.xlsx), kommer du att se, förnamn finns i kolumn A medan efternamn finns i kolumn B som visas i den här skärmdumpen.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
