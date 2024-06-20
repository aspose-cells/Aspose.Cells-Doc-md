---
title: rsreportserver.configでDeviceInfoを設定する
type: docs
weight: 60
url: /ja/reportingservices/set-deviceinfo-in-rsreportserver-config/
---

- **FileExtension** 
  値がnullの場合、エクスポートされたレポートファイルの拡張子はデフォルト値になります。値がnullでない場合、エクスポートされたレポートファイルの拡張子はその値になります。
- **SimplePageHeaders** 
  値がtrueの場合、レポートヘッダーアイテムがExcelページヘッダーにレンダリングされます。デフォルト値はfalseです。
- **SimplePageFooters** 
  値がtrueの場合、レポートフッターアイテムがExcelページフッターにレンダリングされます。デフォルト値はtrueです。
- **PutoutHeader** 
  値がtrueの場合、レポートヘッダーアイテムがエクスポートされます。値がfalseの場合、レポートヘッダーアイテムはエクスポートされません。デフォルト値はtrueです。この値はExcel2007Xlsx(Data Only)拡張子のみをサポートします。
- **PutoutFooter** 
  値がtrueの場合、レポートのフッターアイテムをエクスポートします。値がfalseの場合、レポートのフッターアイテムをエクスポートしません。デフォルト値はtrueです。これはExcel2007Xlsx（Data Only）拡張子のみをサポートします。
- **FillTableGroupHeaderForSimpleOutPut** 
  デフォルト値はfalseです。これはExcel2007Xlsx（Data Only）拡張子のみをサポートします。
- **NoOutPutTotalForSimpleOutPut** 
  デフォルト値はfalseです。これはExcel2007Xlsx（Data Only）拡張子のみをサポートします。
- **NoOutPutGroupForSimpleOutPut** 
  デフォルト値はfalseです。これはExcel2007Xlsx（Data Only）拡張子のみをサポートします。
- **NoDoGroupPageForSimpleOutPut** 
  デフォルト値はtrueです。これはExcel2007Xlsx（Data Only）拡張子のみをサポートします。
- **NoDoPageForSimpleOutPut** 
  デフォルト値はtrueです。これはExcel2007Xlsx（Data Only）拡張子のみをサポートします。
- **FieldDelimiter** 
  フィールドの区切り文字を設定します。この値はCSVおよびTXT拡張子をサポートします。 
