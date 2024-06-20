---
title: Шифрование
type: docs
weight: 40
url: /ru/reportingservices/encryption/
---

Aspose.Cells for Reporting Services поддерживает три вида шифрования: XOR, WEAK ENCRYPTION и Microsoft Strong Cryptographic Provider. См. информацию о конфигурации шифрования в файле **Aspose.Cells.ReportingServices.xml**.

Когда значение Encryption равно **off**, Aspose.Cells for Reporting Services отключает функции шифрования.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

Когда значение Encryption равно **on**, Aspose.Cells for Reporting Services включает шифрование.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Есть четыре параметра в разделе шифрования:

- **ReportName**: указывает на отчет, который нуждается в шифровании. Если параметр оставлен пустым, все отчеты используют один и тот же метод шифрования.
- **Пароль**: устанавливает пароль. Не может быть пустым.
- **ТипШифрования**: устанавливает тип шифрования. Не может быть пустым.
- **ДлинаКлюча**: устанавливает длину ключа. Не может быть пустым.

{{< highlight java >}}

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
