---
title: Kryptera Excel-filer i Aspose.Cells
type: docs
weight: 90
url: /sv/net/encrypting-excel-files-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) gör att du kan kryptera och lösenordsskydda dina kalkylblad. Den använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är 'Office 97/2000 Compatible' eller 'Weak Encryption (XOR)'. Det är viktigt att välja rätt längd på krypteringsnyckeln. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara en svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller CSP:er som också erbjuder starka krypteringstyper, till exempel "Microsoft Strong Cryptographic Provider". För att ge dig en uppfattning är 128-bitars kryptering vad banker använder för att kryptera anslutningen till sina Internetbanksystem.

Aspose.Cells låter dig kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}} 
## **Använder Microsoft Excel**
Så här ställer du in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1.  Från**Verktyg** menyn, välj**alternativ**.
 En dialogruta visas.
1.  Välj**säkerhet** flik.
1.  Ange ett lösenord och klicka**Avancerad** 
   **Dialogrutan Alternativ** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_1.png)




1.  Välj krypteringstyp och bekräfta lösenordet.

   **Dialogrutan Krypteringstyp** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_2.png)



## **Kryptering med Aspose.Cells**
Följande exempel visar hur man krypterar och lösenordsskyddar en excel-fil med Aspose.Cells API.

**C#**

{{< highlight "csharp" >}}

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
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
