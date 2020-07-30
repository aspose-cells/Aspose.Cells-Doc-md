---
title : "DeviceInfo in rsreportserver.config file" 
description : "" 
weight : 12087 
toc : false
type: docs
url: /reportingservices/userguide/configuration/deviceinfo+in+rsreportserver.config+file/
---

# Aspose.Cells for Reporting Services : DeviceInfo in rsreportserver.config file


The `DeviceInfo` section in **rsreportserver.config** takes the following parameters that affects Aspose.Cells' behavior:

*   **`FileExtension`**: when the value is **null**, the exported report file extension is the default value. When the value is not null, the report's extension is set to the value.
*   **`SimplePageHeaders`**: when the value is **true**, the report header item is rendered as a Microsoft Excel page header. The default value is **false**.
*   **`SimplePageFooters`**: when **true**, the report footer item is rendered as a Microsoft Excel page footer. The default value is **true**.
*   **`PutoutHeader`**: when **true** (default), the report header item is exported. When **false**, the report header item is not exported. Only supports the Excel 2007 XLSX (data only) extension.
*   **`PutoutFooter`**: when **true** (default), the report footer item is exported. When **false**, it is not. Only supports the Excel 2007 XLSX (data only) extension.
*   **`FillTableGroupHeaderForSimpleOutPut`**: **false** by default. The value only supports the Excel 2007 XLSX (data only) extension.
*   **`NoOutPutTotalForSimpleOutPut`**: **false** by default. The value only supports the Excel 2007 XLSX (data only) extension.
*   **`NoOutPutGroupForSimpleOutPut`**: **false** by default. The value only supports the Excel 2007 XLSX (data only) extension.
*   **`NoDoGroupPageForSimpleOutPut`**: **true** by default. The value only supports the Excel 2007 XLSX (data only) extension.
*   **`NoDoPageForSimpleOutPut`**: **true** by default. The value only supports the Excel 2007 XLSX (data only) extension.
*   **`FieldDelimiter`**: sets field delimiters. The value supports CSV and TXT extensions.

