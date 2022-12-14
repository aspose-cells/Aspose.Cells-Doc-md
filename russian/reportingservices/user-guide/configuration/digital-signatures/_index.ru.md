---
title: Цифровые подписи
type: docs
weight: 50
url: /ru/reportingservices/digital-signatures/
---
 Aspose.Cells для служб Reporting Services поддерживает цифровые подписи при экспорте Microsoft файлов Excel 2007 или файлов ODS. У нас есть некоторая информация о конфигурации цифровых подписей, которую можно установить в**Aspose.Cells.ReportingServices.xml** файл.

 Когда значение DigitalSignature равно**выключенный**, Aspose.Cells для Reporting Services отключает цифровые подписи.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 Когда значение DigitalSignature равно**на**, Aspose.Cells для Reporting Services включает цифровые подписи.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 В разделе DigitalSignature есть четыре параметра. Это:

- **имя**представляет отчет, для которого требуется цифровая подпись. Если параметр оставить пустым, в отчетах для цифровых подписей используется файл PFX.
- **pfxFilename**: относится к файлу PFX. Имя файла должно быть полным именем файла, дополненным путем и расширением файла. Не должно быть пустым.
- **pfxPwd**: устанавливает пароль. Не должно быть пустым.
- **цель**: описание того, для чего подпись. Может быть пустым.

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
