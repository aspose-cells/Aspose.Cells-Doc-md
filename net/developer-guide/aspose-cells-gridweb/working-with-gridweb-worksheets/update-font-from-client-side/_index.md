---
title: Update Font Settings From Client Side
type: docs
weight: 170
url: /net/update-font-from-client-side/
---

{{% alert color="primary" %}}

This topic discusses changing font settings from client side in the Aspose.Cells.GridWeb control.

{{% /alert %}}

Aspose.Cells GridWeb now supports changing font settings from the client side. For this, the API provides the following functions

- **updateCellFontStyle**: Params - r/i/b/ib for regular/italic/bold/italic&&bold
- **updateCellFontSize**: Params - fontname, etc. 'System'
- **updateCellFontName**: Params - fontsize,etc. '12pt'
- **updateCellFontColor**: Params - none/u/l/ul/ for none/underline/strikout/underline&&strikout
- **updateCellFontLine**: Params - html color like #aa22ee or wellknown color name like green,red,...
- **updateCellBackGroundColor**: Params - html color like #aa22ee or wellknown color name like green,red,...

The following code snippet demonstrates changing font settings from client side in GridWeb.

## Sample Code

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples.GridWeb-CSharp-Worksheets-UpdateFontFromClientSide.aspx" >}}
