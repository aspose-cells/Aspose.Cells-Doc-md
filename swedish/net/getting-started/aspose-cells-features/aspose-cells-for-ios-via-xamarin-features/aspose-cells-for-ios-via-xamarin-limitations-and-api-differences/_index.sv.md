---
title: Aspose.Cells för iOS via Xamarin-begränsningar och API-skillnader
type: docs
weight: 10
url: /sv/net/aspose-cells-for-ios-via-xamarin-limitations-and-api-differences/
---
## Senaste versionen av Aspose.Cells för iOS via Xamarin kanske inte fungerar med den gamla versionen av Xamarin.iOS
Observera att Aspose.Cells för iOS via Xamarin alltid byggs med de senaste stabila versionerna av Xamarin och Xamarin.iOS-plattformarna. Om du stöter på några problem när du använder Aspose.Cells för iOS via Xamarin i din Xamarin.Android-applikation, se till att du har de senaste Xamarin- och Xamarin.iOS-versionerna installerade. Ibland byggs Aspose.Cells för iOS via Xamarin med den senaste versionen av Xamarin (Xamarin.iOS) som inte fungerar med äldre versioner av Xamarin.
## Aspose.Cells för iOS via Xamarin-begränsningar
- Infoga bilder - Stöds inte.
- Skapa diagram - Stöds inte.
- Ställa in gradientbakgrund - Stöds inte.
- Lägga till kommentarer till celler - Stöds inte.
- Implementera datavalideringar - Stöds inte.
- Skapa anpassade sidbrytningar - Stöds inte.
- Implementering av smarta markörer – stöds inte.
- Skydda/avskydda arbetsblad - stöds inte.
- Ange avancerade skyddsalternativ som introducerats i Excel XP och senare versioner - stöds inte.
- Infoga formulärkontroller och andra ritningsformer/objekt - Stöds inte.
- Skapa pivottabeller och pivotdiagram - Stöds inte.
- Bevara eller ta bort ett tillägg, VBA, makron - stöds inte.
- Implementering av transponeringsalternativ - Stöds inte.
- Skapa anpassade diagram - Stöds inte.
- Lägga till, bevara eller extrahera OLE-objekt från kalkylarken - stöds inte.
- Implementering av Microsoft Excel 2010 gnistlinjer - stöds inte.
- Kryptera filer - Stöds inte.
## Offentliga API (namnutrymme) skillnader
I Aspose.Cells för iOS via Xamarin används Aspose.Cells.Drawing namespace istället för System.Drawing i .NET API. Listan över berörda objekt är följande:

- Aspose.Cells.Drawing.Color
- Aspose.Cells.Drawing.ColorConverter
- Aspose.Cells.Drawing.ColorTranslator
- Aspose.Cells.Drawing.FontStyle
- Aspose.Cells.Drawing.GraphicsUnit
- Aspose.Cells.Drawing.ImageFormatConverter
- Aspose.Cells.Drawing.KnownColor
- Aspose.Cells.Drawing.KnownColors
- Aspose.Cells.Drawing.Locale
- Aspose.Cells.Drawing.SystemColors
- Aspose.Cells.Drawing.Imaging.PixelFormat
- Aspose.Cells.Drawing.Imaging.ImageFormat
- Aspose.Cells.Drawing.Imaging.ImageFlags
- Aspose.Cells.Drawing.Drawing2D.SmoothingMode
- Aspose.Cells.Drawing.Drawing2D.PathPointType
- Aspose.Cells.Drawing.Drawing2D.PathData
- Aspose.Cells.Drawing.Drawing2D


