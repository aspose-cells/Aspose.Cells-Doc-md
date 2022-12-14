---
title: Aspose.Cells för Java 7.3.1 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-7-3-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 7.3.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.1/)

{{% /alert %}} 

Vi är
 glad att kunna meddela Aspose.Cells för Java v7.3.1 för användarna!

 Nya egenskaper

 - Analysera skript i sidinställningarnas sidhuvuden/sidfötter

- Villkorlig formatering - Inkludera DataBar-typens saknade fält
- Villkorlig formatering - Inkludera IconSet-typens saknade värden
- Villkorlig formatering - Support
- Läs regler för villkorlig formatering med formler för tvärark
- Stöd Cells.MinDataColumn och Cells.MinDataRow egenskaper
- Stöd Cell Bakgrundsfärger med villkorlig formatering (MS Excel 2010)
- Datafilter för pivottabellen stöds
- Avancerad datavalidering av MS Excel 2010 stöds

 (Notera:

Alla ovanstående biljetter
läggs ursprungligen till på uppdrag av .NET-användare. Sedan vår Java-version av
produkten är lika matchad (avseende funktioner och förbättringar) med .NET
nu, så vi har införlivat dessa nya funktioner/förbättringar i Java-versionen
 av produkten också.
) 

 Förbättringar

 -Tillfälliga teckensnittsfiler skapas mer än en gång när du sparar till PDF

 -Datum i sidhuvud/sidfot har inte formaterats i enlighet med arbetsbokens lokalinställningar

- Supportnew option: Aspose.Cells.Disable=SunFontManager istället för java.awt.headlessför JVM-krasch av Open JDK

 -Exportera automatiska former för HTML-fil

 Undantag

- Undantag: "Shape to Image Error" när du sparar till PDF

 -Shape to Image-problem när du sparar till PDF

- "NullPointerException" för metoden Chart.calculate().

 - Att spara XLS som PDF orsakade ett undantag

 - Att spara XLS som PDF orsakade ett undantag II

 Buggar

 -Överlappande text och missade rutnät för att spara PDF

 -Extra ramar visades när du sparade om

mallfil som XLS-fil

 -Läsning av namn med referens "!$A$1" orsakade ett undantag

 -PDF-generering misslyckades med specifika diagramdata

 -Formlerna är felaktiga efter att ha infogat intervall

 -Den genererade PDF-filen från Excel-arbetsboken hade fler sidor

 - Diagrametiketter blev feljusterade och överlappade när kalkylbladet hanterades
