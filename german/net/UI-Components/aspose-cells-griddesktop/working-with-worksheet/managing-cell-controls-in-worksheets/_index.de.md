---
title: Verwalten von Zellensteuerelementen in Arbeitsblättern
type: docs
weight: 130
url: /de/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop,Zellensteuerung,Steuerung,Steuerelemente
description: Dieser Artikel stellt vor, wie mit Zellensteuerelementen in GridDesktop gearbeitet wird.
---

{{% alert color="primary" %}} 

In diesem Thema werden einige wichtige Konzepte zum Verwalten von Zellensteuerelementen mithilfe der API von Aspose.Cells.GridDesktop erläutert. Es wird erklärt, wie Entwickler auf Zellensteuerelemente zugreifen, diese modifizieren und aus ihren Arbeitsblättern entfernen können. Sehen wir uns das an.

{{% /alert %}} 
## **Zugriff auf Zellensteuerelemente**
Um auf ein vorhandenes Zellensteuerelement im Arbeitsblatt zuzugreifen und es zu modifizieren, können Entwickler ein bestimmtes Zellensteuerelement aus der **Controls**-Sammlung des **Arbeitsblatts** zugreifen, indem sie die Zelle angeben, in der das Zellensteuerelement angezeigt wird (unter Verwendung des Zellnamens oder seiner Position in Bezug auf Zeilen- und Spaltennummern). Sobald ein Zellensteuerelement zugegriffen wurde, können Entwickler dessen Eigenschaften zur Laufzeit modifizieren. In dem unten gegebenen Beispiel haben wir beispielsweise ein vorhandenes **CheckBox**-Zellensteuerelement aus dem **Arbeitsblatt** abgerufen und seine Checked-Eigenschaft geändert.

**WICHTIG:** Die **Controls**-Sammlung enthält alle Arten von Zellensteuerelementen in Form von **CellControl**-Objekten. Wenn Sie also auf einen bestimmten Typ von Zellensteuerelement zugreifen möchten, z.B. **CheckBox**, müssen Sie das **CellControl**-Objekt in die **CheckBox**-Klasse umwandeln.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Entfernen von Zellensteuerelementen**
Um ein vorhandenes Zellensteuerelement zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann das Zellensteuerelement aus der **Controls**-Sammlung des **Worksheet** entfernen, indem sie die Zelle (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer) angeben, die das Zellensteuerelement enthält.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
