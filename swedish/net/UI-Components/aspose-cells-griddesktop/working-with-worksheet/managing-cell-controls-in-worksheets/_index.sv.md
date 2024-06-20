---
title: Hantera cellkontroller i arbetsblad
type: docs
weight: 130
url: /sv/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop, cellkontroll, kontroll, kontroller
description: Den här artikeln introducerar hur man arbetar med cellkontroller i GridDesktop.
---

{{% alert color="primary" %}} 

Det här ämnet diskuterar några viktiga koncept om att hantera cellkontroller med hjälp av Aspose.Cells.GridDesktop API. Vi kommer att förklara hur utvecklare kan få åtkomst till, ändra och ta bort cellkontroller från deras arbetsblad. Låt oss titta närmare på det.

{{% /alert %}} 
## **Åtkomst till cellkontroller**
För att komma åt och ändra en befintlig cellkontroll i arbetsbladet kan utvecklare komma åt en specifik cellkontroll från **Controls** -samlingen av **Worksheet** genom att ange cellen (använda cellnamnet eller dess plats i form av rad- och kolumnnummer) där cellkontrollen visas. När en cellkontroll har kommit åt kan utvecklare ändra dess egenskaper under körning. Till exempel, i det givna exemplet nedan har vi kommit åt en befintlig **CheckBox** cellkontroll från **Worksheet** och ändrat dess Checked-egenskap.

**Viktigt:** **Controls** -samlingen innehåller alla typer av cellkontroller i form av **CellControl** -objekt. Så om du behöver komma åt en specifik typ av cellkontroll, säg **CheckBox** måste du typomvandla **CellControl** -objektet till **CheckBox** -klass.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Ta bort cellkontroller**
För att ta bort en befintlig cellkontroll kan utvecklare helt enkelt komma åt ett önskat arbetsblad och sedan **Ta bort** cellkontrollen från **Controls** -samlingen av **Worksheet** genom att ange cellen (använda dess namn eller rad- och kolumnnummer) som innehåller cellkontrollen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
