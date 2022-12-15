---
title: Настройка шифрования
type: docs
weight: 40
url: /ru/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services поддерживает шифрование, и вы можете отображать зашифрованные Microsoft файлы Excel.

{{% /alert %}} 
### **Типы шифрования**
Aspose.Cells for Reporting Services поддерживает шифрование при экспорте файлов Excel. Он поддерживает три типа шифрования:

- исключающее ИЛИ
- СЛАБОЕ ШИФРОВАНИЕ
- Microsoft Сильный поставщик криптографии
### **Настройка информации**
 Информация о настройке шифрования находится в**Aspose.Cells.ReportingServices.xml** файл. Когда для параметра Шифрование установлено значение «Выкл.», Aspose.Cells.ReportingServices отключает шифрование.

**XML**

{{< highlight "csharp" >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

Когда шифрование включено, Aspose.Cells.ReportingServices включает шифрование.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

В разделе Encryption есть четыре параметра: ReportName, Password, EncryptionType и KeyLength.

- ReportName — задает отчет, для которого требуются параметры шифрования. В отчете используется тот же способ шифрования, если параметр не указан.
- Пароль – устанавливает пароль. Его нельзя оставлять пустым.
- EncryptionType — устанавливает тип шифрования. Его нельзя оставлять пустым.
-  KeyLength — устанавливает длину ключа. Его нельзя оставлять пустым.

**XML**

{{< highlight "csharp" >}}

 <Encryption value="on">

<Report name="Test" >

<Password value="12345"/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

<Report name="" >

<Password value="123456"/>

<EncryptionType value="XOR"/>

<KeyLength value="128"/>

</Report>

</Encryption>



{{< /highlight >}}
