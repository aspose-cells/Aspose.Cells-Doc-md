---
title: Aspose.Cells for .NET 21.12 Release Notes
type: docs
weight: 1
url: /sv/net/aspose-cells-for-net-21-12-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.12](https://www.nuget.org/packages/Aspose.Cells/21.12.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-49680|Stöd för konvertering av Excel till SQL-skript.|Ny funktion|
|CELLSNET-49717|Stöd för konvertering av Excel till XML-data|Ny funktion|
|CELLSNET-49853| Stöd för import av xml-data|Ny funktion|
|CELLSNET-48190|Uppdatera prioriteringar när du lägger till nytt formatvillkor|Förbättring|
|CELLSNET-49758| Sortering med DataSorter påverkar tabellformateringen|Förbättring|
|CELLSNET-49828|FormatConditionCollection.AddCondition() ger olika beteende för formeln|Förbättring|
|CELLSNET-49981|Lägg till filteralternativ för revisionsloggar medan du skapar arbetsbok från mallfil|Förbättring|
|CELLSNET-49739|Ignorera 3D-referenser för villkorlig formatering när du kopierar till en annan arbetsbok|Förbättring|
|CELLSNET-49984|Läs en del data från skadad xls-fil.|Förbättring|
|CELLSNET-49990|Stöd inställning av anpassade totaler radformel för tabell.|Förbättring|
|CELLSNET-49825|Prestandaproblem med ExportImagesAsBase64-attributet i Excel till HTML konvertering|Prestanda|
|CELLSNET-49827|RefersTo för definierat intervall är felaktigt escaped|Insekt|
|CELLSNET-49759|Tomma celler exporteras fortfarande som tomma XML-element|Insekt|
|CELLSNET-49817|Texten är inte mittjusterad med teckensnittet "Credit Suisse Type Light" vid rendering till Emf|Insekt|
|CELLSNET-49864|Ord som visas i omvänd ordning för höger-till-vänster text i XLSX till PDF rendering|Insekt|
|CELLSNET-49873|Xlsx till pdf: Sidbrytning är annorlunda jämfört med Excel-genererad pdf|Insekt|
|CELLSNET-49922|Tecken får inte plats på en sida och utskriftspositionen ändras i Excel till PDF-rendering|Insekt|
|CELLSNET-49998|Kan inte visa specifik XLS-fil med HTML-uppmärkning|Insekt|
|CELLSNET-49742|Skillnader i chart1.xml efter sparande|Insekt|
|CELLSNET-49875|XLSX till EMF överlappande bockmarkeringar|Insekt|
|CELLSNET-49904|Diagram till PNG datum som inte konverterats korrekt|Insekt|
|CELLSNET-49905|Regression: Problem vid konvertering av diagram till PNG|Insekt|
|CELLSNET-49969|Overflow-fel när XLS-dokument sparas till XLSX/XSLM|Insekt|
|CELLSNET-49760|Merged Area visas fel vid konvertering till html.|Insekt|
|CELLSNET-49789|Excel originalrutnät bör inte ändras när du sparar html-fil|Insekt|
|CELLSNET-49850|Bild: FitToCell-parametern fungerar inte i bildsmarta markörer|Insekt|
|CELLSNET-49870|Rubriken blir bredare när du kombinerar flera ark i Excel-kalkylblad|Insekt|
|CELLSNET-49898|Visa kanten på cellerna medan bilderna anpassas till cellerna med hjälp av smarta markörer|Insekt|
|CELLSNET-49924|Aspose-genererade XLSX-filer öppnas med fel|Insekt|
|CELLSNETCORE-301|Lägg till kalkylblad misslyckas när hyperlänk har en nolladress|Insekt|
|CELLSNET-49812|Undantag när filen ODS är öppen|Undantag|
|CELLSNET-49876|Undantag när du sparar om en XLSX-fil|Undantag|
|CELLSNET-49943|System.NullReferenceException vid kopiering av arbetsbok|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Fler begränsningar för att lägga till områden för validering.**

Vi har ändrat områdesmodellen för validering och villkorlig formatering för prestandaövervägande. Den nya modellen kräver fler begränsningar för sekvensen av tillagda områden. För Validation.AddArea(CellArea cellArea, bool checkIntersection, bool checkEdge) och Validation.AddAreas(CellArea[]areas, bool checkIntersection, bool checkEdge), om de två "check"-parametrarna är falska, måste användaren se till att de tillagda områdena sorteras i stigande ordning efter de övre vänstra hörnen. Annars kan oväntade resultat fås för andra operationer. I den nya versionen, eftersom prestandan för att lägga till stora mängder områden har förbättrats avsevärt, tror vi inte att Validation.AddArea(CellArea cellArea) kommer att vara en flaskhals längre. Så vi tror att användare bara kan ringa AddArea(CellArea cellArea) direkt, utan att behöva använda dessa två speciella metoder.

### **Ändrade beteende för att lägga till formatvillkor i FormatConditionCollection.**

För FormatConditionCollection.AddCondition(...)-metoder, gör gamla versioner prioritet för en nyligen tillagd som den lägsta. Det skiljer sig från ms excels beteende. Från den här versionen, precis som vad du får för operationen i ms excel, gör vi det nyligen tillagda formatvillkorets prioritet som den högsta.

### **Lägger till egenskapen AbstractInterruptMonitor.TerminateWithoutException.**

Den här egenskapen anger när ett avbrott har krävts för en process, om processen ska avslutas med ett undantag eller bara avslutas tyst. Som standard är den här egenskapen falsk, det vill säga att processen avslutas av ett undantag när den avbryts.

### **Lägger till WorkbookSettings.ResourceProvider-egenskapen.**

Omdöpt egenskap för WorkbookSettings.StreamProvider för att göra den mer lämpad för sin funktion och lättare för användare att förstå.

### **Lägger till alternativet LoadDataFilterOptions.Revision.**

Vissa mallfiler kan innehålla stora mängder revisionsloggar och som orsakar dålig prestanda för att ladda arbetsboken. Användaren kan använda detta alternativ för att kontrollera om dessa revisionsloggar ska laddas eller inte.

### **Föråldrad WorkbookSettings.StreamProvider-egenskap.**

Använd egenskapen WorkbookSettings.ResourceProvider istället.

### **Tar bort den föråldrade egenskapen PdfSaveOptions.StreamProvider.**

Använd egenskapen WorkbookSettings.ResourceProvider istället.

### **Lägger till egenskapen JsonLoadOptions.MultipleWorksheets.**

Anger om varje attribut för JsonObject-objekt importeras som ett kalkylblad när alla underordnade noder är matrisnoder.

### **Lägger till FileFormatType.SqlScript, SaveFormat.SqlScript och SqlScriptSaveOptions**

Representerar alternativen för att spara sql-skript.

### **Lägger till SaveFormat.Xml, LoadFormat.Xml, XmlSaveOptions och XmlLoadOptions**

Representerar alternativen för R/W xml-filer.

### **Lägger till egenskapen HtmlSaveOptions.SaveAsSingleFile.**

 Anger om excel sparas som en enda fil.

### **Lägger till egenskapen JsonLoadOptions.MultipleWorksheets.**

 Anger om data från Json-filen laddas till flera kalkylblad

### **Lägger till egenskapen PdfSaveOptions.Producer.**

 Hämtar och ställer in producent av genererade pdf-dokument.

### **Lägger till metoderna ListColumn.GetCustomTotalsRowFormula() och ListColumn.SetCustomTotalsRowFormula()**

 Hämtar och ställer in den anpassade formeln för totalraden i tabellen.

