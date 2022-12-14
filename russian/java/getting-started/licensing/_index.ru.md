---
title: Лицензирование
type: docs
weight: 50
url: /ru/java/licensing/
---
{{% alert color="primary" %}} 

 Вы можете скачать пробную версию**Aspose.Cells** for Java от[его страница загрузки](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven репозиторий. Ознакомительная версия предоставляет абсолютно те же возможности, что и лицензионная версия продукта. Кроме того, ознакомительная версия просто становится лицензируемой, когда вы покупаете лицензию и добавляете пару строк кода для применения лицензии.

 Когда вы довольны своей оценкой**Aspose.Cells** , Вы можете[купить лицензию](https://purchase.aspose.com)на сайте Aspose. Ознакомьтесь с различными предлагаемыми типами подписки. Если у вас есть какие-либо вопросы, не стесняйтесь обращаться к отделу продаж Aspose.

Каждая лицензия Aspose включает годовую подписку на бесплатные обновления до любых новых версий или исправлений, которые выйдут в течение этого времени. Техническая поддержка бесплатна и неограниченна и предоставляется как лицензированным, так и ознакомительным пользователям.

{{% /alert %}} {{% alert color="primary" %}} 

 Если вы хотите протестировать**Aspose.Cells** без ограничений ознакомительной версии запросите временную лицензию на 30 дней. Пожалуйста, обратитесь к[Как получить временную лицензию?](https://purchase.aspose.com/temporary-license) Чтобы получить больше информации.

{{% /alert %}}

## **Ограничения ознакомительной версии**

 Оценочная версия**Aspose.Cells** продукт (без указанной лицензии) обеспечивает полную функциональность продукта, но он ограничен открытием 100 файлов в одной программе и дополнительным рабочим листом с водяным знаком оценки.

Ограничения показаны ниже:

### **1-е ограничение: количество открытых файлов**

При запуске вашей программы вы можете открыть только 100 файлов Excel. Если ваше приложение превысит это число, будет выдано исключение.

### **2-е ограничение: Рабочий лист с оценочным водяным знаком**

![дело:изображение_альтернативный_текст](licensing_1.png)

Этот рабочий лист всегда будет отображаться как активный рабочий лист. Только в лицензионной версии вы можете установить активный рабочий лист на другие рабочие листы.

## **Установка лицензии**

Лицензия представляет собой простой текстовый XML-файл, который содержит такие сведения, как название продукта, количество разработчиков, для которых он лицензируется, дату истечения срока действия подписки и т. д. Файл имеет цифровую подпись, поэтому не изменяйте файл; даже непреднамеренное добавление дополнительного разрыва строки в файл сделает его недействительным.

Вам необходимо установить лицензию перед использованием Aspose.Cells, если вы хотите избежать ограничений оценки. Вы должны установить лицензию только один раз для каждого приложения или процесса.

Лицензия может быть загружена из потока или файла в следующих местах:

1. Явный путь.
1. Папка, содержащая файл Aspose.Cells.jar.

 Использовать[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) способ лицензирования компонента. Часто самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и Aspose.Cells.jar, и указать только имя файла без пути, как показано в следующем примере:

### **Пример 1**

 В этом примере**Aspose.Cells** попытается найти файл лицензии в папке, содержащей JAR-файлы вашего приложения.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Пример 2**

Инициализирует лицензию из потока.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Примечания по применению лицензии в Aspose.Cells.GridWeb**

Рекомендуется поместить лицензионный код в то место вашего веб-приложения, где он должен быть обработан в первую очередь.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Применение ограниченной лицензии**

Aspose.Cells позволяет разработчикам применять лимитный ключ. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться наряду с существующим методом лицензирования. Те клиенты, которые хотят получать счета на основе использования функций API, могут использовать лимитное лицензирование. Для получения более подробной информации см.[Часто задаваемые вопросы об ограниченном лицензировании](https://purchase.aspose.com/faqs/licensing/metered)раздел.

Новый класс[Измеренный](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)был введен для применения измеренного ключа. Ниже приведен пример кода, демонстрирующий, как установить открытый и закрытый ключ с измерителем.

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
