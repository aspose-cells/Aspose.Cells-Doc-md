---
title: Kryptera och dekryptera Excel filer
type: docs
weight: 10
url: /sv/python-net/encrypt-and-decrypt-excel-files/
description: Hur man krypterar och dekrypterar Excel filer med hjälp av Python. Lås och lås upp Excel filer.
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

## **Kryptera Excel-fil med Aspose.Cells**

Nedan visas ett exempel på hur du krypterar och lösenordsskyddar en Excel-fil med Aspose.Cells för Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Ange lösenord för att ändra alternativ**

Nedan visas ett exempel på hur du ställer in alternativet **Lösenord för att ändra** för en befintlig fil med Aspose.Cells för Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}


## **Avkryptering av Excelfil med Aspose.Cells**
Det är mycket enkelt att öppna lösenordsskyddad Excel-fil och dekryptera med Aspose.Cells för Python via .NET API enligt följande koder:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-Decrypt-Excel-File.py" >}}


## **Fortsatta ämnen**
- [Kryptera och dekryptera ODS-filer](/cells/sv/python-net/encrypt-and-decrypt-ods-files/)
- [Ange stark krypterings typ](/cells/sv/python-net/setting-strong-encryption-type/)
- [Ange författare vid skrivskydd av arbetsbok](/cells/sv/python-net/specify-author-while-write-protecting-workbook/)
- [Verifiera lösenord för krypterade filer](/cells/sv/python-net/verify-password-of-encrypted-excel-and-ods-files/)

