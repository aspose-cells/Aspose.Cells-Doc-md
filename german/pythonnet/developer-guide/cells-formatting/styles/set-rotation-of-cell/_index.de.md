---
title: Wie man Text in einer Zelle dreht
type: docs
weight: 80
url: /de/python-net/how-to-rotate-text-of-cell/
description: C# Code zum Drehen des Texts in Zellen mit Aspose.Cells für Python via .NET API
keywords: Python Text in Zelle drehen, Programmatisches Drehen des Texts in Zellen im Arbeitsbuch, Einstellung des Drehwinkels der Zelle im Arbeitsbuch, Wie man in Excel Text in Zelle dreht
---

## **Text in Zelle drehen mit Aspose.Cells für Python via .NET**

Aspose.Cells für Python via .NET ist eine leistungsstarke .NET- und Java-Komponente, die es Entwicklern ermöglicht, mit Excel-Tabellen programmatisch zu arbeiten. Eine der Funktionen von Aspose.Cells für Python via .NET ist das Drehen von Zellen, um die Ausrichtung des Texts anzupassen und die visuelle Präsentation Ihrer Daten zu verbessern. In diesem Dokument zeigen wir, wie man Zellen mit Aspose.Cells für Python via .NET dreht.

## **Wie man den Text einer Zelle in Excel dreht**
Um eine Zelle in Excel zu drehen, können Sie die folgenden Schritte verwenden:
1. Öffnen Sie Excel und wählen Sie die Zelle oder den Zellenbereich aus, den Sie drehen möchten.
1. Klicken Sie mit der rechten Maustaste auf die ausgewählte Zelle(n) und wählen Sie "Zellen formatieren" aus dem Kontextmenü. Alternativ können Sie zum Register "Start" im Excel-Menüband gehen, auf die Dropdown-Schaltfläche "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.
1. In dem Dialogfeld "Zellen formatieren" wechseln Sie zum Register "Ausrichtung".
1. Im Abschnitt "Ausrichtung" sehen Sie die Optionen zum Drehen des Textes. Sie können den gewünschten Drehwinkel in Grad direkt in das Feld "Grad" eingeben. Positive Werte drehen den Text gegen den Uhrzeigersinn, und negative Werte drehen ihn im Uhrzeigersinn.
<br>
![todo:image_alt_text](alignment.png)
1. Nachdem Sie die gewünschte Rotation ausgewählt haben, klicken Sie auf "OK", um die Änderungen anzuwenden. Die ausgewählte(n) Zelle(n) wird/werden nun je nach gewähltem Rotationswinkel oder -orientierung gedreht.

## **So drehen Sie den Text in Zellen mit Aspose.Cells für Python via .NET API**

[**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle)-Eigenschaft macht es bequem, Zellen zu drehen. Um Zellen in Aspose.Cells für Python via .NET zu drehen, folgen Sie diesen Schritten:
1. Laden Sie die Excel-Arbeitsmappe
<br>
Zuerst müssen Sie das Excel-Arbeitsbuch mit Aspose.Cells für Python via .NET laden. Sie können die Klasse Workbook verwenden, um eine bestehende Excel-Datei zu öffnen oder eine neue zu erstellen. 

1. Zugriff auf das Arbeitsblatt
<br>
Sobald die Arbeitsmappe geladen ist, müssen Sie auf das Arbeitsblatt zugreifen, auf dem Sie die Zellen drehen möchten. Sie können entweder auf das Arbeitsblatt nach Index oder Namen zugreifen. 

1. Text der Zelle drehen
<br>
Nun, da Sie Zugriff auf das Arbeitsblatt haben, können Sie die Zellen drehen, indem Sie das Style-Objekt der gewünschten Zellen ändern. Das Style-Objekt ermöglicht es Ihnen, verschiedene Formatierungsoptionen festzulegen, einschließlich der Rotation. 

1. Arbeitsmappe speichern
<br>
Nachdem die Zellen gedreht wurden, können Sie die modifizierte Arbeitsmappe mithilfe der Save-Methode wieder in eine Datei oder einen Stream speichern.

## **Python-Beispielcode**

Bitte beachten Sie den folgenden Code, er erstellt ein Arbeitsmappenobjekt und setzt verschiedene Rotationswinkel für mehrere Zellen. Der Screenshot zeigt das Ergebnis nach der Ausführung des Beispielscodes.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

{{< app/cells/assistant language="python-net" >}}
