---
title: Zellwert abrufen und ändern
type: docs
weight: 20
url: /de/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb, Zellwert, ändern, Wert
description: In diesem Artikel wird erläutert, wie Sie den Zellwert in GridWeb abrufen und ändern.
---

{{% alert color="primary" %}} 

[Auf Arbeitsblattzellen zugreifen](/cells/de/net/aspose-cells-gridweb/access-worksheet-cells/) behandelt den Zugriff auf Zellen. Dieses Thema erweitert diese Diskussion, um zu zeigen, wie auf Zellwerte mit der Aspose.Cells.GridWeb-API zugegriffen und diese geändert werden können.

{{% /alert %}} 
## **Zugriff und Ändern des Zellwerts**
### **Zeichenfolgenwerte**
Bevor der Wert einer Zelle abgerufen und geändert wird, müssen Sie wissen, wie Sie auf Zellen zugreifen. Für Details zu den unterschiedlichen Ansätzen zum Zugriff auf Zellen, siehe [Auf Arbeitsblattzellen zugreifen](/cells/de/net/aspose-cells-gridweb/access-worksheet-cells/).

Jede Zelle hat eine Eigenschaft namens StringValue. Sobald auf eine Zelle zugegriffen wurde, können Entwickler die Eigenschaft StringValue verwenden, um auf den Zeichenwert der Zelle zuzugreifen. Zum Ändern von Zellwerten wird eine spezielle Methode PutValue bereitgestellt, die verwendet werden kann, um den Zeichenwert der Zelle zu aktualisieren.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Alle Arten von Werten**
Die PutValue-Methode eines Zellenobjekts hat 8 verfügbare Überlastungen, die zum Ändern beliebiger Typen von Werten (Boolean, int, double, DateTime und string) in einer Zelle verwendet werden können.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Es gibt auch eine überladene Version der PutValue-Methode, die jeden Wert in Zeichenfolgenformat entgegennehmen und automatisch in einen entsprechenden Datentyp konvertieren kann. Um dies zu ermöglichen, übergeben Sie den Boolean-Wert true an einen anderen Parameter der PutValue-Methode, wie im folgenden Beispiel gezeigt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
