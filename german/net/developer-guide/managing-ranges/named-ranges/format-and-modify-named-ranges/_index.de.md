---
title: Benannte Bereiche formatieren und ändern
type: docs
weight: 85
url: /de/net/format-and-modify-named-ranges/
---
## **Formatbereiche**

### **Einstellen von Hintergrundfarbe und Schriftattributen auf einen benannten Bereich**

 Um eine Formatierung anzuwenden, definieren Sie a[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt, um die Stileinstellungen anzugeben und auf die anzuwenden[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range)Objekt.

Das folgende Beispiel zeigt, wie Sie die solide Füllfarbe (Schattierungsfarbe) mit Schriftarteinstellungen auf einen Bereich festlegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Rahmen zu einem benannten Bereich hinzufügen**

 Es ist möglich, statt nur einer einzelnen Zelle Rahmen zu einem Bereich von Zellen hinzuzufügen. Das[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt bietet a[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)Methode, die die folgenden Parameter verwendet, um dem Zellbereich einen Rahmen hinzuzufügen:

-  Rahmentyp, der Typ des Rahmens, ausgewählt aus der[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)Aufzählung.
-  Linienart, die Linienart, ausgewählt aus der[**CellRandType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)Aufzählung.
- Color, die Linienfarbe, ausgewählt aus der Color-Enumeration.

Das folgende Beispiel zeigt, wie Sie einen Gliederungsrahmen für einen Bereich festlegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

Das folgende Beispiel zeigt, wie Rahmen um jede Zelle im Bereich festgelegt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Benannten Bereich umbenennen**

 Aspose.Cells ermöglicht es Ihnen, einen benannten Bereich nach Bedarf umzubenennen. Sie können den benannten Bereich abrufen und ihn umbenennen, indem Sie verwenden[**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)Attribut. Das folgende Beispiel zeigt, wie Sie einen benannten Bereich umbenennen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Union der Bereiche**

 Aspose.Cells bietet[**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)Methode, um die Union für Bereiche zu nehmen, gibt die Methode an zurück[*Anordnungsliste*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)Objekt. Das folgende Beispiel zeigt, wie Union für Bereiche verwendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Schnittpunkt der Bereiche**

 Aspose.Cells bietet die[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) Methode, um zwei Bereiche zu schneiden. Die Methode gibt a zurück[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt. Um zu prüfen, ob ein Bereich einen anderen Bereich schneidet, verwenden Sie die[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)Methode, die einen booleschen Wert zurückgibt. Das folgende Beispiel zeigt, wie die Bereiche geschnitten werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Führen Sie Cells im benannten Bereich zusammen**

 Aspose.Cells bietet[**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)Methode zum Zusammenführen der Zellen im Bereich. Das folgende Beispiel zeigt, wie die einzelnen Zellen eines benannten Bereichs zusammengeführt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Entfernen Sie einen benannten Bereich**

 Aspose.Cells bietet die[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) Methode, um den Namen des Bereichs zu löschen. Um den Inhalt des Bereichs zu löschen, verwenden Sie[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)Methode. Das folgende Beispiel zeigt, wie ein benannter Bereich mit seinem Inhalt entfernt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
