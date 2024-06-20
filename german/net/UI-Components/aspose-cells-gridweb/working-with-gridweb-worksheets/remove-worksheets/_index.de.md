---
title: Arbeitsblätter entfernen
type: docs
weight: 30
url: /de/net/aspose-cells-gridweb/remove-worksheets/
keywords: GridWeb, entfernen, GridWorksheet entfernen, Arbeitsblatt entfernen
description: Dieser Artikel zeigt, wie ein Arbeitsblatt (GridWorksheet) in GridWeb entfernt wird.
---

{{% alert color="primary" %}} 

In diesem Thema wird beschrieben, wie Arbeitsblätter aus Microsoft Excel-Dateien mithilfe der Aspose.Cells.GridWeb-API entfernt werden können. Es ist möglich, ein Arbeitsblatt entweder durch Angabe seines Blattindex oder seines Namens zu entfernen.

{{% /alert %}} 
## **Arbeitsblatt entfernen**
### **Verwenden des Blattindex**
Der folgende Code zeigt, wie ein Arbeitsblatt entfernt wird, indem sein Blattindex im RemoveAt-Verfahren der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **Verwendung des Blattnamens**
Der folgende Code zeigt, wie ein Arbeitsblatt entfernt wird, indem sein Blattname im RemoveAt-Verfahren der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

Es ist auch möglich, ein Arbeitsblatt unter Verwendung seines Verweises oder der Instanz zu entfernen. Verwenden Sie dazu die Remove-Methode der GridWorksheetCollection. Dieser Ansatz wird häufig verwendet.

{{% /alert %}}
