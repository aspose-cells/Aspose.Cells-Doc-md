---
title: Skydda arbetsblad
type: docs
weight: 10
url: /sv/net/protecting-worksheets/
---
{{% alert color="primary" %}}

När ett kalkylblad är skyddat är de åtgärder en användare kan vidta begränsade. Till exempel kan de inte mata in data, infoga eller ta bort rader eller kolumner etc.

{{% /alert %}}

## **Skydda arbetsblad**

### **Introduktion**

De allmänna skyddsalternativen i Microsoft Excel är:

- Innehåll
- Objekt
- Scenarier

Skyddade kalkylblad döljer eller skyddar inte känslig data, så det skiljer sig från filkryptering. I allmänhet är kalkylbladsskydd lämpligt för presentationsändamål. Det hindrar slutanvändaren från att ändra data, innehåll och formatering i kalkylbladet.

### **Skydda ett arbetsblad**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass.

 De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass ger[**Skydda**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) metod som används för att tillämpa skydd på kalkylbladet.[**Skydda**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) metoden accepterar följande parametrar:

-  Skyddstyp, den typ av skydd som ska tillämpas på kalkylbladet. Skyddstyp appliceras med hjälp av[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)uppräkning.
- Nytt lösenord, det nya lösenordet som används för att skydda kalkylbladet.
- Old Password, det gamla lösenordet, om kalkylbladet redan är lösenordsskyddat. Om kalkylbladet inte redan är skyddat, skicka bara null.

 De[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)uppräkningen innehåller följande fördefinierade skyddstyper:

|**Skyddstyper**|**Beskrivning**|
|:- |:- |
|Allt|Användaren kan inte ändra något i detta kalkylblad|
|Innehåll|Användaren kan inte ange data i detta kalkylblad|
|Objekt|Användaren kan inte ändra ritobjekt|
|Scenarier|Användaren kan inte ändra sparade scenarier|
|Strukturera|Användaren kan inte ändra strukturen|
|Windows|Skydd tillämpas på fönster|
|Ingen|Inget skydd tillämpas|

Exemplet nedan visar hur man skyddar ett kalkylblad med ett lösenord.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Efter att ovanstående kod har använts för att skydda kalkylbladet kan du kontrollera skyddet på kalkylbladet genom att öppna det. När du öppnar filen och försöker lägga till några data till kalkylbladet kommer du att se följande dialogruta:

|**En dialogruta som varnar om att en användare inte kan ändra kalkylbladet**|
|:- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

 För att arbeta med kalkylbladet, avskydda kalkylbladet genom att välja**Skydd** , då**Avskydda arket** från**Verktyg** menyalternativ.

När du har valt menyalternativet Unprotect Sheet öppnas en dialogruta som uppmanar dig att ange lösenordet så att du kan arbeta med kalkylbladet enligt nedan:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Skydda några Cells i kalkylbladet med hjälp av Microsoft Excel**

Det kan finnas vissa scenarier där du bara behöver låsa några få celler i kalkylbladet. Om du vill låsa vissa specifika celler i kalkylbladet måste du låsa upp alla andra celler i kalkylbladet. Alla celler i ett kalkylblad är redan initierade för låsning, du kan kontrollera detta genom att öppna valfri Excel-fil i MS Excel och klicka på**Format | Cells...** att visa**Format Cells** dialogrutan och klicka sedan på**Skydd** fliken och se en kryssruta märkt "Låst" är markerad som standard.

Följande punkter beskriver hur du låser några celler med MS Excel. Denna metod gäller för Microsoft Office Excel 97, 2000, 2002, 2003 och senare versioner.

1.  Välj hela kalkylbladet genom att klicka på**Välj alla** knappen (den grå rektangeln direkt ovanför radnumret för rad 1 och till vänster om kolumn bokstaven A).
1.  Klick**Cells** på**Formatera** menyn, klicka på**Skydd** fliken och rensa sedan**Låst** kryssruta.
Detta låser upp alla celler i kalkylbladet
 Om**Cells** kommandot är inte tillgängligt, delar av kalkylbladet kan redan vara låst. På**Verktyg** meny, peka på**Skydd** , och klicka sedan**Avskydda arket**.
1. Välj bara de celler du vill låsa och upprepa steg 2, men den här gången väljer du**Låst** kryssruta.
1.  På**Verktyg** meny, peka på**Skydd** , klick**Skydda ark** och klicka sedan**OK**.
1.  I den**Skydda ark** dialogrutan har du möjlighet att ange ett lösenord och välja de element som du vill att användarna ska kunna ändra.

### **Skydda några Cells i arbetsbladet med Aspose Cells**

I den här metoden använder vi bara Aspose.Cells API för att utföra uppgiften.

 Exempel: Följande exempel visar hur man skyddar några få celler i kalkylbladet. Den låser upp alla celler i kalkylbladet först och låser sedan 3 celler (A1, B1, C1) i det. Slutligen skyddar det kalkylbladet. De[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objektet innehåller en boolesk egenskap,[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Du kan ställa in[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) egenskapen till sant eller falskt och tillämpas*Column/Row.ApplyStyle()* metod för att låsa eller låsa upp raden/kolumnen med dina önskade attribut.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Skydda en rad i arbetsbladet**

Aspose.Cells låter dig enkelt låsa valfri rad i kalkylbladet. Här kan vi använda oss av[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metod av[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) klass att ansöka[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) till en viss rad i kalkylbladet. Denna metod tar två argument: a[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt och[**StilFlagga**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur man skyddar en rad i kalkylbladet. Den låser upp alla celler i kalkylbladet först och låser sedan den första raden i det. Slutligen skyddar det kalkylbladet. De[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objektet innehåller en boolesk egenskap,[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Du kan ställa in[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) egenskapen till true eller false för att låsa eller låsa upp raden/kolumnen med hjälp av[**StilFlagga**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objekt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Skydda en kolumn i arbetsbladet**

 Aspose.Cells låter dig enkelt låsa valfri kolumn i kalkylbladet. Här kan vi använda oss av[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) metod av[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) klass att ansöka[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) till en viss kolumn i kalkylbladet. Denna metod tar två argument: a[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt och[**StilFlagga**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objekt som har alla medlemmar relaterade till tillämpad formatering.

 Följande exempel visar hur man skyddar en kolumn i kalkylbladet. Det låser upp alla celler i kalkylbladet först och låser sedan den första kolumnen i det. Slutligen skyddar det kalkylbladet. De[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objektet innehåller en boolesk egenskap,[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Du kan ställa in[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) egenskapen till true eller false för att låsa eller låsa upp raden/kolumnen med hjälp av[**StilFlagga**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objekt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Tillåt användare att redigera intervall**

Följande exempel visar hur man tillåter användare att redigera ett intervall i ett skyddat kalkylblad.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
