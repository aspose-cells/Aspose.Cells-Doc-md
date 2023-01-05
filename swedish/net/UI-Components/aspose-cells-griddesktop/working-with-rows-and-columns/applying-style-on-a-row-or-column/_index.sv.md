---
title: Tillämpa stil på en rad eller kolumn
type: docs
weight: 50
url: /sv/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

I det här ämnet kommer vi att diskutera hur du ändrar teckensnitt och teckensnittsfärg på rader och kolumner i ett kalkylblad. Detta är en grundläggande formateringsfunktion som erbjuds av Aspose.Cells.GridDesktop som ger utvecklare möjlighet att anpassa synen på sina kalkylblad för att göra dem mer presentabla.

{{% /alert %}} 
## **Applicera stil på en kolumn**
För att tillämpa en anpassad stil på en kolumn med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Få åtkomst till alla önskade**Arbetsblad**
-  Tillgång a**Kolumn** på vilken vi vill tillämpa en**Stil**
-  Skaffa sig**Stil** av**Kolumn**
-  Uppsättning**Stil** egenskaper enligt dina anpassade behov
-  Slutligen, ställ in**Stil** av**Kolumn** med den uppdaterade

 Det finns många användbara egenskaper och metoder som erbjuds av**Stil** objekt som kan användas av utvecklare för att anpassa stilen efter deras krav.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Tillämpa stil på en rad**
För att tillämpa en anpassad stil på en rad med Aspose.Cells.GridDesktop, följ stegen nedan:

-  Få åtkomst till alla önskade**Arbetsblad**
-  Tillgång a**Rad** på vilken vi vill tillämpa en**Stil**
-  Skaffa sig**Stil** av**Rad**
-  Uppsättning**Stil** egenskaper enligt dina anpassade behov
-  Slutligen, ställ in**Stil** av**Rad** med den uppdaterade

 Det finns många användbara egenskaper och metoder som erbjuds av**Stil** objekt som kan användas av utvecklare för att anpassa stilen efter deras krav.



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
