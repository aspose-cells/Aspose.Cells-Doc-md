---
title: Kryptera och dekryptera Excel-filer
type: docs
weight: 40
url: /sv/java/encrypt-and-decrypt-excel-files/
description: Hur man krypterar och dekrypterar Excel-filer med java. Lås och lås upp Excel-filer.
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365) gör att du kan kryptera / lösenordsskydda dina kalkylblad. Den använder algoritmer från Crypto Service Provider. En kryptotjänstleverantör eller CSP är en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är "Office 97/2000 Compatible" eller " Week Encryption (XOR) ". Det är också viktigt att välja en korrekt krypteringsnyckellängd. Vissa av kryptotjänsteleverantörerna stöder inte mer än 40 eller 56 bitar. Det anses vara en svag krypteringstyp. Men för stark krypteringstyp krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller Crypto Service Providers som erbjuder starka krypteringstyper också, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge en uppfattning är 128-bitars kryptering vad banker använder för att kryptera anslutningen med sina Internetbanksystem. Aspose.Cells låter dig kryptera / lösenordsskydda dina Excel-filer med önskad krypteringstyp.

{{% /alert %}}

## **Använder MS Excel**

I MS Excel (t.ex. MS Excel 2003), för att implementera filkrypteringsinställningar, kan du försöka:

-  Från**Verktyg** menyn, välj**alternativ** och välj sedan**säkerhet** flik.
-  Inmatning**Lösenord för att öppna** och klicka på**Avancerad** knapp.
- Välj krypteringstyp och bekräfta lösenordet.

![todo:image_alt_text](encrypting-excel-files_1.png)

**Bild: Dialogrutan Alternativ**

![todo:image_alt_text](encrypting-excel-files_2.png)

**Bild: Dialogrutan Krypteringstyp**

## **Krypterar Excel-fil**
Följande exempel visar hur du kan kryptera / lösenordsskydda en Excel-fil med hjälp av Aspose.Cells API.

### **Exempelkod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Dekrypterar Excel-fil med Aspose.Cells**
Det är mycket att öppna lösenordsskyddad excel-fil och dekryptera med Aspose.Cells API som följande koder:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



