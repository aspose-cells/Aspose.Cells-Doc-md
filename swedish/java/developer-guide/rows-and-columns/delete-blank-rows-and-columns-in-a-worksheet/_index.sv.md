---
title: Radera tomma rader och kolumner i ett kalkylblad
type: docs
weight: 360
url: /sv/java/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}} 

Det är möjligt att ta bort alla tomma rader och kolumner från ett kalkylblad. Detta är användbart till exempel när du genererar en PDF-fil från en Microsoft Excel-fil och vill konvertera endast rader och kolumner som innehåller data.

Använd följande Aspose.Cells-metoder för att ta bort tomma rader och kolumner:

1. För att ta bort tomma rader, använd metoden [Cells.deleteBlankRows()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteBlankRows--) .
1. För att ta bort tomma kolumner, använd metoden [Cells.deleteBlankColumns()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteBlankColumns--) .

{{% /alert %}} 
## **Tar bort tomma rader**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletingBlankRows-DeletingBlankRows.java" >}}
## **Tar bort tomma kolumner**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletingBlankColumns-DeletingBlankColumns.java" >}}
{{< app/cells/assistant language="java" >}}
