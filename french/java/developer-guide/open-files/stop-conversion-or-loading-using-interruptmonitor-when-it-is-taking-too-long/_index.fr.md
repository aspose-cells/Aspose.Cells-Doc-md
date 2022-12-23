---
title: Arrêtez la conversion ou le chargement à l'aide d'InterruptMonitor lorsque cela prend trop de temps
type: docs
weight: 100
url: /fr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d'arrêter la conversion de Workbook en différents formats comme PDF, HTML, etc. en utilisant le[**Moniteur d'interruption**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)objet quand cela prend trop de temps. Le processus de conversion est souvent gourmand en CPU et en mémoire et il est souvent utile de l'arrêter lorsque les ressources sont limitées. Vous pouvez utiliser[**Moniteur d'interruption**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)à la fois pour arrêter la conversion et pour arrêter le chargement d'un énorme classeur. Veuillez utiliser[**Workbook.InterruptMonitorWorkbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)propriété d'arrêter la conversion et[**LoadOptions.InterruptMonitorLoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)propriété pour charger un énorme classeur.

## **Arrêtez la conversion ou le chargement à l'aide d'InterruptMonitor lorsque cela prend trop de temps**

L'exemple de code suivant explique l'utilisation de[**Moniteur d'interruption**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)objet. Le code convertit un fichier Excel assez volumineux en PDF. Cela prendra plusieurs secondes (c'est-à-dire*plus de 30 secondes*) pour le convertir à cause de ces lignes de code.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Comme tu vois**AB1000000**est une cellule assez éloignée dans le fichier XLSX. Cependant, le*WaitForWhileAndThenInterrupt()*La méthode interrompt la conversion après 10 secondes et le programme se termine/se termine. Veuillez utiliser le code suivant pour exécuter l'exemple de code.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
