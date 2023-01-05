---
title: Aspose.Cells for Java 7.3.3 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-7-3-3-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 7.3.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.3/)

{{% /alert %}} 

Vi är
 glad att meddela Aspose.Cells for Java v7.3.3!

 Nya egenskaper

- Lägg till metoden Row.getLastDataCell() för att få den sista cellen som har data i en rad
- Nya API:er har lagts till för att få samma Styleobject för celler med samma stilinställningar

 Förbättringar

- Lägg till citattecken till tomma cellvärden när du exporterar en CSV med

 alternativ

 Undantag

- Villkorlig formatering med Unicode-tecken misslyckas
- Att ställa in formel innan du lägger till områden för villkorlig formatering och sedan byter namn på kalkylblad orsakade ett fel när arbetsboken sparades
- Återspara en XLS mallfil orsakadNegativeArraySizeException

 Buggar

- Formaterat datumvärde skilde sig från det som visas i MS Excel
- Diagramserienamn går förlorade om CellCollection rensas
- Att visa tomt som luckor/nollor fungerar inte för XLSX-filer
- Dataetikettformatering för diagram är inte bra
- Teckensnittets understrykning försvann i den renderade PDF-filen
- Att ställa in teckensnittsstilar fick ingen effekt för XLSX i LightCells-läge
- En del av sidfoten försvann när du sparade till PDF
