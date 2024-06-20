---
title: Лицензирование
type: docs
weight: 50
url: /ru/java/licensing/
description: Aspose.Cells for JAVA предоставляет различные планы для покупки или предлагает бесплатную пробную версию и временную лицензию на 30 дней для оценки с использованием политик по лицензированию и подписке на Java.
keywords: Применить лицензию в Aspose.Cells for Java.
---

## **Как применить лицензию в компонент Aspose.Cells**

Лицензия представляет собой файл XML в формате обычного текста, который содержит такие детали, как название продукта, количество разработчиков, на которых она лицензирована, дата истечения подписки и т. д. Файл имеет цифровую подпись, поэтому не изменяйте его; даже непреднамеренное добавление дополнительного перевода строки в файл приведет к его недействительности.

Вам необходимо установить лицензию перед использованием Aspose.Cells, если вы хотите избежать оценочных ограничений. Вам нужно установить лицензию только один раз для каждого приложения или процесса.

 Лицензия может быть загружена из потока или файла в следующих местах:

1. Явный путь.
 1. Папка, содержащая файл Aspose.Cells.jar.

 Используйте метод [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) для лицензирования компонента. Часто самым простым способом установить лицензию является поместить файл лицензии в ту же папку, что и Aspose.Cells.jar, и указать только имя файла без пути, как показано в следующем примере:

### ** Как применить лицензию с диска**

 В этом примере **Aspose.Cells** попытается найти файл лицензии в папке, содержащей JAR вашего приложения.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### ** Как применить лицензию из потока**

Инициализирует лицензию из потока.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Как применить лицензию в Aspose.Cells.GridWeb**

Рекомендуется разместить лицензионный код в месте вашего веб-приложения, где он должен быть обработан в первую очередь.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Как применить метрическую лицензию**

Aspose.Cells позволяет разработчикам применять метрический ключ. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться вместе с существующим методом лицензирования. Те клиенты, которые хотят платить в зависимости от использования функций API, могут использовать метрическое лицензирование. Для получения дополнительной информации обратитесь к разделу [Часто задаваемые вопросы о метрическом лицензировании](https://purchase.aspose.com/faqs/licensing/metered).

Введен новый класс [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) для применения метрического ключа. Ниже приведен образец кода, демонстрирующий, как установить открытый и закрытый метрический ключ.

{{< highlight java >}}

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
