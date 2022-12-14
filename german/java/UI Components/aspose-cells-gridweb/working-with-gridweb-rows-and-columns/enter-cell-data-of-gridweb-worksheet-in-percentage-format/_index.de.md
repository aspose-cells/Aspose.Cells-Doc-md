---
title: Geben Sie Cell Daten des GridWeb-Arbeitsblatts im Prozentformat ein
type: docs
weight: 1010
url: /de/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **Mögliche Nutzungsszenarien**
GridWeb unterstützt jetzt Benutzer bei der Eingabe von Zellendaten im Prozentformat wie 3 %, und die Daten in der Zelle werden automatisch als 3,00 % formatiert. Sie müssen den Zellenstil jedoch auf das Prozentformat festlegen, das entweder GridTableItemStyle.NumberType a 9 oder 10 ist. Die Zahl 9 formatiert 3 % als 3 %, aber die Zahl 10 formatiert 3 % als 3,00 %.

{{% alert color="primary" %}} 

Wenn Sie den Zellenstil nicht auf Prozentformat eingestellt haben, werden die Eingabedaten 3 % als 0,03 angezeigt.

{{% /alert %}} 
## **Geben Sie Cell Daten des GridWeb-Arbeitsblatts im Prozentformat ein**
Der folgende Beispielcode legt die Zelle A1 GridTableItemStyle.NumberType auf 10 fest, daher werden die Eingabedaten 3 % automatisch als 3,00 % formatiert, wie im Screenshot gezeigt.

![todo: Bild_alt_Text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **Beispielcode**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






