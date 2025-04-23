---
title: Skydda kalkylbladen
type: docs
weight: 10
url: /sv/python-net/protecting-worksheets/
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

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger tillgång till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller metoden [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) som används för att tillämpa skydd på arbetsbladet. [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType-str-str)-metoden accepterar följande parametrar:

- Skyddstyp, typen av skydd att tillämpa på arbetsbladet. Skyddstypen appliceras med hjälp av [**ProtectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/protectiontype)-uppräkningen.
- Nya lösenordet, det nya lösenordet som används för att skydda kalkylbladet.
- Gammalt lösenord, det gamla lösenordet om arbetsbladet redan är lösenordsskyddat. Om arbetsbladet inte redan är skyddat, skicka bara null.

Uppräkningen [**ProtectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/protectiontype) innehåller följande fördefinierade skydds typer:

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectingWorksheet-1.py" >}}

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

I denna metod använder vi Aspose.Cells för Python via .NET API endast för att utföra uppgiften.

Exempel: Följande exempel visar hur man skyddar några celler i arbetsbladet. Det låser upp alla celler i arbetsbladet först och låser sedan 3 celler (A1, B1, C1) i den. Slutligen skyddar det arbetsbladet. Objektet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) innehåller en boolesk egenskap, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Du kan ange [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked)-egenskapen till true eller false och tillämpa metoden *Column/Row.ApplyStyle()* för att låsa eller låsa upp rad/kolumn med dina önskade attribut.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectingSpecificCellsinaWorksheet-1.py" >}}

### **Skydda en rad i kalkylarket**

Aspose.Cells för Python via .NET tillåter dig att enkelt låsa vilken rad du vill i arbetsbladet. Här kan vi använda [**apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style)-metoden i [**Aspose.Cells.Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) på en specifik rad i arbetsbladet. Denna metod tar två argument: ett [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt och ett [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)-objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur du skyddar en rad i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första raden i det. Slutligen skyddar det kalkylarket. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektet innehåller en boolesk egenskap, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Du kan ställa in [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) egenskapen till true eller false för att låsa eller låsa upp rad/kolumn med hjälp av [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) objektet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectingSpecificRowInWorksheet-1.py" >}}

### **Skydda en kolumn i kalkylarket**

Aspose.Cells för Python via .NET tillåter dig att enkelt låsa vilken kolumn du vill i arbetsbladet. Här kan vi använda [**apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/column/apply_style)-metoden i [**Aspose.Cells.Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)-klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) på en specifik kolumn i arbetsbladet. Denna metod tar två argument: ett [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt och ett [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)-objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur du skyddar en kolumn i kalkylarket. Det låser upp alla celler i kalkylarket först och låser sedan den första kolumnen i det. Slutligen skyddar det kalkylarket. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektet innehåller en boolesk egenskap, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Du kan ställa in [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) egenskapen till true eller false för att låsa eller låsa upp rad/kolumn med hjälp av [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) objektet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectColumnWorksheet-1.py" >}}

### **Tillåt användare att redigera områden**

Följande exempel visar hur du tillåter användare att redigera ett område i ett skyddat kalkylark.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EditRangesWorksheet-1.py" >}}

