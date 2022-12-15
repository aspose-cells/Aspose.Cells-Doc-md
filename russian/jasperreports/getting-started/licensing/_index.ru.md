---
title: Лицензирование
type: docs
weight: 40
url: /ru/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells for JasperReports доступен в качестве бесплатной, неограниченной по времени пробной версии от[страница загрузки](https://downloads.aspose.com/cells/jasperreports). Ознакомительная и лицензионная версии продукта загружаются одинаково.

 Если вас устраивает ознакомительная версия, вы можете[купить лицензию](https://purchase.aspose.com/). Убедитесь, что вы понимаете и согласны с условиями лицензии.

Лицензия доступна для скачивания со страницы заказа после оплаты заказа. Лицензия представляет собой обычный текстовый XML-файл с цифровой подписью. Лицензия содержит такую информацию, как имя клиента, приобретенный продукт и тип лицензии. Не изменяйте содержимое файла лицензии: это делает лицензию недействительной.

Применить лицензию можно двумя способами:

- [Вызов setLicense](/cells/ru/jasperreports/licensing/#call-setlicense)
- [Установите параметр экспортера в applicationContext.xml](/cells/ru/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

После установки лицензии

- [Убедитесь, что это работает](/cells/ru/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Вызов setLicense**

{{% alert color="primary" %}}

Этот метод применим для использования с JasperReports.

{{% /alert %}}

 Загрузите лицензию на свой компьютер и скопируйте ее в соответствующую папку (например, папку вашего приложения или**JasperReports\lib**).
Добавьте в свой проект следующий код:

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Задайте параметр экспортера licenseFile в applicationContext.xml.**

{{% alert color="primary" %}}

Этот метод применим для использования с JasperServer.

{{% /alert %}}

1.  Загрузите лицензию на свой компьютер и скопируйте ее на**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF**папка, где**\<Каталог_установки>** обозначает каталог установки JasperServer.
1.  Найдите**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** файл и добавьте следующие строки:

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Убедитесь, что лицензия работает**

Экспортируйте любой отчет в формат XLS и проверьте, содержит ли отчет оценочное сообщение. Если оценочного сообщения нет, значит, лицензия работает правильно.

**Aspose.Cells for JasperReports вводит лист оценки в режиме оценки** 

![дело:изображение_альтернативный_текст](licensing_1.png)

**При действующей лицензии лист оценки отсутствует** 

![дело:изображение_альтернативный_текст](licensing_2.png)
