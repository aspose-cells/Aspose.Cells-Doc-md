---
title: Aspose.Cells for .NET 8.7.0 Release Notes
type: docs
weight: 140
url: /sv/net/aspose-cells-for-net-8-7-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.7.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.7.0/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-43938) - Stöd för export av VBA-certifikat till fil eller stream

 (CELLSNET-43920) - Stöd en API för att kontrollera om VBA-koden är signerad

 (CELLSNET-43867) - Signera VBA-projekt/makron digitalt

 (CELLSNET-44150) - Möjlighet att arbeta med XML-kartor

(CELLSNET-43992) - Stöd för XML-mappningsimportfunktion som det görs från fliken Excel-utvecklare


## **Förbättringar**


 (CELLSNET-43878) - VBA digital skylt försvinner under konvertering (XLSM till XLS)

 (CELLSNET-43160) - VBA Project förlorar digital signatur när xls sparas som xlsm-filformat

 (CELLSNET-44169) - Validation.Value1-arrayordningen skiljer sig från vad som visas i Excel

 (CELLSNET-44168) - Det går inte att skapa villkorlig formatering med 2-färgsskala

 (CELLSNET-44167) - Stöd ISOWEEKNUM MS Excel 2013-funktion

 (CELLSNET-44166) - VBA digital skylt försvinner under konvertering (XLSB till XLSM)


## **Prestanda**


 (CELLSNET-44156) - Konsolapplikation kraschar på Workbook.CalculateFormula

 (CELLSNET-44120) - Workbook.CalculateFormula tar mer tid att beräkna formlerna i arbetsboken.

 (CELLSNET-43896) - Processen avslutades vid anrop av Workbook.CalculateFormula


## **Buggar**


 (CELLSNET-44164) - Ofullständig HTML-struktur när du sparar till en ström

(CELLSNET-44147) - Uppdatering av pivottabellen genererar korrupt Excel-fil

 (CELLSNET-44022) - Workbook.Copy bevarar inte formatering för pivottabeller

 (CELLSNET-44139) - Olika värden för samma cell före och efter anropet av metoden CalculateFormula()

 (CELLSNET-44135) - Excel-filen är inte korrekt (fullständigt) beräknad (avseende diagram) före PDF-genereringen

 (CELLSNET-44138) - Cell skuggning överlappar gränsen vilket gör att gränsen förtunnas

 (CELLSNET-44136) - Excel visar en sida i förhandsgranskning där Aspose.Cells återges till PDF sidor

 (CELLSNET-44122) - Bilderna i arken återges inte på samma sätt som i den ursprungliga Excel-mallen

 (CELLSNET-43587) - Cell Området överlappar Cell-gränsen medan kalkylbladet konverteras till PDF

 (CELLSNET-44171) - CopyData mellan intervall fungerar inte horisontellt men det fungerar bra vertikalt

(CELLSNET-44153) - XLSB till XLSM fungerar inte korrekt och producerar skadad fil

 (CELLSNET-44149) - OleObjects tas bort efter konvertering från XLSB till XLSM

 (CELLSNET-44146) - Resultaten för villkorlig formatering återges inte korrekt i PDF

 (CELLSNET-44144) - Lägga till anpassade egenskaper tar bort kalkylbladets innehåll

 (CELLSNET-44141) - Diagrammets primära kategoriaxel blir fel när du sparar om källexcelfilen

 (CELLSNET-44160) - Horisontell axel ändrades till andra etiketter än den ursprungliga filen

 (CELLSNET-44157) - Anpassat diagrams primära x-axel ändrades efter att ha öppnat och sparat mallen XLSX filen

 (CELLSNET-43910) - Att extrahera bilden från kalkylbladet och infoga den i dokumentfilen gör den ofullständig


## **Undantag**


 (CELLSNET-44119) - Fel vid beräkning i Workbook.CalculateFormula

 (CELLSNET-44089) - System.IndexOutOfRangeException vid pivottabell.CalculateData

(CELLSNET-44064) - CalculateFormula kastar undantag på källan xlsm

 (CELLSNET-44055) - Aspose.Cell. Undantag orsakat av pdf-konvertering på grund av minnesinställningar

 (CELLSNET-44179) - Undantag vid inläsning av en HTML-fil (skapad från XSLT)

 (CELLSNET-44145) - System.NullReferenceException i WorkbookMetadata ctor

 (CELLSNET-44143) - Undantag vid arbetsboken under laddning XLSX

 (CELLSNET-44142) - IndexOutOfBoundsException när du skapar en instans av arbetsbok med XLS



 \2) Aspose.Cells Grid Suite


## **Andra förbättringar och förändringar**

## **Buggar**


 (CELLSNET-44151) - JavaScript utlöses inte när innehåll tas bort från GridWeb-cellen

 (CELLSNET-44113) - Rubrikradstext visas också i filtervärdena


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



 Lägger till egenskapen TxtLoadOptions.HasFormula.

 Indikerar om csv-filen innehåller formel.



 Lägger till egenskapen ColorScale.Is3ColorScale.

 Anger om villkorlig formatering är 3 färgskala.



 Tar bort föråldrad Workbook.SaveOptions-egenskap.

 Använd metoden Workbook.Save(Stream,SaveOptions) eller Workbook.Save(string,SaveOptions) istället.



 Lägger till metoden Protection.VerifyPassword.

 Verifierar lösenordet för kalkylbladets skydd.



Lägger till egenskapen Proptection.IsProtectedWithPassword.

 Indikerar om kalkylbladet är skyddat med lösenord.



 Lägger till VbaProject.Sign-metoden.

 Signera VBA-projekt med en DigitalSignature.



 Lägger till egenskapen VbaProject.IsValidSigned.

 Indikerar om signaturen för VBA-projektet är giltig eller inte.



 Lägger till egenskapen VbaProject.CertRawData.

 Får certifikatrådata om VBA-projektet signeras.



 Lägger till egenskapen PdfSaveOptions.OptimizationType.

 Hämtar och ställer in pdf-optimeringstyp.


