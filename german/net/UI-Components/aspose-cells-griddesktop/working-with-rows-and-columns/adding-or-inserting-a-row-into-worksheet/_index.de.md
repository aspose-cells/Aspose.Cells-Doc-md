---
title: Hinzufügen oder Einfügen einer Zeile in ein Arbeitsblatt
type: docs
weight: 30
url: /de/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

Ähnlich wie in einem unserer vorherigen Themen beschreibt dieses Thema die Funktion zum Hinzufügen und Einfügen von Zeilen in die Arbeitsblätter zur Laufzeit mithilfe von API von Aspose.Cells.GridDesktop. Der grundlegende Unterschied zwischen Hinzufügen und Einfügen besteht darin, dass zusätzlich eine Zeile am Ende der Zeilensammlung des Arbeitsblatts hinzugefügt wird, wobei wie beim Einfügen eine Zeile an jeder angegebenen Position im Arbeitsblatt hinzugefügt werden kann.

{{% /alert %}} 
## **Hinzufügen einer Zeile zum Arbeitsblatt**
Um dem Arbeitsblatt eine neue Zeile hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Hinzufügen**Die Zeile** zum**Arbeitsblatt**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Einfügen einer Zeile in ein Arbeitsblatt**
Um eine neue Zeile an einer bestimmten Position in das Arbeitsblatt einzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Einfügung**Die Zeile** hinein**Arbeitsblatt**(an einer bestimmten Position durch Angabe des Index der Zeile, wo es eingefügt werden soll)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
