---
title: rsreportserver.config文件中的DeviceInfo
type: docs
weight: 70
url: /zh/reportingservices/deviceinfo-in-rsreportserver-config-file/
---

**rsreportserver.config**中的DeviceInfo部分包含以下参数，影响Aspose.Cells的行为:

- **FileExtension**：当值为**null**时，导出的报告文件扩展名为默认值。当值不为null时，报告的扩展名将设置为该值。
- **SimplePageHeaders**：当值为**true**时，报告头项呈现为Microsoft Excel页眉。默认值为**false**。
- **SimplePageFooters**：当**true**时，报告页脚项呈现为Microsoft Excel页脚。默认值为**true**。
- **PutoutHeader**：当**true**（默认）时，导出报告头项。当**false**时，报告头项不导出。仅支持Excel 2007 XLSX（仅数据）扩展名。
- **PutoutFooter**：当**true**（默认）时，导出报告页脚项。当**false**时，不导出。仅支持Excel 2007 XLSX（仅数据）扩展名。
- **FillTableGroupHeaderForSimpleOutPut**：默认情况下为**false**。该值仅支持Excel 2007 XLSX（仅数据）扩展名。
- **NoOutPutTotalForSimpleOutPut**：默认情况下为**false**。该值仅支持Excel 2007 XLSX（仅数据）扩展名。
- **NoOutPutGroupForSimpleOutPut**：默认情况下为**false**。该值仅支持Excel 2007 XLSX（仅数据）扩展名。
- **NoDoGroupPageForSimpleOutPut**：默认情况下为**true**。该值仅支持Excel 2007 XLSX（仅数据）扩展名。
- **NoDoPageForSimpleOutPut**：默认情况下为**true**。该值仅支持Excel 2007 XLSX（仅数据）扩展名。
- **FieldDelimiter**：设置字段分隔符。该值支持CSV和TXT扩展名。
