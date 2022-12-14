---
title: Ändra en befintlig stil
type: docs
weight: 90
url: /sv/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Om du vill använda samma formateringsalternativ på celler skapar du ett nytt formateringsobjekt. Ett formateringsstilsobjekt är en kombination av formateringsegenskaper, såsom teckensnitt, teckenstorlek, indrag, nummer, kantlinje, mönster etc., namngivna och lagrade som en uppsättning. När den tillämpas tillämpas all formatering i den stilen.

Du kan också använda en befintlig stil, spara den med arbetsboken och använda för att formatera information med samma attribut.

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

 Följande exempel visar hur man använder[**Style.Update**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)metod.

### **Skapa och ändra en stil**

 Detta exempel skapar en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt, tillämpar det på ett cellintervall och ändrar[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objekt. Ändringarna tillämpas automatiskt på cellen och det område som stilen tillämpades på.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Ändra en befintlig stil**

Det här exemplet använder en enkel mall i Excel-fil där en stil som heter Procent redan har tillämpats på ett intervall. Exemplet:

1. får stilen,
1. skapar ett stilobjekt och
1. ändrar stilformateringen.

Ändringarna tillämpas automatiskt på det område som stilen tillämpades på.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
