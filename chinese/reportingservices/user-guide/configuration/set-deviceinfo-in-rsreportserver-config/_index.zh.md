---
title: 在 rsreportserver.config 中设置 DeviceInfo
type: docs
weight: 60
url: /zh/reportingservices/set-deviceinfo-in-rsreportserver-config/
---

- **FileExtension** 
  当值为null时，导出的报表文件扩展名将是默认值。当值不为null时，导出的报表文件的扩展名为该值。
- **SimplePageHeaders** 
  当该值为true时，将报表头项呈现为Excel页面页眉。默认值为false。
- **SimplePageFooters** 
  当该值为true时，将报表页脚项呈现为Excel页面页脚。默认值为true。
- **PutoutHeader** 
  当该值为true时，将导出报表头项。 当该值为false时，不导出报表头项。默认值为true。该值仅支持Excel2007Xlsx(Data Only)扩展名。
- **PutoutFooter** 
  当该值为true时，将导出报表页脚项。 当该值为false时，不导出报表页脚项。默认值为true。该值仅支持Excel2007Xlsx(Data Only)扩展名。
- **FillTableGroupHeaderForSimpleOutPut** 
  默认值为false。该值仅支持Excel2007Xlsx(Data Only)扩展名。
- **NoOutPutTotalForSimpleOutPut** 
  默认值为false。该值仅支持Excel2007Xlsx(Data Only)扩展名。
- **NoOutPutGroupForSimpleOutPut** 
  默认值为false。该值仅支持Excel2007Xlsx(Data Only)扩展名。
- **NoDoGroupPageForSimpleOutPut** 
  默认值为true。该值仅支持Excel2007Xlsx(Data Only)扩展名。
- **NoDoPageForSimpleOutPut** 
  默认值为true。该值仅支持Excel2007Xlsx(Data Only)扩展名。
- **FieldDelimiter** 
  它设置字段分隔符。该值支持CSV和TXT扩展名。 
