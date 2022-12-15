---
title: Aspose.Cells for .NET 8.8.0 Release Notes
type: docs
weight: 110
url: /sv/net/aspose-cells-for-net-8-8-0-release-notes/
---
### **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44376 | Ge möjligheten att förbjuda konvertering av långa numeriska värden till exponentiell notation vid import från HTML|Ny funktion|
|CELLSNET-44360 | Upptäcker ledande enkla citattecken i cellen|Ny funktion|
|CELLSNET-44356 | Hämta mål- eller utdatacellsadress för en ExternalConnection|Ny funktion|
|CELLSNET-44340 | Stöd för lokalisering (tyska) av validering på klientsidan|Ny funktion|
|CELLSNET-44345 | Formel för WordArt reagerar inte på argumentändringar när XLS konverteras till XLSB| Förbättring|
|CELLSNET-44342 | Processen verkar hänga med 100 % CPU-användning för att konvertera ensidigt kalkylblad till PDF| Prestanda|
|CELLSNET-44324 | XLSM blir skadad efter att ha fyllt i data igen och uppdaterat pivottabellen| Insekt|
|CELLSNET-44312 |Radbrytningar går förlorade vid import av HTML och export till kalkylark| Insekt|
|CELLSNET-44311 | Gränser försvinner vid import av HTML och export till kalkylark| Insekt|
|CELLSNET-44286 | Sample1.xlsx blir skadad efter att ha öppnats och uppdaterats| Insekt|
|CELLSNET-44375 | Felaktig kodning med målfilen (CSV).| Insekt|
|CELLSNET-44368 | Miljontalsformateringsproblem vid konvertering av Excel till PDF| Insekt|
|CELLSNET-44347 | API återger två PDF-sidor för ett kalkylblad oavsett om OnePagePerSheet ställs in på sant| Insekt|
|CELLSNET-44335 | Text beskärs under rendering av kalkylark| Insekt|
|CELLSNET-44382 | Diagrammet genereras inte korrekt i utdata Excel-filen| Insekt|
|CELLSNET-44373 | Justeringsproblem med punktlista (form) i den renderade bilden| Insekt|
|CELLSNET-44337 | Stilen på punktlistan (formen) är annorlunda i utdatabilden| Insekt|
|CELLSNET-44300 | En del av X-axeletiketter renderas i horisontell orientering medan diagram konverteras till bild| Insekt|
|CELLSNET-44372 | Excel-fil med inbäddade dokument blir korrupta när du sparar| Insekt|
|CELLSNET-44369 |# Ref! efter att ha kopierat celler som innehåller referenser till namngivna celler från en arbetsbok till en annan
| Insekt|
|CELLSNET-44359 |Om du tar bort lösenordet från ett skyddat kalkylblad ändras namnet på det inbäddade objektet| Insekt|
|CELLSNET-44348 | Antalet avrundas när HTML konverteras till kalkylarksformat| Insekt|
|CELLSNET-44330 | Objektreferens inte angett undantag vid öppning av en Excel-fil| Undantag|
|CELLSNET-44323 | Objektreferens är inte inställd på en instans av ett objekt i PivotTable.RefreshData| Undantag|
|CELLSNET-44355 | Index låg utanför gränserna för arrayundantaget när Excel konverterades till PDF| Undantag|
|CELLSNET-44354 | Form till bild Fel vid konvertering av Excel till PDF| Undantag|
|CELLSNET-44380 | "Ogiltig formel" när en specifik Excel-fil laddas via Aspose.Cells API:er| Undantag|
|CELLSNET-44370 | "Ogiltigt avsnitts-ID för sidfotsbild" när du öppnar Excel-filen| Undantag|
|CELLSNET-44357 | System.ArgumentException: Objektet har redan lagts till, på Workbook ctor| Undantag|
### **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44350 | Lägg till varning för sessionstimeout för GridWeb|Ny funktion|
|CELLSNET-44339 | 500 Internt fel: "Fel i Cell: Ogiltig formel" genom att infoga ogiltig formel i GridWeb UI| Undantag|
|CELLSNET-44326 | Genom att klicka på en cell ändras den formaterade texten till dess HTML-källa| Insekt|
|CELLSNET-44325 | GridWeb ändrar innehållet i datavalideringslista/rullgardinsmeny| Insekt|
|CELLSNET-44321 |Snabbmenyn växer upp när rader eller kolumner läggs till genom den| Insekt|
|CELLSNET-44320 | Att lägga till rader och kolumner via snabbmenyn fungerar inte| Insekt|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen HTMLLoadOptions.DeleteRedundantSpaces**
 Indikerar om överflödiga mellanslag tas bort när texten radbryts med hjälp av<br>märka.
#### **Föråldrar egenskapen LoadOptions.ConvertNumericData och lägger till egenskapen TxtLoadOptions.ConvertNumericData.**
Använd egenskapen TxtLoadOptions.ConvertNumericData eller HTMLLoadOptions.ConvertNumericData istället.
#### **Lägger till egenskapen Style.QuotePrefix.**
Anger om cellens värde börjar med enkla citattecken.
#### **Lägger till egenskapen QueryTable.ConnectionId.**
Hämtar anslutnings-id för frågetabellen.
#### **Lägger till egenskapen ExternalConnection.Id.**
Får anslutningens ID.
#### **Lägger till egenskapen ListObject.QueryTable.**
Hämtar den länkade frågetabellen för tabellen.
#### **Lägger till egenskapen HTMLLoadOptions.KeepPrecision.**
Anger om ett strängvärde inte analyseras om längden är 15.
