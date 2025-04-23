---
title: Signera digitalt ett VBA kodprojekt med certifikat
type: docs
weight: 110
url: /sv/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Du kan digitalt underteckna ditt VBA-kodprojekt med Aspose.Cells för Python via .NET med dess [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature)-metod. Följ dessa steg för att kontrollera om din Excel-fil är digitalt signerad med ett certifikat.

- Klicka på **Visual Basic** från fliken **Utvecklare** för att öppna **Visual Basic for Applications IDE**
- Klicka på **Verktyg** > **Digitala signaturer...**  i **Visual Basic for Applications IDE**

och det kommer att visa **Digital Signature Form** och visa om dokumentet är signerat digitalt med ett certifikat eller inte.

{{% /alert %}} 

## **Digitalt signera ett VBA-kodprojekt med certifikat i Python**

Följande exempelkod illustrerar hur man använder [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature) metoden. Här är indata- och utdatafilerna för exempelkoden. Du kan använda vilken excel-fil och vilket certifikat som helst för att testa denna kod.

- [Källa Excel-fil](5115028.xlsm) använd i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa digital signatur. Installera den på din dator för att köra denna kod. Dess lösenord är 1234.
- [Utdatat Excel-fil](5115029.xlsm) genererad av exempelkoden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

