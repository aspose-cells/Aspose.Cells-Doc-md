---
title: Radera tomma rader och kolumner i ett kalkylblad
type: docs
weight: 300
url: /sv/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

Det är möjligt att ta bort alla tomma rader och kolumner från ett kalkylblad. Detta är användbart när man till exempel genererar en PDF-fil från en Microsoft Excel-fil och vill konvertera endast rader och kolumner som innehåller data eller relaterade objekt.

Använd följande Aspose.Cells-metoder för att ta bort tomma rader och kolumner:

1. För att ta bort tomma rader, använd metoden [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows). Observera, för tomma rader som kommer att tas bort, krävs det inte bara att [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) ska vara sant, utan det får inte heller finnas någon synlig kommentar definierad för någon cell i dessa rader, och ingen pivottabell vars omfång korsar dem.
1. För att ta bort tomma kolumner, använd metoden [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns).

{{% /alert %}}

## C# kod för att ta bort tomma rader

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## C# kod för att ta bort tomma kolumner

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
