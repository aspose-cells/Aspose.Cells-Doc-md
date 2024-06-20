---
title: Lägg till digital signatur i en redan signerad Excelfil
type: docs
weight: 20
url: /sv/net/add-digital-signature-to-an-already-signed-excel-file/
description: Den här artikeln beskriver hur man lägger till en digital signatur till en redan signerad Excel fil med hjälp av C# koder med Aspose.Cells for .Net.
keywords: Lägg till digital signatur till redan signerad Excel fil, Hur man lägger till en digital signatur till en redan signerad Excel dokument.
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller metoden [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) som du kan använda för att lägga till en digital signatur i en redan signerad Excel-fil.

{{% alert color="primary" %}}

Observera att när du lägger till en digital signatur i en redan signerad Excel-dokument, om det ursprungliga dokumentet är genererat av Aspose.Cells-motorn fungerar det bra. Men om det ursprungliga dokumentet är genererat av andra motorer (t.ex. Microsoft Excel etc.), kan inte Aspose.Cells behålla filen oförändrad efter att ha laddat och sparar om den, vilket gör att den ursprungliga signaturen blir ogiltig.

{{% /alert %}}

## **Hur man lägger till en digital signatur till en redan signerad Excel-fil**

Följande kodexempel visar hur du använder metoden [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) för att lägga till en digital signatur i en redan signerad Excel-fil. Vänligen kontrollera den [provsfil](50528280.xlsx) som används i denna kod. Den här filen är redan digitalt signerad. Vänligen kontrollera den [utdata-Excel-fil](50528281.xlsx) som genereras av koden. Vi har använt det demo-certifikat som heter [AsposeDemo.pfx](50528279.pfx) i den här koden som har ett lösenord **aspose**. Skärmbilden visar effekten av kodexemplet på provfilen efter exekvering.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
