---
title: Formel für benanntes Bereich setzen
type: docs
weight: 20
url: /de/python-net/setting-formula-for-named-range/
---

## **Formel für benanntes Bereich setzen**
Wie die Excel-Anwendung bieten die Aspose.Cells für Python via .NET APIs die Möglichkeit, eine Formel für einen benannten Bereich anzugeben, während Sie die [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to)-Eigenschaft verwenden. Es gibt zahlreiche Anwendungsfälle für dieses Feature, einige davon sind im Folgenden detailliert.
### **Eine einfache Formel für benannten Bereich setzen**
Eine einfache Formel könnte eine Referenz auf eine andere Zelle im gleichen (oder anderen) Arbeitsblatt sein. Das folgende Beispiel erstellt einen benannten Bereich in einem neuen Tabellenblatt und setzt seine Referenz auf eine andere Zelle.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **Eine komplexe Formel für benannten Bereich setzen**
Eine komplexe Formel könnte alles Mögliche sein, zum Beispiel ein dynamischer Bereich oder eine Formel über mehrere Zellen in verschiedenen Arbeitsblättern. Das folgende Beispiel erstellt einen dynamischen Bereich mit der INDEX-Funktion, um den Wert aus einer Liste basierend auf seiner Position zu erhalten.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



Hier ist ein weiteres Beispiel, das einen benannten Bereich verwendet, um Werte aus 2 Zellen in verschiedenen Arbeitsblättern zu summieren.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
