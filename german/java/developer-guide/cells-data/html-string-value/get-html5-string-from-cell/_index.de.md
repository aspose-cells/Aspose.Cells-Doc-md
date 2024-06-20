---
title: HTML5 String aus Zelle abrufen
type: docs
weight: 90
url: /de/java/get-html5-string-from-cell/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells liefert den HTML-String der Zelle mithilfe der Methode [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) zurück. Wenn Sie false als Parameter übergeben, erhalten Sie normalen HTML-Code, aber wenn Sie true als Parameter übergeben, erhalten Sie HTML5-String zurück.

## **Holen Sie sich HTML5-String aus der Zelle**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt etwas Text in Zelle A1 des ersten Arbeitsblatts ein. Dann wird der normale HTML- und HTML5-String aus Zelle A1 mithilfe der Methode [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) abgerufen und auf der Konsole gedruckt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
