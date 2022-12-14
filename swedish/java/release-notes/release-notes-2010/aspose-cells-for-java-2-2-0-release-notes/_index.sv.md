---
title: Aspose.Cells för Java 2.2.0 Release Notes
type: docs
weight: 80
url: /sv/java/aspose-cells-for-java-2-2-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 2.2.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.2.0/)

{{% /alert %}} 

 Vi är glada att kunna meddela Aspose.Cells för Java 2.2.0!

 Vad har ändrats:

- Ställer in formler med rad/kolumn/parametrar som överskrider MS Excel 2003-gränsen
 Stöder för att behålla originaldata som läses från MS Excel 2010 mallfil
 Manipulera MS Excel 2010 Sparklines
 Ger utökade stilar sparade av MS Excel 2007 för XLS-filer
 Stöder för att automatiskt upptäcka filformatstyp när du öppnar mallfil utan att ange format för HTML- och SpreadSheeML-filer
 Tar bort ett diagram från diagramsamlingen
Tillåter att radera tomma rader/kolumner i kalkylbladet
 Stöder för att spara färgen till närmaste matchande färg i paletten när den användarspecificerade färgen inte finns i standardpaletten.
 Exporterar rotationsattribut för text för Excel till Pdf-funktion
 Exporterar diagram som bilder för Excel till Pdf-funktion
 Tar bort befintligt utskriftsområde
 Inkluderar förbättringar för att spara sammanslagna områden: kontrollera och ta bort eller kombinera de duplicerade/överlappande områdena som kan orsaka att den genererade filen visar ett varningsmeddelande när den öppnas i MS Excel
 Innehåller förbättringar för att lägga till sidbrytningar: kontrollera och ta bort dubblerade sidbrytningar innan du sparar
 Inkluderar förbättring för diagram till bild-funktionen
 65 korrigeringar och andra förbättringar.

 Problem lösta i Aspose.Cells för Jav

 Anmärkningsvärda förändringar för användare:



 I de gamla versionerna kommer metoderna Workbook.save(String) och Workbook.save(InputStream) alltid att spara den resulterande filen som Excel97TO2003-filformat.

Från den här versionen, om arbetsbokens formattyp har specificerats, kommer metoderna Workbook.save(String) och Workbook.save(InputStream) att spara den resulterande filen i det format som specificeras av arbetsboken. Formattypen för arbetsboken kan ställas in med metoden Workbook.setFileFormatType(int). Eller så kan den ställas in som inmatningsmallfilens format automatiskt när en befintlig mallfil öppnas.

 Dessutom beror gränsen för rad/kolumn för formler och parameterantalgräns för formler också på arbetsbokens formattyp. Innan du överskrider gränsen för rad/kolumn/parameter för formler för MS Excel 2003, måste du ställa in arbetsbokens format uttryckligen till vissa andra typer, till exempel EXCEL2007.
