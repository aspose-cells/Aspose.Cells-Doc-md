---
title: Pdf med Node.js via C++
linktitle: Pdf
type: docs
weight: 220
url: /sv/nodejs-cpp/convert-excel-to-pdf/
description: Lär dig konvertera Excel arbetsbok till PDF med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells stöder konvertering av Excel-arbetsbok till PDF. I det här exemplet kommer vi att se komplett konvertering av en Excel-arbetsbok till PDF.
{{% /alert %}}

## **Konvertering av Excelarbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ skriver direkt information om API och versionsnummer i utdata dokument. Till exempel, vid rendering av dokument till PDF, fyller Aspose.Cells for Node.js via C++ i **PDF Producer**-fältet värdet, t.ex. 'Aspose.Cells v23.2'.

Observera att du kan ändra denna information i utdata-dokument genom [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--) -egenskapen.
{{% /alert %}}

### **Direkt konvertering**

Aspose.Cells for Node.js via C++ stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil till PDF med hjälp av [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassens [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) metod. [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-metoden ger medlemmarna [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) i enumeration som konverterar de inbyggda Excel-filerna till PDF-format.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) -klassen genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
1. Gör något arbete (infodata, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, etc.) på kalkylbladet med hjälp av Aspose.Cells APIs.
1. När kalkylbladskoden är klar, anropa [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassens [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) metod för att spara kalkylbladet.

Filtypen ska vara PDF, så välj *Pdf* (ett fördefinierat värde) från [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) -uppräkningen för att generera det slutliga PDF-dokumentet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **Avancerad konvertering**

Du kan också välja att använda [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)-klassen för att ange olika egenskaper för konverteringen. Genom att ange olika egenskaper för [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)-klassen får du kontroll över utskrifts-, font-, säkerhets- och komprimeringsinställningar för utdata-PDF:en. 

Den viktigaste egenskapen är [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) som möjliggör att du ställer in efterlevnadsnivån för PDF-standarden. För närvarande kan du spara i PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u-format. Observera att med PDF/A-formatet är filstorleken större än en vanlig PDF-filstorlek.

#### **Spara arbetsboken som PDF/A-kompatibla filer**

Den nedanstående kodsnutten visar hur man använder [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) -klassen för att spara Excel-filer i PDF/A-kompatibilt PDF-format.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
Observera att egenskapen [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) lades till med släppet av Aspose.Cells for Node.js via C++ 5.3.0.
{{% /alert %}}

#### **Ange PDF-skapandetid**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) -klassen kan du få eller ställa in PDF-skapandetid. Följande kod visar användningen av [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) -egenskapen för att ange skapandetiden för PDF-filen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **Ange alternativet för att kopiera innehållet för tillgänglighet**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) -klassen kan du få eller ställa in PDF [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) -alternativet för att kontrollera tillgången till innehållet i den konverterade PDF:en.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **Exportera anpassade egenskaper till PDF**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)-klassen kan du exportera de anpassade egenskaperna i källarbetsboken till PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/)-enumeratorn används för att ange sättet som egenskaper exporteras på. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Fil och sedan alternativet Egenskaper enligt följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ned [här](sourceWithCustProps.xlsx) för testning och utdatapdf-filen "outSourceWithCustProps" är tillgänglig [här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **Konverteringsattribut**

Vi arbetar med att förbättra konverteringsfunktionerna med varje ny version. Aspose.Cells Excel till PDF-konvertering har fortfarande ett par begränsningar. MapChart stöds inte vid konvertering till PDF-format. Även vissa ritningsobjekt stöds inte väl.

Tabellen nedan listar alla funktioner som är fullt eller delvis stödda vid export till PDF med Aspose.Cells. Denna tabell är inte slutgiltig och täcker inte alla kalkylbladsattribut, men den identifierar de funktioner som inte stöds eller endast delvis stöds för konvertering till PDF.

|**Dokumentelement**|**Attribut**|**Stöds**|**Noter**|
| :- | :- | :- | :- |
|Justering| |Ja| |
|Bakgrundsin...  |Ja| 
|Gräns|Färg|Ja| 
|Gräns|Linjestil|Ja| 
|Gräns|Linjebredd|Ja| 
|Cell Data| |Ja| 
|Kommentarer| |Ja| 
|Villkorlig formatering| |Ja| 
|Dokumentegenskaper| |Ja| 
|Ritobjekt| |Delvis|Skuggor och 3D-effekter för ritobjekt stöds inte bra; WordArt och SmartArt stöds delvis.
|Teckensnitt|Storlek|Ja| 
|Teckensnitt|Färg|Ja| 
|Teckensnitt|Stil|Ja| 
|Teckensnitt|Understrykning|Ja| 
|Teckensnitt|Effekter|Ja| 
|Bilder| |Ja| 
|Hypertextlänk| |Ja| 
|Diagram| |Delvis|Kartdiagram stöds inte.|
|Sammanfogade celler| |Ja| |
|Sidbrytning| |Ja| |
|Sidoppsett|Sidhuvud/-fot|Ja| |
|Sidoppsett|Marginaler|Ja| |
|Sidoppsett|Sidorientering|Ja| |
|Sidoppsett|Sidstorlek|Ja| |
|Sidoppsett|Utskriftsområde|Ja| |
|Sidoppsett|Utskriftsrubriker|Ja| |
|Sidoppsett|Skalning|Ja| |
|Radhöjd/Kolumnbredd| |Ja| |
|RTL (Höger-till-vänster) språk| |Ja| |

{{% alert color="primary" %}}
Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.
{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till bokmärken i PDF med namngivna destinationer](/cells/sv/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut](/cells/sv/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändra typsnitt på bara specifika Unicode-tecken vid sparande till PDF](/cells/sv/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Konvertera XLSX-fil till PDF-format](/cells/sv/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [Konvertera Excel-fil till PDF-format kompatibelt med PDFA-1a](/cells/sv/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertera XLS-fil med bilder eller diagram till PDF](/cells/sv/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Skapa PdfBookmarkEntry för diagramblad](/cells/sv/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Anpassa alla arbetsbokskolumner på en enda PDF-sida](/cells/sv/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Hämta DrawObject och gräns vid rendering till PDF med hjälp av DrawObjectEventHandler-klassen](/cells/sv/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Hämta varningar för teckensnittsbyte vid konvertering av Excel-fil](/cells/sv/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorera fel vid rendering av Excel till PDF](/cells/sv/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Begränsa antalet genererade sidor - Excel till PDF-konvertering](/cells/sv/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Skriv ut kommentarer vid sparande till PDF](/cells/sv/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [Rendera Office-tillägg vid konvertering av Excel till PDF](/cells/sv/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendera en PDF-sida per Excel-ark - Konvertering från Excel till PDF](/cells/sv/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendera Unicode-supplementära tecken i utgående PDF med Aspose.Cells](/cells/sv/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resamplings tillagda bilder - Konvertering från Excel till PDF](/cells/sv/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Spara varje arbetsblad i en separat PDF-fil](/cells/sv/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Spara Excel som PDF med standard- eller minsta storlek](/cells/sv/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Spara angivna arbetsblad som PDF](/cells/sv/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [Säkra PDF-dokument](/cells/sv/nodejs-cpp/secure-pdf-documents/)
- [Ange hur textsträngar ska korsas i utgående PDF och bild](/cells/sv/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
