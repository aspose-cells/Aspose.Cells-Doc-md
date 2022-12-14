---
title: Aspose.Cells för Java 8.8.3 Release Notes
type: docs
weight: 80
url: /sv/java/aspose-cells-for-java-8-8-3-release-notes/
---
## **1) Aspose.Cells**

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41866|Hur man ställer in egenskaper för textinmatning för textalternativ|Ny funktion|
|CELLSJAVA-41865|Skapa textruta där varje rad har olika horisontell justering|Ny funktion|
|CELLSJAVA-41873|Konvertering till HTML gör överflödiga tomma rader|Insekt|
|CELLSJAVA-41869|Textjusteringen ändras efter att en mall XLS-fil har sparats på nytt|Insekt|
|CELLSJAVA-41854|Excel-fil med DataBars som inte konverterats till HTML korrekt|Insekt|
|CELLSJAVA-41851|Pivotdiagram skapat med Aspose.Cells visas inte i Excel 2016 för MAC|Insekt|
|CELLSJAVA-41840|Aspose.Cells lägger till null i slutet av sökvägen för resurser HTML|Insekt|
|CELLSJAVA-41878|LightCells API:er genererar endast händelser för den första kolumnen i raden|Insekt|
|CELLSJAVA-41859|Cell kanter visas efter att XLS har sparats om|Insekt|
|CELLSJAVA-41888|Logotypbild försvinner när XLS konverteras till PDF|Insekt|
|CELLSJAVA-41874|Teckenpositionen skiljer sig i den renderade PDF-filen från en XLS-fil|Insekt|
|CELLSJAVA-41852|Text överlappar när kalkylblad konverteras till EMF på Linux|Insekt|
|CELLSJAVA-41823|Textdensitet och radbrytningar är olika jämfört med Excel-genererade PDF|Insekt|
|CELLSJAVA-41822|Text beskärs och överlappas medan kalkylarket renderas till PDF|Insekt|
|CELLSJAVA-41856|Problem med att rendera diagram till PDF|Insekt|
|CELLSJAVA-41855|Att öppna och spara Excel-filen ändrar trendlinjerna|Insekt|
|CELLSJAVA-41890|Spara arbetsbok två gånger, innehållet som sparas andra gången kommer att skilja sig från första gången|Insekt|
|CELLSJAVA-41884|Problem med PageBreaks som inte sorteras innan du sparar till Excel-fil|Insekt|
|CELLSJAVA-41876|Fil korrupt om den öppnas, sparas, öppnas igen och sparas av Aspose.Cells API:er|Insekt|
|CELLSJAVA-41867|Diagramaxelvärden har ändrats efter att en XLS-fil har sparats på nytt|Insekt|
|CELLSJAVA-41861|NullReferenceException när en Excel XLS-fil laddas|Insekt|
|CELLSJAVA-41298|Får inte korrekt information om WordArt-formformatering från Aspose.Cells API:er|Insekt|
|CELLSJAVA-40366|Inbäddad ikon - inte utskrift|Insekt|
|CELLSJAVA-41883|CellsException: Okänd typ av tilläggsfunktion: 9, på Workbook.calculateFormula|Undantag|
|CELLSJAVA-41858|CellsException: Fel vid beräkning av Cell[0BMW CAN Bus Codes V0.4!R4], på Workbook.calculateFormula|Undantag|
|CELLSJAVA-41870|java.lang.ArrayIndexOutOfBoundsException: 4 på Workbook.save medan XLS sparas på nytt|Undantag|
|CELLSJAVA-41864|Undantag: java.lang.IllegalStateException: Ogiltig kodning: null vid omspara av en XLS-fil|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till metoden Cell.GetCharacters(flagga).**
Returnerar alla teckenobjekt.
### **Lägger till egenskapen OleObject.AutoLoad**
Anger om värdapplikationen för det inbäddade objektet ska anropas för att ladda objektdata automatiskt när den överordnade arbetsboken öppnas.
### **Lägger till egenskapen HTMLLoadOptions.SupportDivTag**
 Anger om layouten för<div> taggen när html-filen innehåller<div> tags.Standardvärdet är false.
### **Lägger till egenskapen HtmlSaveOptions.ExportGridLines**
Indikerar om rutnätslinjerna ska exporteras. Standardvärdet är falskt.
### **Lägger till egenskapen ShapeTextAlignment.TextShapeType**
Anger den förinställda geometrin som kommer att användas för en formförvrängning på ett textstycke.
### **Lägger till metoden LoadOptions.SetPaperSize(PaperSizeType-typ).**
Ställer in standardstorleken för utskriftspapper från standardskrivarens inställning.
### **Tar bort föråldrad Workbook.Decrypt()-metod**
Vänligen ställ in WorkbookSettings.Password som null.
### **Lägger till egenskapen ListObject.Comment**
Får och ställer tabellens kommentar.
### **Lägger till metoden ShapeCollection.AddActiveXControl().**
Lägger till ActiveX-kontroll.

{{% alert color="primary" %}} 

Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.8.3 också i denna Aspose.Cells för Java v8.8.3.

{{% /alert %}}
