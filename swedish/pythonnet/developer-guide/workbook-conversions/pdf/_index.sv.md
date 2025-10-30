---
title: Pdf
type: docs
weight: 220
url: /sv/python-net/convert-excel-to-pdf/
description: Lär dig hur man konverterar Excel till PDF med Aspose.Cells for Python via .NET API.
keywords: Python konvertera Excel till PDF, Konvertera Excel till PDF med Python, Spara Excel till PDF i Python, Excel till PDF i Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET stödjer konvertering av Excel arbetsbok till PDF. I det här exemplet kommer vi att se den kompletta konverteringen av en Excel-arbetsbok till PDF.

{{% /alert %}}

## **Konvertering av Excelarbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells for Python via .NET stödjer konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET skriver direkt information om API och versionsnummer i utdata-dokument. Till exempel, vid rendering av dokument till PDF, populerar Aspose.Cells for Python via .NET **PDF Producer**-fältet med värdet, t.ex 'Aspose.Cells for Python via .NET v23.2'.

Observera att du kan ändra denna information i utdata-dokument genom [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/) -egenskapen.

{{% /alert %}}

### **Direkt konvertering**

Aspose.Cells for Python via .NET stödjer konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excelfil till PDF med hjälp av [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassens [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) metod. [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) metoden tillhandahåller [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) uppräkningsmedlem som konverterar de nativa Excelfilerna till PDF-format.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) -klassen genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
1. Gör något arbete (ange data, tillämpa formatering, ställ in formler, sätt in bilder eller andra ritobjekt osv.) på kalkylbladet med hjälp av Aspose.Cells for Python via .NET' API:er.
1. När kalkylbladskoden är komplett, anropa [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) -klassens [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) -metod för att spara kalkylbladet.

Filformatet ska vara PDF så välj *PDF* (ett fördefinierat värde) från [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) uppräkningen för att generera det slutgiltiga PDF-dokumentet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Avancerad konvertering**

Du kan också använda [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) -klassen för att ange olika attribut för konverteringen. Att ställa in olika egenskaper för [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) -klassen ger dig kontroll över utskrift, typsnitt, säkerhets- och komprimeringsinställningar för utdata-PDF. Den viktigaste egenskapen är [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) som möjliggör att spara Excel-filerna som PDF/A-kompatibla PDF-filer.

#### **Spara arbetsboken som PDF/A-kompatibla filer**

Den nedanstående kodsnutten visar hur man använder [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) -klassen för att spara Excel-filer i PDF/A-kompatibilt PDF-format.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Observera att [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) egenskapen lades till med släppet av Aspose.Cells for Python via .NET för .NET 5.3.0.

{{% /alert %}}

#### **Ange PDF-skapandetid**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) -klassen kan du få eller ställa in PDF-skapandetid. Följande kod visar användningen av [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) -egenskapen för att ange skapandetiden för PDF-filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **Ange alternativet för att kopiera innehållet för tillgänglighet**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) -klassen kan du få eller ställa in PDF [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) -alternativet för att kontrollera tillgången till innehållet i den konverterade PDF:en.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Exportera anpassade egenskaper till PDF**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)-klassen kan du exportera de anpassade egenskaperna i källarbetsboken till PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)-enumeratorn används för att ange sättet som egenskaper exporteras på. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Fil och sedan alternativet Egenskaper enligt följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ned [här](sourceWithCustProps.xlsx) för testning och utdatapdf-filen "outSourceWithCustProps" är tillgänglig [här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Konverteringsattribut**

Vi arbetar med att förbättra konverteringsfunktionerna med varje ny version. Aspose.Cells Excel till PDF-konvertering har fortfarande ett par begränsningar. MapChart stöds inte vid konvertering till PDF-format. Även vissa ritningsobjekt stöds inte väl.

Tabellen nedan listar alla funktioner som är helt eller delvis stödda vid exportering till PDF med Aspose.Cells for Python via .NET. Denna tabell är inte definitiv och täcker inte alla kalkylbladsegenskaper men den identifierar de funktioner som inte stöds eller delvis stöds för konvertering till PDF.

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

Om din kalkylblad innehåller formler är det bäst att anropa [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metoden precis innan kalkylbladet renderas till PDF-format. På så sätt säkerställs att formelberoende värden omräknas och de korrekta värdena renderas i PDF:en.

{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till bokmärken i PDF](/cells/sv/python-net/add-pdf-bookmarks/)
- [Lägg till bokmärken i PDF med namngivna destinationer](/cells/sv/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut](/cells/sv/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Konvertera XLSX-fil till PDF-format](/cells/sv/python-net/convert-xlsx-file-to-pdf-format/)
- [Konvertera Excel-fil till PDF-format kompatibelt med PDFA-1a](/cells/sv/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertera XLS-fil med bilder eller diagram till PDF](/cells/sv/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Skapa PdfBookmarkEntry för diagramblad](/cells/sv/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Anpassa alla arbetsbokskolumner på en enda PDF-sida](/cells/sv/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorera fel vid rendering av Excel till PDF](/cells/sv/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begränsa antalet genererade sidor - Excel till PDF-konvertering](/cells/sv/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Skriv ut kommentarer vid sparande till PDF](/cells/sv/python-net/print-comments-while-saving-to-pdf/)
- [Rendera Office-tillägg vid konvertering av Excel till PDF](/cells/sv/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendera en PDF-sida per Excel-ark - Konvertering från Excel till PDF](/cells/sv/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendera Unicode-supplementära tecken i utgående PDF med Aspose.Cells](/cells/sv/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resamplings tillagda bilder - Konvertering från Excel till PDF](/cells/sv/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Spara varje arbetsblad i en separat PDF-fil](/cells/sv/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Spara Excel som PDF med standard- eller minsta storlek](/cells/sv/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Spara angivna arbetsblad som PDF](/cells/sv/python-net/save-specified-worksheets-to-pdf/)
- [Säkra PDF-dokument](/cells/sv/python-net/secure-pdf-documents/)
- [Ange hur textsträngar ska korsas i utgående PDF och bild](/cells/sv/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="python-net" >}}
