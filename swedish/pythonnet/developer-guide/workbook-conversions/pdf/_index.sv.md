---
title: Pdf
type: docs
weight: 220
url: /sv/python-net/convert-excel-to-pdf/
description: Lär dig hur du konverterar Excel till PDF med Aspose.Cells for Python via .NET API.
keywords: Python converT Excel to PDF, ConverT Excel to PDF using Python, Python save Excel to PDF, Excel to PDF in Python
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET stöder konvertering av Excel-arbetsbok till PDF. I det här exemplet kommer vi att se den fullständiga konverteringen av en Excel-arbetsbok till PDF.

{{% /alert %}}

##  **Konvertera Excel Workbook till PDF**

PDF-filer används ofta för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells for Python via .NET stöder konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET skriver direkt informationen om API och versionsnummer i utgående dokument. Till exempel, vid rendering av dokument till PDF, Aspose.Cells for Python via .NET fylls i**PDF Producent** fält med värde, t.ex. 'Aspose.Cells for Python via .NET v23.2'.

 Observera att du kan ändra denna information i utdatadokument med**[PdfSaveOptions.producer](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/)** fast egendom.

{{% /alert %}}

###  **Direkt konvertering**

 Aspose.Cells for Python via .NET stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil till PDF med hjälp av**[Arbetsbok](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**klass'**[spara](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** metod. De**[spara](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** metoden ger**[SaveFormat.PDF](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**uppräkningsmedlem som konverterar de ursprungliga Excel-filerna till formatet PDF.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till formatet PDF:

1.  Instantiera ett objekt av**[Arbetsbok](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**klass genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda in en befintlig mallfil eller hoppa över det här steget om du skapar arbetsboken från början.
1. Gör något arbete (mata in data, tillämpa formatering, ställ in formler, infoga bilder eller andra ritobjekt och så vidare) på kalkylarket med hjälp av Aspose.Cells for Python via .NET' API:er.
1.  När kalkylarkskoden är klar ringer du**[Arbetsbok](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**klass'**[spara](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**metod för att spara kalkylarket.

 Filformatet ska vara PDF så välj*PDF* (ett fördefinierat värde) från**[SaveFormat](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**uppräkning för att generera det slutliga PDF-dokumentet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

###  **Avancerad konvertering**

 Du kan också välja att använda**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** klass för att ställa in olika attribut för konverteringen. Ställa in olika egenskaper för**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** klass ger dig kontroll över utskrifts-, teckensnitts-, säkerhets- och komprimeringsinställningar för utdata PDF. Den viktigaste egenskapen är**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**vilket gör att du kan spara Excel-filerna till PDF/A-kompatibla PDF-filer.

####  **Sparar arbetsbok till PDF/A överensstämmande filer**

 Det nedan tillhandahållna kodavsnittet visar hur du använder**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**klass för att spara Excel-filer till PDF/A-kompatibelt PDF-format.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Observera att**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**egendom lades till när Aspose.Cells for Python via .NET for .NET 5.3.0 släpptes.

{{% /alert %}}

####  **Ställ in PDF Creation Time**

 Med**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**klass, kan du hämta eller ställa in skapelsetiden PDF. Följande kod visar användningen av**[PdfSaveOptions.created_time](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/)** egenskap för att ställa in skapelsetiden för PDF-filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

####  **Ställ in alternativet ContentCopyForAccessibility**

Med**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** klass, kan du få eller ställa in PDF**[PdfSecurityOptions.accessibility_extract_content](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)** alternativet för att kontrollera innehållsåtkomsten i den konverterade PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

####  **Exportera anpassade egenskaper till PDF**

Med**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** klass, kan du exportera de anpassade egenskaperna i källarbetsboken till PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)**Enumerator tillhandahålls för att specificera hur egenskaper exporteras. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Arkiv och sedan egenskaper alternativ som visas i följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ner[här](sourceWithCustProps.xlsx) för testning och utdata PDF filen "outSourceWithCustProps" är tillgänglig[här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

###  **Konverteringsattribut**

Vi arbetar för att förbättra konverteringsfunktionerna med varje ny version. Aspose.Cell's omvandling av Excel till PDF har fortfarande ett par begränsningar. MapChart stöds inte vid konvertering till PDF-format. Vissa ritobjekt stöds inte heller bra.

Tabellen som följer listar alla funktioner som helt eller delvis stöds vid export till Aspose.Cells med Aspose.Cells for Python via .NET. Den här tabellen är inte slutgiltig och täcker inte alla kalkylbladsattribut men den identifierar de funktioner som inte stöds eller delvis stöds för konvertering till PDF.

|**Dokumentelement**|**Attribut**|**Stöds**|**Anteckningar**|
| :- | :- | :- | :- |
|Inriktning| |Ja| |
|Bakgrundsinställningar| |Ja| |
|Gräns|Färg|Ja| |
|Gräns|Linjestil|Ja| |
|Gräns|Linjebredd|Ja| |
|Cell Data| |Ja| |
|Kommentarer| |Ja| |
|Villkorlig formatering| |Ja| |
|Dokument egenskaper| |Ja| |
|Rita objekt| |Delvis|Skugg- och 3D-effekter för att rita objekt stöds inte bra; WordArt och SmartArt stöds delvis.|
|Font|Storlek|Ja| |
|Font|Färg|Ja| |
|Font|Stil|Ja| |
|Font|Understrykning|Ja| |
|Font|Effekter|Ja||
|Bilder| |Ja| |
|Hyperlänk| |Ja| |
|Diagram| |Delvis|MapChart stöds inte.|
|Sammanslagna Cells| |Ja| |
|Sidbrytning| |Ja| |
|Utskriftsformat|Sidhuvud/sidfot|Ja| |
|Utskriftsformat|Marginaler|Ja| |
|Utskriftsformat|Sidorientering|Ja| |
|Utskriftsformat|Sidstorlek|Ja| |
|Utskriftsformat|Utskriftsområde|Ja| |
|Utskriftsformat|Skriv ut titlar|Ja| |
|Utskriftsformat|Skalning|Ja| |
|Radhöjd/kolumnbredd| |Ja| |
|RTL-språk (Right to Left).| |Ja| |

{{% alert color="primary" %}}

 Om ditt kalkylblad innehåller formler är det bäst att ringa[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)metod precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}

##  **Förhandsämnen**
- [Lägg till PDF Bokmärken](/cells/sv/python-net/add-pdf-bookmarks/)
- [Lägg till PDF bokmärken med namngivna destinationer](/cells/sv/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Undvik tom sida i utdata PDF när det inte finns något att skriva ut](/cells/sv/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Konvertera XLSX-fil till PDF-format](/cells/sv/python-net/convert-xlsx-file-to-pdf-format/)
- [Konvertera Excel-fil till PDF-format som är kompatibelt med PDFA-1a](/cells/sv/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertera XLS-fil med bilder eller diagram till PDF](/cells/sv/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Skapa PdfBookmarkEntry för diagramblad](/cells/sv/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Anpassa alla kalkylbladskolumner på en PDF sida](/cells/sv/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorera fel när du renderar Excel till PDF](/cells/sv/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begränsa antalet genererade sidor - Excel till PDF konvertering](/cells/sv/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Skriv ut kommentarer samtidigt som du sparar till PDF](/cells/sv/python-net/print-comments-while-saving-to-pdf/)
- [Återge Office-tillägg medan du konverterar Excel till PDF](/cells/sv/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendera en PDF sida per Excel-arbetsblad - Excel till PDF konvertering](/cells/sv/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Återge Unicode-tilläggstecken i utdata PDF av Aspose.Cells](/cells/sv/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Omsampling av tillagda bilder - Konvertering av Excel till PDF](/cells/sv/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Spara varje kalkylblad till en annan PDF-fil](/cells/sv/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Spara Excel i PDF med standard- eller minimistorlek](/cells/sv/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Spara specificerade arbetsblad till PDF](/cells/sv/python-net/save-specified-worksheets-to-pdf/)
- [Säkra PDF Dokument](/cells/sv/python-net/secure-pdf-documents/)
- [Ange hur strängen ska korsas i utgång PDF och bild](/cells/sv/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
