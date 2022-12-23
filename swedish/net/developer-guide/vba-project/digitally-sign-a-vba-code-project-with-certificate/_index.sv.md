---
title: Signera digitalt ett VBA-kodprojekt med certifikat
type: docs
weight: 110
url: /sv/net/digitally-sign-a-vba-code-project-with-certificate/
---
{{% alert color="primary" %}}

 Du kan digitalt signera ditt VBA-kodprojekt med Aspose.Cells med dess[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign)metod. Följ dessa steg för att kontrollera om din excel-fil är digitalt signerad med ett certifikat.

-  Klick**Visual Basic** från**Utvecklare** fliken för att öppna**Visual Basic för applikationer IDE**
-  Klick**Verktyg** > **Digitala signaturer...** av**Visual Basic för applikationer IDE**

 och det kommer att visa**Digital signaturformulär** som visar om dokumentet är digitalt signerat med ett certifikat eller inte.

{{% /alert %}} 

## **Signera digitalt ett VBA-kodprojekt med certifikat på C#**

 Följande exempelkod illustrerar hur du använder[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign)metod. Här är in- och utdatafilerna för exempelkoden. Du kan använda valfri excel-fil och vilket certifikat som helst för att testa den här koden.

- [Excel-källfil](5115028.xlsm) används i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa en digital signatur. Installera den på din dator för att köra den här koden. Dess lösenord är 1234.
- [Utdata Excel-fil](5115029.xlsm) genereras av exempelkoden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
