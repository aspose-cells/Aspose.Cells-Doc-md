---
title: Arbeitsblätter hinzufügen
type: docs
weight: 20
url: /de/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: In diesem Artikel wird erläutert, wie Arbeitsblätter (GridWorksheet) in GridWeb hinzugefügt werden.
---

{{% alert color="primary" %}} 

Arbeitsblätter sind ein integraler Bestandteil von Aspose.Cells.GridWeb. Alle Daten werden in Form von Arbeitsblättern verwaltet und gespeichert. Aspose.Cells.GridWeb ermöglicht Entwicklern, ein oder mehrere Arbeitsblätter der Aspose.Cells.GridWeb-Steuerung hinzuzufügen. Dieses Thema zeigt einfache Ansätze zum Hinzufügen von Arbeitsblättern zu Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Ein Arbeitsblatt hinzufügen**
### **Ohne Angabe des Blattnamens**
Der einfachste Weg, ein Arbeitsblatt zu Aspose.Cells.GridWeb hinzuzufügen, besteht darin, die Add-Methode der GridWorksheetCollection-Steuerung in der GridWeb-Steuerung aufzurufen. Dadurch werden Arbeitsblätter mit Standardnamen (wie Blatt1, Blatt2, Blatt3 usw.) erstellt und der GridWeb-Steuerung hinzugefügt.

**Ausgabe: Ein Arbeitsblatt mit Standardnamen wurde zu GridWeb hinzugefügt** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Die Add-Methode gibt den Index des neuen Arbeitsblatts zurück, der verwendet werden kann, um auf die Instanz dieses Arbeitsblatts zuzugreifen. Für weitere Details zum Zugriff auf Arbeitsblätter, lesen Sie [Arbeitsblätter zugreifen](/cells/de/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 
### **Mit angegebenem Blattnamen**
Um ein Arbeitsblatt mit einem bestimmten Namen zum GridWeb-Control hinzuzufügen, anstatt das Standardbenennungsschema zu verwenden, rufen Sie eine überlastete Version der Add-Methode auf, die den angegebenen SheetName verwendet. Zum Beispiel fügt das folgende Beispiel ein Arbeitsblatt mit dem Namen Rechnung hinzu.

**Ausgabe: Ein Arbeitsblatt mit angegebenem Namen wurde zu GridWeb hinzugefügt** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Die Add-Methode, die den Arbeitsblattnamen als Zeichenfolge akzeptiert, gibt eine Instanz von GridWorksheet zurück.

{{% /alert %}}
