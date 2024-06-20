---
title: Füge Zellenformeln hinzu
type: docs
weight: 30
url: /de/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb,formel
description: Dieser Artikel zeigt, wie man Formeln in Zellen in GridWeb hinzufügt.
---

{{% alert color="primary" %}} 

Das wertvollste Feature, das von Aspose.Cells.GridWeb angeboten wird, ist die Unterstützung von Formeln oder Funktionen. Aspose.Cells.GridWeb verfügt über seinen eigenen Formel-Engine, die die Formeln in Arbeitsblättern berechnet. Aspose.Cells.GridWeb unterstützt sowohl eingebaute als auch benutzerdefinierte Funktionen oder Formeln. Dieses Thema erläutert ausführlich, wie Formeln mithilfe der Aspose.Cells.GridWeb-API zu Zellen hinzugefügt werden.

{{% /alert %}} 
## **Hinzufügen von Formeln zu Zellen**
### **Wie füge ich eine Formel hinzu und berechne sie?**
Es ist möglich, Formeln in Zellen hinzuzufügen, darauf zuzugreifen und sie zu ändern, indem man die Eigenschaft Formula einer Zelle verwendet. Aspose.Cells.GridWeb unterstützt benutzerdefinierte Formeln von einfach bis komplex. Allerdings sind auch eine große Anzahl von integrierten Funktionen oder Formeln (ähnlich wie in Microsoft Excel) in Aspose.Cells.GridWeb enthalten. Um die vollständige Liste der integrierten Funktionen zu sehen, verweisen Sie bitte auf diese [Liste der unterstützten Funktionen.](/cells/de/net/aspose-cells-gridweb/list-of-supported-functions/)

{{% alert color="primary" %}} 

Die Formelsyntax muss mit der Microsoft Excel-Syntax kompatibel sein. Alle Formeln müssen beispielsweise mit einem Gleichheitszeichen (=) beginnen.

Um eine Formel dynamisch hinzuzufügen, wird diese von Aspose.Cells.GridWeb auch erkannt, wenn Sie kein **=**-Zeichen verwenden. Wenn Endbenutzer jedoch in der GUI arbeiten, müssen sie das "="-Zeichen verwenden.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formel zu Zelle B3 hinzugefügt, aber nicht durch GridWeb berechnet** 

![todo:image_alt_text](add-cell-formulas_1.png)

Im obigen Screenshot ist zu sehen, dass eine Formel zu B3 hinzugefügt, aber noch nicht berechnet wurde. Um alle Formeln zu berechnen, rufen Sie die Methode CalculateFormula der GridWeb-Steuerung GridWorksheetCollection auf, nachdem Sie Formeln zu Arbeitsblättern hinzugefügt haben, wie unten gezeigt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

Benutzer können auch Formeln durch Klicken auf **Senden** berechnen.

**Klicken Sie auf die Schaltfläche Senden von GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**WICHTIG**: Wenn ein Benutzer auf die Schaltflächen **Speichern** oder **Rückgängig** oder auf die Blattregisterkarten klickt, werden alle Formeln automatisch von GridWeb berechnet.

**Formelergebnis nach Berechnung** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Bezugnahme auf Zellen aus anderen Arbeitsblättern**
Mit Aspose.Cells.GridWeb ist es möglich, Werte in verschiedenen Arbeitsblättern in ihren Formeln zu referenzieren und komplexe Formeln zu erstellen.

Die Syntax zum Referenzieren eines Zellwerts aus einem anderen Arbeitsblatt lautet Arbeitsblattname!Zellenname.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
