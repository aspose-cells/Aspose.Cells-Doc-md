---
title: Aspose.Cells för Java 8.4.1 Release Notes
type: docs
weight: 70
url: /sv/java/aspose-cells-for-java-8-4-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 8.4.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.1/)

{{% /alert %}}

Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells

## Aspose.Cells

### **Huvudfunktioner**

Flyttade huvudkodbasen till Java 6 (Java 7 och 8 stöds också). Släppt stöd för Java 5 och 1.4.

### **Andra förbättringar och förändringar**

### **Nya egenskaper**

(CELLSJAVA-41235) - Stöd RenderToSize API för kalkylbladsbild

(CELLSJAVA-41234) - Stöd kulor när du använder SmartMarkers eller Cell.setHtmlString-metoden

### **Buggar**

(CELLSJAVA-41229) - Aspose.Cells genererar inte individuella HTM:er och CSS-filer för arken i Excel till HTML-konvertering

(CELLSJAVA-41170) - SheetRender.toImage återger bilden med "(tom)"-etiketter på diagrammets x-axel

(CELLSJAVA-41270) - Problem med Cells.insertRange() eftersom det sammanslagna området inte förskjuts fint

(CELLSJAVA-41240) - Text i Arial-teckensnitt trimmas uppifrån samtidigt som kalkylarket renderas till PDF

(CELLSJAVA-41238) - PAPPER_A_2 fungerar inte som förväntat när du sparar som PDF

(CELLSJAVA-41217) - När seriekategoridata har kommatecken visas inte PIE-diagramförklaringar korrekt

(CELLSJAVA-41194) - Överlappning av förklaringsposterna vid konvertering av diagram till bild

(CELLSJAVA-41002) - Prickad linje saknas i diagram 1

(CELLSJAVA-40993) - Horisontella rutnätslinjer saknas i tillväxtdiagrammet

(CELLSJAVA-41259) - Inställning av Name.setRefersTo och omräkning av formler resulterar i felaktigt värde vid konvertering av kalkylblad till HTML

(CELLSJAVA-41258) - Laddar och sparar XLSX med Aspose.Cells gör det resulterande kalkylarket korrupt

(CELLSJAVA-41255) - Anpassad knapp blir bild och bildtexten försvinner i utgången XLSX

(CELLSJAVA-41254) - Microsoft Excel kraschar när XLSX-filen öppnas

(CELLSJAVA-41253) - Dropdown försvinner i XLSX-filen

### **Undantag**

(CELLSJAVA-41266) - java.lang.NumberFormatException inträffade när mallen XLSX-fil öppnades

(CELLSJAVA-41248) - Null-pekareundantag vid öppningskällans XLSX-fil

(CELLSJAVA-41265) - Undantag: "java.lang.NullPointerException" vid öppning av en SpreadsheetML-fil

(CELLSJAVA-41264) - Undantag vid användning av Cell.getStringValueWithoutFormat

(CELLSJAVA-41246) - Undantag: Ogiltig dynamisk formel... som involverar indexfunktion när du använder Smart Markers dynamiska formler

## Aspose.Cells Grid Suite

### **Andra förbättringar och förändringar**

### **Förbättringar**

(CELLSJAVA-41213) - Gridweb: sätter olika gränser genom webboperation

### **Buggar**

(CELLSJAVA-41261) - Flerbytetecken i datavalideringslistan ändras till "??" när du väljer det i FireFox

(CELLSJAVA-41260) - Kan inte visa, välja eller öka höjden på den dolda raden i GridWeb

(CELLSJAVA-41257) - Navigeringen är fel när du flyttar från C1 --> C3-cell med piltangenterna

(CELLSJAVA-41256) - Vissa regler för villkorlig formatering kan inte användas eller delvis användas i mallfilen när de importeras till GridWeb

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

Lägger till egendomen Workbook.IsLicensed.

Anger om licensen har ställts in.

Obsoletes Workbook.ValidateFormula-metoden.

Använd Cell.Formula-egenskap istället.

Lägger till egenskapen ImageOrPrintOptions.SVGFitToViewPort.

Indikerar om den genererade SVG-bilden är lämplig för visningsport.

Lägger till metoden ImageOrPrintOptions.SetDesiredSize.

Ställer in önskad bredd och höjd på bilden.

Lägger till metoden Aspose.Cells.GridDesktop.WorksheetCollection.MoveTo

Flyttar kalkylbladet vid angivet index till anther index.

**Notera**

Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.4.1 också i denna Aspose.Cells för Java v8.4.1.
