---
title: Ställa in stark krypteringstyp
type: docs
weight: 10
url: /sv/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) gör att du kan kryptera och lösenordsskydda kalkylblad. Den använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör. En kryptografisk tjänsteleverantör (eller CSP) är en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är "Office 97/2000 Compatible". Det här är en CSP med vissa kända säkerhetsproblem. Kalkylblad som är säkrade med "svag kryptering (XOR)" eller med "Office 97/2000-kompatibel" krypteringstyp kan enkelt knäckas.

För att övervinna detta problem, använd en av de starka krypteringstyperna som tillhandahålls av Microsoft Excel. Du kan ändra krypteringstypen till den starkaste tillgängliga CSP. För stark kryptering krävs en miniminyckellängd på 128 bitar, till exempel 'Microsoft Strong Cryptographic Provider'.

Du kan också kryptera och lösenordsskydda Excel-filer med stark krypteringstyp med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Tillämpa kryptering med Microsoft Excel**

För att implementera filkryptering i Microsoft Excel (till exempel 2007):

1. Från menyn **Verktyg** väljer du **Alternativ**.
1. Välj fliken **Säkerhet**.
1. Ange ett värde för fältet **Lösenord för att öppna**.
1. Klicka på **Avancerat**.
1. Välj krypteringstyp och bekräfta lösenordet.

   **Inställning av kryptering i Microsoft Excel**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Tillämpa kryptering med Aspose.Cells**

I kodexemplet nedan tillämpas stark kryptering på en fil och ett lösenord anges.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
