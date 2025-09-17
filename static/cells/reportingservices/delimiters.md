##Delimiters
Aspose.Cells for Reporting Services supports a specified delimiter when rendering TXT or CSV format. Two settings control the field delimiter in Aspose.Cells for Reporting Services.
1. The field delimiter parameter in **rsreportserver.config** can only control a specified rendering extension.
Specified field delimiters configuration reference:
1. The field delimiter parameter in **Aspose.Cells.ReportingServices.xml** can control all TXT type rendering extensions.
The field delimiter parameter in **rsreportserver.config** takes priority over the field delimiter parameter in **Aspose.Cells.ReportingServices.xml**. When the field delimiter parameter in **rsreportserver.config** is null or the default value, the field delimiter parameter in **Aspose.Cells.ReportingServices.xml** is used.
