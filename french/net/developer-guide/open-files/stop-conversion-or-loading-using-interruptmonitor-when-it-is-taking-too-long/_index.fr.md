---
title: Arrêtez la conversion ou le chargement à l'aide d'InterruptMonitor lorsque cela prend trop de temps
type: docs
weight: 100
url: /fr/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d'arrêter la conversion de Workbook en différents formats comme PDF, HTML etc. en utilisant le[**Moniteur d'interruption**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) objet quand cela prend trop de temps. Le processus de conversion est souvent gourmand en CPU et en mémoire et il est souvent utile de l'arrêter lorsque les ressources sont limitées. Vous pouvez utiliser[**Moniteur d'interruption**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)à la fois pour arrêter la conversion et pour arrêter le chargement d'un énorme classeur. Veuillez utiliser[**Workbook.InterruptMonitorWorkbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) propriété d'arrêter la conversion et[**LoadOptions.InterruptMonitorLoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) propriété pour charger un énorme classeur.

## **Arrêtez la conversion ou le chargement à l'aide d'InterruptMonitor lorsque cela prend trop de temps**

L'exemple de code suivant explique l'utilisation de[**Moniteur d'interruption**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) objet. Le code convertit un fichier Excel assez volumineux en PDF. Cela prendra plusieurs secondes (c'est-à-dire*plus de 30 secondes*) pour le convertir à cause de ces lignes de code.

{{< highlight "csharp" >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

 Comme tu vois**J1000000** est une cellule assez éloignée dans le fichier XLSX. Cependant, le**WaitForWhileAndThenInterrupt()**La méthode interrompt la conversion après 10 secondes et le programme se termine/se termine. Veuillez utiliser le code suivant pour exécuter l'exemple de code.

{{< highlight "csharp" >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
