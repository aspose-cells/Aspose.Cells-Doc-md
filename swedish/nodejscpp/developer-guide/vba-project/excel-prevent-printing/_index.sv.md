---  
title: Hur man förhindrar användare från att skriva ut Excel fil med Node.js via C++  
linktitle: Hur man förhindrar användare från att skriva ut Excel fil  
type: docs  
weight: 600  
url: /sv/nodejs-cpp/how-to-prevent-printing-excel/  
description: Lär dig hur du förhindrar användare från att skriva ut Excel filer med Aspose.Cells for Node.js via C++.  
keywords: excel utskrift, förhindra utskrift av Excel, hur man förhindrar användare från att skriva ut Excel, Excel förhindra utskrift, förhindra utskrift av arbetsbok, Förhindra användare från att skriva ut hela arbetsboken med VBA.  
---  

## **Möjliga användningsscenario**  
I vårt dagliga arbete kan det finnas viktig information i Excel-filen; för att skydda den interna datan från att spridas tillåter inte företaget oss att skriva ut den. Det här dokumentet visar hur du förhindrar andra från att skriva ut Excel-filer.  

## **Hur man förhindrar användare från att skriva ut fil i MS-Excel**  
Du kan tillämpa följande VBA-kod för att skydda din specifika fil från att skrivas ut.  
1. Öppna arbetsboken som du inte tillåter andra att skriva ut.  
1. Välj fliken "Utvecklare" i Excel-menyn och klicka på knappen "Visa kod" i avsnittet "Kontroller". Alternativt kan du hålla ned tangenterna ALT + F11 för att öppna Microsoft Visual Basic för applikationer-fönstret.  
<br>  
<img src="1.png" width=70% />  
1. Dubbelklicka på ThisWorkbook i vänstra Projektutforskaren för att öppna modulen och lägg till några VBA-koder.  
<br>  
<img src="2.png" width=70% />  
1. Spara och stäng detta kodfönster, gå tillbaka till arbetsboken, och nu när du skriver ut exempelfilen tillåts det inte att skrivas ut, och du får följande varningsruta:  
<br>  
<img src="3.png" width=70% />  

## **Hur man förhindrar användare från att skriva ut Excel-fil med Aspose.Cells for Node.js via C++**  

Följande exempel visar hur man förhindrar användare från att skriva ut en Excel-fil:  

1. Ladda in [provfilen](sample.xlsx).  
1. Hämta VbaModuleCollection-objektet från VbaProject-egenskapen för Workbook.  
1. Hämta VbaModule-objektet via namnet "ThisWorkbook".  
1. Ange egenskapen codes på VbaModule.  
1. Spara provfilen till [xlsm-format](out.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

wb.save("out.xlsm");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
