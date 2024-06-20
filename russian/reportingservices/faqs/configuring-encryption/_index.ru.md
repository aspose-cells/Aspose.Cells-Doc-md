---
title: Настройка шифрования
type: docs
weight: 40
url: /ru/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services поддерживает шифрование и вы можете отображать зашифрованные файлы Microsoft Excel. 

{{% /alert %}} 
### **Типы шифрования**
Aspose.Cells for Reporting Services поддерживает шифрование при экспорте файлов Excel. Он поддерживает три типа шифрования:

- XOR
- СЛАБОЕ ШИФРОВАНИЕ
- Провайдер криптографии Microsoft Strong
### **Настройка информации**
Существует информация для настройки шифрования в файле **Aspose.Cells.ReportingServices.xml**. Когда значение Encryption установлено в «выключено», Aspose.Cells.ReportingServices отключает шифрование.

**XML**

{{< highlight csharp >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

Когда Encryption установлено в «включено», Aspose.Cells.ReportingServices включает шифрование.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

В разделе шифрования есть четыре параметра: ReportName, Password, EncryptionType и KeyLength.

- ReportName – Устанавливает отчет, который нуждается в настройках шифрования. Отчет использует тот же способ шифрования, когда параметр пуст.
- Password – Устанавливает пароль. Не может быть пустым.
- EncryptionType – Устанавливает тип шифрования. Не может быть пустым.
- KeyLength – Устанавливает длину ключа. Не может быть пустым. 

**XML**

{{< highlight csharp >}}

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
