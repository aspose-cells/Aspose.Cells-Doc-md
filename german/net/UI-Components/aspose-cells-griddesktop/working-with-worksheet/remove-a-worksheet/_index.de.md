---
title: Entfernen Sie ein Arbeitsblatt
type: docs
weight: 30
url: /de/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

In diesem Thema wird das Entfernen von Arbeitsblättern mit dem Aspose.Cells.GridDesktop-Steuerelement erläutert. Es gibt ein paar einfache Ansätze, um diese grundlegende Aufgabe zu erfüllen.

{{% /alert %}} 
## **Entfernen eines Arbeitsblatts**
Um ein Arbeitsblatt mit dem Aspose.Cells.GridDesktop-Steuerelement zu entfernen, führen Sie bitte die folgenden Schritte aus:

1. Fügen Sie einem Formular das Aspose.Cells.GridDesktop-Steuerelement hinzu.
1. Rufen Sie die Remove-Methode der Worksheets-Auflistung im GridDesktop-Steuerelement auf.
### **Verwenden des Arbeitsblattindex**
Übergeben Sie bei diesem Ansatz einfach den Arbeitsblattindex (in der Arbeitsblattsammlung des Rasters) des zu entfernenden Arbeitsblatts.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Verwenden des Arbeitsblattnamens**
Wenn der Name des Arbeitsblatts bekannt ist, ist es möglich, ein bestimmtes Arbeitsblatt zu entfernen, indem Sie seinen Namen angeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Entfernen ist eine Methode. Verwenden Sie es, um ein Arbeitsblatt mithilfe seines Index (in der Arbeitsblattsammlung) zu entfernen, oder verwenden Sie die RemoveAt-Methode, um das Arbeitsblatt mithilfe seines Index/Namens zu entfernen.

{{% /alert %}}
