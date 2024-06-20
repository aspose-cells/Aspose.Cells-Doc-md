---
title: Ein Arbeitsblatt entfernen
type: docs
weight: 30
url: /de/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop,remove,worksheet
description: Dieser Artikel zeigt, wie man ein Arbeitsblatt in GridDesktop entfernt.
---

{{% alert color="primary" %}} 

In diesem Artikel wird erörtert, wie Arbeitsblätter mithilfe der Aspose.Cells.GridDesktop-Steuerung entfernt werden können. Es gibt einige einfache Ansätze, um diese grundlegende Aufgabe zu erledigen.

{{% /alert %}} 
## **Arbeitsblatt entfernen**
Um ein Arbeitsblatt unter Verwendung der Aspose.Cells.GridDesktop-Steuerung zu entfernen, befolgen Sie bitte die untenstehenden Schritte:

1. Fügen Sie der Form die Aspose.Cells.GridDesktop-Steuerung hinzu.
1. Rufen Sie die Remove-Methode der Arbeitsblattkollektion in der GridDesktop-Steuerung auf.
### **Verwendung des Arbeitsblattindexes**
In diesem Ansatz geben Sie einfach den Arbeitsblattindex (in der Arbeitsblattkollektion des Rasters) des zu entfernenden Arbeitsblatts an.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Verwendung des Arbeitsblattnamens**
Wenn der Name des Arbeitsblatts bekannt ist, ist es möglich, ein bestimmtes Arbeitsblatt zu entfernen, indem sein Name angegeben wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Remove ist eine Methode. Verwenden Sie sie, um ein Arbeitsblatt über seinen Index (in der Arbeitsblattkollektion) zu entfernen oder verwenden Sie die RemoveAt-Methode, um das Arbeitsblatt über seinen Index/Name zu entfernen.

{{% /alert %}}
