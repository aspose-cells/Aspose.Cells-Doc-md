---
title: Hinzufügen oder Einfügen einer Spalte in ein Arbeitsblatt
type: docs
weight: 10
url: /de/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

In diesem Thema beschreiben wir die grundlegende Funktion zum Hinzufügen und Einfügen von Spalten in die Arbeitsblätter zur Laufzeit mithilfe von API von Aspose.Cells.GridDesktop. Der grundlegende Unterschied zwischen Hinzufügen und Einfügen besteht darin, dass zusätzlich eine Spalte am Ende der Spaltensammlung des Arbeitsblatts hinzugefügt wird, wobei wie beim Einfügen eine Spalte an jeder angegebenen Position im Arbeitsblatt hinzugefügt werden kann.

{{% /alert %}} 
## **Hinzufügen einer Spalte zum Arbeitsblatt**
Führen Sie die folgenden Schritte aus, um dem Arbeitsblatt eine neue Spalte hinzuzufügen:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Addieren**Spalte** zum**Arbeitsblatt**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Einfügen einer Spalte in ein Arbeitsblatt**
Um eine neue Spalte an einer bestimmten Position in das Arbeitsblatt einzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Einfügung**Spalte** hinein**Arbeitsblatt** (an einer bestimmten Position durch Angabe des Index der Spalte, wo es eingefügt werden soll)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
