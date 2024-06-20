---
title: Formel für benanntes Bereich setzen
type: docs
weight: 20
url: /de/net/setting-formula-for-named-range/
---

## **Formel für benanntes Bereich setzen**
Wie die Excel-Anwendung bieten auch die Aspose.Cells APIs die Möglichkeit, eine Formel für einen benannten Bereich spezifisch zu benennen und dabei die [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)-Eigenschaft zu verwenden. Es gibt zahlreiche Anwendungsszenarien für diese Funktion, von denen einige im Folgenden näher erläutert werden.
### **Eine einfache Formel für benannten Bereich setzen**
Eine einfache Formel könnte eine Referenz auf eine andere Zelle im gleichen (oder anderen) Arbeitsblatt sein. Das folgende Beispiel erstellt einen benannten Bereich in einem neuen Tabellenblatt und setzt seine Referenz auf eine andere Zelle.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Eine komplexe Formel für benannten Bereich setzen**
Eine komplexe Formel könnte alles Mögliche sein, zum Beispiel ein dynamischer Bereich oder eine Formel über mehrere Zellen in verschiedenen Arbeitsblättern. Das folgende Beispiel erstellt einen dynamischen Bereich mit der INDEX-Funktion, um den Wert aus einer Liste basierend auf seiner Position zu erhalten.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Hier ist ein weiteres Beispiel, das einen benannten Bereich verwendet, um Werte aus 2 Zellen in verschiedenen Arbeitsblättern zu summieren.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
