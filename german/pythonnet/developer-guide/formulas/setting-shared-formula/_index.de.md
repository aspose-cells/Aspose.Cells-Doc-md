---
title: Einstellung gemeinsamer Formel
type: docs
weight: 10
url: /de/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

Wenn Sie eine Funktion in einem Arbeitsblatt hinzufügen möchten, die einige Berechnungen durchführt, erklärt dieser Artikel, wie Sie diese Aufgabe mit Aspose.Cells für Python via .NET erreichen können.

{{% /alert %}}

## Gemeinsame Formel mit Aspose.Cells für Python via .NET setzen

Angenommen, Sie haben ein Arbeitsblatt mit Daten im Format, das wie das folgende Beispieldatenblatt aussieht.

|**Eingabedatei mit einer Spalte oder Daten**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Sie möchten eine Funktion in B2 hinzufügen, die die Verkaufssteuer für die erste Datensatzzeile berechnet. Die Steuer beträgt **9%**. Die Formel, die die Verkaufssteuer berechnet, lautet: **"=A2*0.09"**. Dieser Artikel erklärt, wie man diese Formel mit Aspose.Cells für Python via .NET anwendet.

Aspose.Cells für Python via .NET ermöglicht es, eine Formel mit der [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula)-Eigenschaft anzugeben. Es gibt zwei Optionen, um Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte hinzuzufügen.

Entweder machen Sie bei der ersten Zelle dasselbe wie zuvor, indem Sie effektiv die Formel für jede Zelle festlegen und die Zellreferenz entsprechend aktualisieren (A3*0.09, A4*0.09, A5*0.09 usw.). Dies erfordert, dass die Zellreferenzen für jede Zeile aktualisiert werden. Es erfordert auch, dass Aspose.Cells für Python via .NET jede Formel einzeln parst, was bei großen Tabellenkalkulationen und komplexen Formeln zeitaufwendig sein kann. Es fügt auch zusätzliche Codezeilen hinzu, obwohl Schleifen dies etwas reduzieren können.

Ein anderer Ansatz ist die Verwendung einer **gemeinsamen Formel**. Mit einer gemeinsamen Formel werden die Formeln automatisch für die Zellbezüge in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Die Methode [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
