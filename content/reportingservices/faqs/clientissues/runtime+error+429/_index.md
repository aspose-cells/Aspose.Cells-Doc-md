---
title : "Runtime Error 429" 
description : "" 
weight : 12103 
toc : false
type: docs
url: /reportingservices/faqs/clientissues/runtime+error+429/
---

# Aspose.Cells for Reporting Services : Runtime Error 429


##### Description

Run-time error: '429'  
ActiveX component can't create object  
The line causing the error is:  
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient").

##### Solution

Re-register **Aspose.Cells.ReportingServices.Client.dll** using the **Regasm.exe** utility:

1.  Run cmd.exe as administrator.
2.  cd $(Aspose.Cells for Reporting Services installation folder).
3.  Execute **regasm.exe** to register **Aspose.Cells.ReportingServices.Client.dll** manually.
    
    ...%WINDIR%\\Microsoft.NET\\Framework\\v2.0.50727\\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase
    

Please check the running environment for your system. For example:

*   If your Microsoft Office is x64, run the command
    
    @: ...%WINDIR%\\Microsoft.NET\\Framework64\\v2.0.50727\\regasm.exe
    
*   If your Microsoft Office is x86, run the command
    
    @: ...%WINDIR%\\Microsoft.NET\\Framework\\v2.0.50727\\regasm.exe
    

Please refer to the following example/command:

...%WINDIR%\\Microsoft.NET\\Framework\\v2.0.50727\\regasm "C:\\Program Files (x86)\\Aspose\\Aspose.Cells for Reporting Services\\Bin\\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

