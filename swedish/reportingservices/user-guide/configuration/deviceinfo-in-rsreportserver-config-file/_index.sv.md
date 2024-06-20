---
title: DeviceInfo i rsreportserver.config filen
type: docs
weight: 70
url: /sv/reportingservices/deviceinfo-in-rsreportserver-config-file/
---

DeviceInfo-avsnittet i **rsreportserver.config** har följande parametrar som påverkar Aspose.Cells beteende:

- **FileExtension**: när värdet är **null** är den exporterade rapportfilens tillägg standardvärdet. När värdet inte är null är rapportens tillägg satt till värdet.
- **SimplePageHeaders**: när värdet är **true** renderas rapporthuvudobjektet som en Microsoft Excel sidhuvud. Standardvärdet är **false**.
- **SimplePageFooters**: när **true** renderas rapportfotsobjektet som en Microsoft Excel sidfot. Standardvärdet är **true**.
- **PutoutHeader**: när **true** (standard) exporteras rapporthuvudobjektet. När **false** exporteras inte rapporthuvudobjektet. Stöder endast Excel 2007 XLSX (endast data) tillägg.
- **PutoutFooter**: när **true** (standard) exporteras rapportfotsobjektet. När **false** exporteras det inte. Stöder endast Excel 2007 XLSX (endast data) tillägg.
- **FillTableGroupHeaderForSimpleOutPut**: **false** som standard. Värdet stöder endast Excel 2007 XLSX (endast data) tillägg.
- **NoOutPutTotalForSimpleOutPut**: **false** som standard. Värdet stöder endast Excel 2007 XLSX (endast data) tillägg.
- **NoOutPutGroupForSimpleOutPut**: **false** som standard. Värdet stöder endast Excel 2007 XLSX (endast data) tillägg.
- **NoDoGroupPageForSimpleOutPut**: **true** som standard. Värdet stöder endast Excel 2007 XLSX (endast data) tillägg.
- **NoDoPageForSimpleOutPut**: **true** som standard. Värdet stöder endast Excel 2007 XLSX (endast data) tillägg.
- **FieldDelimiter**: sätter fältdelare. Värdet stödjer CSV- och TXT-tillägg.
