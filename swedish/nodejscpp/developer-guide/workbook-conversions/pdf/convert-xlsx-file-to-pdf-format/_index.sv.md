---
title: Konvertera XLSX fil till PDF format med Node.js via C++
linktitle: Konvertera XLSX fil till PDF format
type: docs
weight: 30
url: /sv/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: Denna guide förklarar hur man konverterar en Excel fil (XLSX) till PDF format med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) representerar dokument oberoende av den programvara, hårdvara och operativsystem som används för att skapa dessa dokument. En PDF-fil kan vara dokument med vilken kombination av text, grafik och bilder som helst på ett enhets- och upplösningsoberoende sätt. PDF-filer är ofta komprimerade, så de tar upp mindre utrymme än den ursprungliga filen.

Ibland behöver du konvertera en Microsoft Excel-fil till PDF. För detta krävs en snabb, säker, noggrann och pålitlig lösning som låter dig distribuera PDF-dokument världen runt. Det finns många konverteringsverktyg som kan utföra denna uppgift. Men du måste se till att layouten för den ursprungliga Excel-dokumentet behålls i den utgångna PDF-filen. Bilder, diagram, former, formatering, teckensnitt, attribut, färger, sidinställningar, textorientering, marginaler, diagram etc. ska renderas exakt och precist. [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/) säkerställer hög fidelity-konvertering.

Detta dokument är utformat för att ge en omfattande förståelse för hur ett Microsoft Excel-dokument (inklusive bilder, diagram, formatering etc.) kan konverteras till PDF. I syfte att visa detta, demonstrerar det hur man skapar en enkel konsolapplikation i Node.js som konverterar en Excel-fil till PDF med Aspose.Cells API. Konverteringen utförs med hög precision och noggrannhet.

{{% /alert %}}

## **Konvertera Excel till PDF**

Detta exempel använder en Excel-fil (SampleInput.xlsx) som mall. Arbetsboken innehåller arbetsblad med diagram och bilder. Varje arbetsblad innehåller olika typer av format med typsnitt, attribut, färger, skuggningseffekter och kantlinjer. Det finns ett kolumndiagram på det första arbetsbladet och en bild på det sista.

### **Den förkonfigurerade Excelfilen**

Mallen har tre blad, inklusive diagram och bilder som media. Det första bladet har diagram och det sista bladet har en bild som visas nedan i skärmbilderna.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|

### **Konverteringsprocess**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

Om kalkylbladet innehåller formel är det bäst att anropa [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) precis innan kalkylbladet renderas till PDF. Detta säkerställer att formelberoende värden omräknas och att rätt värden visas i PDF:en.

{{% /alert %}}

### **Resultat**

När ovanstående kod har körts skapas en PDF-fil i mappen Files i din programkatalog.
Följande skärmbilder visar PDF-sidorna. Observera att sidhuvuden och sidfötter också behålls i den utmatade PDF-filen.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|
{{< app/cells/assistant language="nodejs-cpp" >}}
