---
title: Spalte in Arbeitsblatt hinzufügen oder einfügen
type: docs
weight: 10
url: /de/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,einfügen,hinzufügen,spalte,eine Spalte einfügen,zeile einfügen
description: In diesem Artikel wird erläutert, wie eine Spalte in GridDesktop eingefügt oder hinzugefügt wird.
---

{{% alert color="primary" %}} 

In diesem Thema werden die grundlegenden Funktionen des Hinzufügens und Einfügens von Spalten in die Tabellenblätter zur Laufzeit unter Verwendung der API von Aspose.Cells.GridDesktop beschrieben. Der grundlegende Unterschied zwischen Hinzufügung und Einfügung besteht darin, dass bei der Hinzufügung die Spalte am Ende der Spaltensammlung des Arbeitsblatts hinzugefügt wird, während bei der Einfügung eine Spalte an einer bestimmten Position im Arbeitsblatt hinzugefügt werden kann.

{{% /alert %}} 
## **Eine Spalte zum Arbeitsblatt hinzufügen**
Um eine neue Spalte zum Arbeitsblatt hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie eine **Spalte** zum **Arbeitsblatt** hinzu



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Einfügen einer Spalte in ein Arbeitsblatt**
Um eine neue Spalte in ein Arbeitsblatt an einer bestimmten Position einzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie eine **Spalte** in das **Arbeitsblatt** ein (an einer bestimmten Position, indem der Index der Spalte angegeben wird, an der sie eingefügt werden soll)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
