---
title: Modifiera en befintlig stil med Golang via C++
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som tillåter användare att modifiera befintliga cellstilar. Denna artikel introducerar hur man ändrar en befintlig cellstil med Aspose.Cells biblioteket så att användare kan ändra utseendet på cellerna efter behov.
keywords: Modifiera befintliga stilar, anpassa utseendet på din applikation, guider, handledningar, hjälpdokumentation, utvecklingsdokumentation, API referenser, exempelkod, nedladdningar, support.
type: docs
weight: 90
url: /sv/go-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

För att tillämpa samma formatering på celler, skapa ett ny formateringsstilobjekt. Ett formateringsstilobjekt är en kombination av formateringsegenskaper, såsom font, fontstorlek, indragning, nummer, kant, mönster etc., namngivet och lagrat som en uppsättning. När den appliceras tillämpas alla formatmallar i den stilen.

Du kan också använda en befintlig stil, spara den med arbetsboken och använda den för att formatera information med samma attribut.

När celler inte är explicit formaterade, tillämpas den **Normal** stilen (arbetsbokens standardstil). Microsoft Excel fördefinierar flera stilar förutom Normal-stilen, inklusive Komma, Valuta och Procent.

Aspose.Cells tillåter att modifiera någon av dessa stilar eller någon annan stil som du definierar med önskade attribut.

{{% /alert %}}

## **Använda Microsoft Excel**

För att uppdatera en stil i Microsoft Excel 97-2003:

1. På **Format**-menyn, klicka på **Stil**.
1. Välj den stil du vill modifiera från listan över **Stilnamn**.
1. Klicka på **Ändra**.
1. Välj de stilalternativ du vill använda med flikarna i dialogrutan Formatcells.
1. Klicka på **OK**.
1. Under **Stilen innehåller**, ange stilfunktionerna du vill använda.
1. Klicka på **OK** för att spara stilen och tillämpa den på det valda området.

## **Använda Aspose.Cells**

Följande exempel visar hur man använder [**Style.Update**](https://reference.aspose.com/cells/go-cpp/style/update/)-metoden.

### **Skapa och modifiera en stil**

Detta exempel skapar ett [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-objekt, tillämpar det på ett cellområde och modifierar [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-objektet. Ändringarna tillämpas automatiskt på cellen och det område där stilen användes.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ModifyAnExistingStyle.go" >}}
### **Modifiera en befintlig stil**

Detta exempel använder en enkel mall Excel-fil där en stil som heter Procent redan har tillämpats på en omfattning. Exemplet:

1. hämtar stilen,
1. skapar en stilobjekt och
1. modifierar stilformatering.

Modifieringarna tillämpas automatiskt på området där stilen applicerades.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ModifyAnExistingStyle-1.go" >}}
