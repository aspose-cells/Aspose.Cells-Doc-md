---  
title: Wie man Text in einer Zelle dreht
linktitle: Wie man Text in einer Zelle dreht  
type: docs  
weight: 80  
url: /de/nodejs-cpp/how-to-rotate-text-of-cell/  
description: Lernen Sie, wie Sie den Text einer Zelle programmatisch mit Aspose.Cells for Node.js via C++ rotieren.  
keywords: node.js Drehung des Textes in Zelle, Node.js Programm, um den Text in Zelle im Arbeitsbuch programmatisch zu drehen, programmatisch den Drehwinkel der Zelle im Arbeitsbuch festlegen, Node.js wie man Text in Excel Zelle dreht  
---  

## **Textrotation in Zelle bei Aspose.Cells for Node.js via C++**

Aspose.Cells ist eine leistungsstarke Node.js-Komponente, die es Entwicklern ermöglicht, mit Excel-Tabellen programmatisch zu arbeiten. Eine der Funktionen von Aspose.Cells ist die Möglichkeit, Zellen zu drehen, sodass Sie die Orientierung des Textes anpassen und die visuelle Präsentation Ihrer Daten verbessern können. In diesem Dokument werden wir erkunden, wie man Zellen mit Aspose.Cells rotiert.

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

Die [**Style.setRotationAngle(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-)-Eigenschaft macht es bequem, Zellen zu drehen. Um Zellen in Aspose.Cells zu drehen, müssen Sie die folgenden Schritte befolgen:
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

## **Beispielcode für Node.js**

Bitte sehen Sie sich den folgenden Code an, er erstellt ein Arbeitsbuch-Objekt und setzt verschiedene Drehwinkel für mehrere Zellen. Der Screenshot zeigt das Ergebnis nach Ausführung des Beispielcodes.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-SetRotationOfCell.js" >}}


