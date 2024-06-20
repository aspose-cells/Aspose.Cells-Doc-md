---
title: Ändra font och färg på en rad eller kolumn
type: docs
weight: 110
url: /sv/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop, font, färg
description: Den här artikeln introducerar hur man ändrar fonten och färgen i en rad eller kolumn i GridDesktop.
---

{{% alert color="primary" %}} 

I det här ämnet kommer vi att diskutera hur man ändrar fonten och fontfärgen för rader och kolumner i en kalkylblad. Detta är en grundläggande formateringsfunktion som erbjuds av Aspose.Cells.GridDesktop och som ger utvecklare möjlighet att anpassa visningen av sina kalkylblad för att göra dem mer presentabla.

{{% /alert %}} 
## **Ändra fonten och färgen på en kolumn**
För att ändra fonten och färgen på en kolumn med Aspose.Cells.GridDesktop, följ stegen nedan:

- Kom åt något önskat **Kalkylblad**
- Öppna en **Kolumn** vars font och färg ska ändras
- Skapa en anpassad **Font**
- Ange **Fonten** för **Kolumnen** till den anpassade
- Slutligen, ange **Fontfärgen** för **Kolumnen** till önskad **Färg**



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
## **Ändra fonten och färgen på en rad**
- Kom åt något önskat **Kalkylblad**
- Öppna en **Rad** vars font och färg ska ändras
- Skapa en anpassad **Font**
- Ange **Fonten** för **Rad** till den anpassade
- Slutligen, ange **Fontfärgen** för **Rad** till önskad **Färg**



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
