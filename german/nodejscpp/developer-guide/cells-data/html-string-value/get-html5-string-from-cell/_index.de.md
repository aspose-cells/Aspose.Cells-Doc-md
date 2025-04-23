---
title: HTML5 String aus Zelle abrufen
type: docs
weight: 90
url: /de/nodejs-cpp/get-html5-string-from-cell/
description: Lernen Sie, wie Sie mit der API Aspose.Cells for Node.js via C++ HTML5 Strings aus Zellen holen.
keywords: HTML5 String aus Zelle holen Node.js via C++, HTML5 String aus Zelle erhalten Node.js via C++, HTML5 String der Zelle verwalten Node.js via C++
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells gibt den HTML-String der Zelle mit der Methode [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) zurück, die einen booleschen Parameter akzeptiert. Wenn Sie **false** als Parameter übergeben, wird normales HTML zurückgegeben, bei Übergabe von **true** erhält man HTML5-String.

## **Holen Sie sich HTML5-String aus der Zelle**

Der folgende Beispielcode erstellt ein Arbeitsblatt-Objekt und fügt einigen Text in die Zelle A1 des ersten Arbeitsblatts ein. Dann erhält er den normalen HTML- und HTML5-String aus Zelle A1 mit der Methode [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) und gibt diese auf der Konsole aus.

## **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Konsolenausgabe**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
