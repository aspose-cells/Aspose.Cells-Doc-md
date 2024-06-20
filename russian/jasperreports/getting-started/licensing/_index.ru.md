---
title: Лицензирование
type: docs
weight: 40
url: /ru/jasperreports/licensing/
---

{{% alert color="primary" %}}

 Aspose.Cells for JasperReports доступно бесплатная, без временных ограничений оценка на [странице загрузки] (https://downloads.aspose.com/cells/jasperreports). Оценочные и лицензионные версии продукта являются одним и тем же загрузкой.

Когда вы будете довольны оценочной версией, вы можете [приобрести лицензию] (https://purchase.aspose.com/). Пожалуйста, ознакомьтесь и согласитесь с условиями лицензии.

 Лицензия доступна для загрузки со страницы заказа после оплаты заказа. Лицензия является четким текстом, цифровым подписанным XML-файлом. Лицензия содержит информацию, такую как имя клиента, купленный продукт и тип лицензии. Не изменяйте содержимое лицензионного файла: это приводит к недействительности лицензии.

Существуют два способа применения лицензии:

- [Вызов setLicense](/cells/ru/jasperreports/licensing/#call-setlicense)
- [Установите параметр экспортера в applicationContext.xml](/cells/ru/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

После установки лицензии,

- [Проверьте, что это работает] (/cells/ru/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Вызов setLicense**

{{% alert color="primary" %}}

Этот метод применим для использования с JasperReports.

{{% /alert %}}

Загрузите лицензию на свой компьютер и скопируйте ее в соответствующую папку (например, папку вашего приложения или **JasperReports\lib**).
Добавьте следующий код в ваш проект:

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Установите параметр экспорта лицензионного файла в applicationContext.xml**

{{% alert color="primary" %}}

Этот метод применим для использования с JasperServer.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Проверьте работу лицензии**

Экспортируйте любой отчет в формат XLS и проверьте, содержит ли отчет сообщение об оценке. Если нет сообщения об оценке, то лицензия работает правильно.

**Aspose.Cells for JasperReports внедряет оценочный рабочий лист в режиме оценки** 

![todo:image_alt_text](licensing_1.png)

**При наличии действительной лицензии нет оценочного рабочего листа** 

![todo:image_alt_text](licensing_2.png)
