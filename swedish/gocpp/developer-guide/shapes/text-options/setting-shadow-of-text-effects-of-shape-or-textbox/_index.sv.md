---
title: Sätta skugga för text effekter av form eller textruta med Golang via C++
linktitle: Ställ in skugga för textstilar
type: docs
weight: 250
url: /sv/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Lär dig hur man ställer in skuggan för textstilar för former eller textrutor med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan ställa in **Skugga** för **Textstilar** på vilken form eller textruta som helst. Använd [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/)-egenskapen. Den visar inställningen för formens text och returnerar [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)-objekt. Efter att ha fått åtkomst till den, ställ sedan in **Skugga** via [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)-egenskapen. Denna egenskap är av typen [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) och har flera värden. Några av dessa är:

- OffsetDiagonalBottomRight
- OffsetBottom
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

Följande kodexempel demonstrerar användningen av [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/)-egenskapen för att ställa in skuggan för textstilar på form eller textruta.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
