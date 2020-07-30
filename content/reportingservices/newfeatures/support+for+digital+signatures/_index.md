---
title : "Support for Digital Signatures" 
description : "" 
weight : 8035 
toc : false
type: docs
url: /reportingservices/newfeatures/support+for+digital+signatures/
---

# Aspose.Cells for Reporting Services : Support for Digital Signatures


A digital signature provides assurance that a workbook is valid and no one has altered it. Attaching a digital signature is similar to sealing an envelope. If an envelope arrives sealed, you have some level of assurance that no one has tampered with its contents.

You can create a personal digital signature by using the Microsoft Selfcert.exe or any other tool, or you can purchase a digital signature. To sign a spreadsheet, attach a signature to your workbooks once you have created a digital signature.

Aspose.Cells for Reporting Services supports digital signatures.

### Working with Digital Signatures

#### Supported Excel Formats for Digital Signatures

Aspose.Cells for Reporting Services supports digital signatures when exporting to Excel 2007 and ODS file formats.

#### Configuring Digital Signatures

The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the `<DigitalSignature>` tag:

*   When `DigitalSignature` is set to `off`, Aspose.Cells for Reporting Services turns off the digital signature functionality.  
    For example:
    
{{< code lang="cs" >}}
<DigitalSignature value="off">
<report name="" pfxFilename="" pfxPwd="" purpose=""/>
</DigitalSignature>
{{< /code >}}
    
*   When the value of `DigitalSignature` is `on`, Aspose.Cells.ReportingServices turns on the functionality of digital signature.  
    For example:
    
{{< code lang="cs" >}}
<DigitalSignature value="on">
{{< /code >}}
    
    There are four parameters in `DigitalSignature` section. These are :
    *   `name` – Points to a report that needs a digital signature. The report uses a PFX file for digital signature when the parameter is blank.
    *   `pfxFilename` – Points to the PFX file. The filename must be a complete filename. It cannot be set to a blank value.
    *   `pfxPwd` – Sets the password. It cannot be left blank.
    *   `purpose` – Explains the signature's purpose. It can be blank.  
        For example:
        
{{< code lang="cs" >}}
<DigitalSignature value="on">
<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>
<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>
</DigitalSignature>
{{< /code >}}
        

