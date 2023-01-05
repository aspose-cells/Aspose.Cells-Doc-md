---
title: Uppdatera referenser i andra kalkylblad samtidigt som du tar bort tomma kolumner och rader i ett kalkylblad
type: docs
weight: 700
url: /sv/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}} 

 När du tar bort tomma kolumner och rader i ett kalkylblad blir dess referenser i andra kalkylblad ogiltiga. Om du vill undvika detta beteende och vill att dessa referenser också ska uppdateras, använd vänligen[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) och ställ in den**Sann**.

{{% /alert %}} 
## **Uppdatera referenser i andra kalkylblad samtidigt som du tar bort tomma kolumner och rader i ett kalkylblad**
 Se följande exempelkod och dess konsolutgång. Cellen E3 i det andra kalkylbladet har en formel =Sheet1!C3 som hänvisar till cell C3 i det första kalkylbladet. Om du vill ställa in[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) egendom som**Sann** , kommer denna formel att uppdateras och bli =Sheet1!A1 vid borttagning av tomma kolumner och rader i det första kalkylbladet. Men om du kommer att ställa in[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) egendom som**falsk**, kommer formeln i cell E3 i det andra kalkylbladet att förbli =Sheet1!C3 och blir ogiltig.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Konsolutgång**
Detta är konsolutgången för ovanstående exempelkod när[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) egenskapen har satts som**Sann**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Detta är konsolutgången för ovanstående exempelkod när[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) egenskapen har satts som**falsk**. Som du kan se är formeln i cell E3 i det andra kalkylbladet inte uppdaterad och dess cellvärde är nu 0 istället för 4, vilket är ogiltigt.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
