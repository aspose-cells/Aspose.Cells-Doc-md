---
title: Set DeviceInfo in rsreportserver.config
type: docs
weight: 60
url: /reportingservices/set-deviceinfo-in-rsreportserver-config/
---

- **FileExtension** 
  When the value is null, the exported report file extension name will be the default value. When the value is not null, the extension name of the exported report file is value.
- **SimplePageHeaders** 
  When the value is true, it renders report header item into Excel page header. The default value is false.
- **SimplePageFooters** 
  When the value is true, it renders report footer item into Excel page footer. The default value is true.
- **PutoutHeader** 
  When the value is true, it will export the report header item. When the value is false, it does not export the report header item. The default value is true. The value only supports Excel2007Xlsx(Data Only) extension.
- **PutoutFooter** 
  When the value is true, it will export the report footer item. When the value is false, it does not export the report footer item. The default value is true. The value only supports Excel2007Xlsx(Data Only) extension.
- **FillTableGroupHeaderForSimpleOutPut** 
  The default value is false. The value only supports Excel2007Xlsx(Data Only) extension.
- **NoOutPutTotalForSimpleOutPut** 
  The default value is false. The value only supports Excel2007Xlsx(Data Only) extension.
- **NoOutPutGroupForSimpleOutPut** 
  The default value is false. The value only supports Excel2007Xlsx(Data Only) extension.
- **NoDoGroupPageForSimpleOutPut** 
  The default value is true. The value only supports Excel2007Xlsx(Data Only) extension.
- **NoDoPageForSimpleOutPut** 
  The default value is true. The value only supports Excel2007Xlsx(Data Only) extension.
- **FieldDelimiter** 
  It sets field delimiters. The value supports CSV and TXT extensions. 
