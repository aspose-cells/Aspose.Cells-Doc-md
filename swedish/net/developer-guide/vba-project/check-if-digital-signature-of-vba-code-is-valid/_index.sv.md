---
title: Kontrollera om den digitala signaturen för VBA-koden är giltig
type: docs
weight: 120
url: /sv/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

 Aspose.Cells låter dig kontrollera om den digitala signaturen för VBA-koden är giltig med hjälp av[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) fast egendom. Det kommer tillbaka**Sann** om signaturen är giltig annars kommer den tillbaka**falsk**. Den digitala signaturen för VBA-koden blir ogiltig när du ändrar VBA-koden.

{{% /alert %}}

## **Kontrollera om den digitala signaturen för VBA-koden är giltig i C#**

Följande kod visar användningen av den här egenskapen med hjälp av[exempel på excel-fil](5115030.xlsm) som du kan ladda ner från den medföljande länken. Samma excel-fil har en giltig signatur men när vi ändrar dess VBA-kod och sparar arbetsboken och sedan kontrollerar igen, finner vi att dess signatur har blivit ogiltig.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
