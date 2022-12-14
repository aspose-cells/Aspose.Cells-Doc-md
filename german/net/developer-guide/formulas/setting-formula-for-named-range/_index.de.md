---
title: Einstellungsformel für den benannten Bereich
type: docs
weight: 20
url: /de/net/setting-formula-for-named-range/
---
## **Einstellungsformel für den benannten Bereich**
 Wie die Excel-Anwendung bieten Aspose.Cells-APIs die Möglichkeit, eine Formel für einen benannten Bereich anzugeben, während sie verwendet werden[Bezieht sich auf](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)Eigentum. Es könnte zahlreiche Nutzungsszenarien für diese Funktion geben, von denen einige im Folgenden detailliert beschrieben werden.
### **Festlegen einer einfachen Formel für einen benannten Bereich**
Eine einfache Formel könnte ein Verweis auf eine andere Zelle in demselben (oder einem anderen) Arbeitsblatt sein. Das folgende Beispiel erstellt einen benannten Bereich in einer neuen Tabelle und legt seinen Verweis auf eine andere Zelle fest.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Festlegen einer komplexen Formel für einen benannten Bereich**
Eine komplexe Formel kann beispielsweise ein dynamischer Bereich oder eine Formel sein, die sich über mehrere Zellen in verschiedenen Arbeitsblättern erstreckt. Im folgenden Beispiel wird mithilfe der INDEX-Funktion ein dynamischer Bereich erstellt, um den Wert anhand seiner Position aus einer Liste abzurufen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Hier ist ein weiteres Beispiel, das einen benannten Bereich verwendet, um Werte aus 2 Zellen in verschiedenen Arbeitsblättern zu summieren.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
