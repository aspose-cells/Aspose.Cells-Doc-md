---
title: Kryptera och dekryptera Excel-filer
type: docs
weight: 10
url: /sv/python-java/encrypt-and-decrypt-excel-files/
description: Hur man krypterar och dekrypterar Excel-filer med Python. Lås och lås upp Excel-filer.
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) gör att du kan kryptera och lösenordsskydda dina kalkylblad. Den använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är 'Office 97/2000 Compatible' eller 'Weak Encryption (XOR)'. Det är viktigt att välja rätt längd på krypteringsnyckeln. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller CSP:er som också erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning är 128-bitars kryptering vad banker använder för att kryptera anslutningen till sina Internetbanksystem.

Aspose.Cells for Python låter dig kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}}

## **Använder Microsoft Excel**

Så här ställer du in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1.  Från**Verktyg** menyn, välj**alternativ**En dialogruta visas.
1.  Välj**säkerhet** flik.
1.  Ange ett lösenord och klicka**Avancerad**
1. Välj krypteringstyp och bekräfta lösenordet.

## **Krypterar Excel-fil med Aspose.Cells**

Följande exempel visar hur man krypterar och lösenordsskyddar en excel-fil med Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **Dekrypterar Excel-fil med Aspose.Cells**
Det är mycket att öppna lösenordsskyddad excel-fil och dekryptera med Aspose.Cells API som följande koder:

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


