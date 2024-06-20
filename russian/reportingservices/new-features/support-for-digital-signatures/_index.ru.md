---
title: Поддержка цифровых подписей
type: docs
weight: 70
url: /ru/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

Цифровая подпись обеспечивает уверенность в том, что рабочая книга действительна и никто ее не изменял. Прикрепление цифровой подписи подобно запечатыванию конверта. Если запечатанный конверт пришел, у вас есть определенная уверенность в том, что никто не манипулировал его содержимым. 

Вы можете создать личную цифровую подпись, используя Microsoft Selfcert.exe или любой другой инструмент, или приобрести цифровую подпись. Чтобы подписать электронную таблицу, присоедините подпись к рабочим книгам после создания цифровой подписи. 

Aspose.Cells for Reporting Services поддерживает цифровые подписи. 

{{% /alert %}} 
### **Работа с цифровыми подписями**
#### **Поддерживаемые форматы Excel для цифровых подписей**
Aspose.Cells for Reporting Services поддерживает цифровые подписи при экспорте в форматах Excel 2007 и ODS.
#### **Настройка цифровых подписей**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- Когда параметр DigitalSignature отключен, Aspose.Cells for Reporting Services отключает функциональность цифровой подписи.
  Например: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Когда значение DigitalSignature включено, Aspose.Cells.ReportingServices включает в функциональность цифровой подписи.
  Например: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

В разделе ЦифроваяПодпись четыре параметра. Они : 

- name – Ссылается на отчет, который требует цифровой подписи. Для подписи отчета используется файл PFX, если параметр пустой.
- pfxFilename – Указывает на файл PFX. Имя файла должно быть полным. Нельзя установить пустое значение.
- pfxPwd – Устанавливает пароль. Нельзя оставить пустым.
- purpose – Объясняет цель подписи. Может быть пустым.
  Например: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
