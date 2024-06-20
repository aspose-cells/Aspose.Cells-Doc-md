---
title: Konvertera Text till Kolumner med Aspose.Cells
type: docs
weight: 30
url: /sv/net/convert-text-to-columns-using-aspose-cells/
---

## **Möjliga användningsscenario**

Du kan konvertera din text till kolumner med Microsoft Excel. Denna funktion är tillgänglig under *Data Tools* under *Data* fliken. För att dela innehållet i en kolumn till flera kolumner, bör datan innehålla en specifik avgränsare såsom ett kommatecken (eller något annat tecken) baserat på vilket Microsoft Excel delar innehållet i en cell till flera celler. Aspose.Cells tillhandahåller också denna funktion via [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metoden.

## **Konvertera Text till Kolumner med Aspose.Cells**

Följande exemplarkod förklarar användningen av [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metod. Koden lägger först till några personers namn i kolumn A av den första kalkylbladet. Förnamnet och efternamnet är separerade av ett blanktecken. Sedan tillämpar det [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) metoden på kolumn A och sparar det som en utfil. Om du öppnar [utfilen](25395213.xlsx) ser du att förnamnen är i kolumn A medan efternamnen är i kolumn B som visas i denna skärmbild.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
