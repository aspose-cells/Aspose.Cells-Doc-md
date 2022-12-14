---
title: Aspose.Cells för Java 7.3.4 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-7-3-4-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 7.3.4](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.4/)

{{% /alert %}} 

Vi är
 glad att kunna meddela Aspose.Cells för Java v7.3.4!

 Nya egenskaper

- Stöd för TIFF-format i Sheet-to-Image-funktion

 Förbättringar

- Höger sidfot är inte ovanför mittfoten som i MS Excel

 Undantag

- Minnet är fullt undantag vid konvertering av Excel till PDF
- Att ställa in "+100" som den villkorliga formeln orsakade ett undantag
- Undantag: "StackOverflowError" vid beräkning av formler
- "IllegalArgumentException" kastas när Workbook.copy() anropas

 Buggar

- Arabisk text blev skräppecken i den sparade CSV-filen med UTF-8
- Felet "Data kan ha gått förlorad" för den återsparade XLS-filen av Aspose.Cells
- "Excel hittade oläsbart innehåll...."fel för Aspose.Cells' genererad rapport
- Cell.getFormula() särskiljde inte olika namngivna intervall med samma namn men olika omfattning
- Automatisk titel för PIE-diagramproblem
- Cell.getR1C1Formula() särskiljde inte olika namngivna intervall med samma namn men olika omfattning
