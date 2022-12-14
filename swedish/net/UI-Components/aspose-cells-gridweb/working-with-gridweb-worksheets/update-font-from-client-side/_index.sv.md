---
title: Uppdatera teckensnittsinställningar från klientsidan
type: docs
weight: 170
url: /sv/net/update-font-from-client-side/
---
{{% alert color="primary" %}}

Det här ämnet diskuterar ändring av teckensnittsinställningar från klientsidan i Aspose.Cells.GridWeb-kontrollen.

{{% /alert %}}

Aspose.Cells GridWeb stöder nu ändring av teckensnittsinställningar från klientsidan. För detta tillhandahåller API följande funktioner

- **uppdateraCellFontStyle**: Params - r/i/b/ib för vanlig/kursiv/fet/kursiv&&fet
- **uppdateraCellFontSize**: Params - teckensnittsnamn, etc. 'System'
- **uppdateraCellFontName**: Params - teckenstorlek, etc. '12pt'
- **uppdateraCellFontColor**: Params - none/u/l/ul/ for none/underline/strikout/underline&&strikout
- **uppdateraCellFontLine**: Params - HTML-färg som #aa22ee eller välkänt färgnamn som grönt, rött,...
- **uppdateraCellBackGroundColor**: Params - HTML-färg som #aa22ee eller välkänt färgnamn som grönt, rött,...

Följande kodavsnitt visar hur du ändrar teckensnittsinställningar från klientsidan i GridWeb.

## Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-Worksheets-UpdateFontFromClientSide.aspx" >}}
