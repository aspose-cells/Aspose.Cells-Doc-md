---
title: Kryptering av Excel filer
type: docs
weight: 90
url: /sv/net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) gör det möjligt för dig att kryptera och lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning krypteringsalgoritmer med olika egenskaper. Standard-CSP är 'Kontors 97/2000-kompatibel' eller 'Svag kryptering (XOR)'. Det är viktigt att välja rätt krypteringsnyckellängd. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller också CSP:er som erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning, 128 bitar kryptering är vad banker använder för att kryptera anslutningen med sina internetbankssystem.

Aspose.Cells gör det möjligt för dig att kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}}

## **Använda Microsoft Excel**

För att ställa in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1. Från menyn **Verktyg**, välj **Alternativ**. En dialogruta kommer att visas.
1. Välj fliken **Säkerhet**.
1. Ange ett lösenord och klicka på **Avancerat**
1. Välj krypteringstyp och bekräfta lösenordet.

## **Kryptering med Aspose.Cells**

Exemplet nedan visar hur man krypterar och lösenordsskyddar en Excel-fil med hjälp av Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Ange lösenord för att ändra alternativ**

Följande exempel visar hur man ställer in alternativet **Lösenord för att ändra** i Microsoft Excel för en befintlig fil med hjälp av Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Verifiera lösenordet för den krypterade filen**

För att verifiera lösenordet för den krypterade filen tillhandahåller Aspose.Cells for .NET [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) metoden. Dessa metoder accepterar två parametrar, filströmmen och lösenordet som ska verifieras.
Följande kodavsnitt demonstrerar användningen av metod [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) för att verifiera om det angivna lösenordet är giltigt eller inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Kryptering/Dekryptering av ODS-fil med Aspose.Cells**

Aspose.Cells tillåter att kryptera och dekryptera ODS-fil. Dekrypterad ODS-fil kan öppnas både i Excel och OpenOffice, men krypterad ODS-fil kan endast öppnas av OpenOffice efter att lösenordet har angetts. Excel kan inte öppna den krypterade ODS-filen och kan visa varningsmeddelande. Krypteringsalternativen gäller inte för ODS-fil som för andra filtyper. För att kryptera en ODS-fil laddar du in filen och anger det [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) värde till det faktiska lösenordet innan du sparar den. Den krypterade ODS-filen kan öppnas i OpenOffice endast.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

För att dekryptera en ODS-fil, ladda in filen genom att ange ett lösenord i [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). När filen har laddats, ställ in strängen för [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) till null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
