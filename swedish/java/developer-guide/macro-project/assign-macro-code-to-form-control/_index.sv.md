---
title: Tilldela makrokod till formulärkontroll
type: docs
weight: 400
url: /sv/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells låter dig tilldela en makrokod till en formulärkontroll som en knapp. Vänligen använd[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) metod för att tilldela en ny makrokod till en formulärkontroll i arbetsboken.

{{% /alert %}} 
## **Tilldela makrokod till formulärkontroll med Aspose.Cells**
Följande exempelkod skapar en ny arbetsbok, tilldelar en makrokod till en formulärknapp och sparar utdata i XLSM-formatet. En gång kommer du att öppna utdatafilen XLSM i Microsoft Excel du kommer att se följande makrokod.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Här är en exempelkod för att generera utdata-XLSM-filen med makrokod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
