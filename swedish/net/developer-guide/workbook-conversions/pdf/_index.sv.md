---
title: Pdf
type: docs
weight: 220
url: /sv/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Excel-arbetsbok till PDF. I det här exemplet kommer vi att se komplett konvertering av en Excel-arbetsbok till PDF.

{{% /alert %}}

## **Konvertering av Excelarbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{% alert color="primary" %}}

Aspose.Cells for .NET skriver direkt in information om API och versionsnummer i utdata-dokument. Till exempel, vid rendering av dokument till PDF, fyller Aspose.Cells for .NET **PDF Producent**-fältet med värdet, t.ex. 'Aspose.Cells v23.2'.

Observera att du kan ändra denna information i utdata-dokument genom [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/) -egenskapen.

{{% /alert %}}

### **Direkt konvertering**

Aspose.Cells for .NET stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil till PDF med hjälp av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) -klassens [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) -metod. [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) -metoden tillhandahåller [**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) -uppräkningsmedlemmen som konverterar de nativa Excel-filerna till PDF-format.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) -klassen genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
1. Gör något arbete (infodata, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, etc.) på kalkylbladet med hjälp av Aspose.Cells APIs.
1. När kalkylbladskoden är komplett, anropa [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) -klassens [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) -metod för att spara kalkylbladet.

Filtypen ska vara PDF, så välj *Pdf* (ett fördefinierat värde) från [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) -uppräkningen för att generera det slutliga PDF-dokumentet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Avancerad konvertering**

Du kan också välja att använda [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)-klassen för att ange olika egenskaper för konverteringen. Genom att ange olika egenskaper för [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)-klassen får du kontroll över utskrifts-, font-, säkerhets- och komprimeringsinställningar för utdata-PDF:en. 

Den viktigaste egenskapen är [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) som möjliggör att du ställer in efterlevnadsnivån för PDF-standarden. För närvarande kan du spara i PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u-format. Observera att med PDF/A-formatet är filstorleken större än en vanlig PDF-filstorlek.

#### **Spara arbetsboken som PDF/A-kompatibla filer**

Den nedanstående kodsnutten visar hur man använder [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) -klassen för att spara Excel-filer i PDF/A-kompatibilt PDF-format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Observera att [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) -egenskapen lades till med version Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Ange PDF-skapandetid**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) -klassen kan du få eller ställa in PDF-skapandetid. Följande kod visar användningen av [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) -egenskapen för att ange skapandetiden för PDF-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Ange alternativet för att kopiera innehållet för tillgänglighet**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) -klassen kan du få eller ställa in PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) -alternativet för att kontrollera tillgången till innehållet i den konverterade PDF:en.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Exportera anpassade egenskaper till PDF**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)-klassen kan du exportera de anpassade egenskaperna i källarbetsboken till PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)-enumeratorn används för att ange sättet som egenskaper exporteras på. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Fil och sedan alternativet Egenskaper enligt följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ned [här](sourceWithCustProps.xlsx) för testning och utdatapdf-filen "outSourceWithCustProps" är tillgänglig [här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

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

Om din kalkylblad innehåller formler är det bäst att använda [**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) strax innan kalkylbladet renderas till PDF-format. På så sätt kommer de formelberoende värdena att omberäknas och de korrekta värdena renderas i PDF.

{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till bokmärken i PDF](/cells/sv/net/add-pdf-bookmarks/)
- [Lägg till bokmärken i PDF med namngivna destinationer](/cells/sv/net/add-pdf-bookmarks-with-named-destinations/)
- [Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut](/cells/sv/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändra typsnitt på bara specifika Unicode-tecken vid sparande till PDF](/cells/sv/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Kontrollera inläsning av externa resurser i MS Excel Arbetsbok vid rendering till PDF](/cells/sv/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Konvertera XLSX-fil till PDF-format](/cells/sv/net/convert-xlsx-file-to-pdf-format/)
- [Konvertera Excel-fil till PDF-format kompatibelt med PDFA-1a](/cells/sv/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertera XLS-fil med bilder eller diagram till PDF](/cells/sv/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Skapa PdfBookmarkEntry för diagramblad](/cells/sv/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Anpassa alla arbetsbokskolumner på en enda PDF-sida](/cells/sv/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Hämta DrawObject och gräns vid rendering till PDF med hjälp av DrawObjectEventHandler-klassen](/cells/sv/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Hämta varningar för teckensnittsbyte vid konvertering av Excel-fil](/cells/sv/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorera fel vid rendering av Excel till PDF](/cells/sv/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begränsa antalet genererade sidor - Excel till PDF-konvertering](/cells/sv/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Skriv ut kommentarer vid sparande till PDF](/cells/sv/net/print-comments-while-saving-to-pdf/)
- [Rendera Office-tillägg vid konvertering av Excel till PDF](/cells/sv/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendera en PDF-sida per Excel-ark - Konvertering från Excel till PDF](/cells/sv/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendera Unicode-supplementära tecken i utgående PDF med Aspose.Cells](/cells/sv/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resamplings tillagda bilder - Konvertering från Excel till PDF](/cells/sv/net/resampling-added-images-excel-to-pdf-conversion/)
- [Spara varje arbetsblad i en separat PDF-fil](/cells/sv/net/save-each-worksheet-to-a-different-pdf-file/)
- [Spara Excel som PDF med standard- eller minsta storlek](/cells/sv/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Spara angivna arbetsblad som PDF](/cells/sv/net/save-specified-worksheets-to-pdf/)
- [Säkra PDF-dokument](/cells/sv/net/secure-pdf-documents/)
- [Ange hur textsträngar ska korsas i utgående PDF och bild](/cells/sv/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}
