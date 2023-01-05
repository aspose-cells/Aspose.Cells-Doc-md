---
title: Skydda och ta bort skydd arbetsblad
type: docs
weight: 50
url: /sv/java/protect-and-unprotect-worksheet/
---
## **Skydda arbetsblad**

När ett kalkylblad är skyddat är de åtgärder en användare kan vidta begränsade. De kan till exempel inte mata in data, infoga eller ta bort rader eller kolumner etc. De allmänna skyddsalternativen i Microsoft Excel är:

- Innehåll
- Föremål
- Scenarier

Skyddade kalkylblad döljer eller skyddar inte känslig data, så det skiljer sig från filkryptering. I allmänhet är kalkylbladsskydd lämpligt för presentationsändamål. Det hindrar slutanvändaren från att ändra data, innehåll och formatering i kalkylbladet.

### **Lägga till eller ta bort skydd**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection som gör det möjligt att komma åt varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

 Worksheet-klassen tillhandahåller[**Skydda**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) metod som används för att tillämpa skydd på ett kalkylblad. Protect-metoden accepterar följande parametrar:

-  Skyddstyp, den typ av skydd som ska tillämpas på kalkylbladet. Skyddstyp appliceras med hjälp av[**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) uppräkning.
- Nytt lösenord, det nya lösenordet som används för att skydda kalkylbladet.
- Old Password, det gamla lösenordet, om kalkylbladet redan är lösenordsskyddat. Om kalkylbladet inte redan är skyddat, skicka bara en noll.

ProtectionType-uppräkningen innehåller följande fördefinierade skyddstyper:

|**Skyddstyper**|**Beskrivning**|
|:- |:- |
|[**ALLT**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|Användaren kan inte ändra något i detta kalkylblad|
|[**INNEHÅLL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|Användaren kan inte ange data i detta kalkylblad|
|[**FÖREMÅL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|Användaren kan inte ändra ritobjekt|
|[**SCENARIER**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|Användaren kan inte ändra sparade scenarier|
|[**STRUKTURERA**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|Användaren kan inte ändra sparad struktur|
|[**FÖNSTER**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|Användaren kan inte ändra sparade fönster|
|[**INGEN**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Inget skydd|

Exemplet nedan visar hur man skyddar ett kalkylblad med ett lösenord.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Efter att ovanstående kod har använts för att skydda kalkylbladet, kontrollera skyddet på kalkylbladet genom att öppna det. När du öppnar filen och försöker lägga till några data till kalkylbladet, visas följande dialogruta:

**En dialogruta som varnar om att en användare inte kan ändra kalkylbladet** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

För att arbeta med kalkylbladet, avskydda kalkylbladet genom att välja**Skydd** , då**Avskydda arket** från**Verktyg** menyalternativ som visas nedan.

**Välja Unprotect Sheet menyalternativ** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

En dialogruta öppnas som frågar efter ett lösenord.

**Ange lösenord för att avskydda kalkylbladet** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Skydda några Cells**

 Det kan finnas vissa scenarier där du bara behöver låsa några få celler i kalkylbladet. Om du vill låsa vissa specifika celler i kalkylbladet måste du låsa upp alla andra celler i kalkylbladet. Alla celler i ett kalkylblad är redan initierade för låsning, du kan kontrollera detta genom att öppna valfri Excel-fil i MS Excel och klicka på**Format | Cells...** att visa**Format Cells** dialogrutan och klicka sedan på fliken Skydd och se en kryssruta märkt "Låst" är markerad som standard.

Följande är de två metoderna för att genomföra uppgiften.

**Metod 1:**

Följande punkter beskriver hur du låser några celler med MS Excel. Denna metod gäller för Microsoft Office Excel 97, 2000, 2002, 2003 och senare versioner.

1. Markera hela kalkylbladet genom att klicka på knappen Välj alla (den grå rektangeln direkt ovanför radnumret för rad 1 och till vänster om kolumn bokstaven A).
1. Klicka på Cells på Format-menyn, klicka på fliken Skydd och avmarkera sedan kryssrutan Låst.

 Detta låser upp alla celler i kalkylbladet

{{% alert color="primary" %}}

Om kommandot celler inte är tillgängligt kan delar av kalkylbladet redan vara låst. Peka på Skydd på Verktyg-menyn och klicka sedan på Ta bort skydd för ark .

{{% /alert %}}

1. Markera bara de celler du vill låsa och upprepa steg 2, men den här gången markerar du kryssrutan Låst.
1.  På**Verktyg** menyn, välj**Skydd** , klick**Skydda ark** , och klicka sedan**OK**.

{{% alert color="primary" %}}

I dialogrutan Skydda ark har du möjlighet att ange ett lösenord och välja de element som du vill att användarna ska kunna ändra.

{{% /alert %}}

**Metod 2:**

den här metoden använder vi Aspose.Cells API endast för att utföra uppgiften.

Följande exempel visar hur du skyddar några få celler i kalkylbladet. Den låser upp alla celler i kalkylbladet först och låser sedan 3 celler (A1, B1, C1) i det. Slutligen skyddar det kalkylbladet. En rad/kolumn har en stil API som dessutom innehåller en uppsättning låst metod. Du kan använda den här metoden för att låsa eller låsa upp raden/kolumnen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Skydda en rad i arbetsbladet**

 Aspose.Cells låter dig enkelt låsa valfri rad i kalkylbladet. Här kan vi använda oss av[**appliceraStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) metod av[**Rad**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) klass för att tillämpa stil på en viss rad i kalkylbladet. Denna metod tar två argument: a[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objekt och[**StilFlagga**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur man skyddar en rad i kalkylbladet. Den låser upp alla celler i kalkylbladet först och låser sedan den första raden i det. Slutligen skyddar det kalkylbladet. En rad/kolumn har stilen API som dessutom innehåller en setCellLocked-metod. Du kan låsa eller låsa upp raden/kolumnen med StyleFlag-strukturen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Skydda en kolumn i arbetsbladet**

 Aspose.Cells låter dig enkelt låsa valfri kolumn i kalkylbladet. Här kan vi använda oss av[**appliceraStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) metod av[**Kolumn**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) klass för att tillämpa stil på en viss kolumn i kalkylbladet. Denna metod tar två argument: a[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objekt och[**StilFlagga**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur man skyddar en kolumn i kalkylbladet. Det låser upp alla celler i kalkylbladet först och låser sedan den första kolumnen i det. Slutligen skyddar det kalkylbladet. En rad/kolumn har en stil API som dessutom innehåller en uppsättning låst metod. Du kan låsa eller låsa upp raden/kolumnen med StyleFlag-strukturen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Ta bort skyddet av ett arbetsblad**

[Skydda arbetsblad](/cells/sv/java/protect-and-unprotect-worksheet/#protect-worksheets) och[Avancerade skyddsinställningar sedan Excel XP](/cells/sv/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) diskuterade olika metoder för att skydda arbetsblad. Vad händer om en utvecklare behöver ta bort skyddet från ett skyddat kalkylblad vid körning så att vissa ändringar kan göras i filen? Detta kan enkelt göras med Aspose.Cells.

### **Använder Microsoft Excel**

Så här tar du bort skyddet från ett kalkylblad:

 Från**Verktyg** menyn, välj**Skydd** följd av**Avskydda arket**.

**Välj Unprotect Sheet** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

Skyddet tas bort om inte kalkylbladet är lösenordsskyddat. I det här fallet uppmanas en dialogruta att ange lösenordet.

**Ange lösenord för att avskydda kalkylbladet** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Använder Aspose.Cells**

 Ett kalkylblad kan oskyddas genom att anropa[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**Avskydda**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect() ) metod. De[**Avskydda**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()) metod kan användas på två sätt, som beskrivs nedan.

### **Avskydda ett enkelt skyddat arbetsblad**

Ett enkelt skyddat kalkylblad är ett som inte är skyddat med ett lösenord. Sådana kalkylblad kan oskyddas genom att anropa unprotect-metoden utan att skicka en parameter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Avskydda ett lösenordsskyddat kalkylblad**

Ett lösenordsskyddat kalkylblad är ett som är skyddat med ett lösenord. Sådana kalkylblad kan oskyddas genom att anropa en överbelastad version av Unprotect-metoden som tar lösenordet som en parameter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Avancerade skyddsinställningar sedan Excel XP**

[Skydda arbetsblad](/cells/sv/java/protect-and-unprotect-worksheet/#protect-worksheets) diskuterade att skydda ett kalkylblad i Microsoft Excel 97 och 2000. Men sedan utgivningen av Excel 2002 eller XP har Microsoft lagt till många avancerade skyddsinställningar. Dessa skyddsinställningar begränsar eller tillåter användare att:

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket mer.

Aspose.Cells stöder alla avancerade skyddsinställningar som erbjuds av Excel XP och senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

Så här visar du skyddsinställningarna i Excel XP:

1.  Från**Verktyg** menyn, välj**Skydd** följd av**Skydda ark**.
 En dialogruta visas.

   **Dialog för att visa skyddsalternativ i Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. Tillåt eller begränsa kalkylbladsfunktioner eller använd ett lösenord.

### **Avancerade skyddsinställningar med Aspose.Cells**

Aspose.Cells stöder alla avancerade skyddsinställningar.

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection-samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

 Klassen Worksheet tillhandahåller skyddsegenskapen som används för att tillämpa dessa avancerade skyddsinställningar. Skyddsegendomen är i själva verket ett föremål för[**Skydd**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) klass som kapslar in flera booleska egenskaper för att inaktivera eller aktivera begränsningar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Nedan finns ett litet exempel på applikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Spara filen i formatet EXCEL97TO2003 eller XLSX eftersom dessa avancerade skyddsinställningar endast stöds av MS Excel XP och senare versioner.

{{% /alert %}}

### **Cell Låsningsproblem**

Om du vill hindra användare från att redigera celler måste cellerna låsas innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om kalkylbladet är skyddat. I Microsoft Excel XP kan celler låsas genom följande dialogruta:

**Dialog för att låsa celler i Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Det är möjligt att låsa celler med Aspose.Cells API också. Varje cell har en stil API som dessutom innehåller en setLocked-metod. Använd den för att låsa eller låsa upp celler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
