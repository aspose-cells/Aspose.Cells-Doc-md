---
title: Aspose.Grid .Net 1.5.2.0 Hot Fix Release Notes
type: docs
weight: 50
url: /sv/net/aspose-grid-net-1-5-2-0-hot-fix-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Grid .Net 1.5.2.0 Hot Fix](https://downloads.aspose.com/cells/net/new-releases/aspose.grid-.net-1.5.2.0-hot-fix/)

{{% /alert %}} 

 Vi har släppt Aspose.Grid 1.5.2!

 Release Notes

 Aspose.Grid.Webb

- Fixat: färgfel vid inställning på klientsidan
- Fixat: TableStyle/TableItemStyle CssClass-egenskapen träder inte i kraft bugg
- Support Skapa pivottabellsrapporter
- Stöd för flera celler på klientsidan välj/kopiera/klipp ut/klistra in/ställ in stil
- Stöd högerklicksmenyoperationer på klientsidan: frysa/låsa upp; infoga/ta bort rad/kolumn; slå samman/upphäva sammanslagningar av celler;
- Stöd hyperlänkar (text- eller bildvisning, UrlLink eller CellCommand Action)
- Tillagda egenskaper: ActiveCell, EnableClientColumnOperations, EnableClientFreeze, EnableClientMergeOperations, EnableClientRowOperations, SelectCells
- Tillagda metoder: WebCells.GetColumnReadonly, WebCells.SetColumnReadonly, WebCells.GetRowReadonly, WebCells.SetRowReadonly
- Tillagda händelser: SheetDataUpdated, LoadCustomData (för dataåterställning i sessionslöst läge), CellCommand, ColumnDeleted, ColumnInserted, RowDeleted, RowInserted, PageIndexChanged
- Ändrad: Nu behövs inte klientfilen web-path(/agw_client) och klientfilerna (htc, gif, etc.) i distributionsmiljön. Dessa filer är nu inbäddade i kontrollen. Detta förenklar driftsättningen och uppgraderingen.

 ` `Aspose.Grid.Skrivbord

 Förbättrad:

- Kolumnrubriktext Stöds.
- Snabbmeny stöds.
- Hyperlänkar, kommentarer, bilderexportering stöds.
- Cell knapp, kryssruta, combox stöds.
- CellClick, CellDoubleClick, CellKeyPressed-händelser stöds.
- Tillämpa stil på cellintervall som stöds.
- Datavalidering stöds.

 Fast:

- Genom att minimera formuläret som innehöll GridDesktop-kontrollen som ställde in Dock-egenskapen Fill, skapas ett undantag.
- Genom att trycka på "delete"-tangenten höjer GridDesktop-kontrollen inte CellDataChanged-händelsen.
- När radnumret är större än 4 digitala, räcker inte radhuvudets bredd.
- När du laddar från en excel-fil är teckensnittet för char som matas in i en cell annorlunda än cellens teckensnitt.
- Kan inte mata in Enter i en cell, använd nu Ctrl + Enter-tangenterna.
- Om det inte finns fokuserade celler, kommer textrutekontrollen att placeras vid felpositionen vid inmatning av tecken.
- Det finns en kommentar i en cell, och sedan fokuserade den högra cellen; När du pekar på cellen som innehåller en kommentar kommer den fokuserade cellen alltid att blinka.
- Att dölja radkolumnen fungerar inte.
