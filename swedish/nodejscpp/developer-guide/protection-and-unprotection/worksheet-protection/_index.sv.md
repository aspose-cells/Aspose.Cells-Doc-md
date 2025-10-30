---  
title: Skydda och avsäkra kalkylbladet med Node.js via C++  
linktitle: Skydda och avskydda kalkylblad  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/protect-and-unprotect-worksheets/  
description: Skydda och avsäkra kalkylbladet i Excel filer med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
För att förhindra att andra användare avsiktligt eller oavsiktligt ändrar, flyttar eller tar bort data i ett kalkylblad kan du låsa cellerna i ditt Excel-kalkylblad och sedan skydda kalkylbladet med ett lösenord.  
{{% /alert %}}  

## **Skydda och avskydda arbetsblad i MS Excel**  

**![skydda och avskydda Arbetsblad](skydda-och-avskydda-arbetsblad.png)**  

1. Klicka på **Översikt > Skydda arbetsblad**.  
1. Ange ett lösenord i **Lösenordsrutan**.  
1. Välj **tillåt** alternativ.  
1. Välj **OK**, ange lösenordet igen för att bekräfta det, och välj sedan **OK** igen.  

## **Skydda kalkylbladet med Aspose.Cells for Node.js via C++**  
Bara behöver följande enkla koder för att implementera skydd av arbetsbokens struktur för Excel-filer.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Avsäkra kalkylbladet med Aspose.Cells for Node.js via C++**  
Att avsäkra kalkylbladet är enkelt med Aspose.Cells API. Om kalkylbladet är lösenordsskyddat krävs ett korrekt lösenord.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Fortsatta ämnen**  
- [Avancerade skyddsinställningar sedan Excel XP](/cells/sv/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Upptäck om arbetsbladet är lösenordsskyddat](/cells/sv/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Skydda kalkylblad](/cells/sv/nodejs-cpp/protecting-worksheets/)  
- [Avskydda ett kalkylblad](/cells/sv/nodejs-cpp/unprotect-a-worksheet/)  
- [Verifiera lösenord som används för att skydda arbetsbladet](/cells/sv/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
