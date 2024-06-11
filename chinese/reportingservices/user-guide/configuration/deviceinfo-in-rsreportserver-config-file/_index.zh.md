---
title: rsreportserver.config 文件中的 DeviceInfo
type: docs
weight: 70
url: /zh/reportingservices/deviceinfo-in-rsreportserver-config-file/
---

**rsreportserver.config** 中的 DeviceInfo 部分包含以下参数，影响 Aspose.Cells 的行为：

- **FileExtension**: 当值为 **null** 时，导出的报表文件扩展名为默认值。当值不为 null 时，报表的扩展名设置为该值。
- **SimplePageHeaders**: 当值为 **true** 时，报表页眉项呈现为 Microsoft Excel 页眉。默认值为 **false**。
- **SimplePageFooters**: 当 **true** 时，报表页脚项呈现为 Microsoft Excel 页脚。默认值为 **true**。
- **PutoutHeader**: 当 **true**（默认）时，导出报表页眉项。当 **false** 时，不导出报表页眉项。仅支持 Excel 2007 XLSX（仅数据）扩展名。
- **PutoutFooter**: 当 **true**（默认）时，导出报表页脚项。当 **false** 时，不导出报表页脚项。仅支持 Excel 2007 XLSX（仅数据）扩展名。
- **FillTableGroupHeaderForSimpleOutPut**: 默认为 **false**。该值仅支持 Excel 2007 XLSX（仅数据）扩展名。
- **NoOutPutTotalForSimpleOutPut**: 默认为 **false**。该值仅支持 Excel 2007 XLSX（仅数据）扩展名。
- **NoOutPutGroupForSimpleOutPut**: 默认为 **false**。该值仅支持 Excel 2007 XLSX（仅数据）扩展名。
- **NoDoGroupPageForSimpleOutPut**: 默认为 **true**。该值仅支持 Excel 2007 XLSX（仅数据）扩展名。
- **NoDoPageForSimpleOutPut**: 默认为 **true**。该值仅支持 Excel 2007 XLSX（仅数据）扩展名。
- **FieldDelimiter**: 设置字段分隔符。该值支持 CSV 和 TXT 扩展名。
