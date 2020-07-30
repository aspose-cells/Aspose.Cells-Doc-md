---
title : "Public API Changes in Aspose.Cells 8.1.2" 
description : "" 
weight : 12292 
toc : false
type: docs
url: /java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.1.2/
---

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.1.2


This document describes changes to the Aspose.Cells API from version 8.1.1 to 8.1.2, that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

### Added Support for Warning if Font Substitution Occur

With Aspose.Cells for Java 8.1.2, the `WarningInfo` and `WarningType` classes, `IWarningCallback` interface, and `SaveOptions.WarningCallback` and `ImageOrPrintOptions.WarningCallback` properties have been added to allow the developers to receive warnings when font substitution occurs when converting spreadsheets to images, XPS & PDF formats.

Please check the detailed article on [Getting Warnings for Font Substitution while Rendering Spreadsheets](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) for more information.

### Deleted Obsolete PdfSaveOptions.ChartImageType Property

Aspose.Cells for Java 8.1.2 has removed the obsolete `PdfSaveOptions.ChartImageType` property from the public API.

