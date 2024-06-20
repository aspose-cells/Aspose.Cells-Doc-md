---
title: Geben Sie Zelldaten des GridWeb Arbeitsblatts im Prozentformat ein
type: docs
weight: 80
url: /de/net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: Dieser Artikel führt die Eingabe von Zelldaten im Prozentsatzformat in GridWeb ein.
---


## **Mögliche Verwendungsszenarien**
GridWeb unterstützt jetzt Benutzer dabei, Zelldaten im Prozentformat wie 3% einzugeben, und die Daten in der Zelle werden automatisch als 3,00% formatiert. Sie müssen jedoch den Zellstil auf Prozentformat setzen, welches entweder GridTableItemStyle.NumberType 9 oder 10 ist. Die Nummer 9 wird 3% als 3% formatieren, aber die Nummer 10 wird 3% als 3,00% formatieren.

{{% alert color="primary" %}} 

Wenn Sie den Zellstil nicht auf Prozentformat gesetzt haben, wird die Eingabedaten 3% als 0,03 angezeigt.

{{% /alert %}} 
## **Eingabe von Zelldaten des GridWeb-Arbeitsblatts im Prozentformat**
Der folgende Beispielcode setzt die Zelle A1 GridTableItemStyle.NumberType auf 10. Daher wird die Eingabedaten 3% automatisch als 3,00% formatiert, wie im Screenshot gezeigt.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Beispielcode**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
