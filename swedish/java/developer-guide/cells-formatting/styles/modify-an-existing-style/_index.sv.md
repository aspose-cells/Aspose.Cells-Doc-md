---
title: Modifiera en befintlig stil
type: docs
weight: 50
url: /sv/java/modify-an-existing-style/
description: Lär dig hur man ändrar stilar i Excel med Microsoft Excel och med Aspose.Cells for Java API.
keywords: ändra en befintlig stil i excel, ändra en befintlig stil i excel java, ändra befintlig stil i excel, ändra befintlig stil i excel java, ändra befintlig stil i excel, ändra befintlig stil i excel java, hur man ändrar stil i excel, hur man ändrar stil i excel med java, hur man ändrar stil i excel med java, hur man ändrar stil i excel med java, ändra befintlig stil i excel java, ändra befintlig stil i excel
---

{{% alert color="primary" %}}

För att tillämpa samma formateringsalternativ på celler, skapa ett nytt formateringsstilobjekt. Ett formateringsstilobjekt är en kombination av formateringsegenskaper, såsom teckensnitt, teckenstorlek, indrag, nummer, kant, mönster etc., namngiven och lagrad som en uppsättning. När den tillämpas, tillämpas all formatering i den stilen.

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

Aspose.Cells tillhandahåller [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) metoden för att uppdatera en befintlig stil.

För att ändra en namngiven stil, antingen skapad dynamiskt med hjälp av Aspose.Cells eller fördefinierad, anropar du [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--)-metoden för att återspegla eventuella ändringar i stilen som tillämpas på en cell eller ett område.

[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--)-metoden fungerar som knappen **OK** i Stil-dialogrutan: efter att ha gjort ändringar i en befintlig stil, anropa för att implementera ändringen. Om du redan har tillämpat en stil på ett cellområde, ändra stilattributen och anropa metoden, uppdateras formateringen av dessa celler automatiskt

### **Skapa och modifiera en stil**

Detta exempel skapar en stilobjekt, tillämpar den på ett cellområde och modifierar stilobjektet. Ändringarna tillämpas automatiskt på cellen och området som stilen tillämpades på.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modifiera en befintlig stil**

Detta exempel använder en enkel mall Excel-fil där en stil som heter Procent redan har tillämpats på en omfattning. Exemplet:

1. hämtar stilen,
1. skapar en stilobjekt och
1. modifierar stilformatering.

Modifieringarna tillämpas automatiskt på området där stilen applicerades.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
