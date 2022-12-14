---
title: Freigegebene Formel einstellen
type: docs
weight: 10
url: /de/net/setting-shared-formula/
---
{{% alert color="primary" %}}

Wenn Sie eine Funktion im Arbeitsblatt hinzufügen möchten, die einige Berechnungen durchführt. In diesem Artikel wird erläutert, wie Sie diese Aufgabe mit Aspose.Cells ausführen.

{{% /alert %}}

## Gemeinsame Formel mit Aspose.Cells einstellen

Angenommen, Sie haben ein Arbeitsblatt, das mit Daten im Format gefüllt ist, das wie das folgende Beispielarbeitsblatt aussieht.

|**Eingabedatei mit einer Spalte oder Daten**|
|:- |
|![todo: Bild_alt_Text](setting-shared-formula_1.png)|

 Sie möchten eine Funktion in B2 hinzufügen, die die Mehrwertsteuer für die erste Datenzeile berechnet. Die Steuer ist**9%** . Die Formel zur Berechnung der Umsatzsteuer lautet:**"=A2*0,09"**. Dieser Artikel erklärt, wie man diese Formel mit Aspose.Cells anwendet.

 Aspose.Cells lässt Sie eine Formel mit angeben[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)Eigentum. Es gibt zwei Optionen zum Hinzufügen von Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte.

Machen Sie entweder das, was Sie für die erste Zelle getan haben, indem Sie effektiv die Formel für jede Zelle festlegen und die Zellreferenz entsprechend aktualisieren (A3*0,09, A4*0,09, A5*0,09 usw.). Dazu müssen die Zellbezüge für jede Zeile aktualisiert werden. Es erfordert auch Aspose.Cells, um jede Formel einzeln zu analysieren, was bei großen Tabellenkalkulationen und komplexen Formeln zeitaufwändig sein kann. Es fügt auch zusätzliche Codezeilen hinzu, obwohl Schleifen sie etwas reduzieren können.

 Ein anderer Ansatz ist die Verwendung von a**gemeinsame Formel** . Bei einer freigegebenen Formel werden die Formeln automatisch für die Zellbezüge in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Das[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)Methode ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
