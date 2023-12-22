---
title: So drehen Sie den Text von Cell
type: docs
weight: 80
url: /de/net/how-to-rotate-text-of-cell/
description: C#-Code zum Drehen des Textes von Cell mit Aspose.Cells for .NET API
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **Drehen Sie den Text von Cell in Aspose.Cells**

Aspose.Cells ist eine leistungsstarke .NET- und Java-Komponente, die es Entwicklern ermöglicht, programmgesteuert mit Excel-Tabellen zu arbeiten. Eine der Funktionen von Aspose.Cells ist die Möglichkeit, Zellen zu drehen, sodass Sie die Textausrichtung anpassen und die visuelle Darstellung Ihrer Daten verbessern können. In diesem Dokument erfahren Sie, wie Sie Zellen mit Aspose.Cells drehen.

##  **So drehen Sie den Text von Cell in Excel**
Um eine Zelle in Excel zu drehen, können Sie die folgenden Schritte ausführen:
1. Öffnen Sie Excel und wählen Sie die Zelle oder den Zellbereich aus, die Sie drehen möchten.
1. Klicken Sie mit der rechten Maustaste auf die ausgewählte(n) Zelle(n) und wählen Sie im Kontextmenü „Format Cells“. Alternativ können Sie im Excel-Menüband zur Registerkarte „Startseite“ gehen, in der Gruppe „Cells“ auf das Dropdown-Menü „Format“ klicken und „Cells formatieren“ auswählen.
1. Navigieren Sie im Dialogfeld „Format Cells“ zur Registerkarte „Ausrichtung“.
1. Im Abschnitt „Ausrichtung“ sehen Sie die Optionen zum Drehen des Textes. Im Feld „Grad“ können Sie direkt den gewünschten Drehwinkel in Grad eingeben. Positive Werte drehen den Text gegen den Uhrzeigersinn, negative Werte drehen ihn im Uhrzeigersinn.
<br>
![todo:image_alt_text](alignment.png)
1. Nachdem Sie die gewünschte Drehung ausgewählt haben, klicken Sie auf „OK“, um die Änderungen zu übernehmen. Die ausgewählten Zellen werden nun basierend auf dem von Ihnen gewählten Drehwinkel oder der gewählten Ausrichtung gedreht.

##  **So drehen Sie den Text von Cell mit Aspose.Cells API**

[**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/) Die Eigenschaft erleichtert das Drehen von Zellen. Um Zellen in Aspose.Cells zu drehen, müssen Sie die folgenden Schritte ausführen:
1. Laden Sie die Excel-Arbeitsmappe
<br>
 Zuerst müssen Sie die Excel-Arbeitsmappe mit Aspose.Cells laden. Mit der Workbook-Klasse können Sie eine vorhandene Excel-Datei öffnen oder eine neue erstellen.

1. Greifen Sie auf das Arbeitsblatt zu
<br>
Sobald die Arbeitsmappe geladen ist, müssen Sie auf das Arbeitsblatt zugreifen, in dem Sie die Zellen drehen möchten. Sie können entweder über den Index oder den Namen auf das Arbeitsblatt zugreifen.

1. Drehen Sie den Text von Cell
<br>
 Da Sie nun Zugriff auf das Arbeitsblatt haben, können Sie die Zellen drehen, indem Sie das Style-Objekt der gewünschten Zellen ändern. Mit dem Style-Objekt können Sie verschiedene Formatierungsoptionen festlegen, einschließlich der Drehung.

1. Speichern Sie die Arbeitsmappe
<br>
Nachdem Sie die Zellen gedreht haben, können Sie die geänderte Arbeitsmappe mithilfe der Save-Methode wieder in einer Datei oder einem Stream speichern.

##  **C# Beispielcode**

Bitte sehen Sie sich den folgenden Code an. Er erstellt ein Arbeitsmappenobjekt und legt unterschiedliche Drehwinkel für mehrere Zellen fest. Der Screenshot zeigt das Ergebnis nach der Ausführung des Beispielcodes.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
