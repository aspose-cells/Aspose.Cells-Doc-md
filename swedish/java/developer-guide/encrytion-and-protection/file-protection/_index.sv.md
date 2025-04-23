---
title: Kryptera och dekryptera Excel filer
type: docs
weight: 40
url: /sv/java/encrypt-and-decrypt-excel-files/
description: Hur man krypterar och avkrypterar Excelfiler med hjälp av Java. Lås och lås upp Excelfiler.
---

{{% alert color="primary" %}}
Microsoft Excel (97 - 365) gör det möjligt att kryptera/lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av Crypto Service Provider. En Crypto Service Provider eller CSP är en uppsättning kryptografiska algoritmer med olika egenskaper. Standard CSP är "Office 97/2000-kompatibel" eller "Vecka Kryptering (XOR)". Det är också viktigt att välja en lämplig krypteringsnyckellängd. Vissa Crypto Service Providers stöder inte mer än 40 eller 56 bitar. Det anses vara en svag typ av kryptering. Men för stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller Crypto Service Providers som också erbjuder starka typer av kryptering, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge en idé, 128 bits kryptering är vad banker använder för att kryptera anslutningen med sina internetbankssystem. Aspose.Cells låter dig kryptera/lösenordsskydda dina excelfiler med önskad typ av kryptering.

{{% /alert %}}

## **Använda MS Excel**

I MS Excel (t.ex. MS Excel 2003), för att implementera filkrypteringsinställningar kan du försöka:

- Från menyn **Verktyg**, välj **Alternativ**, och välj sedan fliken **Säkerhet**.
- Ange **Lösenord för att öppna** och klicka på **Avancerat**-knappen.
- Välj krypteringstyp och bekräfta lösenordet.

![todo:image_alt_text](encrypting-excel-files_1.png)

**Figur: Dialogrutan Alternativ**

![todo:image_alt_text](encrypting-excel-files_2.png)

**Figur: Dialogrutan Krypteringstyp**

## **Kryptering av Excelfil**
Följande exempel visar hur du kan kryptera/lösenordsskydda en excelfil med hjälp av Aspose.Cells API.

### **Exempelkod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Avkryptering av Excelfil med Aspose.Cells**
Det är väldigt enkelt att öppna ett lösenordsskyddat excelfil och avkryptera det med hjälp av Aspose.Cells API enligt följande koder:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



{{< app/cells/assistant language="java" >}}
