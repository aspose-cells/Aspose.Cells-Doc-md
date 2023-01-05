---
title: Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie
linktitle: Rich-Formatierungstext
type: docs
weight: 440
url: /de/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Mit Aspose.Cells können Sie auf die Teile des Rich-Texts der Zelle zugreifen und diese aktualisieren. Zu diesem Zweck können Sie die Methoden Cell.getCharacters() und Cell.setCharacters() verwenden. Diese Methoden geben das Array von FontSetting-Objekten zurück und akzeptieren es, mit dem Sie auf verschiedene Eigenschaften von Schriftarten wie Schriftartname, Schriftfarbe, Fettschrift usw. zugreifen und diese aktualisieren können.

{{% /alert %}} 
## **Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie**
 Der folgende Code demonstriert die Verwendung der Methoden Cell.getCharacters() und Cell.setCharacters() mit der[Excel-Quelldatei](5472937.xlsx) die Sie über den angegebenen Link herunterladen können. Die Excel-Quelldatei hat einen Rich-Text in der Zelle A1. Es hat 3 Teile und jeder Teil hat eine andere Schriftart. Wir werden auf diese Teile zugreifen und den ersten Teil mit einem neuen Schriftartnamen aktualisieren. Schließlich speichert es die Arbeitsmappe als[Excel-Datei ausgeben](5472930.xlsx) . Wenn Sie es öffnen, werden Sie feststellen, dass sich die Schriftart des ersten Teils des Textes geändert hat**"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Konsolenausgabe**
 Hier ist die Konsolenausgabe des obigen Beispielcodes mit der[Excel-Quelldatei](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
