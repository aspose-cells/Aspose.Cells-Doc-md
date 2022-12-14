---
title: Arbeitsblätter hinzufügen
type: docs
weight: 20
url: /de/net/add-worksheets/
---
{{% alert color="primary" %}} 

Arbeitsblätter sind fester Bestandteil von Aspose.Cells.GridWeb. Alle Daten werden in Form von Arbeitsblättern verwaltet und gespeichert. Aspose.Cells.GridWeb ermöglicht Entwicklern das Hinzufügen eines oder mehrerer Arbeitsblätter zum Aspose.Cells.GridWeb-Steuerelement. Dieses Thema zeigt einfache Ansätze zum Hinzufügen von Arbeitsblättern zu Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Hinzufügen eines Arbeitsblatts**
### **Ohne Angabe des Blattnamens**
Die einfachste Methode zum Hinzufügen eines Arbeitsblatts zu Aspose.Cells.GridWeb besteht darin, die Add-Methode der GridWorksheetCollection-Auflistung im GridWeb-Steuerelement aufzurufen. Dadurch werden Arbeitsblätter erstellt, die Standardnamen verwenden (dh Sheet1, Sheet2, Sheet3 usw.) und dem GridWeb-Steuerelement hinzugefügt.

**Ausgabe: GridWeb wurde ein Arbeitsblatt mit Standardnamen hinzugefügt** 

![todo: Bild_alt_Text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 Die Add-Methode gibt den Index des neuen Arbeitsblatts zurück, der verwendet werden kann, um auf die Instanz dieses Arbeitsblatts zuzugreifen. Weitere Informationen zum Zugriff auf Arbeitsblätter finden Sie unter[Greifen Sie auf Arbeitsblätter zu](/cells/de/net/access-worksheets/).

{{% /alert %}} 
### **Mit angegebenem Blattnamen**
Um dem GridWeb-Steuerelement ein Arbeitsblatt mit einem bestimmten Namen hinzuzufügen, anstatt das standardmäßige Benennungsschema zu verwenden, rufen Sie eine überladene Version der Add-Methode auf, die den angegebenen SheetName annimmt. Für eine Instanz fügt das folgende Beispiel ein Arbeitsblatt mit dem Namen Invoice hinzu.

**Ausgabe: GridWeb wurde ein Arbeitsblatt mit einem bestimmten Namen hinzugefügt** 

![todo: Bild_alt_Text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Die Add-Methode, die den Arbeitsblattnamen als Zeichenfolge akzeptiert, gibt eine Instanz von GridWorksheet zurück.

{{% /alert %}}
