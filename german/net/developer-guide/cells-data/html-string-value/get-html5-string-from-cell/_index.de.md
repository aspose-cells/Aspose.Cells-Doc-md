---
title: HTML5 String aus Zelle abrufen
type: docs
weight: 90
url: /de/net/get-html5-string-from-cell/
description: Erfahren Sie, wie Sie den HTML5 String aus der Zelle durch die Aspose.Cells for .NET API erhalten können.
keywords: Holen Sie den HTML5 String aus der Zelle, HTML5 String aus der Zelle erhalten, HTML5 String der Zelle verwalten
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells gibt den HTML-String der Zelle mit der Methode [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) zurück, die einen booleschen Parameter akzeptiert. Wenn Sie **false** als Parameter übergeben, wird Normal HTML zurückgegeben, aber wenn Sie **true** als Parameter übergeben, wird ein HTML5-String zurückgegeben.

## **Holen Sie sich HTML5-String aus der Zelle**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt etwas Text in Zelle A1 des ersten Arbeitsblatts ein. Anschließend wird der Normal HTML- und HTML5-String aus Zelle A1 mit der Methode [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) geholt und auf der Konsole gedruckt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
