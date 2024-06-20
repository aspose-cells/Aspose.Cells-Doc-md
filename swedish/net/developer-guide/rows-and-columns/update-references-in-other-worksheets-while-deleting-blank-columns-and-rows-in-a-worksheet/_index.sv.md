---
title: Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad
type: docs
weight: 5000
url: /sv/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

När du tar bort tomma kolumner och rader i en arbetsbok blir dess hänvisningar i andra arbetsblad ogiltiga. Om du vill undvika detta beteende och vill att hänvisningarna från det nuvarande arbetsbladet i andra arbetsblad också uppdateras, använd sedan egenskapen [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) och sätt den till **true**.

{{% /alert %}}

## **Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad**

Vänligen se följande exempelkod och dess konsolresultat. Cell E3 i det andra arbetsbladet har en formel =Sheet1!C3 som hänvisar till cell C3 i det första arbetsbladet. Om du ställer in [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egenskapen som **true**, kommer denna formel att uppdateras och bli =Sheet1!A1 när du tar bort tomma kolumner och rader i det första arbetsbladet. Om du däremot ställer in [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egenskapen som **false**, kommer formeln i cell E3 i det andra arbetsbladet att förbli =Sheet1!C3 och bli ogiltig.

### **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Konsoloutput**

Detta är konsolresultatet av ovanstående exempelkod när [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egenskapen har ställts in som **true**.

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

Detta är konsolresultatet av ovanstående exempelkod när [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) egenskapen har ställts in som **false**. Som du kan se har formeln i cell E3 på det andra arbetsbladet inte uppdaterats och dess cellvärde är nu 0 istället för 4, vilket är ogiltigt.

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
