---
title: Ändra teckensnitt och färg för en rad eller kolumn
type: docs
weight: 110
url: /sv/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

I det här ämnet kommer vi att diskutera hur du ändrar teckensnitt och teckensnittsfärg på rader och kolumner i ett kalkylblad. Detta är en grundläggande formateringsfunktion som erbjuds av Aspose.Cells.GridDesktop som ger utvecklare möjlighet att anpassa synen på sina kalkylblad för att göra dem mer presentabla.

{{% /alert %}} 
## **Ändra teckensnitt och färg för en kolumn**
För att ändra teckensnitt och färg på en kolumn med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Få åtkomst till alla önskade**Arbetsblad**
-  Tillgång a**Kolumn** vars teckensnitt och färg ska ändras
-  Skapa en anpassad**Font**
-  Ställ in**Font** av**Kolumn** till den skräddarsydda
-  Slutligen, ställ in**Fontfärg** av**Kolumn** till någon önskad**Färg**



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
## **Ändra teckensnitt och färg på en rad**
-  Få åtkomst till alla önskade**Arbetsblad**
-  Tillgång a**Rad** vars teckensnitt och färg ska ändras
-  Skapa en anpassad**Font**
-  Ställ in**Font** av**Rad** till den skräddarsydda
-  Slutligen, ställ in**Fontfärg** av**Rad** till någon önskad**Färg**



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
