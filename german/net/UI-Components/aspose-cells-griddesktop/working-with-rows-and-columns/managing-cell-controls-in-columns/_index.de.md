---
title: Verwalten von Cell-Steuerelementen in Spalten
type: docs
weight: 100
url: /de/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

In diesem Thema werden einige wichtige Konzepte zum Verwalten von Zellsteuerelementen in Spalten mit Aspose.Cells.GridDesktop API erläutert. Wir erklären, wie Entwickler auf Zellsteuerelemente zugreifen, diese ändern und aus den Spalten ihrer Arbeitsblätter entfernen können. Lassen Sie uns einen Blick darauf werfen.

{{% /alert %}} 
## **Zugriff auf die Cell-Steuerung**
 Um auf ein vorhandenes Zellsteuerelement in der Spalte zuzugreifen und es zu ändern, können Entwickler die CellControl-Eigenschaft von a verwenden**Aspose.Cells.GridDesktop.Data.GridColumn** . Sobald auf ein Zellensteuerelement zugegriffen wird, können Entwickler seine Eigenschaften zur Laufzeit ändern. Für eine Instanz haben wir im unten angegebenen Beispiel auf eine vorhandene zugegriffen**Kontrollkästchen** Zellkontrolle von einem bestimmten**Aspose.Cells.GridDesktop.Data.GridColumn** und seine Checked-Eigenschaft geändert.

**WICHTIG:** Die CellControl-Eigenschaft stellt ein Zellensteuerelement in Form von bereit**CellControl**Objekt. Wenn Sie also beispielsweise auf eine bestimmte Art von Zellsteuerung zugreifen müssen**Kontrollkästchen** dann müssen Sie die typisieren**CellControl** widersprechen**Kontrollkästchen** Klasse.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Entfernen der Cell-Steuerung**
 Um ein vorhandenes Zellsteuerelement zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann**Entfernen** die Zellkontrolle aus der spezifischen Spalte mithilfe von**RemoveCellControl** Methode von**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 Jede Spalte in der**Säulen** Sammlung der**Arbeitsblatt** wird durch eine Instanz von dargestellt**Aspose.Cells.GridDesktop.Data.GridColumn** Klasse.

{{% /alert %}}
