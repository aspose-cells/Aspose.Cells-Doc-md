---
title: Lägg till digital signatur i en redan signerad Excelfil
type: docs
weight: 20
url: /sv/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: Denna artikel beskriver hur man lägger till digital signatur i en redan undertecknad Excel fil med C# kod med Aspose.Cells för Python via .NET.
keywords: Lägg till digital signatur till redan signerad Excel fil, Hur man lägger till en digital signatur till en redan signerad Excel dokument.
---

## **Möjliga användningsscenario**

Aspose.Cells för Python via .NET tillhandahåller metoden [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) som du kan använda för att lägga till digital signatur till en redan signerad Excel-fil.

{{% alert color="primary" %}}

Vänligen notera att när du lägger till en digital signatur i ett redan signerat Excel-dokument, fungerar det bäst om det ursprungliga dokumentet är genererat av Aspose.Cells för Python via .NET. Men om det ursprungliga dokumentet är skapat av andra motorer (t.ex. Microsoft Excel), kan Aspose.Cells för Python via .NET inte behålla samma fil efter inläsning och omarbetning, vilket kan göra den ursprungliga signaturen ogiltig.

{{% /alert %}}

## **Hur man lägger till en digital signatur till en redan signerad Excel-fil**

Följande kodexempel visar hur du använder metoden [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) för att lägga till en digital signatur i en redan signerad Excel-fil. Vänligen kontrollera den [provsfil](50528280.xlsx) som används i denna kod. Den här filen är redan digitalt signerad. Vänligen kontrollera den [utdata-Excel-fil](50528281.xlsx) som genereras av koden. Vi har använt det demo-certifikat som heter [AsposeDemo.pfx](50528279.pfx) i den här koden som har ett lösenord **aspose**. Skärmbilden visar effekten av kodexemplet på provfilen efter exekvering.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
