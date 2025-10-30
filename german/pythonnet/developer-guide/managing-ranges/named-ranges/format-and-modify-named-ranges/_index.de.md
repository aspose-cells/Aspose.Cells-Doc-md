---
title: Benannte Bereiche formatieren und ändern
type: docs
weight: 85
url: /de/python-net/format-and-modify-named-ranges/
description: Dieser Artikel zeigt, wie man Namenbereiche formatiert und ändert, indem man die Aspose.Cells für Python via .NET API verwendet.
keywords: Python Excel Bibliothek, Python Namenbereiche formatieren und ändern, Hintergrundfarbe und Schriftattributen zu einem benannten Bereich festlegen, Rahmen zu einem benannten Bereich hinzufügen, einen benannten Bereich umbenennen, Vereinigung von Bereichen in Python, Schnittmenge von Bereichen in Python, Zellen in dem benannten Bereich verbinden in Python.
---

## **Bereiche formatieren**

### **Wie man Hintergrundfarbe und Schriftattributen zu einem benannten Bereich festlegt**

Um die Formatierung anzuwenden, definieren Sie ein [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekt, um die Formatierungseinstellungen anzugeben, und wenden Sie es auf das [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-Objekt an.

Das folgende Beispiel zeigt, wie die Füllfarbe (Hintergrundfarbe) mit Schrifteinstellungen für einen Bereich festgelegt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **Wie man einem benannten Bereich Rahmen hinzufügt**

Es ist möglich, Rahmen zu einem Bereich von Zellen hinzuzufügen, anstatt nur zu einer einzelnen Zelle. Das [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-Objekt bietet eine [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor)-Methode, die die folgenden Parameter verwendet, um einen Rahmen zum Zellenbereich hinzuzufügen:

- Rahmenart, die Art des Rahmens, ausgewählt aus der [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype)-Aufzählung.
- Linienstil, der Linienstil, ausgewählt aus der [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)-Aufzählung.
- Farbe, die Linienfarbe, ausgewählt aus der Farb-Aufzählung.

Im folgenden Beispiel wird gezeigt, wie einem Bereich ein Umrissrahmen gesetzt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **Wie man einen benannten Bereich umbenennt**

Aspose.Cells ermöglicht es Ihnen, einen benannten Bereich nach Bedarf umzubenennen. Sie können den benannten Bereich abrufen und umbenennen, indem Sie das [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text)-Attribut verwenden. Das folgende Beispiel zeigt, wie ein benannter Bereich umbenannt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **Wie man Schnittmenge von Bereichen erstellt**

Aspose.Cells bietet die [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range)-Methode zum Erstellen der Schnittmenge von Bereichen. Das folgende Beispiel zeigt, wie man die Schnittmenge von Bereichen erstellt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **Wie man die Bereiche schneidet**

Aspose.Cells bietet die [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range)-Methode, um zwei Bereiche zu schneiden. Die Methode gibt ein [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-Objekt zurück. Um zu überprüfen, ob ein Bereich einen anderen Bereich schneidet, verwenden Sie die [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range)-Methode, die einen booleschen Wert zurückgibt. Das folgende Beispiel zeigt, wie die Bereiche geschnitten werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **Wie man Zellen im benannten Bereich zusammenführt**

Aspose.Cells bietet die [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#)-Methode, um die Zellen im Bereich zusammenzuführen. Das folgende Beispiel zeigt, wie die einzelnen Zellen eines benannten Bereichs zusammengeführt werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
