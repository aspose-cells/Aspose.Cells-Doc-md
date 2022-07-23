---
title: Different Ways to Open Files
type: docs
weight: 10
url: /python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

With Aspose.Cells it is simple to open files, for example, to retrieve data, or to use a designer template to speed up the development process.

{{% /alert %}}

## **Opening a File via a Path**

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the **[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Opening a File with Data only**

To open a file with data only, use the **[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** and **[LoadFilter](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)** classes to set the related attribute and options of the classes for the template file to be loaded.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

An exception will be thrown if you try to open non-native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) by Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

There are fair chances that the **[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** constructor may throw *System.OutOfMemoryException* while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the Memory Preferences.

{{% /alert %}}
