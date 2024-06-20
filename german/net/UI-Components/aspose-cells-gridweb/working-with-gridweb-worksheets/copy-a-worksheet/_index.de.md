---
title: Ein Arbeitsblatt kopieren
type: docs
weight: 50
url: /de/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb, kopieren, GridWorksheet
description: Dieser Artikel stellt vor, wie ein Arbeitsblatt (GridWorksheet) in GridWeb kopiert werden kann.
---

{{% alert color="primary" %}} 

[Arbeitsblätter hinzufügen](/cells/de/net/aspose-cells-gridweb/add-worksheets/) beschreibt, wie neue Arbeitsblätter zu Aspose.Cells.GridWeb hinzugefügt werden. Es ist auch möglich, eine Kopie (oder ein Duplikat) eines anderen Arbeitsblatts der Aspose.Cells.GridWeb-Steuerung hinzuzufügen. Diese Funktion kann nützlich sein, wenn identische oder ähnliche Daten in einem Arbeitsblatt auch in einem anderen Arbeitsblatt benötigt werden. In diesem Fall ist es einfacher, ein vorhandenes Arbeitsblatt zu kopieren und es dem Aspose.Cells.GridWeb als neues Arbeitsblatt hinzuzufügen, anstatt es von Grund auf zu erstellen.

{{% /alert %}} 
## **Kopieren eines Arbeitsblatts**
### **Verwendung des Blattindex**
Der folgende Beispielcode zeigt, wie eine Kopie eines Arbeitsblatts zur GridWeb-Steuerung hinzugefügt wird, indem der Index des Arbeitsblatts in der Methode AddCopy der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Verwendung des Blattnamens**
Der folgende Beispielcode zeigt, wie eine Kopie eines Arbeitsblatts zur GridWeb-Steuerung hinzugefügt wird, indem der Name des Arbeitsblatts in der Methode AddCopy der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

Die AddCopy-Methode gibt den Index des neu hinzugefügten Arbeitsblatts zurück, der verwendet werden kann, um auf die Arbeitsblattinstanz zuzugreifen. Weitere Details zum Zugriff auf Arbeitsblätter finden Sie unter [Arbeitsblätter zugreifen](/cells/de/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}}
