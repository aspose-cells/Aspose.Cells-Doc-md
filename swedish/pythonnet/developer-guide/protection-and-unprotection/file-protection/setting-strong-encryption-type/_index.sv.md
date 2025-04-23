---
title: Ställa in stark krypteringstyp
type: docs
weight: 60
url: /sv/python-net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) möjliggör kryptering och lösenordsskydd av kalkylblad. Det använder algoritmer som tillhandahålls av en kryptotjänsteleverantör. En kryptotjänsteleverantör (eller CSP) är en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är "Office 97/2000 Compatible". Detta är en CSP med vissa allmänt kända säkerhetsproblem. Kalkylblad som är säkrade med "svag kryptering (XOR)" eller med "Office 97/2000 Compatible"-krypteringstyp kan enkelt knäckas.

För att övervinna detta problem, använd en av de starka krypteringstyper som tillhandahålls av Microsoft Excel. Du kan ändra krypteringstypen till den starkaste tillgängliga CSP. För stark kryptering krävs en miniminyckellängd på 128 bitar, till exempel 'Microsoft Strong Cryptographic Provider'.

Du kan också kryptera och lösenordsskydda Excel-filer med stark krypteringstyp med API:et Aspose.Cells för Python via .NET.

{{% /alert %}} 

## **Tillämpa kryptering med Microsoft Excel**
För att implementera filkryptering i Microsoft Excel (till exempel 2007):

1. Från menyn **Verktyg** väljer du **Alternativ**.
1. Välj fliken **Säkerhet**.
1. Ange ett värde för fältet **Lösenord för att öppna**.
1. Klicka på **Avancerat**.
1. Välj krypteringstyp och bekräfta lösenordet.

## **Tillämpa kryptering med Aspose.Cells**
Kodexemplen nedan tillämpar stark kryptering på en fil och anger ett lösenord.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SettingStrongEncryptionType-1.py" >}}

