---
title: Kryptera och dekryptera Excel filer
type: docs
weight: 10
url: /sv/net/encrypt-and-decrypt-excel-files/
description: Hur man krypterar och dekrypterar excel filer med C#. Lås och lås upp Excel filer.
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

## **Kryptera Excel-fil med Aspose.Cells**

Exemplet nedan visar hur man krypterar och lösenordsskyddar en Excel-fil med hjälp av Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Ange lösenord för att ändra alternativ**

Följande exempel visar hur man ställer in alternativet **Lösenord för att ändra** i Microsoft Excel för en befintlig fil med hjälp av Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Avkryptering av Excelfil med Aspose.Cells**
Det är väldigt enkelt att öppna ett lösenordsskyddat excelfil och avkryptera det med hjälp av Aspose.Cells API enligt följande koder:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Fortsatta ämnen**
- [Kryptera och dekryptera ODS-filer](/cells/sv/net/encrypt-and-decrypt-ods-files/)
- [Ange stark krypterings typ](/cells/sv/net/setting-strong-encryption-type/)
- [Ange författare vid skrivskydd av arbetsbok](/cells/sv/net/specify-author-while-write-protecting-workbook/)
- [Verifiera lösenord för krypterade filer](/cells/sv/net/verify-password-of-encrypted-excel-and-ods-files/)

