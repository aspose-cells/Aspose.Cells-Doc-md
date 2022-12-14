---
title: Aspose.Cells för Java 8.7.2 Release Notes
type: docs
weight: 120
url: /sv/java/aspose-cells-for-java-8-7-2-release-notes/
---
## **Andra förbättringar och förändringar**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41334 | HYPERLINK formel/funktion - Utöka kalkylbladets hyperlänksamling för att hämta objektet| Ny funktion|
|CELLSJAVA-41788 | Start-egenskapen för en ordnad lista fungerar inte korrekt| Insekt|
|CELLSJAVA-41763 | Aspose Cells API kan inte konvertera varje innehåll i HTML-filen till Excel-fil| Insekt|
|CELLSJAVA-41759 |Layouten är annorlunda när du sparar kalkylark till HTML| Insekt|
|CELLSJAVA-41677 | Hyperlänk som pekar på ett definierat namn resulterar i bruten länk när kalkylblad konverteras till HTML| Insekt|
|CELLSJAVA-41774 | Fel beräkning på vad-om-analys| Insekt|
|CELLSJAVA-41748 | Ryska månadens namn återges annorlunda i PDF jämfört med Excel| Insekt|
|CELLSJAVA-41735 | Cell med valutaformat i BMD detekteras som DateTime| Insekt|
|CELLSJAVA-41648 | Språkberoende datumformat ändras till fast anpassat format samtidigt som SpreadsheetML konverteras till XLSX| Insekt|
|CELLSJAVA-41777 | Problem med den utgående XLSB-filen - XLS to XLSB Conversion| Insekt|
|CELLSJAVA-41749 | Om du ställer in bild i sidhuvud (för att skapa vattenstämpel) återställs formatera bildinställningar| Insekt|
|CELLSJAVA-41787 | Excel-konvertering till PDF tar evigheter| Insekt|
|CELLSJAVA-41762 | Axis Label överlappar vid konvertering av kalkylblad till PDF| Insekt|
|CELLSJAVA-41752 | Dataetiketter överlappar cirkeldiagrammet när de renderas till PDF| Insekt|
|CELLSJAVA-41751 | Horisontell/vertikal versaler Axis titeltext visas i meningsskifte i diagrammets PDF-format| Insekt|
|CELLSJAVA-41736 | Diagramjusteringsproblem vid rendering av arbetsblad till bild| Insekt|
|CELLSJAVA-41755 | Vertikal regel saknas i diagrammets PDF-format| Insekt|
|CELLSJAVA-41756 |Tjockleken på horisontella regler är mer än tjockleken i det faktiska diagrammet vid rendering till PDF| Insekt|
|CELLSJAVA-41754 | SmartArt kopieras inte när arbetsbok kopieras| Insekt|
|CELLSJAVA-41717 | Vertikal justering av diagrammets förklaring har ändrats när ODS konverterades till XLSX| Insekt|
|CELLSJAVA-41716 | Diagram saknas vid konvertering av ODS till XLSX| Insekt|
|CELLSJAVA-41636 | Cell formatproblem - visningsvärdet är inte korrekt i GridWeb (JAVA)| Insekt|
|CELLSJAVA-41746 | java.lang.OutOfMemoryError: GC-overheadgränsen har överskridits, medan kalkylbladet sparades till PDF| Undantag|
|CELLSJAVA-41768 | com.aspose.cells.Name kan inte castas till java.lang.Integer när du kopierar arbetsblad| Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen TextBoxCollection[string].**
Hämtar textrutan med namnet.
### **Lägger till klassen AbstractCalculationEngine och CalculationData.**
Nytt API för användare att implementera sin egen beräkningsmotor för att utöka standardberäkningsmotorn Aspose.Cells.
### **Lägger till egenskapen CalculationOptions.CustomEngine.**
Tillåt användaren att använda den nya anpassade beräkningsmotorn för att beräkna formler.

{{% alert color="primary" %}} 

Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.7.2 också inkluderade i denna Aspose.Cells för Java v8.7.2.

{{% /alert %}}
