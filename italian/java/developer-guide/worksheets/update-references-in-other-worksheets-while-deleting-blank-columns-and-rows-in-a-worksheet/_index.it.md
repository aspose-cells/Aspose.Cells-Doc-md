---
title: Aggiorna i riferimenti in altri fogli di lavoro eliminando colonne e righe vuote in un foglio di lavoro
type: docs
weight: 700
url: /it/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Quando elimini colonne e righe vuote in un foglio di lavoro, i suoi riferimenti in altri fogli di lavoro diventano non validi. Se vuoi evitare questo comportamento e vuoi che anche quei riferimenti vengano aggiornati, usa il file[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) e impostalo**VERO**.

{{% /alert %}} 
## **Aggiorna i riferimenti in altri fogli di lavoro eliminando colonne e righe vuote in un foglio di lavoro**
 Consultare il seguente codice di esempio e il relativo output della console. La cella E3 nel secondo foglio di lavoro ha una formula =Foglio1!C3 che fa riferimento alla cella C3 nel primo foglio di lavoro. Se metterai[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) proprietà come**VERO** , questa formula verrà aggiornata e diventerà =Foglio1!A1 eliminando colonne e righe vuote nel primo foglio di lavoro. Tuttavia, se imposterai[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) proprietà come**falso**, la formula nella cella E3 del secondo foglio di lavoro rimarrà =Foglio1!C3 e non sarà più valida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Uscita console**
Questo è l'output della console del codice di esempio precedente when[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) proprietà è stata impostata come**VERO**.

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

Questo è l'output della console del codice di esempio precedente when[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) proprietà è stata impostata come**falso**. Come puoi vedere, la formula nella cella E3 del secondo foglio di lavoro non viene aggiornata e il suo valore di cella ora è 0 invece di 4 che non è valido.

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
