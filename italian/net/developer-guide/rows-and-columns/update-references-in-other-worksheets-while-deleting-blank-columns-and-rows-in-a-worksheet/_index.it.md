---
title: Aggiorna i riferimenti in altri fogli di lavoro eliminando colonne e righe vuote in un foglio di lavoro
type: docs
weight: 5000
url: /it/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}}

Quando elimini colonne e righe vuote in un foglio di lavoro, i suoi riferimenti in altri fogli di lavoro diventano non validi. Se si desidera evitare questo comportamento e si desidera aggiornare anche i riferimenti del foglio di lavoro corrente in altri fogli di lavoro, utilizzare il[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) proprietà e impostarlo su**VERO**.

{{% /alert %}}

## **Aggiorna i riferimenti in altri fogli di lavoro eliminando colonne e righe vuote in un foglio di lavoro**

 Consultare il seguente codice di esempio e il relativo output della console. La cella E3 nel secondo foglio di lavoro ha una formula =Foglio1!C3 che fa riferimento alla cella C3 nel primo foglio di lavoro. Se metterai[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) proprietà come**VERO** , questa formula verrà aggiornata e diventerà =Foglio1!A1 eliminando colonne e righe vuote nel primo foglio di lavoro. Tuttavia, se imposterai[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) proprietà come**falso**, la formula nella cella E3 del secondo foglio di lavoro rimarrà =Foglio1!C3 e non sarà più valida.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Uscita console**

 Questo è l'output della console del codice di esempio precedente when[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) proprietà è stata impostata come**VERO**.

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

 Questo è l'output della console del codice di esempio precedente when[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) proprietà è stata impostata come**falso**. Come puoi vedere, la formula nella cella E3 del secondo foglio di lavoro non viene aggiornata e il suo valore di cella ora è 0 invece di 4 che non è valido.

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
