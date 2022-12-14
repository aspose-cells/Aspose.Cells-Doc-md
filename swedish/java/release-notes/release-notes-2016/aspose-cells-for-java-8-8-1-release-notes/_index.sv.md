---
title: Aspose.Cells för Java 8.8.1 Release Notes
type: docs
weight: 100
url: /sv/java/aspose-cells-for-java-8-8-1-release-notes/
---
## **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41664 |Exportera datafält baserat på villkorlig formatering till HTML| Ny funktion|
|CELLSJAVA-40746 | Stöd ColorScale, DataBar, IconSet när du exporterar XLSX till HTML| Ny funktion|
|CELLSJAVA-41820 | Kalkylbladet har ingen metod calcualteFormula(Strängformel, alternativ för beräkningsalternativ)| Ny funktion|
|CELLSJAVA-40544 | Prestandaflaskhals på Workbook.calculateFormula| Förbättring|
|CELLSJAVA-41817 | Att ställa in ShowAllItems för PivotField verkar inte ha effekt| Insekt|
|CELLSJAVA-41810 | Texten blir överbelastad och överlappar i EMF-bilden| Insekt|
|CELLSJAVA-41801 | Textetiketter överlappar varandra i EMF-bilden| Insekt|
|CELLSJAVA-41834 | Undantag görs vid kopiering av arbetsbok| Insekt|
|CELLSJAVA-41819 | Kalkylark till HTML: Inriktningen av text i en form är fel efter kopiering av tema från källkalkylark| Insekt|
|CELLSJAVA-41824 | Grafen återges inte i utdata-PDF-filen| Insekt|
|CELLSJAVA-41805 | X-axeletiketter saknas i diagrammets PDF| Insekt|
|CELLSJAVA-41767 | Felaktigt nummerformat för X-axeletiketter i diagrammets PDF| Insekt|
|CELLSJAVA-41640 | Långa bindestreck visas inte på rätt sätt i utdata-PDF/bilden för diagrammet| Insekt|
|CELLSJAVA-41604 | Horisontella rutnätslinjer i diagrammet visas inte korrekt i den utgående PDF-filen| Insekt|
|CELLSJAVA-41832 |Få diagramstaplar saknas vid rendering av kalkylblad till bild| Insekt|
|CELLSJAVA-41837 | Lägg till Chart.toPDF(java.io.OutputStream, com.aspose.cells.PdfSaveOptions)| Insekt|
|CELLSJAVA-41839 | Ett namngivet intervall skapas när metoden Cells.copyRow() används inom ett namngivet intervall| Insekt|
|CELLSJAVA-41838 | När du använder autoSizeColumns på arket breddas kolumnen inte ordentligt| Insekt|
|CELLSJAVA-41835 | CellsException medan du sparar kalkylark till PDF| Undantag|
|CELLSJAVA-41826 | NaN Undantag| Undantag|
## **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41719 | Hur man skapar anpassade kommandoknappar i GridWeb (JAVA)| Ny funktion|
|CELLSJAVA-41718 | GridCell.createValidation()-metoden saknas i GridWeb| Förbättring|
|CELLSJAVA-41649 | Scroll stannar inte ibland - Aspose.Cells.GridWeb för JAVA| Insekt|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen WorkbookSettings.PaperSize.**
Den används för att ställa in pappersstorleken för standardskrivaren som standardpappersstorlek för arbetsboken.
### **Lägger till klassen LoadDataFilterOptions och egenskapen LoadOptions.LoadDataFilterOptions.**
Den används för att specificera vilken typ av data som ska laddas när man bygger arbetsboken från mallfilen. Filtrering av laddad data kan förbättra prestandan för användarens speciella syfte, särskilt när du använder LightCells API:er.
### **Lägger till Worksheet.CalculateFormula(strängformel, CalculationOptions opts) metod.**
Den används för att beräkna given formel direkt med användaranpassade alternativ.
### **Lägger till klasser av namnutrymme Aspose.Cells.Drawing.Texts.**
Den används för att ställa in egenskaperna för formens textteckensnitt.
### **Föråldrad Shape.TextFrame-egenskap.**
Använd egenskapen Shape.TextBody.TextAlignment istället.
### **Lägger till egenskapen Shape.TextBody.**
Presenterar inställningen av formens text.
### **Lägger till metoden GridCell.CreateValidation(GridValidationType validationType, bool isRequired).**
Skapar ett valideringsobjekt för en rutnätscell.
### **Lägger till metoden GridCell.RemoveValidation().**
Tar bort valideringsobjektet från en rutnätscell.
### **Lägger till metoden Chart.ToPdf (System.IO.Stream stream).**
Lägger till spardiagram till PDF som en ström.

{{% alert color="primary" %}} 

Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.8.1 också i denna Aspose.Cells för Java v8.8.1.

{{% /alert %}}
