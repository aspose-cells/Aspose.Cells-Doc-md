---
title: Aspose.Cells för Java 7.2.2 Release Notes
type: docs
weight: 60
url: /sv/java/aspose-cells-for-java-7-2-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 7.2.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.2/)

{{% /alert %}} 

Vi är
 glad att kunna meddela Aspose.Cells för Java v7.2.2!

 Nya egenskaper

- RegEx-textsökning efter Cells.Find()-metoden

 Förbättringar

- Gör Aspose.Cells kompatibel med äldre versioner av Woodstox-burkar
- OLE-inbäddade OOXML-filer i XLS kommer ut som OLE-paketerade filer istället för uppackade filer
- Stöd ExportObjectListener för att spara HTML-filer
- Kopiera villkorlig formatering vid kopiering av rader

 Undantag

- Picture.isPrintable() för Picture inPageSetup orsakar NullPointerException
- Sparar krypterad arbetsbok med Pivot Tablecauses java.lang.NegativeArraySizeException

 Buggar

- Cells.importCustomObjects() med specificerat DateTime-format fungerar inte
- Fel diagramTyp av punktdiagram
- Dubbelt värde förlorar precision vid läsning från CSV-mallfil
- Diagramserien vänds upp och ner när den konverterades till en bild
- Återsparad XLSX-fil orsakar felet "Excelfound oläsbart innehåll...".
- Sparad pivottabell orsakade "ProtectionView" när den öppnades i MS Excel
- Genom att använda listvalidering av Aspose.Cellscreates en XLS-fil som inte fungerar efter att ha ändrat systemets listseparator
