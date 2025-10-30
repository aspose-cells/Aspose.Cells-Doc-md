---
title: Wie man den Text einer Zelle mit Golang über C++ dreht
linktitle: Wie man Text in einer Zelle dreht
type: docs
weight: 80
url: /de/go-cpp/how-to-rotate-text-of-cell/
description: C++ Code zur Drehung des Zellentexts mit der API Aspose.Cells for C++
keywords: c++ Drehung des Textes in einer Zelle, c++ Programm zur programmatischen Drehung des Textes in einer Zelle im Arbeitsbuch, programmatische Einstellung des Zellrotationswinkels im Arbeitsbuch, c++ wie man den Text in einer Zelle in Excel dreht
---

## **Text einer Zelle in Aspose.Cells drehen**

Aspose.Cells ist eine leistungsstarke C++-Komponente, die Entwicklern ermöglicht, Excel-Tabellen programmatisch zu bearbeiten. Eine der Funktionen von Aspose.Cells ist die Fähigkeit, Zellen zu rotieren, um die Ausrichtung des Textes anzupassen und die visuelle Darstellung Ihrer Daten zu verbessern. In diesem Dokument erfahren Sie, wie man Zellen mit Aspose.Cells rotiert.

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

Die [**Style.GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/)-Eigenschaft macht es bequem, Zellen zu drehen. Um Zellen in Aspose.Cells zu drehen, müssen Sie die folgenden Schritte befolgen:
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

## **C++ Beispielcode**

Bitte beachten Sie den folgenden Code, er erstellt ein Arbeitsmappenobjekt und setzt verschiedene Rotationswinkel für mehrere Zellen. Der Screenshot zeigt das Ergebnis nach der Ausführung des Beispielscodes.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetRotationOfCell.go" >}}
