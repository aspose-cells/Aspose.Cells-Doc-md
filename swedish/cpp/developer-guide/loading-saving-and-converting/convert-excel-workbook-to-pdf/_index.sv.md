---
title: Konvertera Excel-arbetsbok till PDF
type: docs
weight: 80
url: /sv/cpp/convert-excel-workbook-to-pdf/
---
##  **Konvertera Excel Workbook till PDF**
PDF-filer används ofta för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

{{% alert color="primary" %}} 

 Aspose.Cells skriver direkt informationen om API och versionsnummer i utdatadokument. Till exempel, när dokumentet återges till PDF, fylls Aspose.Cells for C++ i**Ansökan** fält med värdet 'Aspose.Cells' och**PDF Producent** fält med värde, t.ex. 'Aspose.Cells v18.5.0'.

Observera att du inte kan instruera Aspose.Cells for C++ att ändra eller ta bort denna information från utdatadokument.

{{% /alert %}} 
###  **Direkt konvertering**
Aspose.Cells stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil till PDF med hjälp av[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)klass'[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metod. De[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metoden ger[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)uppräkningsmedlem som konverterar de ursprungliga Excel-filerna till formatet PDF.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till formatet PDF:

1.  Instantiera ett objekt av[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)klass genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda in en befintlig mallfil eller hoppa över det här steget om du skapar arbetsboken från början.
1. Gör något arbete (mata in data, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, och så vidare) på kalkylarket med hjälp av Aspose.Cells' API:er.
1.  När kalkylarkskoden är klar ringer du[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)klass'[Spara](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metod för att spara kalkylarket.

Filformatet ska vara PDF så välj relevant PDF (ett fördefinierat värde) från SaveFormat-uppräkningen för att generera det slutliga PDF-dokumentet

 Se följande exempelkod, dess[exempel på Excel-fil](67338368.xlsx) och[utgång PDF](67338369.pdf) för din kännedom.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **Avancerad konvertering**
Du kan också välja att använda[PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)klass för att ställa in olika attribut för konverteringen. Ställa in olika egenskaper för**PdfSaveOptions** klass ger dig kontroll över utskrifts-, teckensnitts-, säkerhets- och komprimeringsinställningar för utdata PDF. Den viktigaste egenskapen är[Ställ inCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)vilket gör att du kan spara Excel-filerna till PDF/A-kompatibla PDF-filer.
####  **Sparar arbetsbok till PDF/A överensstämmande filer**
Följande kodavsnitt visar hur du använder**PdfSaveOptions**klass för att spara Excel-filer till PDF/A-kompatibelt PDF-format

 Se följande exempelkod och dess[utgång PDF](67338370.pdf) för din kännedom.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **Ställ in PDF Creation Time**
Med**IPdfSaveOptions** klass, kan du hämta eller ställa in skapelsetiden PDF.

 Se följande exempelkod och dess[utgång PDF](67338371.pdf) för din kännedom.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
