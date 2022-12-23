---
title: Aspose.Cells for .NET 8.7.1 Release Notes
type: docs
weight: 130
url: /sv/net/aspose-cells-for-net-8-7-1-release-notes/
---
### **Andra förbättringar och förändringar**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44154 |Stöd för att läsa/skriva frågetabell.|Ny funktion|
|CELLSNET-43616 | Stöd Array-formel som involverar "TABELL"-funktionen.|Ny funktion|
|CELLSNET-44195 | Filen öppnas i skyddad vy efter konvertering till filformatet XLS| Förbättring|
|CELLSNET-44182 | Cells hitta med anpassad formatering fungerar i äldre version men inte i nyare version| Förbättring|
|CELLSNET-44187 | Cell-värden är felaktigt ersatta med # när de konverteras till HTML| Insekt|
|CELLSNET-44161 | Aspose.Cells genererad XLSX gör att Excel 2007 reparerar kalkylarket| Insekt|
|CELLSNET-44063 | Pivottabell förlorar rubrikens ordning efter att ha arbetat med indatafilen| Insekt|
|CELLSNET-44215 | Spara till pdf som visar ovidkommande data till höger om tabellen| Insekt|
|CELLSNET-44201 | Problem gällande teckenindex som inte stöds i CHAR-formeln| Insekt|
|CELLSNET-44193 | Sned cellskuggning återges inte korrekt till PDF| Insekt|
|CELLSNET-44213 | Att spara bild från kalkylblad resulterar i en lite annorlunda bild| Insekt|
|CELLSNET-44192 | Kategorietiketter överst i diagrammet är högerjusterade istället för vänsterjusterade| Insekt|
|CELLSNET-44240 | Problem med att byta namn på ett namngivet intervall| Insekt|
|CELLSNET-44239 | Cell.ContainsExternalLink returnerar sant om formeln är =VECKANT| Insekt|
|CELLSNET-44231 |Om du sparar kalkylarket förstörs resultatet| Insekt|
|CELLSNET-44222 | Arbetsbok med makron blir skadad med version 8.7.0| Insekt|
|CELLSNET-44220 | Att ställa in egenskapen WorkbookSettings.Password förstör det resulterande kalkylarket| Insekt|
|CELLSNET-44218 | Om du sparar om XLSX byter namn på filen xl\embeddings\oleObject1.bin| Insekt|
|CELLSNET-44214 | Copy Range behåller inte ListObject-inställningarna| Insekt|
|CELLSNET-44203 | Formelreferenser skiljer sig mellan 8.6.2 och 8.7.0 för Worksheet.Copy operation| Insekt|
|CELLSNET-44241 | System.IndexOutOfRangeException på Cells.ImportData| Undantag|
|CELLSNET-44226 | System.ArgumentException at Workbook.Save medan du sparar i ODS-format| Undantag|
|CELLSNET-44225 | Undantag: "Ogiltig text för det definierade namnet." inträffade vid kopiering av arbetsblad| Undantag|
|CELLSNET-44223 | NullReferenceException när en specifik XLSX-fil laddas| Undantag|
|CELLSNET-44212 | NullReference undantag vid öppning av källexcelfilen| Undantag|
|CELLSNET-44204 | CellsException: Teckenstorleken är utanför intervallet, i Workbook ctor| Undantag|
|CELLSNET-44196 | Ge möjligheten att upptäcka vilken kolumn som filtreras och vilket värde som ska filtreras efter i GridWeb-gränssnittet|Ny funktion|
|CELLSNET-44232 |GridDesktop problem med RemoveRow(index) där index är "0"| Insekt|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen LookInType.OriginalValues.**
Hitta bara objekt från de ursprungliga värdena utan format.
