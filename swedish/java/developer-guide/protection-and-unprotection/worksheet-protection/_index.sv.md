---
title: Skydda och avskydda kalkylblad
type: docs
weight: 50
url: /sv/java/protect-and-unprotect-worksheet/
---

## **Skydda kalkylblad**

När ett kalkylblad är skyddat är användarens åtgärder begränsade. Till exempel kan de inte mata in data, infoga eller ta bort rader eller kolumner osv. De generella skyddsalternativen i Microsoft Excel är:

- Innehåll
- Objekt
- Scenarier

Skyddade kalkylblad döljer inte eller skyddar känsliga data, så det skiljer sig från filkryptering. I allmänhet är kalkylbladsskydd lämpligt för presentationsändamål. Det förhindrar att slutanvändaren ändrar data, innehåll och formatering i kalkylbladet.

### **Lägga till eller ta bort skydd**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Arbetsboken-klassen tillhandahåller metoden [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect-int-) som används för att tillämpa skydd på ett kalkylblad. Metoden Protect accepterar följande parametrar:

- Skyddstyp, typen av skydd som ska tillämpas på kalkylbladet. Skyddstypen tillämpas med hjälp av [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType)-uppräkningen.
- Nya lösenordet, det nya lösenordet som används för att skydda kalkylbladet.
- Gammalt lösenord, det gamla lösenordet, om kalkylbladet redan är lösenordsskyddat. Om kalkylbladet inte redan är skyddat med lösenord, skicka bara en null.

SkyddsType-uppräkningen innehåller följande fördefinierade skyddstyper:

|**Skydds typer**|**Beskrivning**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|Användaren kan inte ändra någonting på den här arbetsbladet|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|Användaren kan inte mata in data på detta arbetsblad|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|Användaren kan inte ändra ritobjekt|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|Användaren kan inte ändra sparade scenarier|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|Användaren kan inte ändra sparad struktur|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|Användaren kan inte ändra sparade fönster|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Inget skydd|

Nedan följer ett exempel på hur man skyddar ett arbetsblad med lösenord.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Efter ovanstående kod används för att skydda arbetsbladet, kontrollera skyddet på arbetsbladet genom att öppna den. När du öppnar filen och försöker lägga till lite data på arbetsbladet, visas följande dialogruta:

**En dialogruta som varnar för att användaren inte kan ändra arbetsbladet** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

För att arbeta med arbetsbladet, avskydda arbetsbladet genom att välja **Skydd**, sedan **Avskydda blad** från **Verktyg** menyobjekt som visas nedan.

**Val av Unprotect Sheet-menyalternativ** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

En dialogruta öppnas som ber om ett lösenord.

**Ange lösenord för att avskydda arbetsbladet** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Skydda några celler**

Det kan finnas vissa scenarier där du behöver låsa några celler endast i arbetsbladet. Om du vill låsa vissa specifika celler i arbetsbladet måste du låsa upp alla andra celler i arbetsbladet. Alla celler i ett arbetsblad är redan initialiserade för låsning, du kan kontrollera detta genom att öppna vilken Excel-fil som helst i MS Excel och klicka på **Format | Cells...** för att visa dialogrutan **Formatera celler** och sedan klicka på fliken Skydd och se en kryssruta med etiketten "Låst" är markerad som standard.

Följande är de två tillvägagångssätten för att genomföra uppgiften.

**Metod1:**

Följande punkter beskriver hur man låser några celler med hjälp av MS Excel. Denna metod gäller för Microsoft Office Excel 97, 2000, 2002, 2003 och senare versioner.

1. Markera hela arbetsbladet genom att klicka på Välj allt-knappen (den grå rektangeln direkt ovanför radnumret för rad 1 och till vänster om kolumnbrev A).
1. Klicka på Cellerna på menyn Format, klicka på fliken Skydd och avmarkera sedan rutan för Låst.

   Det låser upp alla cellerna på arbetsbladet

{{% alert color="primary" %}}

Om cellkommandot inte är tillgängligt, kan delar av arbetsbladet redan vara låsta. På menyn Verktyg, peka på Skydd och klicka sedan på Avskydda blad.

{{% /alert %}}

1. Markera bara de celler du vill låsa och upprepa steg 2, men välj den här gången rutan bredvid Låst.
1. På **Verktyg**-menyn väljer du **Skydd**, klickar på **Skydda blad** och klickar sedan på **OK**.

{{% alert color="primary" %}}

I dialogrutan Skydda blad har du möjlighet att ange ett lösenord och välja de element som du vill att användarna ska kunna ändra.

{{% /alert %}}

**Metod2:**

I denna metod använder vi endast Aspose.Cells API för att utföra uppgiften.

Följande exempel visar hur du låser några celler i arbetsbladet. Det låser upp alla celler i arbetsbladet först och sedan låser 3 celler (A1, B1, C1) i det. Till slut skyddas arbetsbladet. En rad/kolumn har en Style API som ytterligare innehåller en metod satt låst. Du kan använda den här metoden för att låsa upp eller låsa en rad/kolumn.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Skydda en rad i kalkylarket**

Aspose.Cells låter dig enkelt låsa vilken rad som helst i kalkylarket. Här kan vi använda metoden [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) av klassen [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) för att tillämpa stil på en särskild rad i kalkylarket. Denna metod tar två argument: ett [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objekt och [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur man skyddar en rad i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första raden i det. Slutligen skyddar det kalkylarket. En rad/kolumn har en Style API som ytterligare innehåller en setCellLocked-metod . Du kan låsa eller låsa upp rad/kolumn med hjälp av StyleFlag struct.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Skydda en kolumn i kalkylarket**

Aspose.Cells låter dig enkelt låsa vilken kolumn som helst i kalkylarket. Här kan vi använda metoden [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) av klassen [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) för att tillämpa stil på en särskild kolumn i kalkylarket. Denna metod tar två argument: ett [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objekt och [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur man skyddar en kolumn i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första kolumnen i det. Slutligen skyddar det kalkylarket. En rad/kolumn har en Style API som ytterligare innehåller en setLocked-metod . Du kan låsa eller låsa upp rad/kolumn med hjälp av StyleFlag struct.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Avskydda ett kalkylblad**

[Skydda arbetsblad](/cells/sv/java/protect-and-unprotect-worksheet/#protect-worksheets) och [Avancerade skyddsinställningar sedan Excel XP](/cells/sv/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) diskuterade olika metoder för att skydda arbetsblad. Vad händer om en utvecklare behöver ta bort skydd från ett skyddat arbetsblad under körning så att vissa ändringar kan göras i filen? Detta kan enkelt göras med Aspose.Cells.

### **Använda Microsoft Excel**

För att ta bort skydd från ett arbetsblad:

Från **Verktyg**-menyn väljer du **Skydd** följt av **Avskydda blad**.

**Välja Avskydda blad** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

Skyddet tas bort, om inte arbetsbladet är lösenordsskyddat. I så fall uppmanar en dialogruta efter lösenordet.

**Ange lösenord för att avskydda arbetsbladet** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Använda Aspose.Cells**

Ett arbetsblad kan avskyddas genom att anropa [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassens [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) metod. Metoden [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) kan användas på två sätt, beskrivna nedan.

### **Avskydda ett enkelt skyddat arbetsblad**

Ett enkelt skyddat arbetsblad är ett som inte är skyddat med ett lösenord. Sådana arbetsblad kan avskyddas genom att anropa avskydda metoden utan att skicka en parameter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Avskydda ett lösenordsskyddat arbetsblad**

Ett lösenordsskyddat arbetsblad är ett som är skyddat med ett lösenord. Sådana arbetsblad kan avskyddas genom att anropa en överbelastad version av avskydda metoden som tar lösenordet som en parameter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Avancerade skyddsinställningar sedan Excel XP**

[Skydda arbetsblad](/cells/sv/java/protect-and-unprotect-worksheet/#protect-worksheets) diskuterade skydd av ett arbetsblad i Microsoft Excel 97 och 2000. Men sedan lanseringen av Excel 2002 eller XP har Microsoft lagt till många avancerade skyddsinställningar. Dessa skyddsinställningar begränsar eller tillåter användare att:

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket annat.

Aspose.Cells stöder alla avancerade skyddsinställningar som erbjuds av Excel XP och senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

För att visa de tillgängliga skyddsinställningarna i Excel XP:

1. Från **Verktyg**-menyn väljer du **Skydd** följt av **Skydda blad**.
   En dialogruta visas.

   **Dialog för att visa skyddsalternativ i Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. Tillåt eller begränsa arbetsbladsfunktioner eller tillämpa ett lösenord.

### **Avancerade skyddsinställningar med hjälp av Aspose.Cells**

Aspose.Cells stödjer alla avancerade skyddsinställningar.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection-samling som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Worksheet-klassen tillhandahåller egenskapen Protection som används för att tillämpa dessa avancerade skyddsinställningar. Egenskapen Protection är faktiskt en instans av klassen [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) som kapslar in flera booleska egenskaper för att inaktivera eller aktivera restriktioner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Nedan finns en liten exempelapplikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Spara filen i formatet EXCEL97TO2003 eller XLSX eftersom dessa avancerade skyddsinställningar bara stöds av MS Excel XP och senare versioner.

{{% /alert %}}

### **Cellåsningsproblem**

Om du vill begränsa användare från att redigera celler måste cellerna låsas innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om arbetsbladet är skyddat. I Microsoft Excel XP kan celler låsas med följande dialog:

**Dialog för att låsa celler i Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Det är möjligt att låsa celler med hjälp av Aspose.Cells API också. Varje cell har en Style API som ytterligare innehåller en setLocked-metod. Använd den för att låsa eller låsa upp celler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
{{< app/cells/assistant language="java" >}}
