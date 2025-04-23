---
title: Tilldela makrokod till formulärkontroll
type: docs
weight: 400
url: /sv/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells tillåter att du tilldelar en makkod till ett formulärkontroll som en knapp. Använd metoden [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-) för att tilldela en ny makkod till en formulärkontroll i arbetsboken.

{{% /alert %}} 
## **Tilldela makrokod till formulärkontroll med hjälp av Aspose.Cells**
Följande exempelkod skapar en ny arbetsbok, tilldelar en makrokod till en formulärknapp och sparar utdata i XLSM-formatet. När du sedan öppnar utdatafilen XLSM i Microsoft Excel kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Här är exempelkod för att generera utdatafilen XLSM med makrokod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
{{< app/cells/assistant language="java" >}}
