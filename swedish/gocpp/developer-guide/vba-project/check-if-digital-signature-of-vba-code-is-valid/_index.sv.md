---
title: Kontrollera om digital signatur av VBA koden är giltig med Golang via C++
linktitle: Kontrollera om den digitala signaturen av VBA koden är giltig
type: docs
weight: 120
url: /sv/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Lär dig att kontrollera giltigheten av en digital signatur i VBA kod med Aspose.Cells med Golang via C++
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att kontrollera om den digitala signaturen för VBA-koden är giltig med hjälp av [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/)-egenskapen. Den returnerar **true** om signaturen är giltig; annars returnerar den **false**. Den digitala signaturen för VBA-koden blir ogiltig när du ändrar VBA-koden.

{{% /alert %}}

## **Kontrollera om digital signatur av VBA-koden är giltig i C++**

 Följande kod demonstrerar användningen av denna egenskap med [exempel-Excelfilen](5115030.xlsm) som du kan ladda ner från länken. Samma Excel-fil har en giltig signatur, men när vi ändrar dess VBA-kod och sparar arbetsboken och sedan kontrollerar igen, konstaterar vi att dess signatur har blivit ogiltig.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
