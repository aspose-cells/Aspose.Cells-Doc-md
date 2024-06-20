---
title: Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro
type: docs
weight: 700
url: /it/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

Quando elimini colonne e righe vuote in un foglio di lavoro, i relativi riferimenti in altri fogli di lavoro diventano non validi. Se vuoi evitare questo comportamento e vuoi che tali riferimenti vengano aggiornati, ti preghiamo di utilizzare il [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) e impostarlo su **true**.

{{% /alert %}} 
## **Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro**
Si prega di visionare il codice di esempio seguente e la relativa output della console. La cella E3 nel secondo foglio di lavoro ha una formula =Foglio1!C3 che si riferisce alla cella C3 nel primo foglio di lavoro. Se imposterai la proprietà [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) su **true**, questa formula verrà aggiornata e diventerà =Sheet1!A1 eliminando colonne e righe vuote nel primo foglio di lavoro. Tuttavia, se imposterai la proprietà [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) su **false**, la formula nella cella E3 del secondo foglio di lavoro rimarrà =Foglio1!C3 e diventerà non valida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Output della console**
Questo è l'output della console del codice di esempio sopra quando la proprietà [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) è stata impostata su **true**.

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

Questo è l'output della console del codice di esempio sopra quando la proprietà [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) è stata impostata su **false**. Come puoi vedere, la formula nella cella E3 del secondo foglio di lavoro non è stata aggiornata e il suo valore è ora 0 invece di 4, il che è non valido.

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
