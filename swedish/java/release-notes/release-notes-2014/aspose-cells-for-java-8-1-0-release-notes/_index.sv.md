---
title: Aspose.Cells för Java 8.1.0 Release Notes
type: docs
weight: 50
url: /sv/java/aspose-cells-for-java-8-1-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 8.1.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.1.0/)

{{% /alert %}} 

 Aspose.Cells för Java har uppdaterats till version 8.1.0 och vi är glada att kunna meddela att denna utgåva innehåller 10 nya användbara förbättringar.
Med Aspose.Cells för Java kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells för Java.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
 Följande är en lista över ändringar i denna version av Aspose.Cells för Java.

Andra förbättringar och förändringar

Förbättringar

(CELLSJAVA-40823) - Begränsa API:et att använda den typsnittskatalog som anges med metoden CellsHelper.setFontDir
(CELLSJAVA-40716) - diagramlinjerna är inte skarpa/skarpa
(CELLSJAVA-40827) - Få skärmfärg definierad i anpassat nummerformat

Buggar

(CELLSJAVA-40809) - Vissa färger visas precis före kolumnen i en tabell
(CELLSJAVA-40814) - Bilder saknas i resulterande PDF när kalkylblad konverteras på Ubuntu
(CELLSJAVA-40826) - Gridlines och Font-inställningar saknas i utdata-HTML
(CELLSJAVA-40829) - Det går inte att ställa in utskriftskvalitet för kalkylblad
(CELLSJAVA-40838) - PrintCopies bevaras för XLS-format men inte för XLSX-format

Undantag

(CELLSJAVA-40739) - Sparar pivotbar som mht
(CELLSJAVA-40531) - Celler Undantag: Kartstorlek (0) måste vara >= 1


Public API och bakåtinkompatibla ändringar

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

Obsoletes BuiltInDocumentPropertyCollection.Bytes/Characters/CharactersWithSpaces/Lines/Paragraphs-egenskaper
Dessa egenskaper är skrivna för Word och PowerPoint, Excel kommer att utelämna dem.

Lägger till egenskapen Cell.StringValueWithoutFormat
Hämtar cellens värde som sträng utan något format.

Lägger till egenskapen HtmlSaveOptions.ExportHiddenWorksheet
Anger om det dolda kalkylbladets innehåll exporteras när html-filen sparas. Standardvärdet är sant.

Notera
Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.1.0 också i denna Aspose.Cells för Java v8.1.0.
