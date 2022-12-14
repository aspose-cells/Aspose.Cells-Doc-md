---
title: Ställa in stark krypteringstyp
type: docs
weight: 10
url: /sv/java/setting-strong-encryption-type/
---
{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) gör att du kan kryptera och lösenordsskydda kalkylblad. Den använder algoritmer som tillhandahålls av en kryptotjänstleverantör. En Crypto Service Provider (eller CSP) är en uppsättning kryptografiska algoritmer med olika egenskaper. Standard CSP är "Office 97/2000 Compatible". Detta är en CSP med några allmänt kända säkerhetsproblem. Kalkylblad som är säkrade med krypteringstypen "svag kryptering (XOR)" eller med "Office 97/2000-kompatibel" krypteringstyp kan lätt knäckas.

För att lösa detta problem, använd en av de starka krypteringstyperna som tillhandahålls av Microsoft Excel. Du kan ändra krypteringstypen till den starkaste tillgängliga CSP. För stark kryptering krävs en minsta nyckellängd på 128 bitar, till exempel "Microsoft Strong Cryptographic Provider".

Du kan också kryptera och lösenordsskydda Excel-filer med stark krypteringstyp med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Tillämpa kryptering med Microsoft Excel**

Så här implementerar du filkryptering i Microsoft Excel (till exempel 2007):

1.  Från**Verktyg** menyn, välj**alternativ**.
1.  Välj**säkerhet** flik.
1.  Ange ett värde för**Lösenord för att öppna** fält.
1.  Klick**Avancerad**.
1. Välj krypteringstyp och bekräfta lösenordet.

   **Ställa in kryptering i Microsoft Excel**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Använder kryptering med Aspose.Cells**

Kodexemplet nedan tillämpar stark kryptering på en fil och anger ett lösenord.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
