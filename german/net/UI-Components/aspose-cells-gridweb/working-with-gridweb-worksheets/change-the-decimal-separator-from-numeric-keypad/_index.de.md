---
title: Ändern Sie das Dezimaltrennzeichen vom Ziffernblock
type: docs
weight: 150
url: /de/net/change-the-decimal-separator-from-numeric-keypad/
---
## **Mögliche Nutzungsszenarien**
Standardmäßig zeigt Aspose.Cells.GridWeb numerische Daten entsprechend den lokalen/regionalen Einstellungen auf dem Computer an. Sie können das Dezimaltrennzeichen vom Ziffernblock programmgesteuert mit Aspose.Cells.GridWeb API ändern. Wenn also eine Datei in die GridWeb-Matrix importiert wird oder Sie einige numerische Daten (über den Ziffernblock) in eine neue Arbeitsblattzelle eingeben, sollte sie Ihre gewünschte Dezimalzahl haben Trennzeichen optisch gesetzt.
## **Ändern Sie das Dezimaltrennzeichen vom Ziffernblock**
Verwendung der**GridWorksheetCollection.NumberDecimalSeparator**-Eigenschaft können Sie das Dezimaltrennzeichen vom Ziffernblock programmgesteuert ändern. Bitte sehen Sie sich die Screenshots an, die zeigen, wie es funktioniert

![todo: Bild_alt_Text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo: Bild_alt_Text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Bitte beachten Sie, dass die Änderung des Dezimaltrennzeichens nur der visuellen Erfahrung der Benutzer in GridWeb dient. Wenn Sie Ihre Arbeitsmappe bearbeiten und speichern, werden die numerischen Werte (in der Tabelle) weiterhin gemäß Ihrem Gebietsschema/regionalen Dezimaltrennzeichen gespeichert.

{{% /alert %}}
