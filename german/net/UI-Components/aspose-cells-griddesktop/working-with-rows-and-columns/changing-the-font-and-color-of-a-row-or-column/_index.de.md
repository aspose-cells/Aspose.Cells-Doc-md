---
title: Schriftart und Farbe einer Zeile oder Spalte ändern
type: docs
weight: 110
url: /de/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

In diesem Thema besprechen wir das Ändern der Schriftart und Schriftfarbe von Zeilen und Spalten eines Arbeitsblatts. Dies ist eine grundlegende Ebene der Formatierungsfunktion, die von Aspose.Cells.GridDesktop angeboten wird und es Entwicklern ermöglicht, die Ansicht ihrer Arbeitsblätter anzupassen, um sie präsentabler zu machen.

{{% /alert %}} 
## **Schriftart und Farbe einer Spalte ändern**
Um die Schriftart und Farbe einer Spalte mit Aspose.Cells.GridDesktop zu ändern, gehen Sie bitte wie folgt vor:

-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Zugriff a**Spalte** dessen Schriftart und Farbe geändert werden soll
-  Erstellen Sie eine angepasste**Schriftart**
-  Stellen Sie die ein**Schriftart** des**Spalte** zum Maßgeschneiderten
-  Endlich einstellen**Schriftfarbe** des**Spalte** zu jedem gewünschten**Farbe**



{{< highlight "csharp" >}}

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
## **Schriftart und Farbe einer Zeile ändern**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Zugriff a**Reihe** dessen Schriftart und Farbe geändert werden soll
-  Erstellen Sie eine angepasste**Schriftart**
-  Stellen Sie die ein**Schriftart** des**Reihe** zum Maßgeschneiderten
-  Endlich einstellen**Schriftfarbe** des**Reihe** zu jedem gewünschten**Farbe**



{{< highlight "csharp" >}}

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
