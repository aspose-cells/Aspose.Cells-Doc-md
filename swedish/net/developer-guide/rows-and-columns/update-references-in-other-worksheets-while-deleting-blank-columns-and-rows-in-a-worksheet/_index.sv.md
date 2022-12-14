---
title: Uppdatera referenser i andra kalkylblad samtidigt som du tar bort tomma kolumner och rader i ett kalkylblad
type: docs
weight: 5000
url: /sv/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}}

 När du tar bort tomma kolumner och rader i ett kalkylblad blir dess referenser i andra kalkylblad ogiltiga. Om du vill undvika detta beteende och vill att referenserna till det aktuella kalkylbladet i andra kalkylblad också uppdateras, använd då[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egenskap och ställ in den på**Sann**.

{{% /alert %}}

## **Uppdatera referenser i andra kalkylblad samtidigt som du tar bort tomma kolumner och rader i ett kalkylblad**

 Se följande exempelkod och dess konsolutgång. Cellen E3 i det andra kalkylbladet har en formel =Sheet1!C3 som hänvisar till cell C3 i det första kalkylbladet. Om du vill ställa in[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egendom som**Sann** , kommer denna formel att uppdateras och bli =Sheet1!A1 vid borttagning av tomma kolumner och rader i det första kalkylbladet. Men om du kommer att ställa in[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egendom som**falsk**, kommer formeln i cell E3 i det andra kalkylbladet att förbli =Sheet1!C3 och blir ogiltig.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Konsolutgång**

 Detta är konsolutgången för ovanstående exempelkod när[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egenskapen har satts som**Sann**.

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

 Detta är konsolutgången för ovanstående exempelkod när[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egenskapen har satts som**falsk**. Som du kan se är formeln i cell E3 i det andra kalkylbladet inte uppdaterad och dess cellvärde är nu 0 istället för 4, vilket är ogiltigt.

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
