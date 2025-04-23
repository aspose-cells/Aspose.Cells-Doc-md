---
title: Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro
type: docs
weight: 5000
url: /it/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

Quando elimini colonne e righe vuote in una tabella, i relativi riferimenti in altre tabelle diventano non validi. Se vuoi evitare questo comportamento e vuoi che quei riferimenti della tabella corrente in altre tabelle siano aggiornati, utilizza la proprietà [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) e impostala su **true**.

{{% /alert %}}

## **Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro**

Per favore, guarda il seguente codice di esempio e il suo output sulla console. La cella E3 nella seconda tabella ha una formula =Sheet1!C3 che si riferisce alla cella C3 nella prima tabella. Se imposterai la proprietà [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) su **true**, questa formula verrà aggiornata e diventerà =Sheet1!A1 eliminando colonne e righe vuote nella prima tabella. Tuttavia, se imposterai la proprietà [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) su **false**, la formula nella cella E3 della seconda tabella rimarrà =Sheet1!C3 e diventerà non valida.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Output della console**

Questo è l'output sulla console del codice di esempio sopra quando la proprietà [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) è stata impostata su **true**.

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

Questo è l'output sulla console del codice di esempio sopra quando la proprietà [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) è stata impostata su **false**. Come puoi vedere, la formula nella cella E3 della seconda tabella non viene aggiornata e il suo valore della cella è ora 0 invece di 4, il che è non valido.

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
{{< app/cells/assistant language="csharp" >}}
