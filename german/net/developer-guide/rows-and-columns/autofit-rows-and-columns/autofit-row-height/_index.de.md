---
title: Automatische Anpassung der Zeilenhöhe beim Laden der Datei
type: docs
weight: 120
url: /de/net/autofit-row-height/
description: Erfahren Sie, wie Sie die Zeilen anpassen, deren Höhe nicht benutzerdefiniert ist.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **Mögliche Nutzungsszenarien**
 Die Höhe der Zeile entspricht automatisch der Schriftart des Inhalts. Wenn die Höhe der zwischengespeicherten Zeile jedoch nicht mit der Höhe des Inhalts in der Datei übereinstimmt, passt MS Excel die Zeilenhöhe beim Laden der Datei automatisch an, während Aspose.Cells dies nicht tut Passen Sie es automatisch an, um die Leistung zu verbessern. Wenn Sie das Programm Aspose.Cells verwenden müssen, um beim Laden von Dateien automatisch die Zeilenhöhe anzupassen, können Sie das Ziel über den Parameter erreichen[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Bitte beachten Sie die folgenden Bilddaten. Wir können beobachten, dass die Cache-Zeilenhöhe in Zeile 11 15 beträgt, Excel die Zeilenhöhe jedoch beim Laden der Datei automatisch angepasst hat.
<br>
<img src="1.png" width=70% />

##  **Passen Sie die Zeilenhöhe mit Aspose.Cells an**
Wenn Sie die Datei direkt laden und unter PDF speichern, werden die Daten in PDF nicht vollständig angezeigt, da die Cache-Zeilenhöhe nur 15 beträgt.
<br>
<img src="2.png" width=70% />
<br>
 Wenn Sie den Parameter festlegen[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) Beim Laden der Datei auf true gesetzt, passt Aspose.Cells die Zeilenhöhe automatisch an. Die angepasste Zeilenhöhe kann die Anforderungen an die Textanzeige effektiv erfüllen.
<br>
<img src="3.png" width=70% />

##  **C# Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}