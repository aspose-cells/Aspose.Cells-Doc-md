---
title: Arbeitsblätter entfernen
type: docs
weight: 30
url: /de/net/remove-worksheets/
---
{{% alert color="primary" %}} 

Dieses Thema enthält Informationen zum Entfernen von Arbeitsblättern aus Microsoft Excel-Dateien mithilfe von Aspose.Cells.GridWeb API. Es ist möglich, ein Arbeitsblatt entweder durch Angabe seines Blattindex oder -namens zu entfernen.

{{% /alert %}} 
## **Entfernen eines Arbeitsblatts**
### **Blattindex verwenden**
Der folgende Code zeigt, wie ein Arbeitsblatt entfernt wird, indem sein Blattindex in der RemoveAt-Methode der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **Blattname verwenden**
Der folgende Code zeigt, wie ein Arbeitsblatt entfernt wird, indem sein Blattname in der RemoveAt-Methode der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

Es ist auch möglich, ein Arbeitsblatt anhand seiner Referenz oder Instanz zu entfernen. Verwenden Sie dazu die Remove-Methode der GridWorksheetCollection. Dieser Ansatz wird häufig verwendet.

{{% /alert %}}
