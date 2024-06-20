---
title: Verwaltung von Zellensteuerelementen in Spalten
type: docs
weight: 100
url: /de/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop, Steuerelemente, Steuerelement
description: In diesem Artikel wird erläutert, wie Steuerelement in Spalte GridDesktop festgelegt wird
---

{{% alert color="primary" %}} 

Dieses Thema erläutert einige wichtige Konzepte zur Verwaltung von Zellensteuerelementen in Spalten mithilfe der Aspose.Cells.GridDesktop-API. Wir werden erklären, wie Entwickler auf Zellensteuerelemente in ihren Arbeitsblättern zugreifen, diese ändern und entfernen können. Schauen wir uns das an

{{% /alert %}} 
## **Zugriff auf Zellensteuerelemente**
Um auf ein vorhandenes Zellensteuerelement in der Spalte zuzugreifen und es zu ändern, können Entwickler die CellControl-Eigenschaft einer **Aspose.Cells.GridDesktop.Data.GridColumn** verwenden. Sobald ein Zellensteuerelement zugegriffen wird, können Entwickler seine Eigenschaften zur Laufzeit ändern. Zum Beispiel haben wir im untenstehenden Beispiel auf ein vorhandenes **CheckBox**-Zellensteuerelement aus einer bestimmten **Aspose.Cells.GridDesktop.Data.GridColumn** zugegriffen und seine Checked-Eigenschaft geändert

**WICHTIG:** Die CellControl-Eigenschaft stellt ein Zellensteuerelement in Form eines **CellControl**-Objekts bereit. Wenn Sie beispielsweise auf einen bestimmten Typ von Zellensteuerelement, sagen wir **CheckBox**, zugreifen müssen, müssen Sie das **CellControl**-Objekt in die **CheckBox**-Klasse umwandeln



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Entfernen von Zellensteuerelementen**
Um ein vorhandenes Zellensteuerelement zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann das Zellensteuerelement aus einer bestimmten Spalte mithilfe der **RemoveCellControl**-Methode von **Aspose.Cells.GridDesktop.Data.GridColumn** entfernen



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Jede Spalte in der **Columns**-Sammlung des **Arbeitsblatts** wird durch eine Instanz der Klasse **Aspose.Cells.GridDesktop.Data.GridColumn** repräsentiert

{{% /alert %}}
