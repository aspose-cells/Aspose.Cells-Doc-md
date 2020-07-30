---
title : "Aspose.Cells for Java 19.6 Release Notes" 
description : "" 
weight : 16897 
toc : false
type: docs
url: /java/releasenotes/asposecellsforjava/java/2019/aspose.cells+for+java+19.6+release+notes/
---

# Aspose.Cells for Java : Aspose.Cells for Java 19.6 Release Notes


This page contains release notes for Aspose.Cells for Java 19.6.

{{< table style="table-striped" >}}
|Key|Summary|Category|
|:----|:----|:----|
|CELLSJAVA-42914|Large conditional formats cause OOM exception|Enhancement|
|CELLSJAVA-42916|Data format issue after Workbook.save()|Enhancement|
|CELLSJAVA-42930|Excel95 load failure|Enhancement|
|CELLSJAVA-42927|The saved file opens slow in Excel after deleting columns|Enhancement|
|CELLSJAVA-42932|Conditional formatting error with Style.getDisplayStyle method|Bug|
|CELLSJAVA-42928|Some lines are not reflected in XLSX to PDF conversion|Bug|
|CELLSJAVA-42904|Header image seemingly corrupts the file|Bug|
|CELLSJAVA-42907|Filter lost after saving the workbook|Bug|
|CELLSJAVA-42915|Filters are changed after adding a sheet to the workbook|Bug|
|CELLSJAVA-42918|Converted file's chart flattened (XLS to XLSX conversion) |Bug|
|CELLSJAVA-42938|Loading XLSX file halts the application|Bug|
|CELLSJAVA-42859|CellsException for loading Name from ODS file|Exception|
|CELLSJAVA-42908|Exception while calling Name.getRefersTo()|Exception|
|CELLSJAVA-42926|IllegalStateException on loading workbook|Exception|
{{< /table >}}

### Public API and Backwards Incompatible Changes

The following is a list of any changes made to the public API such as added, renamed, removed or deprecated members as well as any non-backward compatible change made to Aspose.Cells for Java. If you have concerns about any change listed, please raise it on the Aspose.Cells support forum.

#### Adds enum FileFormatType.FODS,FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS and SaveFormat.SXC

Represents the .FODS and .SXC file format types.

#### Adds enum WarningType.UnsupportedFileFormat

Represents unsupported file format for warning types.

#### Adds enum ODSGeneratorType

Represents the generator type of ods.

#### OoxmlSaveOptions.EmbedOoxmlAsOleObject

Indicates whether embeding OOXML file as OleObject.

#### Adds Row.CopySettings(Aspose.Cells.Row,System.Boolean)

Copy settings of row, such as style, height, visibility, ...etc.

