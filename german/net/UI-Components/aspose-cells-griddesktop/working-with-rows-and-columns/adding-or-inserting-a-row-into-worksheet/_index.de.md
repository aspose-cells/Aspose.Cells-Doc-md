---
title: Hinzufügen oder Einfügen einer Zeile in ein Arbeitsblatt
type: docs
weight: 30
url: /de/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: Dieser Artikel zeigt, wie Sie eine Zeile in GridDesktop hinzufügen oder einfügen können.
---

{{% alert color="primary" %}} 

Ähnlich wie in einem unserer vorherigen Themen beschreibt dieses Thema die Funktion des Hinzufügens und Einfügens von Zeilen in die Arbeitsblätter zur Laufzeit unter Verwendung der API von Aspose.Cells.GridDesktop. Der grundlegende Unterschied zwischen Hinzufügung und Einfügung besteht darin, dass bei der Hinzufügung eine Zeile am Ende der Zeilenkollektion des Arbeitsblatts hinzugefügt wird, während bei der Einfügung eine Zeile an einer beliebigen Position im Arbeitsblatt hinzugefügt werden kann.

{{% /alert %}} 
## **Hinzufügen einer Zeile zum Arbeitsblatt**
Um dem Arbeitsblatt eine neue Zeile hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie eine **Zeile** zum **Arbeitsblatt** hinzu



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Einfügen einer Zeile in ein Arbeitsblatt**
Um eine neue Zeile in das Arbeitsblatt an einer bestimmten Position einzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie eine **Zeile** in das **Arbeitsblatt** ein (an einer bestimmten Position, indem Sie den Index der Zeile angeben, an der sie eingefügt werden soll)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
