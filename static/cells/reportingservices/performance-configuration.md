##Performance Configuration
Users can optimize performance to a certain extent. You can configure some attributes and parameters in the **Aspose.Cells.ReportingServices.xml** file as described below.
### **Performance Section**
This shows the Performance section as it is by default.
**XML**
### **Performance Parameters**
- LimitCellsNumberForMerged – The default value of the parameter is 1000000. The parameter value is set by the client and is not effected by the performance parameter's switch. Please refer to the following configuration.
**XML**
- IsAutoRowFit – Can be either true or false:
- When the Performance parameter is set to ‘off’, the default value is false.
- When the Performance parameter is set to ‘on’, the default value is true.
- When the Performance parameter is set to ‘on’, a sub-element report can re-set the report’s AutoRowFile paramter.
Please refer to the following configuration.
**XML**
- IsMerged – Can be either true or false:
- When the Performance parameter is set to ‘off’, the default value is false.
- When the Performance parameter is set to ‘on’, the default value is true.
- When the Performance parameter is set to ‘on’, a sub-element report can re-set the report’s AutoRowFile paramter.
Please refer to the following configuration.
**XML**
- IsSetStyle – Can be either true or false:
- When the Performance parameter is set to ‘off’, the default value is false.
- When the Performance parameter is set to ‘on’, the default value is true.
- When the Performance parameter is set to ‘on’, a sub-element report can re-set the report’s AutoRowFile paramter.
Please refer to the following configuration.
**XML**
- IsConditionalFormatting – Can be either true or false:
- When the Performance parameter is set to ‘off’, the default value is false.
- When the Performance parameter is set to ‘on’, the default value is true.
- When the Performance parameter is set to ‘on’, sub-element report can re-set point report’s AutoRowFile paramter.
- When the IsSetStyle parameter is set to false, the value of the Performance parameter is invalid.
Please refer to the following configuration.
**XML**
