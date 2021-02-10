---
title: Aspose.Cells for iOS via Xamarin Limitations and API Differences
type: docs
weight: 10
url: /net/aspose-cells-for-ios-via-xamarin-limitations-and-api-differences/
---

## Latest Version of Aspose.Cells for iOS via Xamarin may not Work with Old Xamarin.iOS Version
Please note that Aspose.Cells for iOS via Xamarin is always built by using the latest stable versions of Xamarin and Xamarin.iOS platforms. If you face any problems when using Aspose.Cells for iOS via Xamarin in your Xamarin.Android application, please make sure you have the latest Xamarin and Xamarin.iOS versions installed. Sometimes Aspose.Cells for iOS via Xamarin is built by using the latest Xamarin (Xamarin.iOS) version which does not work with older versions of Xamarin.
## Aspose.Cells for iOS via Xamarin Limitations
- Inserting images - Not Supported.
- Creating charts - Not Supported.
- Setting gradient background - Not Supported.
- Adding comments to cells - Not Supported.
- Implementing data validations - Not Supported.
- Creating custom page breaks - Not Supported.
- Implementing Smart Markers - Not Supported.
- Protecting/unprotecting Worksheets - Not Supported.
- Specifying advanced protection options introduced in Excel XP and later versions - Not Supported.
- Inserting form controls and other drawing shapes/objects - Not Supported.
- Creating pivot tables and pivot charts - Not Supported.
- Preserving or removing an Add-in, VBA, macros - Not Supported.
- Implementing transpose options - Not Supported.
- Creating custom charts - Not Supported.
- Adding, preserving or extracting OLE objects from the spreadsheets - Not Supported.
- Implementing Microsoft Excel 2010 spark lines - Not Supported.
- Encrypting files - Not Supported.
## Public API (namespace) differences
In Aspose.Cells for iOS via Xamarin, Aspose.Cells.Drawing namespace is used instead of System.Drawing in .NET API. The list of affected objects are as follows:

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


