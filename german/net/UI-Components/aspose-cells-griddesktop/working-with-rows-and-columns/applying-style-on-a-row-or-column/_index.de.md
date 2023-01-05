---
title: Stil auf eine Zeile oder Spalte anwenden
type: docs
weight: 50
url: /de/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

In diesem Thema besprechen wir das Ändern der Schriftart und Schriftfarbe von Zeilen und Spalten eines Arbeitsblatts. Dies ist eine grundlegende Ebene der Formatierungsfunktion, die von Aspose.Cells.GridDesktop angeboten wird und es Entwicklern ermöglicht, die Ansicht ihrer Arbeitsblätter anzupassen, um sie präsentabler zu machen.

{{% /alert %}} 
## **Stil auf eine Spalte anwenden**
Führen Sie die folgenden Schritte aus, um mithilfe von Aspose.Cells.GridDesktop einen benutzerdefinierten Stil auf eine Spalte anzuwenden:

-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Zugriff a**Spalte** auf die wir a anwenden wollen**Stil**
-  Bekommen**Stil** des**Spalte**
-  Satz**Stil** Eigenschaften nach Ihren individuellen Bedürfnissen
-  Endlich einstellen**Stil** des**Spalte** mit dem aktualisierten

 Es gibt viele nützliche Eigenschaften und Methoden, die von angeboten werden**Stil** Objekt, das von Entwicklern verwendet werden kann, um den Stil an ihre Anforderungen anzupassen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Stil auf eine Reihe anwenden**
Führen Sie die folgenden Schritte aus, um mit Aspose.Cells.GridDesktop einen benutzerdefinierten Stil auf eine Zeile anzuwenden:

-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Zugriff a**Reihe** auf die wir a anwenden wollen**Stil**
-  Bekommen**Stil** des**Reihe**
-  Satz**Stil** Eigenschaften nach Ihren individuellen Bedürfnissen
-  Endlich einstellen**Stil** des**Reihe** mit dem aktualisierten

 Es gibt viele nützliche Eigenschaften und Methoden, die von angeboten werden**Stil** Objekt, das von Entwicklern verwendet werden kann, um den Stil an ihre Anforderungen anzupassen.



{{< highlight "csharp" >}}

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
