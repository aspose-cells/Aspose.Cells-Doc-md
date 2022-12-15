---
title: Поддержка цифровых подписей
type: docs
weight: 70
url: /ru/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

 Цифровая подпись гарантирует, что рабочая книга действительна и ее никто не изменил. Добавление цифровой подписи аналогично запечатыванию конверта. Если конверт приходит запечатанный, у вас есть определенная уверенность в том, что никто не подделывал его содержимое.

 Вы можете создать личную цифровую подпись с помощью Microsoft Selfcert.exe или любого другого инструмента, либо вы можете приобрести цифровую подпись. Чтобы подписать электронную таблицу, добавьте подпись к своим книгам после создания цифровой подписи.

 Aspose.Cells for Reporting Services поддерживает цифровые подписи.

{{% /alert %}} 
### **Работа с цифровыми подписями**
#### **Поддерживаемые форматы Excel для цифровых подписей**
Aspose.Cells for Reporting Services поддерживает цифровые подписи при экспорте в форматы файлов Excel 2007 и ODS.
#### **Настройка цифровых подписей**
**Aspose.Cells.ReportingServices.xml** файл содержит информацию о конфигурации и текст цифровой подписи в<DigitalSignature> ярлык:

- Когда цифровая подпись выключена, Aspose.Cells for Reporting Services отключает функцию цифровой подписи.
 Например:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Когда значение DigitalSignature включено, Aspose.Cells.ReportingServices включает функциональные возможности цифровой подписи.
 Например:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 В разделе DigitalSignature есть четыре параметра. Это :

- name — указывает на отчет, для которого требуется цифровая подпись. В отчете используется файл PFX для цифровой подписи, если параметр не указан.
- pfxFilename — указывает на файл PFX. Имя файла должно быть полным именем файла. Не может быть установлено пустое значение.
- pfxPwd — устанавливает пароль. Его нельзя оставлять пустым.
- цель – Объясняет цель подписи. Он может быть пустым.
 Например:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
