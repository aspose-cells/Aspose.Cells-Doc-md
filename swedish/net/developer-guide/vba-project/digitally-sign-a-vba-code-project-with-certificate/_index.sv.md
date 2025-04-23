---
title: Signera digitalt ett VBA kodprojekt med certifikat
type: docs
weight: 110
url: /sv/net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Du kan signera ditt VBA-kodprojekt digitalt med Aspose.Cells med dess [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign) metod. Följ dessa steg för att kontrollera om din Excel-fil är signerad digitalt med ett certifikat.

- Klicka på **Visual Basic** från fliken **Utvecklare** för att öppna **Visual Basic for Applications IDE**
- Klicka på **Verktyg** > **Digitala signaturer...**  i **Visual Basic for Applications IDE**

och det kommer att visa **Digital Signature Form** och visa om dokumentet är signerat digitalt med ett certifikat eller inte.

{{% /alert %}} 

## **Signera digitalt ett VBA-kodprojekt med certifikat i C#**

Följande exempelkod illustrerar hur man använder [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign) metoden. Här är indata- och utdatafilerna för exempelkoden. Du kan använda vilken excel-fil och vilket certifikat som helst för att testa denna kod.

- [Källa Excel-fil](5115028.xlsm) använd i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa digital signatur. Installera den på din dator för att köra denna kod. Dess lösenord är 1234.
- [Utdatat Excel-fil](5115029.xlsm) genererad av exempelkoden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
