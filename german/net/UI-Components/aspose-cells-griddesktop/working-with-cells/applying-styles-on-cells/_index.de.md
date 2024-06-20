---
title: Stil auf Zelle anwenden
type: docs
weight: 50
url: /de/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop, Format, Stil, Zahlenformate, Zahlenformat, NumberFormat
description: Dieser Artikel zeigt, wie man das Format des Stils in der Zelle im Arbeitsblatt in GridDesktop erhält oder setzt.
---

{{% alert color="primary" %}} 

Dieses Thema beschäftigt sich mit dem Anwenden von Stilformat auf eine Zelle. Wir werden fast alle relevanten Eigenschaften behandeln, die verwendet werden können, um einen Stil auf eine Zelle anzuwenden. Neben einigen grundlegenden Formatierungseinstellungen werden wir auch ausführlich das Zeichnen von Rahmen und das Festlegen des Zahlenformats in der Zelle behandeln.

{{% /alert %}} 
## **Anwendung eines benutzerdefinierten Stils auf eine Zelle - ein Beispiel**
Um die Schriftart und Farbe einer Zelle mit Aspose.Cells.GridDesktop zu ändern, befolgen Sie bitte die folgenden Schritte:

- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Zugriff auf eine **Zelle**, auf die wir einen **Stil** anwenden möchten
- **Stil** der **Zelle** erhalten
- Setzen Sie die Eigenschaften des **Stils** gemäß Ihren individuellen Anforderungen
- Schließlich den **Stil** der **Zelle** mit dem aktualisierten festlegen

Es gibt viele nützliche Eigenschaften und Methoden des **Stil**-Objekts, die von Entwicklern genutzt werden können, um den Stil entsprechend ihren Anforderungen anzupassen. Im folgenden Code wird demonstriert, wie ein benutzerdefinierter Stil auf eine Zelle angewendet wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Zeichnen von Zellgrenzen**
Mit dem **Stil**-Objekt können wir die Grenzen einer Zelle sehr einfach zeichnen. Die Grenzen können in jeder Farbe gezeichnet werden. Darüber hinaus haben Entwickler auch die Flexibilität, einen bestimmten Linientyp auszuwählen, der verwendet wird, um die Grenzen um die Zelle zu zeichnen. Entwickler können die Methoden **SetBorderLine** und **SetBorderColor** des **Stil**-Objekts verwenden, um Grenzen jeder Art und Farbe zu zeichnen. Ebenso können Entwickler zur Ermittlung von Grenzinformationen einer Zelle auch die Methoden **GetBorderLine** und **GetBorderColor** des **Stil**-Objekts verwenden.
### **Arten von Grenzen**
Aspose.Cells.GridDesktop unterstützt sechs Arten von Grenzen, wie folgt:

- **Links**, repräsentiert linke Grenze
- **Rechts**, repräsentiert rechte Grenze
- **Oben**, repräsentiert obere Grenze
- **Unten**, repräsentiert untere Grenze
- **DiagonalDown**, repräsentiert diagonale Abwärtsgrenze
- **DiagonalUp**, repräsentiert diagonale Aufwärtsgrenze
### **Arten von Grenzlinien**
Eine Grenze besteht aus einer Linie. Durch Ändern des Linientyps ändert sich das Aussehen einer Grenze. Aspose.Cells.GridDesktop unterstützt viele Arten von Grenzlinien, die unten ebenfalls aufgelistet sind:

- **Keine**, repräsentiert keine Grenze
- **Dünn**, repräsentiert eine durchgezogene Grenzlinie
- **Mittel**, repräsentiert eine durchgezogene Grenzlinie mit einer Linienbreite von 2f
- **Gestrichen** , repräsentiert gestrichene Linienränder
- **Gepunktet** , repräsentiert gepunktete Linienränder
- **Dick** , repräsentiert solide Linienränder mit einer Linienbreite von 3f
- **Mitteldurchgezogen** , repräsentiert gestrichene Linienränder mit einer Linienbreite von 2f
- **Dünn-Gestrichen-Gepunktet** , repräsentiert gestrichen gepunktete Linienränder
- **Mitteldurchgezogen-Gepunktet** , repräsentiert gestrichen gepunktete Linienränder mit einer Linienbreite von 2f
- **Dünn-Gestrichen-Gepunktet-Gepunktet** , repräsentiert gestrichen gepunktet gepunktete Linienränder
- **Mitteldurchgezogen-Gepunktet-Gepunktet** , repräsentiert gestrichen gepunktet gepunktete Linienränder mit einer Linienbreite von 2f
## **Zusammenfassung aller Features - Beispiel**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Einstellen von Zahlenformaten**
Aspose.Cells.GridDesktop bietet auch verschiedene Arten der Einstellung von Zahlenformaten. Es gibt 58 eingebaute Zahlenformate, die von Aspose.Cells.GridDesktop angeboten werden. Um eine vollständige Liste aller unterstützten Zahlenformate zu sehen, beachten Sie bitte die [Liste der unterstützten Zahlenformate.](/cells/de/net/list-of-supported-number-formats/)

Allen eingebauten Zahlenformaten ist eine **Index**-Nummer zugewiesen. **Zum Beispiel** ist die **Index**-Nummer des Zahlenformats **0.00E+00** die **11**. Um ein eingebautes Zahlenformat in einer Zelle zu verwenden, können Entwickler die NumberFormat-Eigenschaft des **Style**-Objekts auf die **Index**-Nummer dieses spezifischen Zahlenformats setzen. Wenn Entwickler jedoch ihr eigenes benutzerdefiniertes Zahlenformat benötigen, können sie auch die Custom-Eigenschaft des **Style**-Objekts verwenden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
