---
title: Digitalt signera ett VBA kodprojekt med certifikat i C++
linktitle: Signera digitalt ett VBA kodprojekt med certifikat
type: docs
weight: 110
url: /sv/go-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Lär dig hur du digitalt signerar ditt VBA kodprojekt med hjälp av Aspose.Cells for C++ med ett certifikat.
---

{{% alert color="primary" %}} 

Du kan digitalt signera ditt VBA-kodprojekt med Aspose.Cells med dess [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/)-metod. Följ dessa steg för att kontrollera om din Excel-fil är digitalt signerad med ett certifikat.

- Klicka på **Visual Basic** från fliken **Utvecklare** för att öppna **Visual Basic for Applications IDE**.
- Klicka på **Verktyg** > **Digitala signaturer...** i **Visual Basic for Applications IDE**.

Den visar **Digital Signature Form** som indikerar om dokumentet är digitalt signerat med ett certifikat eller inte.

{{% /alert %}} 

## **Digitalt signera ett VBA-kodprojekt med certifikat i C++**

Följande exempel på kod visar hur man använder [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/) metod. Här är in- och utdatafilerna för exemplet. Du kan använda vilken Excel-fil och certifikat som helst för att testa denna kod.

- [Källa Excel-fil](5115028.xlsm) använd i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa digital signatur. Installera den på din dator för att köra denna kod. Dess lösenord är 1234.
- [Utdatat Excel-fil](5115029.xlsm) genererad av exempelkoden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DigitallySignAVbaCodeProjectWithCertificate.go" >}}
