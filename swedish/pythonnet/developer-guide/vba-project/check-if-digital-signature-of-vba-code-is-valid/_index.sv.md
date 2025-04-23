---
title: Kontrollera om den digitala signaturen av VBA koden är giltig
type: docs
weight: 120
url: /sv/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET låter dig kontrollera om den digitala signaturen för VBA-koden är giltig med hjälp av [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed)-egenskapen. Det kommer att returnera **true** om signaturen är giltig, annars returnerar det **false**. Den digitala signaturen för VBA-koden blir ogiltig när du ändrar VBA-koden.

{{% /alert %}}

## **Kontrollera om digital signatur för VBA-kod är giltig i Python**

Följande kod visar användningen av denna egenskap med [exempel excelfil](5115030.xlsm) som du kan ladda ner från den angivna länken. Samma excelfil har en giltig signatur, men när vi ändrar dess VBA-kod och sparar arbetsboken och sedan kontrollerar på nytt, finner vi att dess signatur har blivit ogiltig.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

