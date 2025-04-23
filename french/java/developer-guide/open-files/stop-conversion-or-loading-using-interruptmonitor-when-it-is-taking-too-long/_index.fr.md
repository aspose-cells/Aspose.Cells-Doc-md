---
title: Arrêter la conversion ou le chargement à l aide d InterruptMonitor lorsqu elle prend trop de temps
type: docs
weight: 100
url: /fr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d'arrêter la conversion du classeur dans divers formats tels que PDF, HTML, etc. en utilisant l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) lorsque cela prend trop de temps. Le processus de conversion est souvent intensif en CPU et en mémoire et il est souvent utile de l'arrêter lorsque les ressources sont limitées. Vous pouvez utiliser [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) pour arrêter à la fois la conversion et le chargement d'un classeur volumineux. Veuillez utiliser la propriété [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor) pour arrêter la conversion et la propriété [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor) pour charger un classeur volumineux.

## **Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps**

Le code d'échantillon suivant explique l'utilisation de l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor). Le code convertit un fichier Excel assez volumineux en PDF. Cela prendra plusieurs secondes (c'est-à-dire *plus de 30 secondes*) pour le convertir en raison de ces lignes de code.

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Comme vous le voyez, **AB1000000** est une cellule assez éloignée dans le fichier XLSX. Cependant, la méthode *WaitForWhileAndThenInterrupt()* interrompt la conversion après 10 secondes et le programme se termine/se ferme. Veuillez utiliser le code suivant pour exécuter le code d'échantillon.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
{{< app/cells/assistant language="java" >}}
