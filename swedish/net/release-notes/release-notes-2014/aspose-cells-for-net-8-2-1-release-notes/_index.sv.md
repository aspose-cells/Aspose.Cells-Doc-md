---
title: Aspose.Cells for .NET 8.2.1 Release Notes
type: docs
weight: 30
url: /sv/net/aspose-cells-for-net-8-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.2.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.2.1/)

{{% /alert %}} 

 Aspose.Cells for .NET har uppdaterats till version 8.2.1 och vi är glada att kunna meddela att denna utgåva kommer med över 30 nya användbara förbättringar.
Med Aspose.Cells for .NET kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också visa, generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells for .NET.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
 Följande är en lista över ändringar i denna version av Aspose.Cells.

\1) Aspose.Cells 
## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-42923) - Stöd alternativet att visa förklaringen utan att överlappa

 (CELLSNET-42935) - Kontrollera att cellvärdet uppfyller reglerna för datavalidering

 (CELLSNET-42911) - Inaktivera textbrytning för dataetiketter i diagrammet


## **Buggar**


 (CELLSNET-42941) - Producerar oläsbart innehållsfel i XLSM-fil

(CELLSNET-42933) - Kan inte undvika radetiketter när de skapas pivot med aspose

 (CELLSNET-42857) - Filen blir korrupt när den öppnas och sparas

 (CELLSNET-42816) - Diagonal textruta visas horisontellt när kalkylblad konverteras till PDF

 (CELLSNET-42815) - Diagonal textruta visas horisontellt när kalkylblad konverteras till HTML

 (CELLSNET-42676) - Tjockleken på pillinjerna i visio-diagrammet är fel i utdata-pdf

 (CELLSNET-41568) - Excel till bild med roterad form som inte återges korrekt

 (CELLSNET-40931) - Fel former exporterade till bilden

 (CELLSNET-42802) - Problem med grafisk rendering vid konvertering av Xls till PDF

 (CELLSNET-42980) - Fel sidbrytning vid rendering av kalkylarket till PDF

 (CELLSNET-42979) - Oönskad förlängning av gränsen vid rendering av kalkylblad till PDF

 (CELLSNET-42970) - Tilläggsoperationen i Excel-sidfoten fungerar inte i PDF-rendering

 (CELLSNET-42936) - Utskrift på båda sidor av sidan

(CELLSNET-42938) - Hyperlänkar för formerna som förlorats i det renderade PDF-filformatet

 (CELLSNET-42966) - Oläsbart innehåll efter att ha öppnat och sparat xlsx-fil

 (CELLSNET-42964) - Excel hittade ett oläsbart innehållsfel vid generering av hyperlänkar

 (CELLSNET-42946) - Värdet på cell L45 är felaktigt efter beräkningsformel

 (CELLSNET-42943) - Excel-begränsning vad gäller hyperlänkar i Aspose.Cells

 (CELLSNET-42934) - Felaktig läsning Referenser för punktdiagramtyp och namnintervall

 (CELLSNET-42926) - Sidfoten är inte korrekt vid konvertering från SpreadsheetML-dokument

 (CELLSNET-42837) - Visa datatabell med förklaringsnyckel för chatt

 (CELLSNET-41129) - Logotypen försvann i PDF-filen

 (CELLSNET-42986) - Felaktig formel kopierades till celler när rader infogades i tabeller

 (CELLSNET-42974) - Aspose.Cells korrumperande kalkylblad som innehåller externa data

 (CELLSNET-42802) - paj, munk. Beräkna formel

 (CELLSNET-42940) - Hyperlänk i PDF av XLS

(CELLSNET-42738) - Utjämnad linje på scatterdiagram innehåller loopar

 (CELLSNET-42739) - Scatter Chart-bilden visar fel rutnätsmarkörer för X-axeln


## **Undantag**


 (CELLSNET-42929) - IndexOutOfRangeException kastat vid pivottabell.CalculateData

 (CELLSNET-42213) - Konvertera en XLS-fil som innehåller en form med en gradientbakgrund till PDF

 (CELLSNET-42962) - Undantag på Workbook.RemoveExternalLinks()

 (CELLSNET-42951) - CellsHelper.ConvertA1FormulaToR1C1 kastar undantag

 (CELLSNET-42930) - System.ArgumentException vid Workbook.Save

 (CELLSNET-42002) - System.ArgumentException undantag på 9110 sida

 (CELLSNET-42977) - Undantag för ritning av bild


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



 Lägger till metoden Cell.GetValidation().

 Får valideringen som gäller för cellen.



 Lägger till metoden Cell.GetValidationValue().

 Indikerar om cellens värde är giltigt.



 Lägger till metoden WorkbookRender.ToPrinter(PrinterSettings PrinterSettings).

 Återge arbetsbok till skrivare via PrinterSettings.


