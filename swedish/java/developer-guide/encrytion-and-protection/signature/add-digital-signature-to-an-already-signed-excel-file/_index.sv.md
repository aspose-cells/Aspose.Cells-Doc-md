---
title: Lägg till digital signatur i en redan signerad Excelfil
type: docs
weight: 20
url: /sv/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller metoden [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-), som du kan använda för att lägga till digital signatur i en redan signerad Excelfil.

{{% alert color="primary" %}}

Observera att när du lägger till en digital signatur i en redan signerad Excel-dokument, om det ursprungliga dokumentet är genererat av Aspose.Cells-motorn fungerar det bra. Men om det ursprungliga dokumentet är genererat av andra motorer (t.ex. Microsoft Excel etc.), kan inte Aspose.Cells behålla filen oförändrad efter att ha laddat och sparar om den, vilket gör att den ursprungliga signaturen blir ogiltig.

{{% /alert %}}

## **Lägg till digital signatur i en redan signerad Excel-fil**

Följande exempelkod förklarar hur man använder [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) metod för att lägga till en digital signatur i redan signerad Excel-fil. Vänligen kontrollera den [exempel Excel-fil](50528287.xlsx) som används i denna kod. Denna fil är redan digitalt signerad. Vänligen kontrollera den [utdatamappar Excel-filen](50528288.xlsx) som genereras av koden. Vi har använt det demokratiska certifikatet med namnet [AsposeTest.pfx](50528289.pfx) i koden som har ett lösenord som är *aspose*. Skärmdumpen visar effekten av exempelkoden på den exempel-Excel-filen efter körning.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
