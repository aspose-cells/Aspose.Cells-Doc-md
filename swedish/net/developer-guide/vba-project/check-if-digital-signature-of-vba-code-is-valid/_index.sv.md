---
title: Kontrollera om den digitala signaturen av VBA koden är giltig
type: docs
weight: 120
url: /sv/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells låter dig kontrollera om den digitala signaturen av VBA-koden är giltig med hjälp av [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) -egenskapen. Den kommer att returnera **true** om signaturen är giltig, annars kommer den att returnera **false**. Den digitala signaturen av VBA-koden blir ogiltig när du ändrar VBA-koden.

{{% /alert %}}

## **Kontrollera om digital signaturen av VBA-koden är giltig i C#**

Följande kod visar användningen av denna egenskap med [exempel excelfil](5115030.xlsm) som du kan ladda ner från den angivna länken. Samma excelfil har en giltig signatur, men när vi ändrar dess VBA-kod och sparar arbetsboken och sedan kontrollerar på nytt, finner vi att dess signatur har blivit ogiltig.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
{{< app/cells/assistant language="csharp" >}}
