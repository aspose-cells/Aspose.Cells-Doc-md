---
title: Konvertera Excel-arbetsbok till PDF
type: docs
weight: 80
url: /sv/cpp/convert-excel-workbook-to-pdf/
---
## **Konvertera Excel-arbetsbok till PDF**
PDF-filer används ofta för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

{{% alert color="primary" %}} 

 Aspose.Cells skriver direkt informationen om API och versionsnummer i utdatadokument. Till exempel, vid rendering av dokument till PDF, fyller Aspose.Cells för C++**Ansökan** fält med värdet 'Aspose.Cells' och**PDF-producent**fält med värde, t.ex. 'Aspose.Cells v18.5.0'.

Observera att du inte kan instruera Aspose.Cells för C++ att ändra eller ta bort denna information från utdatadokument.

{{% /alert %}} 
### **Direkt konvertering**
Aspose.Cells stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil till PDF med hjälp av[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)klass'[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metod. De[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metoden ger[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)uppräkningsmedlem som konverterar de ursprungliga Excel-filerna till PDF-format.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1.  Instantiera ett objekt av[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)klass genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda in en befintlig mallfil eller hoppa över det här steget om du skapar arbetsboken från början.
1. Gör något arbete (mata in data, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, och så vidare) på kalkylarket med hjälp av Aspose.Cells' API:er.
1.  När kalkylarkskoden är klar ringer du[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)klass'[Spara](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)metod för att spara kalkylarket.

Filformatet bör vara PDF så välj relevant PDF (ett fördefinierat värde) från SaveFormat-uppräkningen för att generera det slutliga PDF-dokumentet

 Se följande exempelkod, dess[exempel på Excel-fil](67338368.xlsx) och[mata ut PDF](67338369.pdf) för din kännedom.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **Avancerad konvertering**
Du kan också välja att använda[IPdfSaveOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)klass för att ställa in olika attribut för konverteringen. Ställa in olika egenskaper för**IPdfSaveOptions** klass ger dig kontroll över utskrifts-, teckensnitts-, säkerhets- och komprimeringsinställningar för utdata-PDF. Den viktigaste egendomen är[Ställ inCompliance](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)som gör att du kan spara Excel-filerna till PDF/A-kompatibla PDF-filer.
#### **Spara arbetsbok till PDF/A-kompatibla filer**
Följande kodavsnitt visar hur du använder**IPdfSaveOptions**klass för att spara Excel-filer till PDF/A-kompatibelt PDF-format

 Se följande exempelkod och dess[mata ut PDF](67338370.pdf) för din kännedom.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **Ställ in tid för att skapa PDF**
Med**IPdfSaveOptions**klass, kan du hämta eller ställa in PDF-genereringstiden.

 Se följande exempelkod och dess[mata ut PDF](67338371.pdf) för din kännedom.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}
