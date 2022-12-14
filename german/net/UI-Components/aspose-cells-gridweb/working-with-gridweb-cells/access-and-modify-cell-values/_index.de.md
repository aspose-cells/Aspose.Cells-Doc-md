---
title: Auf Cell-Werte zugreifen und diese ändern
type: docs
weight: 20
url: /de/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[Greifen Sie auf das Arbeitsblatt Cells zu](/cells/de/net/access-worksheet-cells/) den Zugriff auf Zellen besprochen. Dieses Thema erweitert diese Diskussion, um zu zeigen, wie Sie mit Aspose.Cells.GridWeb API auf Zellwerte zugreifen und diese ändern.

{{% /alert %}} 
## **Zugriff auf und Änderung des Werts von Cell**
### **Zeichenfolgenwerte**
 Bevor Sie auf den Wert einer Zelle zugreifen und diesen ändern können, müssen Sie wissen, wie Sie auf Zellen zugreifen. Einzelheiten zu den verschiedenen Ansätzen für den Zugriff auf Zellen finden Sie unter[Greifen Sie auf das Arbeitsblatt Cells zu](/cells/de/net/access-worksheet-cells/).

Jede Zelle hat eine Eigenschaft namens StringValue. Sobald auf eine Zelle zugegriffen wird, können Entwickler die StringValue-Eigenschaft verwenden, um auf den Zeichenfolgenwert der Zelle zuzugreifen. Um Zellwerte zu ändern, wird eine spezielle Methode PutValue bereitgestellt, die verwendet werden kann, um den Zeichenfolgenwert der Zelle zu aktualisieren.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Alle Arten von Werten**
Die PutValue-Methode eines Zellenobjekts verfügt über 8 verfügbare Überladungen, die verwendet werden können, um jeden Werttyp (Boolean, Int, Double, DateTime und String) in einer Zelle zu ändern.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Es gibt auch eine überladene Version der PutValue-Methode, die jede Art von Wert im Zeichenfolgenformat annehmen und automatisch in einen geeigneten Datentyp konvertieren kann. Um dies zu erreichen, übergeben Sie den booleschen Wert true an einen anderen Parameter der PutValue-Methode, wie unten im Beispiel gezeigt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
