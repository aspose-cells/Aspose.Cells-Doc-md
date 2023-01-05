---
title: Lägg till digital signatur i en redan signerad Excel-fil
type: docs
weight: 20
url: /sv/net/add-digital-signature-to-an-already-signed-excel-file/
---
## **Möjliga användningsscenarier**

 Aspose.Cells tillhandahåller[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)metod som du kan använda för att lägga till digital signatur i en redan signerad Excel-fil.

{{% alert color="primary" %}}

Observera att när du lägger till en digital signatur till ett redan signerat Excel-dokument, om originaldokumentet är Aspose.Cells-genererat dokument, fungerar det bra. Men om originaldokumentet genereras av andra motorer (t.ex. Microsoft Excel etc.), kan Aspose.Cells inte behålla filen densamma efter att ha laddats in och sparats på nytt, vilket gör att den ursprungliga signaturen blir ogiltig.

{{% /alert %}}

## **Lägg till digital signatur i en redan signerad Excel-fil**

Följande exempelkod visade hur man använder sig av[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) metod för att lägga till digital signatur till redan signerad Excel-fil. Vänligen kontrollera[exempel på Excel-fil](50528280.xlsx) används i denna kod. Den här filen är redan digitalt signerad. Vänligen kontrollera[utdata Excel-fil](50528281.xlsx) genereras av koden. Vi har använt democertifikatet som heter[AsposeDemo.pfx](50528279.pfx) i denna kod som har ett lösenord**aspose**Skärmdumpen visar effekten av exempelkoden på exemplet i Excel-filen efter körning.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
