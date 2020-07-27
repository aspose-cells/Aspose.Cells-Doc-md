+++
title = "Encryption" 
description = "" 
weight = 12084 
+++

Aspose.Cells for Reporting Services : Encryption  

# Aspose.Cells for Reporting Services : Encryption


Aspose.Cells for Reporting Services supports three kinds of encryption: XOR, WEAK ENCRYPTION, and Microsoft Strong Cryptographic Provider. See the encryption configuration information in the **Aspose.Cells.ReportingServices.xml** file.

When the value of `Encryption` is **off**, Aspose.Cells for Reporting Services turns off encryption features.

{{< code lang="cs" >}}
  < Encryption value="off">
    <Report name="" >
      <Password value=""/>
      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>
      <KeyLength value="128"/>
    </Report>
  </ Encryption >
{{< /code >}}

When the value of `Encryption` is **on**, Aspose.Cells for Reporting Services turns encryption on.

{{< code lang="cs" >}}
<Encryption value="on">
{{< /code >}}

There are four parameters in the encryption section:

*   **`ReportName`**: points to a report that needs encryption. If the parameter is left blank, all reports use the same encryption method.
*   **`Password`**: sets the password. Cannot be blank.
*   **`EncryptionType`**: sets an encryption type. Cannot be blank.
*   **`KeyLength`**: sets the key length. Cannot be blank.

{{< code lang="cs" >}}
<Encryption value="on">
  <Report name="Test" >
      <Password value="12345"/>
      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>
      <KeyLength value="128"/>
    </Report>
  	  <Report name="" >
      <Password value="123456"/>
      <EncryptionType value=" XOR "/>
      <KeyLength value="128"/>
    </Report>
 </Encryption>
{{< /code >}}

