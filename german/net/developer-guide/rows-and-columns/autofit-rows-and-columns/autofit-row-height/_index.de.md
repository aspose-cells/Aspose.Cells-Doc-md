---
title: Automatische Anpassung der Zeilenhöhe beim Laden der Datei
type: docs
weight: 120
url: /de/net/autofit-row-height/
description: Erfahren Sie, wie Sie die Zeilen anpassen können, deren Höhe nicht benutzerdefiniert ist.
keywords: Automatische Anpassung der Zeilenhöhe beim Laden der Datei, passt automatisch die Zeilenhöhe beim Öffnen der Excel Datei an. 
---

## **Mögliche Verwendungsszenarien**
Die Höhe der Zeile entspricht automatisch der Schriftart des Inhalts, aber wenn die Höhe der zwischengespeicherten Zeile nicht mit der Höhe des Inhalts in der Datei übereinstimmt, passt MS Excel die Zeilenhöhe automatisch an, wenn die Datei geladen wird. Aspose.Cells passt sie jedoch nicht automatisch an, um die Leistung zu verbessern. Wenn Sie das Programm Aspose.Cells verwenden müssen, um die Zeilenhöhen beim Laden von Dateien automatisch anzugleichen, können Sie dies über den Parameter [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) erreichen.

Bitte beachten Sie die folgenden Bilddaten. Wir können beobachten, dass die zwischengespeicherte Zeilenhöhe in Zeile 11 15 beträgt, aber Excel passt die Zeilenhöhe automatisch an, wenn die Datei geladen wird.
<br>
<img src="1.png" width=70% />

## **Anpassen der Zeilenhöhe mit Aspose.Cells**
Wenn Sie die Datei direkt laden und sie als PDF speichern, wird die Daten nicht vollständig in PDF angezeigt, weil die Zeilenhöhe des zwischengespeicherten Inhalts nur 15 beträgt.
<br>
<img src="2.png" width=70% />
<br>
Wenn Sie den Parameter [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) auf true setzen beim Laden der Datei, wird Aspose.Cells die Zeilenhöhe automatisch anpassen. Die angepasste Zeilenhöhe kann effektiv den Anzeigebedarf des Textes erfüllen.
<br>
<img src="3.png" width=70% />

## **C# Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
