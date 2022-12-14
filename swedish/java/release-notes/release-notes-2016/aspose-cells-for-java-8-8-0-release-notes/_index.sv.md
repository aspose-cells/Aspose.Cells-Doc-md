---
title: Aspose.Cells för Java 8.8.0 Release Notes
type: docs
weight: 110
url: /sv/java/aspose-cells-for-java-8-8-0-release-notes/
---
## **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41812 | Bildmarkörer stöds inte när data grupperas i smarta markörer| Förbättring|
|CELLSJAVA-41772 | Konvertering till HTML resulterar i tom sida| Insekt|
|CELLSJAVA-41738 | Vertikal justering av texten i en textruta ändras från mitten till toppen medan kalkylbladet renderas till bild och PDF| Insekt|
|CELLSJAVA-41503 | Teckensnittsersättningsvarningar fungerar inte vid konvertering av kalkylark till HTML-format| Insekt|
|CELLSJAVA-41797 | Aspose.Cells beräknar inte värdet på cellen korrekt| Insekt|
|CELLSJAVA-41779 | Metoden Cell.calculate() beräknar inte värdena korrekt| Insekt|
|CELLSJAVA-41813 | Mellanslagsförvrängning i slutet av andra sidan markerad som röd i exemplet i Excel-fil| Insekt|
|CELLSJAVA-41744 | Texten är feljusterad i den utgående PDF-filen| Insekt|
|CELLSJAVA-41723 | Aspose.Cells genererade PDF-fel överensstämmer med Excel-genererade PDF-filer av samma kalkylblad| Insekt|
|CELLSJAVA-41802 |Kategoriaxelns ticketiketter matchar inte i utdata från PDF i Excel till PDF-rendering| Insekt|
|CELLSJAVA-41800 | Vinkeln för diagrametiketter har ändrats i diagrammets PDF| Insekt|
|CELLSJAVA-41798 | Förklaringsposten trimmas när diagrammet konverteras till PDF| Insekt|
|CELLSJAVA-41792 | Rödfärgad stapel saknas i Excel men visas i PDF| Insekt|
|CELLSJAVA-41785 | Kalkylarket blir skadat efter att ha kopierat arbetsboken och ställt in dataetikettens position| Insekt|
|CELLSJAVA-41784 | Felfältet saknas vid kopiering av arbetsbok| Insekt|
|CELLSJAVA-41780 | Text i TextBox renderas ofullständig när kalkylblad konverteras till bild| Insekt|
|CELLSJAVA-41773 | DataLabels saknas för ett diagram i utdatabilden/PDF för kalkylarket| Insekt|
|CELLSJAVA-41757 | Positivt värderade staplar visas under 0-värdets x-axelregel i diagrammets PDF| Insekt|
|CELLSJAVA-41734 | Diagrammets teckenordning är omvänd när kalkylblad renderas till bild| Insekt|
|CELLSJAVA-41811 | Aspose.Cells bryter Power Pivot-tabellerna när du öppnar och sparar XLSM-filformatet| Insekt|
|CELLSJAVA-41807 | Problem med grupperade rader vid kopiering av intervall i XLSX-fil| Insekt|
|CELLSJAVA-41806 | Problem med grupperade rader vid kopiering av intervall i XLS-fil| Insekt|
|CELLSJAVA-41804 |Formel för WordArt reagerar inte på argumentändringar efter konvertering av XLS till XLSB| Insekt|
|CELLSJAVA-41803 | Det villkorliga formateringsintervallet är felaktigt och matchar inte med Microsoft Excel| Insekt|
|CELLSJAVA-41809 | Worksheet.calculateFormula kastar noll-pekareundantag när formel ställs in via NameCollection| Undantag|
|CELLSJAVA-41808 | "java.lang.NullPointerException" på Workbook.save| Undantag|
## **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41615 | Inställning av rubrikfält och flikstilar fungerar inte| Insekt|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen HTMLLoadOptions.DeleteRedundantSpaces**
 Indikerar om överflödiga mellanslag tas bort när texten radbryts med hjälp av<br>märka.
### **Föråldrar egenskapen LoadOptions.ConvertNumericData och lägger till egenskapen TxtLoadOptions.ConvertNumericData.**
Använd egenskapen TxtLoadOptions.ConvertNumericData eller HTMLLoadOptions.ConvertNumericData istället.
### **Lägger till egenskapen Style.QuotePrefix.**
Anger om cellens värde börjar med enkla citattecken.
### **Lägger till egenskapen QueryTable.ConnectionId.**
Hämtar anslutnings-id för frågetabellen.
### **Lägger till egenskapen ExternalConnection.Id.**
Får anslutningens ID.
### **Lägger till egenskapen ListObject.QueryTable.**
Hämtar den länkade frågetabellen för tabellen.
### **Lägger till egenskapen HTMLLoadOptions.KeepPrecision.**
Anger om ett strängvärde inte analyseras om längden är 15.

{{% alert color="primary" %}} 

Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.8.0 också i denna Aspose.Cells för Java v8.8.0.

{{% /alert %}}
