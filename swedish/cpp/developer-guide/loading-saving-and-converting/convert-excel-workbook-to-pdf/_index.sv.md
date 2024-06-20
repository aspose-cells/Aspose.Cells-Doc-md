---
title: Konvertera Excelarbetsbok till PDF
type: docs
weight: 80
url: /sv/cpp/convert-excel-workbook-to-pdf/
---

## **Konvertering av Excelarbetsbok till PDF**
PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{% alert color="primary" %}} 

Aspose.Cells skriver direkt informationen om API och versionsnummer i utdata-Dokument. Till exempel fyller Aspose.Cells for C++ i fältet **Program** med värdet 'Aspose.Cells' och **PDF-producenter** fält med värde, t.ex. 'Aspose.Cells v18.5.0', vid bearbetning av dokument till PDF.

Observera att du inte kan instruera Aspose.Cells for C++ att ändra eller ta bort denna information från utdata-dokument.

{{% /alert %}} 
### **Direkt konvertering**
Aspose.Cells stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil till PDF med hjälp av Workbook-klassens [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metod. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metoden tillhandahåller medlemsuppräkningen [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som konverterar de nativa Excel-filerna till PDF-format.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1. Skapa ett objekt i klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
1. Gör något arbete (infodata, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, etc.) på kalkylbladet med hjälp av Aspose.Cells APIs.
1. När kalkylbladets kod är komplett, kalla på [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassens [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod för att spara kalkylbladet.

Filformatet ska vara PDF så välj relevant PDF (ett fördefinierat värde) från SaveFormat uppräkningen för att generera det slutgiltiga PDF-dokumentet.

Se följande exempelkod, dess [exempel Excel-fil](67338368.xlsx) och [utmatnings-PDF](67338369.pdf) för din referens.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **Avancerad konvertering**
Du kan också välja att använda [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) klassen för att ställa in olika attribut för konverteringen. Genom att ställa in olika egenskaper i klassen **PdfSaveOptions** ger du kontroll över utskrift, typsnitt, säkerhet och komprimeringsinställningar för utmatnings-PDF:n. Den viktigaste egenskapen är [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/) som gör det möjligt för dig att spara Excel-filerna som PDF/A-kompatibla PDF-filer.
#### **Spara arbetsboken som PDF/A-kompatibla filer**
Följande kodsnutt visar hur man använder klassen **PdfSaveOptions** för att spara Excel-filer som PDF/A-kompatibla PDF-format

Se följande exempelkod och [utmatnings-PDF](67338370.pdf) för din referens.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **Ange PDF-skapandetid**
Med klassen **IPdfSaveOptions** kan du hämta eller ställa in PDF-skapandetid.

Se följande exempelkod och [utmatnings-PDF](67338371.pdf) för din referens.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
