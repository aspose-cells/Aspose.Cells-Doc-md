---
title: Kryptera Excel-filer med Aspose.Cells
type: docs
weight: 30
url: /sv/net/encrypting-excel-files-using-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) gör att du kan kryptera och lösenordsskydda dina kalkylblad. Den använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är 'Office 97/2000 Compatible' eller 'Weak Encryption (XOR)'. Det är viktigt att välja rätt längd på krypteringsnyckeln. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara en svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller CSP:er som också erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning är 128-bitars kryptering vad banker använder för att kryptera anslutningen till sina Internetbanksystem.

Aspose.Cells låter dig kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}} 
## **Använder Microsoft Excel**
Så här ställer du in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1.  Från**Verktyg** menyn, välj**alternativ**.
 En dialogruta visas.
1.  Välj**säkerhet** flik.
1.  Ange ett lösenord och klicka**Avancerad** 
   **Dialogrutan Alternativ** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_1.png)




1.  Välj krypteringstyp och bekräfta lösenordet.

   **Dialogrutan Krypteringstyp** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_2.png)



## **Kryptering med Aspose.Cells**
Följande exempel visar hur man krypterar och lösenordsskyddar en excel-fil med Aspose.Cells API.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string srcFileName = FilePath + "Encrypting Excel Files.xlsx";

string destFileName = FilePath + "Result Encrypting Excel Files.xlsx";

//Open an excel file.

Workbook workbook = new Workbook(srcFileName);

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save(destFileName);

{{< /highlight >}}
## **Ladda ner Running Code**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **Ladda ner provkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

