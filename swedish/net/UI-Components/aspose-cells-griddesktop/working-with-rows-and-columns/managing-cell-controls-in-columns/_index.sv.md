---
title: Hantering av cellkontroller i kolumner
type: docs
weight: 100
url: /sv/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop, kontroller, kontroll
description: Den här artikeln introducerar hur man ska ställa in kontrollen i kolumner GridDesktop.
---

{{% alert color="primary" %}} 

Detta ämne diskuterar några viktiga begrepp om hantering av cellkontroller i kolumner med Aspose.Cells.GridDesktop API. Vi kommer förklara hur utvecklare kan komma åt, modifiera och ta bort cellkontroller från kolumnerna i sina arbetsblad. Låt oss ta en titt på det.

{{% /alert %}} 
## **Åtkomst till cellkontroller**
För att komma åt och modifiera en befintlig cellkontroll i kolumnen kan utvecklare använda egenskapen CellControl i **Aspose.Cells.GridDesktop.Data.GridColumn**. När en cellkontroll är åtkomst kan utvecklarna modifiera dess egenskaper vid körning. Till exempel, i det givna exemplet nedan har vi kommit åt en befintlig **CheckBox** cellkontroll från en specifik **Aspose.Cells.GridDesktop.Data.GridColumn** och modifierat dess Checked-egenskap.

**VIKTIGT:** Egenskapen CellControl tillhandahåller en cellkontroll i form av **CellControl** objekt. Så, om du behöver komma åt en specifik typ av cellkontroll, säg **CheckBox** så måste du typomvandla **CellControl** objektet till **CheckBox** klass.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Ta bort cellkontroller**
För att ta bort en befintlig cellkontroll kan utvecklare helt enkelt komma åt ett önskat arbetsblad och sedan **ta bort** cellkontrollen från den specifika kolumnen genom att använda metoden **RemoveCellControl** i **Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Varje kolumn i **Columns** -samlingen i **Arbetsbladet** representeras av en instans av klassen **Aspose.Cells.GridDesktop.Data.GridColumn**.

{{% /alert %}}
