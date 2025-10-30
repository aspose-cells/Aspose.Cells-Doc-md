---
title: Skydda arbetsblad med Node.js via C++
linktitle: Skydda kalkylbladen
type: docs
weight: 10
url: /sv/nodejs-cpp/protecting-worksheets/
description: Lär dig hur du skyddar arbetsblad i Excel med Aspose.Cells for Node.js via C++, inklusive att skydda rader, kolumner och specifika celler.
---


{{% alert color="primary" %}}

När ett arbetsblad är skyddat begränsas de åtgärder en användare kan utföra. Till exempel kan de inte mata in data, infoga eller ta bort rader eller kolumner osv.

{{% /alert %}}

## **Skydda kalkylblad**

### **Introduktion**

De allmänna skyddsalternativen i Microsoft Excel är:

- Innehåll
- Objekt
- Scenarier

Skyddade arbetsblad döljer inte eller skyddar känsliga data, så det skiljer sig från filkryptering. I allmänhet passar arbetsbladsskydd för presentationsändamål. Det förhindrar slutanvändaren från att ändra data, innehåll och formatering i arbetsbladet.

### **Skydda ett arbetsblad**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som ger åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) tillhandahåller metoden [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) som används för att tillämpa skydd på arbetsbladet. Metoden [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) accepterar följande parametrar:

- Skyddstyp, typen av skydd som ska tillämpas på kalkylbladet. Skyddstypen tillämpas med hjälp av [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype)-uppräkningen.
- Nya lösenordet, det nya lösenordet som används för att skydda kalkylbladet.
- Gammalt lösenord, det gamla lösenordet om arbetsbladet redan är lösenordsskyddat. Om arbetsbladet inte redan är skyddat, skicka bara null.

Enumeringen [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) innehåller följande fördefinierade skyddstyper:

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

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

Efter ovanstående kod används för att skydda arbetsbladet kan du kontrollera skyddet på arbetsbladet genom att öppna det. När du öppnar filen och försöker lägga till några data i arbetsbladet, kommer du att se följande dialogruta:

|**En dialogruta som varnar användaren om att den inte kan ändra arbetsbladet**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

För att arbeta med arbetsbladet, avse skyddet genom att välja **Skydd** och sedan **Avskydda ark** från menyalternativet **Verktyg**.

När du väljer menyalternativet Avskydda ark öppnas en dialogruta som uppmanar dig att ange lösenordet så att du kan arbeta med arbetsbladet som visas nedan:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Skydda ett fåtal celler i arbetsbladet med hjälp av Microsoft Excel**

Det kan finnas scenarier där du bara behöver låsa några celler i arbetsbladet. Om du vill låsa några specifika celler i arbetsbladet måste du låsa upp alla andra celler i arbetsbladet. Alla celler i ett arbetsblad är redan initialiserade för låsning; du kan kontrollera detta genom att öppna en valfri Excel-fil i MS Excel och klicka på **Format | Celler...** för att visa **Format Celler**-dialogrutan och sedan klicka på fliken **Skydd** och se att en kryssruta märkt "Låst" är i standardläge.

Följande punkter beskriver hur man låser några celler med MS Excel. Denna metod gäller för Microsoft Office Excel 97, 2000, 2002, 2003 och senare versioner.

1. Markera hela arbetsbladet genom att klicka på knappen **Markera allt** (den grå rektangeln direkt ovanför radnumret för rad 1 och till vänster om kolumnbrevet A).
2. Klicka på **Celler** i **Format**-menyn, klicka på fliken **Skydd** och avmarkera kryssrutan **Låst**.
   Detta låser upp alla celler på arbetsbladet.
   Om kommandot **Celler** inte är tillgängligt kan delar av arbetsbladet redan vara låst. På **Verktyg**-menyn, peka på **Skydd** och klicka sedan på **Avskydda ark**.
3. Välj bara de celler du vill låsa och upprepa steg 2, men den här gången markerar du kryssrutan **Låst**.
4. På **Verktyg**-menyn, rikta musen mot **Skydd**, klicka på **Skydda blad** och klicka sedan på **OK**.
5. I dialogrutan **Skydda blad**, har du möjlighet att ange ett lösenord och välja de element som du vill att användare ska kunna ändra.

### **Skydda några celler i kalkbladet med Aspose.Cells**

I denna metod använder vi bara Aspose.Cells API för att utföra uppgiften.

Exempel: Följande exempel visar hur man skyddar vissa celler i kalkbladet. Det låser först upp alla celler i kalkbladet och låser sedan 3 celler (A1, B1, C1). Slutligen skyddar det kalkbladet. Objektet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) innehåller en booleanegenskap, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Du kan ställa in [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) egenskapen till sann eller falsk och tillämpa *Column/Row.applyStyle()*-metoden för att låsa eller låsa upp raden/kolumnen med dina önskade attribut.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Skydda en rad i kalkylarket**

Aspose.Cells låter dig enkelt låsa vilken rad som helst i kalkbladet. Här kan vi använda [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)-metoden av [**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) på en specifik rad i kalkbladet. Denna metod tar två argument: ett [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objekt och ett [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur man skyddar en rad i kalkbladet. Det låser först upp alla celler i kalkbladet och låser sedan den första raden. Slutligen skyddar det kalkbladet. Objektet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) innehåller en booleanegenskap, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Du kan ställa in [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)-egenskapen till sann eller falsk för att låsa eller låsa upp raden/kolumnen med [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-objektet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Skydda en kolumn i kalkylarket**

Aspose.Cells låter dig enkelt låsa vilken kolumn som helst i kalkbladet. Här kan vi använda [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-)-metoden av [**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column)-klassen för att tillämpa [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) på en specifik kolumn i kalkbladet. Denna metod tar två argument: ett [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objekt och ett [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-objekt som har alla medlemmar relaterade till tillämpad formatering.

Följande exempel visar hur man skyddar en kolumn i kalkbladet. Det låser först upp alla celler i kalkbladet och låser sedan den första kolumnen. Slutligen skyddar det kalkbladet. Objektet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) innehåller en booleanegenskap, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Du kan ställa in [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)-egenskapen till sann eller falsk för att låsa eller låsa upp raden/kolumnen med [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-objektet.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Tillåt användare att redigera områden**

Följande exempel visar hur du tillåter användare att redigera ett område i ett skyddat kalkylark.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
