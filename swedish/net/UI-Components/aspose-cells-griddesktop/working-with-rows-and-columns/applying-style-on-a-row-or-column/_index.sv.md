---
title: Applicera stil på en rad eller kolumn
type: docs
weight: 50
url: /sv/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop, stil, rad, kolumn
description: Denna artikel introducerar hur man applicerar stil på en rad eller kolumn i GridDesktop.
---

{{% alert color="primary" %}} 

I det här ämnet kommer vi att diskutera hur man ändrar fonten och fontfärgen för rader och kolumner i en kalkylblad. Detta är en grundläggande formateringsfunktion som erbjuds av Aspose.Cells.GridDesktop och som ger utvecklare möjlighet att anpassa visningen av sina kalkylblad för att göra dem mer presentabla.

{{% /alert %}} 
## **Applicera stil på en kolumn**
För att tillämpa en anpassad stil på en kolumn med hjälp av Aspose.Cells.GridDesktop, följ följande steg:

- Kom åt något önskat **Kalkylblad**
- Öppna en **Kolumn** på vilken vi vill applicera en **Stil**
- Hämta **Stil** för **Kolumnen**
- Ange **Stil**-egenskaper enligt dina anpassade behov
- Slutligen, ange **Stilen** för **Kolumnen** med den uppdaterade

Det finns många användbara egenskaper och metoder som erbjuds av **Stil**-objektet som kan användas av utvecklare för att anpassa stilen enligt deras krav.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Applicera stil på en rad**
För att tillämpa en anpassad stil på en rad med hjälp av Aspose.Cells.GridDesktop, följ följande steg:

- Kom åt något önskat **Kalkylblad**
- Öppna en **Rad** på vilken vi vill applicera en **Stil**
- Hämta **Stil** för **Radet**
- Ange **Stil**-egenskaper enligt dina anpassade behov
- Slutligen, ange **Stilen** för **Radet** med den uppdaterade

Det finns många användbara egenskaper och metoder som erbjuds av **Stil**-objektet som kan användas av utvecklare för att anpassa stilen enligt deras krav.



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
