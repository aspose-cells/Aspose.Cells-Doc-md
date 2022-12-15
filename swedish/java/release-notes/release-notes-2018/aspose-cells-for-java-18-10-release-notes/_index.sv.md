---
title: Aspose.Cells for Java 18.10 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-java-18-10-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.10.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42634|Konvertera vänster höger bandform till bild|Förbättring|
|CELLSJAVA-42713|Aspose.Cells for Java JavaDocs - paketlistfil saknas|Förbättring|
|CELLSJAVA-42528|Teckensnitt är inte en giltig HTML5 och självstängande tagg och webbläsare ger en felaktig bild av dess innehåll|Förbättring|
|CELLSJAVA-42728|Ett undantag (StackOverFlow) uppstår när du sparar till PDF-utdata|Insekt|
|CELLSJAVA-42729|Fel värde beräknat av ROUNDUP()|Insekt|
|CELLSJAVA-42724|Kopiera ett intervall med PasteType.ALL (Klistra in alternativ) som inte kopierar radhöjder korrekt|Insekt|
|CELLSJAVA-42722|Hyperlänktextformatering förloras när ny text ställs in|Insekt|
|CELLSJAVA-42688|Ogiltigt ryskt datumformat|Insekt|
|CELLSJAVA-42721|Problem med SheetRender-teckensnitt|Insekt|
|CELLSJAVA-42723|Undantag "java.lang.OutOfMemoryError: Java heap space" vid rendering av MS Excel-fil till PDF|Insekt|
|CELLSJAVA-42725|Citat visas i formeln när cellformeln hämtas via Aspose.Cells|Insekt|
|CELLSJAVA-42720|Prestandaförsämring vid användning av villkorlig formatering|Insekt|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till egenskapen HtmlSaveOptions.WidthScalable**
Anger om skalbar enhet används för att beskriva kolumnbredden vid export av fil till HTML. Standardvärdet är falskt.
### **Lägger till egenskapen WorkbookDesigner.UpdateEmptyStringAsNull**
Anger om det tomma strängvärdet bearbetas som null.
### **Uppdaterar det returnerade värdet för metoden DocumentProperty.ToDateTime(), egenskaperna BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted och BuiltInDocumentPropertyCollection.LastSavedTime.**
Returnerar tiden i lokal tidszon.
### **Kräver starkare begränsningar för användarens input för FormatCondition.Formula1/Formula2**
Den vanliga inmatningssträngen kan inte bestämmas om den ska referera till en namnreferens eller om det bara är ett konstant strängvärde. Så nu kräver vi att formeln måste börja med '='-tecken. För vanligt strängvärde "sss", använd format som "=\"sss\"".
