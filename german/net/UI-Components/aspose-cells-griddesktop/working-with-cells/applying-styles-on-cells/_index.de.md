---
title: Anwenden von Stilen unter Cells
type: docs
weight: 50
url: /de/net/applying-styles-on-cells/
---
{{% alert color="primary" %}} 

Dieses Thema befasst sich mit dem Anwenden von Stilen auf Zellen, daher werden wir versuchen, fast alles abzudecken, was zum Anwenden von Stilen auf eine Zelle verwendet werden kann. Neben einigen grundlegenden Formatierungseinstellungen werden wir auch das Zeichnen von Rahmen und das Festlegen des Zahlenformats von Zellen im Detail besprechen.

{{% /alert %}} 
## **Anwenden eines benutzerdefinierten Stils auf eine Cell – ein Beispiel**
Um die Schriftart und Farbe einer Zelle mit Aspose.Cells.GridDesktop zu ändern, gehen Sie bitte wie folgt vor:

-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Zugriff a**Cell** auf die wir a anwenden wollen**Stil**
-  Bekommen**Stil** des**Cell**
-  Satz**Stil** Eigenschaften nach Ihren individuellen Bedürfnissen
-  Endlich einstellen**Stil** des**Cell** mit dem aktualisierten

 Es gibt viele nützliche Eigenschaften und Methoden, die von angeboten werden**Stil** Objekt, das von Entwicklern verwendet werden kann, um den Stil an ihre Anforderungen anzupassen. Im folgenden Code wird gezeigt, wie ein benutzerdefinierter Stil auf eine Zelle angewendet wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Zeichnen von Grenzen von Cells**
 Verwenden**Stil**Objekt können wir sehr einfach Grenzen einer Zelle ziehen. Die Ränder können in jeder Farbe gezeichnet werden. Darüber hinaus haben Entwickler auch die Flexibilität, einen bestimmten Linientyp auszuwählen, der verwendet wird, um Grenzen um die Zelle zu ziehen. Entwickler können verwenden**Randlinie setzen** und**Rahmenfarbe festlegen** Methoden von**Stil** Objekt zum Zeichnen von Rändern jeglicher Art und Farbe. Um Grenzinformationen einer beliebigen Zelle zu erhalten, können Entwickler ebenfalls davon Gebrauch machen**Holen Sie sich BorderLine** und**GetRandfarbe** Methoden von**Stil** Objekt.
### **Arten von Grenzen**
Es gibt sechs Arten von Rahmen, die von Aspose.Cells.GridDesktop wie folgt unterstützt werden:

- **Links** , stellt den linken Rand dar
- **Recht** , stellt die rechte Grenze dar
- **oben** , stellt den oberen Rand dar
- **Unterseite** , stellt den unteren Rand dar
- **DiagonalUnten** , stellt eine diagonal nach unten gerichtete Grenze dar
- **Diagonal nach oben** , steht für eine diagonal nach oben gerichtete Grenze
### **Arten von Grenzlinien**
Eine Grenze besteht aus einer Linie. Das Ändern des Linientyps ändert das Aussehen eines Rahmens. Es gibt viele Arten von Grenzlinien, die von Aspose.Cells.GridDesktop unterstützt werden, die auch unten aufgeführt sind:

- **Keiner** , stellt keine Grenze dar
- **Dünn** , stellt eine durchgezogene Umrandung dar
- **Mittel** , stellt eine durchgezogene Umrandung mit einer Linienbreite gleich 2f dar
- **Gestrichelt** , stellt eine gestrichelte Grenze dar
- **Gepunktet** , stellt eine gepunktete Grenzlinie dar
- **Dick** , stellt eine durchgezogene Umrandung mit einer Linienbreite von 3f dar
- **Mittelgestrichelt** , stellt eine gestrichelte Grenze mit einer Linienbreite gleich 2f dar
- **ThinDashDotted** , stellt die strichpunktierte Grenze dar
- **MittelStrichGepunktet** stellt eine strichpunktierte Umrandung mit einer Linienbreite gleich 2f dar
- **ThinDashDotDotted** , stellt die strichpunktierte Grenze dar
- **MediumDashDotDotted** , stellt eine strichpunktierte Umrandung mit einer Linienbreite gleich 2f dar
## **Alles zusammenfassen - Beispiel**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Zahlenformate einstellen**
Aspose.Cells.GridDesktop bietet auch eine starke Funktion zum Festlegen von Zahlenformaten für die in Zellen eingegebenen Werte. Es gibt 58 integrierte Zahlenformate, die von Aspose.Cells.GridDesktop angeboten werden. Eine vollständige Liste aller unterstützten Zahlenformate finden Sie unter[Unterstützte Zahlenformate.](/cells/de/net/list-of-supported-number-formats/)

 Allen eingebauten Zahlenformaten wird ein zugewiesen**Index** Anzahl.**Zum Beispiel** Die**Index** Anzahl von**0.00E+00** Zahlenformat ist**11** . Um ein integriertes Zahlenformat in einer beliebigen Zelle zu verwenden, können Entwickler die NumberFormat-Eigenschaft von festlegen**Stil** Widerspruch gegen die**Index** Nummer dieses bestimmten Zahlenformats. Wenn Entwickler jedoch ein eigenes benutzerdefiniertes Zahlenformat benötigen, können sie auch die benutzerdefinierte Eigenschaft von verwenden**Stil** Objekt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
