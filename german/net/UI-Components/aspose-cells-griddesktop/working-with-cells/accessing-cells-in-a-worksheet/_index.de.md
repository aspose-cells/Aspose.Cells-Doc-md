---
title: Zugriff auf Cells in einem Arbeitsblatt
type: docs
weight: 10
url: /de/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

Wir haben bisher über die Arbeit mit Arbeitsblättern, Zeilen und Spalten gesprochen, aber jetzt ist es an der Zeit, tiefer zu gehen und über Zellen zu sprechen. In diesem Thema würden wir also unsere Diskussion über Zellen mit einer grundlegenden Funktion für den Zugriff auf Zellen beginnen.

{{% /alert %}} 
## **Zugriff auf Cells in einem Arbeitsblatt**
Mit API von Aspose.Cells.GridDesktop können wir auf jede Zelle eines Arbeitsblatts zugreifen. Es könnte drei Möglichkeiten geben, wie folgt auf Zellen zuzugreifen:

- **Verwendung des Namens Cell**
- **Verwenden der Zeilen- und Spaltenindizes von Cell**
- **Fokussieren Cell**

Lassen Sie uns alle oben genannten drei Ansätze nacheinander besprechen.
### **Verwendung des Namens Cell**
 Alle Zellen in einem Arbeitsblatt haben einen eindeutigen Namen. Zum Beispiel A1, A2, B1, B2 usw. Aspose.Cells.GridDesktop ermöglicht Entwicklern den Zugriff auf jede gewünschte Zelle, indem sie ihren Zellnamen verwenden. Alles, was wir tun müssen, ist, einfach den Zellennamen (als Index) an die zu übergeben**Cells** Sammlung der**Arbeitsblatt**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Verwenden der Zeilen- und Spaltenindizes von Cell**
 Eine Zelle in einem Arbeitsblatt kann auch anhand ihrer Position in Bezug auf ihre Zeilen- und Spaltenindizes erkannt werden. Alles, was wir tun müssen, ist, einfach die Zeilen- und Spaltenindizes der Zelle an die zu übergeben**Cells** Sammlung der**Arbeitsblatt**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **Fokussieren Cell**
 Wenn Sie nicht genau wissen, auf welche Zelle zugegriffen werden soll. Dann ermöglicht Ihnen Aspose.Cells.GridDesktop auch den Zugriff auf eine Zelle, die sich gerade im Fokus eines Benutzers befindet. Mit dieser Funktion können Sie einem Benutzer erlauben, eine beliebige Zelle auszuwählen, und Sie können dann im Backend auf diese Zelle zugreifen. Es kann einfach durch die Verwendung erreicht werden**GetFocusedCell** Methode der**Arbeitsblatt**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
