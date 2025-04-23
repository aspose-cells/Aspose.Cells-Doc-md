---
title: Konvertera Excelarbetsbok till PDF
type: docs
weight: 80
url: /sv/go-cpp/convert-excel-workbook-to-pdf/
---

## **Konvertering av Excelarbetsbok till PDF**

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{% alert color="primary" %}}

 Aspose.Cells skriver direkt ut information om API och versionsnummer i utdata. Till exempel, vid rendering av dokumentet till PDF, fyller Aspose.Cells for Go via C++ i **Application**-fältet med värdet 'Aspose.Cells' och **PDF Producer**-fältet med exempelvis 'Aspose.Cells v24.12.0'.

 Observera att du inte kan instruera Aspose.Cells for Go via C++ att ändra eller ta bort denna information från utdata Dokument.

{{% /alert %}}

### **Direkt konvertering**

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1. Skapa ett objekt av klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
1. Gör något arbete (infodata, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, etc.) på kalkylbladet med hjälp av Aspose.Cells APIs.
1. När kalkylbladsprogrammet är klart, anropa [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) klassens [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) metod för att spara kalkylbladet.

 Filformatet ska vara PDF, så välj relevant PDF (en fördefinierad värde) från enumerationen SaveFormat för att generera slutdokumentet i PDF-format.

 Se följande kodexempel, dess [exempel-Excel-fil](67338368.xlsx) och [utdata PDF](67338369.pdf) för referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
