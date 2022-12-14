---
title: Ändra en befintlig stil
type: docs
weight: 50
url: /sv/java/modify-an-existing-style/
description: Lär dig hur du ändrar stilar i Excel med Microsoft Excel och med Aspose.Cells för Java API.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

Om du vill använda samma formateringsalternativ på celler skapar du ett nytt formateringsobjekt. Ett formateringsstilsobjekt är en kombination av formateringsegenskaper, såsom teckensnitt, teckenstorlek, indrag, nummer, ram, mönster, etc., namngivna och lagrade som en uppsättning. När den tillämpas tillämpas all formatering i den stilen.

Du kan också använda en befintlig stil, spara den med arbetsboken och använda den för att formatera information med samma attribut.

 När celler inte är explicit formaterade,**Vanligt** stil (arbetsbokens standardstil) tillämpas. Microsoft Excel fördefinierar flera stilar utöver den normala stilen inklusive komma, valuta och procent.

Aspose.Cells tillåter modifiering av någon av dessa stilar eller någon annan stil som du definierar med dina önskade attribut.

{{% /alert %}}

## **Använder Microsoft Excel**

Så här uppdaterar du en stil i Microsoft Excel 97-2003:

1.  På**Formatera** menyn, klicka**Stil**.
1.  Välj den stil du vill ändra från**Stilnamn** lista.
1.  Klick**Ändra**.
1. Välj de stilalternativ du vill använda med flikarna i dialogrutan Format Cells.
1.  Klick**OK**.
1.  Under**Stil inkluderar**, ange de stilegenskaper du vill ha.
1.  Klick**OK** för att spara stilen och tillämpa den på det valda intervallet.

## **Använder Aspose.Cells**

 Aspose.Cells tillhandahåller[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) metod för att uppdatera en befintlig stil.

 För att ändra en namngiven stil, oavsett om den är skapad dynamiskt med Aspose.Cells eller fördefinierad, ring[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) metod för att återspegla alla ändringar i stil som tillämpas på en cell eller ett område.

 De[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() )-metoden beter sig som**OK** knapp i dialogrutan Stil: efter att ha gjort ändringar i en befintlig stil, ring för att implementera ändringen. Om du redan har tillämpat en stil på ett cellintervall, ändra stilattributen och anropa metoden, uppdateras formateringen av dessa celler automatiskt

### **Skapa och ändra en stil**

Det här exemplet skapar ett stilobjekt, tillämpar det på ett cellintervall och modifierar stilobjektet. Ändringarna tillämpas automatiskt på cellen och det område som stilen tillämpades på.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Ändra en befintlig stil**

Det här exemplet använder en enkel mall i Excel-fil där en stil som heter Procent redan har tillämpats på ett intervall. Exemplet:

1. får stilen,
1. skapar ett stilobjekt och
1. ändrar stilformateringen.

Ändringarna tillämpas automatiskt på det område som stilen tillämpades på.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
