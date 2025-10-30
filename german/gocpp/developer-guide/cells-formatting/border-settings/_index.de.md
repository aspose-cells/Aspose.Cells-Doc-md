---
title: Rahmeneinstellungen mit Golang via C++
linktitle: Rahmeneinstellungen
description: So verwenden Sie die Aspose.Cells Bibliothek in C++, um den Rahmenstil und die farbe von Zellen festzulegen. Durch Anpassen der Breite, des Stils und der Farbe des Rahmens haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Zellrahmeneinstellungen, C++, Rahmenbreite, Rahmenstil, Rahmenfarbe
type: docs
weight: 40
url: /de/go-cpp/cells-border-settings/
---

## **Rahmen zu Zellen hinzufügen**

Microsoft Excel ermöglicht es Benutzern, Zellen durch Hinzufügen von Rändern zu formatieren. Der Randtyp hängt davon ab, wo er hinzugefügt wird. Zum Beispiel ist ein oberer Rand einer, der an die obere Position einer Zelle gesetzt wird. Benutzer können auch den Linienstil und die Farbe der Ränder anpassen.

Mit Aspose.Cells können Entwickler Rahmen hinzufügen und anpassen, wie sie in der gleichen flexiblen Weise wie in Microsoft Excel aussehen.

### **Rahmen zu Zellen hinzufügen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)–Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse bietet die [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse.

Aspose.Cells bietet die [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)-Methode in der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse. Die [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)-Methode wird verwendet, um den Formatierungsstil einer Zelle festzulegen. Die [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Klasse stellt Eigenschaften zum Hinzufügen von Rändern zu Zellen bereit.

#### **Rahmen zu einer Zelle hinzufügen**

Entwickler können Ränder zu einer Zelle hinzufügen, indem sie die [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-Eigenschaftensammlung des [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)-Objekts verwenden. Der Rahmentyp wird als Index an die [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)-Sammlung übergeben. Alle Rahmentypen sind in der [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/)-Aufzählung vorab definiert.

**Rahmen-Aufzählung**

| **Rahmenarten** | **Beschreibung** |
|------------------|-----------------|
| UntererRahmen     | Eine untere Rahmenlinie |
| DiagonalLinksRechts | Eine diagonale Linie von oben links nach unten rechts |
| DiagonalRechtsLinks | Eine diagonale Linie von unten links nach oben rechts |
| LinkerRahmen     | Eine linke Rahmenlinie |
| RechterRahmen    | Eine rechte Rahmenlinie |
| ObererRahmen     | Eine obere Rahmenlinie |

Die [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)-Sammlung speichert alle Ränder. Jeder Rand in der [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)-Sammlung wird durch ein [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/)-Objekt repräsentiert, das zwei Eigenschaften, [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) und [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/), zur Festlegung der Linienfarbe und des Stils eines Rands bereitstellt.

Um die Linienfarbe eines Rahmens festzulegen, wählen Sie eine Farbe mit dem Enum Color aus und weisen Sie sie der Color-Eigenschaft des Rahmenobjekts zu.

Der Linienstil des Rands wird festgelegt, indem ein Linienstil aus der [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/)-Aufzählung ausgewählt wird.

**Zellrahmentyp-Enumeration**

| **Linienstile** | **Beschreibung** |
|------------------------|-------------------------------|
| DashDot          | Dünne gepunktete Linie |
| DashDotDot       | Dünne gepunktet-gestreifte Linie |
| Gestrichelt       | Gitterlinie |
| Gepunktet        | Gepunktete Linie |
| Doppel           | Doppellinie |
| Haar            | Haarlinie |
| MediumDashDot   | Mittlere dash-dot-Linie |
| MediumDashDotDot| Mittlere Dash-dot-gestreifte Linie |
| MittlereGestrichelt| Mittlere gestrichelte Linie |
| Keine           | Keine Linie |
| Mittel          | Mittlere Linie |
| SchrägDashDot   | Schräg gestreifte dash-dot-Linie |
| Dick            | Dicke Linie |
| Schmal          | Schmale Linie |

Wählen Sie einen der Linienstile aus und weisen Sie ihn der [**Border**](https://reference.aspose.com/cells/go-cpp/border/)-Eigenschaft des [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/)-Objekts zu.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

Sie sollten sowohl den Linienstil als auch die Farbe gleichzeitig festlegen. Die beiden diagonalen Ränder sollten den gleichen Linienstil und die gleiche Farbe haben.

{{% /alert %}}

#### **Hinzufügen von Rahmen zu einem Zellenbereich**

Es ist auch möglich, Ränder an einen Zellbereich statt nur an eine einzelne Zelle hinzuzufügen. Dazu erstellen Sie zunächst einen Zellbereich, indem Sie die [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/)-Sammlung mit der [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/)-Methode aufrufen. Diese nimmt die folgenden Parameter:

- Erste Zeile, die erste Zeile des Bereichs.
- Erste Spalte, stellt die erste Spalte des Bereichs dar.
- Anzahl der Zeilen, die Anzahl der Zeilen im Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Bereich.

Die [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/)-Methode gibt ein [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt zurück, das den angegebenen Zellbereich enthält. Das [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt bietet eine [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/)-Methode, die die folgenden Parameter akzeptiert, um einen Rand zum Zellbereich hinzuzufügen:

- **Ramentyp**, der Randtyp, ausgewählt aus der [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/)-Aufzählung.
- **Linienstil**, der Linienstil des Rands, ausgewählt aus der [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/)-Aufzählung.
- **Farbe**, die aus der Farb-Aufzählung ausgewählte Linienfarbe.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
