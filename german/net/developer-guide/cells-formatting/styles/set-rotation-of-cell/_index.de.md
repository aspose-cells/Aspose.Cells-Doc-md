---
title: Wie man Text in einer Zelle dreht
type: docs
weight: 80
url: /de/net/how-to-rotate-text-of-cell/
description: C# Code zum Drehen des Textes einer Zelle mit der Aspose.Cells for .NET API
keywords: c# Text einer Zelle drehen, c# programmgesteuert Text einer Zelle in einem Arbeitsbuch drehen, programmgesteuert den Drehwinkel einer Zelle in einem Arbeitsbuch festlegen, c# wie man den Text einer Zelle in Excel dreht
---

## **Text einer Zelle in Aspose.Cells drehen**

Aspose.Cells ist eine leistungsstarke .NET- und Java-Komponente, die es Entwicklern ermöglicht, programmgesteuert mit Excel-Arbeitsblättern zu arbeiten. Eine der von Aspose.Cells bereitgestellten Funktionen ist die Möglichkeit, Zellen zu drehen, was es Ihnen ermöglicht, die Ausrichtung von Text anzupassen und die visuelle Darstellung Ihrer Daten zu verbessern. In diesem Dokument werden wir erkunden, wie man Zellen mit Aspose.Cells dreht.

## **Wie man den Text einer Zelle in Excel dreht**
Um eine Zelle in Excel zu drehen, können Sie die folgenden Schritte verwenden:
1. Öffnen Sie Excel und wählen Sie die Zelle oder den Zellenbereich aus, den Sie drehen möchten.
1. Klicken Sie mit der rechten Maustaste auf die ausgewählte Zelle(n) und wählen Sie "Zellen formatieren" aus dem Kontextmenü. Alternativ können Sie zum Register "Start" im Excel-Menüband gehen, auf die Dropdown-Schaltfläche "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.
1. In dem Dialogfeld "Zellen formatieren" wechseln Sie zum Register "Ausrichtung".
1. Im Abschnitt "Ausrichtung" sehen Sie die Optionen zum Drehen des Textes. Sie können den gewünschten Drehwinkel in Grad direkt in das Feld "Grad" eingeben. Positive Werte drehen den Text gegen den Uhrzeigersinn, und negative Werte drehen ihn im Uhrzeigersinn.
<br>
![todo:image_alt_text](alignment.png)
1. Nachdem Sie die gewünschte Rotation ausgewählt haben, klicken Sie auf "OK", um die Änderungen anzuwenden. Die ausgewählte(n) Zelle(n) wird/werden nun je nach gewähltem Rotationswinkel oder -orientierung gedreht.

## **Wie man den Text einer Zelle mit Aspose.Cells API dreht**

Die [**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/)-Eigenschaft macht es bequem, Zellen zu drehen. Um Zellen in Aspose.Cells zu drehen, müssen Sie die folgenden Schritte befolgen:
1. Laden Sie die Excel-Arbeitsmappe
<br>
Zunächst müssen Sie die Excel-Arbeitsmappe mit Aspose.Cells laden. Sie können die Workbook-Klasse verwenden, um eine vorhandene Excel-Datei zu öffnen oder eine neue zu erstellen. 

1. Zugriff auf das Arbeitsblatt
<br>
Sobald die Arbeitsmappe geladen ist, müssen Sie auf das Arbeitsblatt zugreifen, auf dem Sie die Zellen drehen möchten. Sie können entweder auf das Arbeitsblatt nach Index oder Namen zugreifen. 

1. Text der Zelle drehen
<br>
Nun, da Sie Zugriff auf das Arbeitsblatt haben, können Sie die Zellen drehen, indem Sie das Style-Objekt der gewünschten Zellen ändern. Das Style-Objekt ermöglicht es Ihnen, verschiedene Formatierungsoptionen festzulegen, einschließlich der Rotation. 

1. Arbeitsmappe speichern
<br>
Nachdem die Zellen gedreht wurden, können Sie die modifizierte Arbeitsmappe mithilfe der Save-Methode wieder in eine Datei oder einen Stream speichern.

## **C# Beispielcode**

Bitte beachten Sie den folgenden Code, er erstellt ein Arbeitsmappenobjekt und setzt verschiedene Rotationswinkel für mehrere Zellen. Der Screenshot zeigt das Ergebnis nach der Ausführung des Beispielscodes.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
{{< app/cells/assistant language="csharp" >}}
