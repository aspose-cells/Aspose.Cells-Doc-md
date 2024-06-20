---
title: Zugriff und Aktualisierung der Teile von Rich Text einer Zelle
linktitle: Rich Text Formatierung
type: docs
weight: 440
url: /de/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells ermöglicht den Zugriff und die Aktualisierung der Textteile einer Zelle mit reichhaltiger Formatierung. Hierfür können die Methoden Cell.getCharacters() und Cell.setCharacters() verwendet werden. Diese Methoden geben ein Array von FontSetting-Objekten zurück und akzeptieren diese, die zur Zugriff und Aktualisierung verschiedener Eigenschaften der Schrift wie Schriftart, Schriftfarbe, Fettdruck usw. verwendet werden können.

{{% /alert %}} 
## **Teile des Rich-Texts der Zelle zugreifen und aktualisieren**
Der folgende Code zeigt die Verwendung der Methode Cell.getCharacters() und Cell.setCharacters() unter Verwendung der [Quellexceldatei](5472937.xlsx), die Sie über den bereitgestellten Link herunterladen können. Die Quellexceldatei enthält einen reichhaltigen Text in der Zelle A1. Es hat 3 Teile, und jeder Teil hat eine andere Schriftart. Wir werden auf diese Teile zugreifen und den ersten Teil mit einer neuen Schriftart aktualisieren. Schließlich speichert es die Arbeitsmappe als [Ausgabeexceldatei](5472930.xlsx). Wenn Sie es öffnen, werden Sie feststellen, dass die Schriftart des ersten Teils des Textes auf **"Arial"** geändert wurde.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes unter Verwendung der [Quellexceldatei](5472937.xlsx).

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
