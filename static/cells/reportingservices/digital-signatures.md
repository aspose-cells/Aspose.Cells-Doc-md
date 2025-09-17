##Digital Signatures
Aspose.Cells for Reporting Services supports digital signatures when exporting Microsoft Excel 2007 files or ODS files. We have some configuration information for digital signatures that can be set in the **Aspose.Cells.ReportingServices.xml** file.
When the value of DigitalSignature is **off**, Aspose.Cells for Reporting Services turns off digital signatures.
When the value of DigitalSignature is **on**, Aspose.Cells for Reporting Services turns digital signatures on.
There are four parameters in the DigitalSignature section. These are:
- **name**: represents a report that needs a digital signature. When the parameter is left blank, reports use a PFX file for digital signatures.
- **pfxFilename**: refers to a PFX file. The filename should be a fully qualified filename, complete with path and file extension. Must not be blank.
- **pfxPwd**: sets the password. Must not be blank.
- **purpose**: a description of what the signature if for. Can be blank.
