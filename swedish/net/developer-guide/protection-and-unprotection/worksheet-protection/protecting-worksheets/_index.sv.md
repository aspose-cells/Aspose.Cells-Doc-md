---
title: Skydda kalkylbladen
type: docs
weight: 10
url: /sv/net/protecting-worksheets/
---

{{% alert color="primary" %}}

När en arbetsbok är skyddad, är användarens åtgärder begränsade. Till exempel kan de inte mata in data, infoga eller ta bort rader eller kolumner etc.

{{% /alert %}}

## **Skydda kalkylblad**

### **Introduktion**

De allmänna skyddsalternativen i Microsoft Excel är:

- Innehåll
- Objekt
- Scenarier

Skyddade arbetsblad döljer inte eller skyddar känsliga data, så det skiljer sig från filkryptering. I allmänhet passar arbetsbladsskydd för presentationsändamål. Det förhindrar slutanvändaren från att ändra data, innehåll och formatering i arbetsbladet.

### **Skydda ett arbetsblad**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som ger åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller metoden [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) som används för att tillämpa skydd på arbetsbladet. [**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1)-metoden accepterar följande parametrar:

- Skyddstyp, typen av skydd att tillämpa på arbetsbladet. Skyddstypen appliceras med hjälp av [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)-uppräkningen.
- Nya lösenordet, det nya lösenordet som används för att skydda kalkylbladet.
- Gammalt lösenord, det gamla lösenordet om arbetsbladet redan är lösenordsskyddat. Om arbetsbladet inte redan är skyddat, skicka bara null.

Uppräkningen [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) innehåller följande fördefinierade skydds typer:

|**Skydds typer**|**Beskrivning**|
| :- | :- |
|All|Användaren kan inte ändra något på detta arbetsblad|
|Contents|Användaren kan inte mata in data på detta arbetsblad|
|Objects|Användaren kan inte ändra ritobjekt|
|Scenarios|Användaren kan inte ändra sparade scenarier|
|Structure|Användaren kan inte ändra strukturen|
|Windows|Skyddet tillämpas på fönster|
|None|Inget skydd tillämpas|

Nedan följer ett exempel på hur man skyddar ett arbetsblad med lösenord.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Efter ovanstående kod används för att skydda arbetsbladet kan du kontrollera skyddet på arbetsbladet genom att öppna det. När du öppnar filen och försöker lägga till några data i arbetsbladet, kommer du att se följande dialogruta:

|**En dialogruta som varnar användaren om att den inte kan ändra arbetsbladet**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

För att arbeta med arbetsbladet, avse skyddet genom att välja **Skydd** och sedan **Avskydda ark** från menyalternativet **Verktyg**.

När du väljer menyalternativet Avskydda ark öppnas en dialogruta som uppmanar dig att ange lösenordet så att du kan arbeta med arbetsbladet som visas nedan:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Skydda ett fåtal celler i arbetsbladet med hjälp av Microsoft Excel**

Det kan finnas vissa scenarier där du behöver låsa endast några celler i arbetsbladet. Om du vill låsa några specifika celler i arbetsbladet måste du låsa upp alla andra celler i arbetsbladet. Alla celler i ett arbetsblad är redan initialiserade för låsning, du kan kontrollera detta genom att öppna vilken Excel-fil som helst i MS Excel och klicka på **Format | Celler…** för att visa dialogrutan **Formatera celler** och sedan klicka på fliken **Skydd** och se att kryssrutan märkt "Låst" är markerad som standard.

Följande punkter beskriver hur man låser några celler med hjälp av MS Excel. Denna metod gäller för Microsoft Office Excel 97, 2000, 2002, 2003 och senare versioner.

1. Markera hela arbetsbladet genom att klicka på knappen **Markera allt** (den grå rektangeln direkt ovanför radnumret för rad 1 och till vänster om kolumnbrevet A).
1. Klicka på **Celler** på **Format**-menyn, klicka på fliken **Skydd** och avmarkera sedan kryssrutan **Låst**.
   Det låser upp alla cellerna på arbetsbladet
   Om kommandot **Celler** inte är tillgängligt kan delar av arbetsbladet redan vara låst. På **Verktyg**-menyn, peka på **Skydd** och klicka sedan på **Avskydda ark**.
1. Välj bara de celler du vill låsa och upprepa steg 2, men den här gången markera kryssrutan **Låst**.
1. På **Verktyg**-menyn, peka på **Skydd**, klicka på **Skydda ark** och klicka sedan på **OK**.
1. I dialogrutan **Skydda ark** har du möjlighet att ange ett lösenord och välja de element som du vill att användarna ska kunna ändra.

### **Skydda en del celler i arbetsbladet med hjälp av Aspose Cells**

I denna metod använder vi endast Aspose.Cells API för att utföra uppgiften.

Exempel: Följande exempel visar hur man skyddar några celler i arbetsbladet. Det låser upp alla celler i arbetsbladet först och låser sedan 3 celler (A1, B1, C1) i den. Slutligen skyddar det arbetsbladet. Objektet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) innehåller en boolesk egenskap, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Du kan ange [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)-egenskapen till true eller false och tillämpa metoden *Column/Row.ApplyStyle()* för att låsa eller låsa upp rad/kolumn med dina önskade attribut.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Skydda en rad i kalkylarket**

Aspose.Cells gör det möjligt för dig att enkelt låsa någon rad i kalkylarket. Här kan vi använda [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metoden av [**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) på en specifik rad i kalkylarket. Denna metod tar två argument: en [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt och [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur du skyddar en rad i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första raden i det. Slutligen skyddar det kalkylarket. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektet innehåller en boolesk egenskap, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Du kan ställa in [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) egenskapen till true eller false för att låsa eller låsa upp rad/kolumn med hjälp av [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objektet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Skydda en kolumn i kalkylarket**

Aspose.Cells gör det möjligt för dig att enkelt låsa en kolumn i kalkylarket. Här kan vi använda [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) metoden av [**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) på en specifik kolumn i kalkylarket. Denna metod tar två argument: en [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt och [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur du skyddar en kolumn i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första kolumnen i det. Slutligen skyddar det kalkylarket. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektet innehåller en boolesk egenskap, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Du kan ställa in [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) egenskapen till true eller false för att låsa eller låsa upp rad/kolumn med hjälp av [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objektet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Tillåt användare att redigera områden**

Följande exempel visar hur du tillåter användare att redigera ett område i ett skyddat kalkylark.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
