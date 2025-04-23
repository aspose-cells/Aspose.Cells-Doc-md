---  
title: Rahmeneinstellungen
linktitle: Rahmeneinstellungen  
description: Wie man die Aspose.Cells Bibliothek in Node.js via C++ verwendet, um den Randstil und die Farbe von Zellen festzulegen. Durch Anpassen der Breite, des Stils und der Farbe des Rands erhalten Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.  
keywords: Aspose.Cells, Zellenrand Einstellungen, Node.js via C++, Randbreite, Randstil, Randfarbe  
type: docs  
weight: 40  
url: /de/nodejs-cpp/cells-border-settings/  
---  

## **Rahmen zu Zellen hinzufügen**  

Microsoft Excel ermöglicht es Benutzern, Zellen durch Hinzufügen von Rändern zu formatieren. Der Randtyp hängt davon ab, wo er hinzugefügt wird. Zum Beispiel ist ein oberer Rand einer, der an die obere Position einer Zelle gesetzt wird. Benutzer können auch den Linienstil und die Farbe der Ränder anpassen.  

Mit Aspose.Cells for Node.js via C++ können Entwickler Rahmen hinzufügen und das Aussehen in der gleichen flexiblen Weise wie in Microsoft Excel anpassen.  

### **Rahmen zu Zellen hinzufügen**  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)–Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet die [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse.  

Aspose.Cells bietet die [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)-Methode in der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse. Die [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)-Methode wird verwendet, um den Formatierungsstil einer Zelle festzulegen. Die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Klasse stellt Eigenschaften zum Hinzufügen von Rändern zu Zellen bereit.  

#### **Rahmen zu einer Zelle hinzufügen**  

Entwickler können Ränder zu einer Zelle hinzufügen, indem sie die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Eigenschaftensammlung des [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)-Objekts verwenden. Der Rahmentyp wird als Index an die [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)-Sammlung übergeben. Alle Rahmentypen sind in der [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype)-Aufzählung vorab definiert.  

**Rahmen-Aufzählung**  

|**Rahmentypen**|**Beschreibung**|  
| :- | :- |  
|BottomBorder|Eine untere Rahmenlinie  
|DiagonalDown|Eine diagonale Linie von oben links nach rechts unten  
|DiagonalUp|Eine diagonale Linie von unten links nach oben rechts|  
|LeftBorder|Eine Linie am linken Rand|  
|RightBorder|Eine Linie am rechten Rand|  
|TopBorder|Eine Linie am oberen Rand|  

Die [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)-Sammlung speichert alle Ränder. Jeder Rand in der [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)-Sammlung wird durch ein [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border)-Objekt repräsentiert, das zwei Eigenschaften, [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) und [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-), zur Festlegung der Linienfarbe und des Stils eines Rands bereitstellt.  

Um die Linienfarbe eines Rands festzulegen, wählen Sie eine Farbe aus der Color-Aufzählung (Teil von Node.js) und weisen Sie sie der Farbeigenschaft des Border-Objekts zu.  

Der Linienstil des Rands wird festgelegt, indem ein Linienstil aus der [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype)-Aufzählung ausgewählt wird.  

**Zellrahmentyp-Enumeration**  

|**Linienstile**|**Beschreibung**|  
| :- | :- |  
|DashDot|Dünne gestrichelt-punktierte Linie|  
|DashDotDot|Dünne gestrichelt-punkt-punktierte Linie|  
|Dashed|Gestrichelte Linie|  
|Dotted|Gepunktete Linie|  
|Double|Doppelte Linie|  
|Hair|Haarlinie|  
|MediumDashDot|Mittlere gestrichelt-punktierte Linie|  
|MediumDashDotDot|Mittlere gestrichelt-punkt-punktierte Linie|  
|MediumDashed|Mittlere gestrichelte Linie|  
|None|Keine Linie|  
|Medium|Mittlere Linie|  
|SlantedDashDot|Geneigte mittlere Strichpunktlinie|  
|Thick|Dicke Linie|  
|Thin|Dünne Linie|  
Wählen Sie einen der Linienstile aus und weisen Sie ihn der [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border)-Eigenschaft des [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-)-Objekts zu.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
Sie sollten sowohl den Linienstil als auch die Farbe gleichzeitig festlegen. Die beiden diagonalen Ränder sollten den gleichen Linienstil und die gleiche Farbe haben.  
{{% /alert %}}  

#### **Hinzufügen von Rahmen zu einem Zellenbereich**  

Es ist auch möglich, Ränder an einen Zellbereich statt nur an eine einzelne Zelle hinzuzufügen. Dazu erstellen Sie zunächst einen Zellbereich, indem Sie die [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung mit der [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-Methode aufrufen. Diese nimmt die folgenden Parameter:  

- Erste Zeile, die erste Zeile des Bereichs.  
- Erste Spalte, stellt die erste Spalte des Bereichs dar.  
- Anzahl der Zeilen, die Anzahl der Zeilen im Bereich.  
- Anzahl der Spalten, die Anzahl der Spalten im Bereich.  

Die [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-Methode gibt ein [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-Objekt zurück, das den angegebenen Zellbereich enthält. Das [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-Objekt bietet eine [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-)-Methode, die die folgenden Parameter akzeptiert, um einen Rand zum Zellbereich hinzuzufügen:  

- **Ramentyp**, der Randtyp, ausgewählt aus der [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype)-Aufzählung.  
- **Linienstil**, der Linienstil des Rands, ausgewählt aus der [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype)-Aufzählung.  
- **Farbe**, die aus der Farb-Aufzählung ausgewählte Linienfarbe.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


