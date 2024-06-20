---
title: Benannte Bereiche formatieren und ändern
type: docs
weight: 85
url: /de/net/format-and-modify-named-ranges/
---

## **Bereiche formatieren**

### **Hintergrundfarbe und Schriftattributen für einen benannten Bereich einstellen**

Um die Formatierung anzuwenden, definieren Sie ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt, um die Formatierungseinstellungen anzugeben, und wenden Sie es auf das [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-Objekt an.

Das folgende Beispiel zeigt, wie die Füllfarbe (Hintergrundfarbe) mit Schrifteinstellungen für einen Bereich festgelegt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Hinzufügen von Rahmen zu einem benannten Bereich**

Es ist möglich, Rahmen zu einem Bereich von Zellen hinzuzufügen, anstatt nur zu einer einzelnen Zelle. Das [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-Objekt bietet eine [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)-Methode, die die folgenden Parameter verwendet, um einen Rahmen zum Zellenbereich hinzuzufügen:

- Rahmenart, die Art des Rahmens, ausgewählt aus der [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)-Aufzählung.
- Linienstil, der Linienstil, ausgewählt aus der [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)-Aufzählung.
- Farbe, die Linienfarbe, ausgewählt aus der Farb-Aufzählung.

Im folgenden Beispiel wird gezeigt, wie einem Bereich ein Umrissrahmen gesetzt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

Das folgende Beispiel zeigt, wie Rahmen um jede Zelle im Bereich festgelegt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Benannten Bereich umbenennen**

Aspose.Cells ermöglicht es Ihnen, einen benannten Bereich nach Bedarf umzubenennen. Sie können den benannten Bereich abrufen und umbenennen, indem Sie das [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)-Attribut verwenden. Das folgende Beispiel zeigt, wie ein benannter Bereich umbenannt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Vereinigung von Bereichen**

Aspose.Cells stellt die [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)-Methode bereit, um die Vereinigung von Bereichen vorzunehmen. Die Methode gibt ein [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)-Objekt zurück. Das folgende Beispiel zeigt, wie die Vereinigung von Bereichen erfolgt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Schnittmenge von Bereichen**

Aspose.Cells bietet die [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)-Methode, um zwei Bereiche zu schneiden. Die Methode gibt ein [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-Objekt zurück. Um zu überprüfen, ob ein Bereich einen anderen Bereich schneidet, verwenden Sie die [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)-Methode, die einen booleschen Wert zurückgibt. Das folgende Beispiel zeigt, wie die Bereiche geschnitten werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Zellen im benannten Bereich zusammenführen**

Aspose.Cells bietet die [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)-Methode, um die Zellen im Bereich zusammenzuführen. Das folgende Beispiel zeigt, wie die einzelnen Zellen eines benannten Bereichs zusammengeführt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Einen benannten Bereich entfernen**

Aspose.Cells stellt die [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat)-Methode bereit, um den Namen des Bereichs zu löschen. Verwenden Sie die [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)-Methode, um den Inhalt des Bereichs zu löschen. Das folgende Beispiel zeigt, wie ein benannter Bereich mit seinem Inhalt entfernt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
