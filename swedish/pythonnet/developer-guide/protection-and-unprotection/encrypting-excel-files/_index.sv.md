---
title: Kryptering av Excel filer
type: docs
weight: 90
url: /sv/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) gör det möjligt för dig att kryptera och lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning krypteringsalgoritmer med olika egenskaper. Standard-CSP är 'Kontors 97/2000-kompatibel' eller 'Svag kryptering (XOR)'. Det är viktigt att välja rätt krypteringsnyckellängd. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller också CSP:er som erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning, 128 bitar kryptering är vad banker använder för att kryptera anslutningen med sina internetbankssystem.

Aspose.Cells för Python via .NET tillåter dig att kryptera och lösenordsskydda Microsoft Excel-filer med din önskade krypteringstyp.

{{% /alert %}}

## **Använda Microsoft Excel**

För att ställa in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1. Från menyn **Verktyg**, välj **Alternativ**. En dialogruta kommer att visas.
1. Välj fliken **Säkerhet**.
1. Ange ett lösenord och klicka på **Avancerat**
1. Välj krypteringstyp och bekräfta lösenordet.

## **Kryptering med Aspose.Cells**

Nedan visas ett exempel på hur du krypterar och lösenordsskyddar en Excel-fil med Aspose.Cells för Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Ange lösenord för att ändra alternativ**

Nedan visas ett exempel på hur du ställer in alternativet **Lösenord för att ändra** för en befintlig fil med Aspose.Cells för Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Verifiera lösenordet för den krypterade filen**

För att verifiera lösenordet för den krypterade filen, tillhandahåller Aspose.Cells för Python via .NET metoden [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Dessa metoder accepterar två parametrar, filsströmmar och lösenordet som ska verifieras.
Följande kodavsnitt demonstrerar användningen av metod [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) för att verifiera om det angivna lösenordet är giltigt eller inte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **Kryptering / Avkryptering av ODS-fil**

Aspose.Cells för Python via .NET tillåter att du krypterar och dekrypterar ODS-fil. Dekrypterad ODS-fil kan öppnas både i Excel och OpenOffice, men krypterad ODS-fil kan endast öppnas av OpenOffice efter att ha angett lösenord. Excel kan inte öppna den krypterade ODS-filen och kan ge varningsmeddelande. Krypteringsalternativen gäller inte för ODS-fil, till skillnad från andra filtyper. För att kryptera en ODS-fil, ladda filen och ställ in värdet [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) till det faktiska lösenordet innan du sparar den. Den krypterade ODS-filen kan öppnas i OpenOffice endast.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

För att dekryptera en ODS-fil, ladda in filen genom att ange ett lösenord i [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). När filen har laddats, ställ in strängen för [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) till null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

