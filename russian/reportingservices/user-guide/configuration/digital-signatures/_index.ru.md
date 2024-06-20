---
title: Цифровые подписи
type: docs
weight: 50
url: /ru/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services поддерживает цифровые подписи при экспорте файлов Microsoft Excel 2007 или файлов ODS. У нас есть некоторая информация о конфигурации для цифровых подписей, которые можно установить в файле **Aspose.Cells.ReportingServices.xml**.

Когда значение DigitalSignature равно **off**, Aspose.Cells for Reporting Services отключает цифровые подписи.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

Когда значение DigitalSignature равно **on**, Aspose.Cells for Reporting Services включает цифровые подписи.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Есть четыре параметра в разделе DigitalSignature. Это: 

- **name**: представляет отчет, который нуждается в цифровой подписи. Когда параметр оставлен пустым, отчеты используют файл PFX для цифровых подписей.
- **pfxFilename**: относится к файлу PFX. Имя файла должно быть полным и содержать путь и расширение файла. Не должно быть пустым.
- **pfxPwd**: устанавливает пароль. Не должно быть пустым.
- **purpose**: описание того, для чего предназначена подпись. Может быть пустым.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
