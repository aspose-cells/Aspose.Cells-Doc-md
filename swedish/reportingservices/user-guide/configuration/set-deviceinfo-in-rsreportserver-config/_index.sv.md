---
title: Ställ in DeviceInfo i rsreportserver.config
type: docs
weight: 60
url: /sv/reportingservices/set-deviceinfo-in-rsreportserver-config/
---

- **FileExtension** 
  När värdet är null, kommer den exporterade rapportfilens filändelse vara standardvärdet. När värdet inte är null, är filändelsen för den exporterade rapportfilen värdet.
- **SimplePageHeaders** 
  När värdet är sant renderar det rapporthuvudobjektet i Excel sidhuvudet. Standardvärdet är falskt.
- **SimplePageFooters** 
  När värdet är sant renderar det rapportfotobjektet i Excel sidfoten. Standardvärdet är sant.
- **PutoutHeader** 
  När värdet är sant exporteras rapporthuvudobjektet. När värdet är falskt exporteras det inte rapporthuvudobjektet. Standardvärdet är sant. Värdet stöder endast Excel2007Xlsx(Data Only) filändelsen.
- **PutoutFooter** 
  När värdet är sant exporteras rapportfotobjektet. När värdet är falskt exporteras det inte rapportfotobjektet. Standardvärdet är sant. Värdet stöder endast Excel2007Xlsx(Data Only) filändelsen.
- **FillTableGroupHeaderForSimpleOutPut** 
  Standardvärdet är falskt. Värdet stöder endast Excel2007Xlsx(Data Only) filändelsen.
- **NoOutPutTotalForSimpleOutPut** 
  Standardvärdet är falskt. Värdet stöder endast Excel2007Xlsx(Data Only) filändelsen.
- **NoOutPutGroupForSimpleOutPut** 
  Standardvärdet är falskt. Värdet stöder endast Excel2007Xlsx(Data Only) filändelsen.
- **NoDoGroupPageForSimpleOutPut** 
  Standardvärdet är sant. Värdet stöder endast Excel2007Xlsx(Data Only) filändelsen.
- **NoDoPageForSimpleOutPut** 
  Standardvärdet är sant. Värdet stöder endast Excel2007Xlsx(Data Only) filändelsen.
- **FieldDelimiter** 
  Det sätter fältdelare. Värdet stöder CSV- och TXT-filändelser. 
