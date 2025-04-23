---
title: Signera digitalt ett VBA kodprojekt med certifikat
type: docs
weight: 110
url: /sv/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Du kan signera ditt VBA-kodprojekt digitalt med Aspose.Cells med dess [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-) metod. Följ dessa steg för att kontrollera om din Excel-fil är signerad digitalt med ett certifikat.

- Klicka på **Visual Basic** från fliken **Utvecklare** för att öppna **Visual Basic for Applications IDE**
- Klicka på **Verktyg** > **Digitala signaturer...** av **Visual Basic for Applications IDE**

och det kommer att visa **Digital Signature Form** och visa om dokumentet är signerat digitalt med ett certifikat eller inte.

{{% /alert %}} 

## **Signera digitalt ett VBA-kodprojekt med certifikat i C#**

Följande exempelkod illustrerar hur man använder [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-) metoden. Här är inmatnings- och utmatningsfilerna för exempelkoden. Du kan använda vilken excel-fil som helst och vilket certifikat som helst för att testa denna kod.

- [Källa Excel-fil](5115028.xlsm) använd i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa digital signatur. Installera den på din dator för att köra denna kod. Dess lösenord är 1234.
- [Utdatat Excel-fil](5115029.xlsm) genererad av exempelkoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
{{< app/cells/assistant language="java" >}}
