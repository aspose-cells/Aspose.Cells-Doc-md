---  
title: Visa och dölj rutnät samt rad och kolumnhuvuden med Node.js via C++  
linktitle: Visa och dölj rutnät och radkolumnhuvuden  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: Denna artikel ger ett kodexempel för att använda Node.js API via C++ för att programmässigt dölja eller visa rutnät, rad och kolumnhuvuden för ett Excel ark.  
---  

{{% alert color="primary" %}}  
Aspose.Cells stödjer döljning och visning av kalkylbladets rutnät som är synliga som standard. Den ger också kontroll över synligheten av radkolumnhuvuden på kalkylbladet.  
{{% /alert %}}  

## **Visa och dölj rutnät**  

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler så att det är lätt att ange data i specifika celler. Rutnät gör det möjligt för oss att se ett kalkylblad som en samling av celler, där varje cell är lätt identifierbar.  

### **Kontrollera synligheten av rutnäten**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att kontrollera synligheten för rutnät, använd egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) är en boolesk egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.  

#### **Gör rutnätslinjer synliga**  

Gör rutnät synliga genom att ställa in egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) till **true**.  

#### **Gömmer rutnätslinjer**  

Dölj rutnät genom att ställa in egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) till **false**.  

Ett komplett exempel visas nedan som demonstrerar användningen av egenskapen [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) genom att öppna en Excel-fil (book1.xls), dölja rutnäten på det första arbetsbladet och spara den modifierade filen som output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Visa och dölj radkolumnhuvuden**  

Alla kalkylblad i en Excel-fil består av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och individuella celler. Till exempel har rader nummer - 1, 2, 3, 4, osv.- och kolumner är ordnade alfabetiskt - A, B, C, D, osv. Rad- och kolumnvärdena visas i huvudena. Med Aspose.Cells kan utvecklare kontrollera synligheten av dessa rad- och kolumnhuvuden.  

### **Kontrollera synligheten av arbetsbladen**  

 Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att kontrollera synligheten av rad- och kolumnhuvuden, använd egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) är en boolesk egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.  

#### **Göra rad-/kolumnrubriker synliga**  

Gör rad- och kolumnhuvuden synliga genom att ställa in egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) till **true**.  

#### **Gömma rad-/kolumnrubriker**  

Dölj rad- och kolumnhuvuden genom att ställa in egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) till **false**.  

Ett komplett exempel visas nedan som visar hur man använder egenskapen [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) genom att öppna en Excel-fil (book1.xls), dölja rad- och kolumnhuvuden på det första arbetsbladet och spara den modifierade filen som output.xls.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Det är också möjligt att använda metoderna [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) och [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) av [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-klassen för att göra flera rader och kolumner synliga.  
{{% /alert %}}  

