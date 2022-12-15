---
title: Шифрование
type: docs
weight: 40
url: /ru/reportingservices/encryption/
---
 Aspose.Cells for Reporting Services поддерживает три вида шифрования: XOR, WEAK ENCRYPTION и Microsoft Strong Cryptographic Provider. См. информацию о конфигурации шифрования в**Aspose.Cells.ReportingServices.xml** файл.

 Когда значение шифрования равно**выключенный**, Aspose.Cells for Reporting Services отключает функции шифрования.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 Когда значение шифрования равно**на**, Aspose.Cells for Reporting Services включает шифрование.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

В разделе шифрования есть четыре параметра:

- **ReportName**: указывает на отчет, который требует шифрования. Если параметр оставить пустым, во всех отчетах используется один и тот же метод шифрования.
- **Пароль**устанавливает пароль. Не может быть пустым.
- **Тип шифрования**: устанавливает тип шифрования. Не может быть пустым.
- **длина ключа**: устанавливает длину ключа. Не может быть пустым.

{{< highlight "java" >}}

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

{{< /highlight >}}
