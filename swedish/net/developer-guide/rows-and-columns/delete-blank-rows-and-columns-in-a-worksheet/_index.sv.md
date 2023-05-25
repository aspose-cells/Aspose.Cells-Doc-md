---
title: Ta bort tomma rader och kolumner i ett kalkylblad
type: docs
weight: 300
url: /sv/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

Det är möjligt att ta bort alla tomma rader och kolumner från ett kalkylblad. Detta är användbart när du till exempel genererar en PDF-fil från en Microsoft Excel-fil och bara vill konvertera rader och kolumner som innehåller data eller relaterat objekt.

Använd följande Aspose.Cells-metoder för att ta bort tomma rader och kolumner:

1.  För att ta bort tomma rader, använd[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) metod. Observera att för tomma rader som kommer att raderas krävs inte bara det[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) bör vara sant, men det bör inte heller finnas någon synlig kommentar definierad för någon cell i dessa rader, och ingen pivottabell vars intervall skär dem.
1.  För att ta bort tomma kolumner, använd[**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) metod.

{{% /alert %}}

##  C# kod för att radera tomma rader

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

##  C# kod för att ta bort tomma kolumner

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
