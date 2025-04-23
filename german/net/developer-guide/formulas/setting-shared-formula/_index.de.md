---
title: Einstellung gemeinsamer Formel
type: docs
weight: 10
url: /de/net/setting-shared-formula/
---

{{% alert color="primary" %}}

Wenn Sie eine Funktion im Arbeitsblatt hinzufügen möchten, die einige Berechnungen durchführt, erläutert dieser Artikel, wie Sie diese Aufgabe mit Aspose.Cells erreichen können.

{{% /alert %}}

## Gemeinsame Formel mit Aspose.Cells festlegen

Angenommen, Sie haben ein Arbeitsblatt mit Daten im Format, das wie das folgende Beispieldatenblatt aussieht.

|**Eingabedatei mit einer Spalte oder Daten**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Sie möchten eine Funktion in B2 hinzufügen, die die Umsatzsteuer für die erste Datensatzreihe berechnet. Die Steuer beträgt **9%**. Die Formel zur Berechnung der Umsatzsteuer lautet: **"=A2*0,09"**. In diesem Artikel wird erläutert, wie diese Formel mit Aspose.Cells angewendet wird.

Mit Aspose.Cells können Sie eine Formel mit der Eigenschaft [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) angeben. Es gibt zwei Optionen, um Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte hinzuzufügen.

Entweder tun Sie das, was Sie für die erste Zelle getan haben, und setzen die Formel für jede Zelle ein, wobei der Zellbezug entsprechend aktualisiert wird (A3*0.09, A4*0.09, A5*0.09 usw.). Dies erfordert, dass die Zellbezüge für jede Zeile aktualisiert werden. Es erfordert auch, dass Aspose.Cells jede Formel einzeln analysiert, was bei großen Tabellenkalkulationen und komplexen Formeln zeitaufwändig sein kann. Es fügt auch zusätzliche Zeilen von Codes hinzu, obwohl Schleifen diese etwas reduzieren können.

Ein anderer Ansatz ist die Verwendung einer **gemeinsamen Formel**. Mit einer gemeinsamen Formel werden die Formeln automatisch für die Zellbezüge in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Die Methode [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
