---
title: Verwalten von Cell-Steuerelementen in Arbeitsblättern
type: docs
weight: 130
url: /de/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

In diesem Thema werden einige wichtige Konzepte zum Verwalten von Zellsteuerelementen mit API von Aspose.Cells.GridDesktop erläutert. Wir werden erklären, wie Entwickler auf Zellsteuerelemente zugreifen, sie ändern und aus ihren Arbeitsblättern entfernen können. Lassen Sie uns einen Blick darauf werfen.

{{% /alert %}} 
## **Zugriff auf die Cell-Steuerung**
 Um auf ein vorhandenes Zellsteuerelement im Arbeitsblatt zuzugreifen und es zu ändern, können Entwickler über das auf ein bestimmtes Zellsteuerelement zugreifen**Kontrollen** Sammlung der**Arbeitsblatt** durch Angabe der Zelle (unter Verwendung des Zellennamens oder seiner Position in Form von Zeilen- und Spaltennummern), in der das Zellensteuerelement angezeigt wird. Sobald auf ein Zellensteuerelement zugegriffen wird, können Entwickler seine Eigenschaften zur Laufzeit ändern. Für eine Instanz haben wir im unten angegebenen Beispiel auf eine vorhandene zugegriffen**Kontrollkästchen** Zellkontrolle aus der**Arbeitsblatt** und seine Checked-Eigenschaft geändert.

**WICHTIG:** **Kontrollen** Sammlung enthält alle Arten von Zellkontrollen in Form von**CellControl** Objekte. Wenn Sie also beispielsweise auf eine bestimmte Art von Zellsteuerung zugreifen müssen**Kontrollkästchen** dann müssen Sie die typisieren**CellControl** widersprechen**Kontrollkästchen** Klasse.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Entfernen der Cell-Steuerung**
 Um ein vorhandenes Zellsteuerelement zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann**Entfernen** die Zellkontrolle aus der**Kontrollen** Sammlung der**Arbeitsblatt** durch Angabe der Zelle (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer), die die Zellsteuerung enthält.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
