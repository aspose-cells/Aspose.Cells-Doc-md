---
title: rsreportserver.configファイルのDeviceInfo
type: docs
weight: 70
url: /ja/reportingservices/deviceinfo-in-rsreportserver-config-file/
---

**rsreportserver.config**のDeviceInfoセクションは、Aspose.Cellsの動作に影響する次のパラメーターを取ります。

- **FileExtension**: 値が**null**の場合、エクスポートされたレポートファイルの拡張子はデフォルト値となります。値がnullでない場合、レポートの拡張子はその値に設定されます。
- **SimplePageHeaders**: 値が**true**の場合、レポートヘッダーアイテムはMicrosoft Excelページヘッダーとしてレンダリングされます。デフォルト値は**false**です。
- **SimplePageFooters**: **true**の場合、レポートフッターアイテムはMicrosoft Excelページフッターとしてレンダリングされます。デフォルト値は**true**です。
- **PutoutHeader**: **true**（デフォルト）の場合、レポートヘッダーアイテムがエクスポートされます。**false**の場合、レポートヘッダーアイテムはエクスポートされません。Excel 2007 XLSX（データのみ）拡張子のみサポートされます。
- **PutoutFooter**: **true**（デフォルト）の場合、レポートフッターアイテムがエクスポートされます。**false**の場合、エクスポートされません。Excel 2007 XLSX（データのみ）拡張子のみサポートされます。
- **FillTableGroupHeaderForSimpleOutPut**: デフォルトでは**false**です。値はExcel 2007 XLSX（データのみ）拡張子のみサポートされます。
- **NoOutPutTotalForSimpleOutPut**: デフォルトでは**false**です。値はExcel 2007 XLSX（データのみ）拡張子のみサポートされます。
- **NoOutPutGroupForSimpleOutPut**: デフォルトでは**false**です。値はExcel 2007 XLSX（データのみ）拡張子のみサポートされます。
- **NoDoGroupPageForSimpleOutPut**: デフォルトでは**true**です。値はExcel 2007 XLSX（データのみ）拡張子のみサポートされます。
- **NoDoPageForSimpleOutPut**: デフォルトでは**true**です。値はExcel 2007 XLSX（データのみ）拡張子のみサポートされます。
- **FieldDelimiter**: フィールド区切り記号を設定します。値はCSVおよびTXT拡張子をサポートしています。
