---
title: Lägg till digital signatur i en redan signerad Excel-fil
type: docs
weight: 20
url: /sv/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **Möjliga användningsscenarier**

Aspose.Cells tillhandahåller[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) metod som du kan använda för att lägga till digital signatur i en redan signerad Excel-fil.

{{% alert color="primary" %}}

Observera att när du lägger till en digital signatur till ett redan signerat Excel-dokument, om originaldokumentet är Aspose.Cells-genererat dokument, fungerar det bra. Men om originaldokumentet genereras av andra motorer (t.ex. Microsoft Excel etc.), kan Aspose.Cells inte behålla filen densamma efter att ha laddats in och sparats på nytt, vilket gör att den ursprungliga signaturen blir ogiltig.

{{% /alert %}}

## **Lägg till digital signatur i en redan signerad Excel-fil**

Följande exempelkod förklarar hur du använder[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) metod för att lägga till en digital signatur till redan signerad Excel-fil. Vänligen kontrollera[exempel på Excel-fil](50528287.xlsx)används i denna kod. Den här filen är redan digitalt signerad. Vänligen kontrollera[utdata Excel-fil](50528288.xlsx)genereras av koden. Vi har använt democertifikatet som heter[AsposeTest.pfx](50528289.pfx)i denna kod som har ett lösenord*aspose*Skärmdumpen visar effekten av exempelkoden på exemplet i Excel-filen efter körning.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
