---
title: Anwenden eines Stils auf eine Zeile oder Spalte
type: docs
weight: 50
url: /de/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop, Stil, Zeile, Spalte
description: Dieser Artikel zeigt, wie man einen Stil auf eine Zeile oder Spalte in GridDesktop anwendet.
---

{{% alert color="primary" %}} 

In diesem Thema werden wir darüber diskutieren, wie die Schriftart und Schriftfarbe von Zeilen und Spalten eines Arbeitsblatts geändert werden können. Dies ist eine grundlegende Formatierungsfunktion, die von Aspose.Cells.GridDesktop angeboten wird und Entwicklern ermöglicht, die Ansicht ihrer Arbeitsblätter anzupassen, um sie ansprechender zu gestalten.

{{% /alert %}} 
## **Anwenden eines Stils auf eine Spalte**
Um einen benutzerdefinierten Stil auf eine Spalte mithilfe von Aspose.Cells.GridDesktop anzuwenden, befolgen Sie bitte die folgenden Schritte:

- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Greifen Sie auf eine **Spalte** zu, auf die wir einen **Stil** anwenden möchten
- Holen Sie den **Stil** der **Spalte**
- Setzen Sie die Eigenschaften des **Stils** gemäß Ihren individuellen Anforderungen
- Legen Sie schließlich den **Stil** der **Spalte** mit dem aktualisierten fest

Es gibt viele nützliche Eigenschaften und Methoden des **Stil**-Objekts, die von Entwicklern verwendet werden können, um den Stil nach ihren Anforderungen anzupassen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Anwenden eines Stils auf eine Zeile**
Um einen benutzerdefinierten Stil auf eine Zeile mithilfe von Aspose.Cells.GridDesktop anzuwenden, befolgen Sie bitte die folgenden Schritte:

- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Greifen Sie auf eine **Zeile** zu, auf die wir einen **Stil** anwenden möchten
- Holen Sie den **Stil** der **Zeile**
- Setzen Sie die Eigenschaften des **Stils** gemäß Ihren individuellen Anforderungen
- Legen Sie abschließend den **Stil** der **Zeile** mit dem aktualisierten fest.

Es gibt viele nützliche Eigenschaften und Methoden des **Stil**-Objekts, die von Entwicklern verwendet werden können, um den Stil nach ihren Anforderungen anzupassen.



{{< highlight csharp >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
