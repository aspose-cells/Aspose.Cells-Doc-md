---
title: Fügen Sie Cell Formeln hinzu
type: docs
weight: 30
url: /de/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

Das wertvollste Feature, das Aspose.Cells.GridWeb bietet, ist die Unterstützung von Formeln oder Funktionen. Aspose.Cells. GridWeb hat eine eigene Formel-Engine, die die Formeln in Arbeitsblättern berechnet. Aspose.Cells. GridWeb unterstützt sowohl eingebaute als auch benutzerdefinierte Funktionen oder Formeln. In diesem Thema wird das Hinzufügen von Formeln zu Zellen mithilfe von Aspose.Cells. GridWeb API im Detail erläutert.

{{% /alert %}} 
## **Formeln zu Cells hinzufügen**
### **Wie fügt man eine Formel hinzu und berechnet sie?**
 Es ist möglich, Formeln in Zellen hinzuzufügen, darauf zuzugreifen und sie zu ändern, indem Sie die Formeleigenschaft einer Zelle verwenden. Aspose.Cells.GridWeb unterstützt benutzerdefinierte Formeln von einfach bis komplex. Aber auch eine Vielzahl eingebauter Funktionen oder Formeln (ähnlich Microsoft Excel) werden mit Aspose.Cells.GridWeb mitgeliefert. Die vollständige Liste der integrierten Funktionen finden Sie hier[Liste der unterstützten Funktionen.](/cells/de/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Die Formelsyntax sollte mit der Excel-Syntax Microsoft kompatibel sein. Beispielsweise müssen alle Formeln mit einem Gleichheitszeichen (=) beginnen.

Um eine Formel dynamisch hinzuzufügen, wird Aspose.Cells.GridWeb sie als Formel erkennen, auch wenn Sie kein **=**-Zeichen verwenden, aber wenn Endbenutzer in der GUI arbeiten, müssen sie das Zeichen „=“ verwenden.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formel zur B3-Zelle hinzugefügt, aber nicht von GridWeb berechnet** 

![todo: Bild_alt_Text](add-cell-formulas_1.png)

Im obigen Screenshot sehen Sie, dass eine Formel zu B3 hinzugefügt, aber noch nicht berechnet wurde. Um alle Formeln zu berechnen, rufen Sie die CalculateFormula-Methode der GridWorksheetCollection des GridWeb-Steuerelements auf, nachdem Sie wie unten gezeigt Formeln zu Arbeitsblättern hinzugefügt haben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

 Benutzer können Formeln auch durch Klicken berechnen**einreichen**.

**Klicken Sie auf die Schaltfläche Senden von GridWeb** 

![todo: Bild_alt_Text](add-cell-formulas_2.png)

**WICHTIG** : Wenn ein Benutzer auf die klickt**Speichern** oder**Rückgängig machen** Schaltflächen oder die Blattregisterkarten werden alle Formeln von GridWeb automatisch berechnet.

**Formelergebnis nach Berechnung** 

![todo: Bild_alt_Text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Verweis auf Cells aus anderen Arbeitsblättern**
Mit Aspose.Cells.GridWeb ist es möglich, auf in verschiedenen Arbeitsblättern gespeicherte Werte in ihren Formeln zu verweisen und komplexe Formeln zu erstellen.

Die Syntax zum Verweisen auf einen Zellenwert aus einem anderen Arbeitsblatt lautet SheetName!CellName.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
