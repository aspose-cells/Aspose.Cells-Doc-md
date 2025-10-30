---  
title: Ställ in standardfont när du renderar kalkylblad till HTML med Node.js via C++  
linktitle: Ange standardfonten vid rendering av kalkylblad till HTML  
type: docs  
weight: 370  
url: /sv/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cells tillåter dig att ställa in standardtypsnittet vid rendering av kalkylblad till HTML. Använd [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) för detta ändamål. Denna egenskap är användbar när det finns några celler i ett kalkylblad som har ogiltiga eller icke-existerande typsnitt. Då kommer dessa celler att renderas i ett typsnitt som anges med egenskapen [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  
{{% /alert %}}  

## Ställ in standardtypsnittet vid rendering av kalkylblad till HTML  

Den följande exempelkoden skapar en arbetsbok och lägger till lite text i cellen B4 på den första arbetsbladet och anger dess font till någon okänd/icke-existerande font. Sedan sparar den arbetsboken i HTML genom att ange olika standardfontnamn som Courier New, Arial, Times New Roman, osv.  

Skärmbilden visar effekten av att ställa in olika standardteckensnittsnamn via [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) egenskap.  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

Koden genererar [utmatnings-HTML-fil med Courier New](5115516), [utmatnings-HTML med Arial](5115518) och [utmatnings-HTML-fil med Times New Roman](5115517).  

## Exempelkod  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
