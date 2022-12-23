---
title: Kryptera Excel-filer
type: docs
weight: 90
url: /sv/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) gör att du kan kryptera och lösenordsskydda dina kalkylblad. Den använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är 'Office 97/2000 Compatible' eller 'Weak Encryption (XOR)'. Det är viktigt att välja rätt längd på krypteringsnyckeln. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller CSP:er som också erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning är 128-bitars kryptering vad banker använder för att kryptera anslutningen till sina Internetbanksystem.

Aspose.Cells låter dig kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}}

## **Använder Microsoft Excel**

Så här ställer du in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1.  Från**Verktyg** menyn, välj**alternativ**En dialogruta visas.
1.  Välj**säkerhet** flik.
1.  Ange ett lösenord och klicka**Avancerad**
1. Välj krypteringstyp och bekräfta lösenordet.

## **Kryptering med Aspose.Cells**

Följande exempel visar hur man krypterar och lösenordsskyddar en excel-fil med Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Ange lösenord för att ändra Alternativ**

 Följande exempel visar hur du ställer in**Lösenord att ändra** Microsoft Excel-alternativ för en befintlig fil med Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Verifiera lösenordet för den krypterade filen**

 För att verifiera lösenordet för den krypterade filen tillhandahåller Aspose.Cells for .NET[**Verifiera lösenord**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) metod. Dessa metoder accepterar två parametrar, filströmmen och lösenordet som måste verifieras.
 Följande kodavsnitt visar användningen av[**Verifiera lösenord**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) metod för att verifiera om det angivna lösenordet är giltigt eller inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Kryptering/Dekryptering av ODS-fil med Aspose.Cells**

Aspose.Cells gör det möjligt att kryptera och dekryptera ODS-filen. Dekrypterad ODS-fil kan öppnas både i Excel och OpenOffice, men krypterad ODS-fil kan endast öppnas av OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan ge ett varningsmeddelande. Krypteringsalternativen är inte tillämpliga för ODS-fil till skillnad från andra filtyper. För att kryptera en ODS-fil, ladda filen och ställ in[**Arbetsbok Inställningar. Lösenord**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) värde till det faktiska lösenordet innan du sparar det. Den utdatakrypterade ODS-filen kan endast öppnas i OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 För att dekryptera en ODS-fil, ladda filen genom att ange ett lösenord i[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . När filen är laddad, ställ in[**Arbetsbok Inställningar. Lösenord**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) sträng till null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
