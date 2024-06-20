---
title: Ändern der Schriftart und Farbe einer Zeile oder Spalte
type: docs
weight: 110
url: /de/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop, Schriftart, Farbe
description: Dieser Artikel zeigt, wie die Schriftart und Farbe in einer Zeile oder Spalte in GridDesktop geändert werden können.
---

{{% alert color="primary" %}} 

In diesem Thema werden wir darüber diskutieren, wie die Schriftart und Schriftfarbe von Zeilen und Spalten eines Arbeitsblatts geändert werden können. Dies ist eine grundlegende Formatierungsfunktion, die von Aspose.Cells.GridDesktop angeboten wird und Entwicklern ermöglicht, die Ansicht ihrer Arbeitsblätter anzupassen, um sie ansprechender zu gestalten.

{{% /alert %}} 
## **Ändern der Schriftart und Farbe einer Spalte**
Um die Schriftart und Farbe einer Spalte mit Aspose.Cells.GridDesktop zu ändern, befolgen Sie bitte die folgenden Schritte:

- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Zugriff auf eine **Spalte**, deren Schriftart und Farbe geändert werden sollen
- Erstellen Sie eine angepasste **Schriftart**
- Legen Sie die **Schriftart** der **Spalte** auf die angepasste ein
- Legen Sie abschließend die **Schriftfarbe** der **Spalte** auf eine beliebige **Farbe** fest



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **Ändern der Schriftart und Farbe einer Zeile**
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Zugriff auf eine **Zeile**, deren Schriftart und Farbe geändert werden sollen
- Erstellen Sie eine angepasste **Schriftart**
- Legen Sie die **Schriftart** der **Zeile** auf die angepasste ein
- Legen Sie abschließend die **Schriftfarbe** der **Zeile** auf eine beliebige **Farbe** fest



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}
