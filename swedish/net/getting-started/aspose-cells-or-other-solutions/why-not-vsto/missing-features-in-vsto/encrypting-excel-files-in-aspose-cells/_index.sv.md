---
title: Kryptera Excel filer i Aspose.Cells
type: docs
weight: 90
url: /sv/net/encrypting-excel-files-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) gör det möjligt för dig att kryptera och lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av en kryptografisk serviceprovider, eller CSP, en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är 'Office 97/2000 Kompatibel' eller 'Svag kryptering (XOR)'. Det är viktigt att välja rätt krypteringsnyckellängd. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara en svag kryptering. För stark kryptering krävs en minimum nyckellängd på 128 bitar. Microsoft Windows innehåller också CSP:er som erbjuder starka typer av kryptering, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en idé, är 128 bitars kryptering vad banker använder för att kryptera anslutningen till sina Internetbankssystem.

Aspose.Cells gör det möjligt för dig att kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}} 
## **Använda Microsoft Excel**
För att ställa in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1. Från menyn **Verktyg** väljer du **Alternativ**.
   En dialogruta visas.
1. Välj fliken **Säkerhet**.
1. Ange ett lösenord och klicka på **Avancerat** 
   **Dialogrutan Alternativ** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_1.png)




1. Välj krypteringstyp och bekräfta lösenordet. 

   **Dialogrutan Krypteringstyp** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_2.png)



## **Kryptering med Aspose.Cells**
Exemplet nedan visar hur man krypterar och lösenordsskyddar en Excel-fil med hjälp av Aspose.Cells API.

**C#**

{{< highlight csharp >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
