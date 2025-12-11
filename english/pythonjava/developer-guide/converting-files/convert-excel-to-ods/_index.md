---
title: Convert Excel to ODS
type: docs
weight: 40
url: /python-java/convert-excel-to-ods/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Convert Excel to ODS**
ODS files are created by the Calc program which is a part of the Apache OpenOffice Suite. ODS files store data that is organized in rows and columns and are formatted using the OASIS OpenDocument XML-based standard.

Aspose.Cells for Python via Java supports working with ODS files. The following examples demonstrate converting Excel to an ODS file.
### **Direct Conversion**
The simplest way to convert an Excel file to ODS is to load the workbook and save it by passing [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) as the second parameter of the [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) method.

The following code snippet demonstrates converting Excel directly to ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Save the ODS document in ODF 1.1 or 1.2 Specifications**
Aspose.Cells for Python via Java supports saving ODS files in ODF 1.1 and ODF 1.2 specifications. For this, the API provides [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) property. Setting this property to **true** will save the file with the ODF 1.1 specification. The default value of [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) is **false**, so the ODS file saved without special settings is saved with ODF 1.2 specification.

The following code snippet demonstrates saving ODS files with ODF 1.1 and 1.2 specifications.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
