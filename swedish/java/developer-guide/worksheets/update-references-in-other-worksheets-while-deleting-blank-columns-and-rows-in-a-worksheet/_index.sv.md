---
title: Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad
type: docs
weight: 700
url: /sv/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

När du tar bort tomma kolumner och rader i ett arbetsblad blir dess referenser i andra arbetsblad ogiltiga. Om du vill undvika detta beteende och vill att de referenserna uppdateras också, använd då [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) och ange det som **true**.

{{% /alert %}} 
## **Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad**
Se följande exempelkod och dess konsolresultat. Cellen E3 i det andra arbetsbladet har en formel =Sheet1!C3 som hänvisar till cellen C3 i det första arbetsbladet. Om du ställer in [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference)egenskapen som **true**, kommer denna formel att uppdateras och bli =Sheet1!A1 vid borttagning av tomma kolumner och rader i det första arbetsbladet. Om du däremot ställer in [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) egenskapen som **false**, kommer formeln i cellen E3 i det andra arbetsbladet att förbli =Sheet1!C3 och bli ogiltig.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Konsoloutput**
Det här är konsolutmatningen av den ovanstående exempelkoden när [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference)egenskapen är inställd som **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Det här är konsolutmatningen av den ovanstående exempelkoden när [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference)egenskapen är inställd som **false**. Som du kan se är formeln i cellen E3 i det andra arbetsbladet inte uppdaterad och dess cellvärde är nu 0 istället för 4, vilket är ogiltigt.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
