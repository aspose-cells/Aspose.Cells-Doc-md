---
title: Arrêter la conversion ou le chargement à l aide d InterruptMonitor lorsqu elle prend trop de temps
type: docs
weight: 100
url: /fr/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d'arrêter la conversion du classeur à divers formats tels que PDF, HTML, etc. en utilisant l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) lorsqu'elle prend trop de temps. Le processus de conversion est souvent intensif en CPU et en mémoire, et il est souvent utile de l'arrêter lorsque les ressources sont limitées. Vous pouvez utiliser [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) à la fois pour arrêter la conversion et pour arrêter le chargement d'un gros classeur. Veuillez utiliser la propriété [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) pour arrêter la conversion et la propriété [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) pour charger un gros classeur.

## **Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps**

Le code d'exemple suivant explique l'utilisation de l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor). Le code convertit un fichier Excel assez volumineux en PDF. Cela prendra plusieurs secondes (c'est-à-dire *plus de 30 secondes*) pour le convertir en raison de ces lignes de code.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

Comme vous pouvez le constater, **J1000000** est une cellule assez éloignée dans le fichier XLSX. Cependant, la méthode **WaitForWhileAndThenInterrupt()** interrompt la conversion après 10 secondes et le programme se termine/se termine. Veuillez utiliser le code suivant pour exécuter le code d'exemple.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
