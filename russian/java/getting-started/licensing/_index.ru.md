---
title: Licensing
type: docs
weight: 50
url: /ru/java/licensing/
description: Aspose.Cells для JAVA предоставляет различные планы покупки или предлагает бесплатную пробную версию и 30-дневную временную лицензию для ознакомления с использованием Licensing и политик подписки в Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **Как применить лицензию в компоненте Aspose.Cells**

Лицензия представляет собой обычный текстовый XML-файл, содержащий такие сведения, как название продукта, количество разработчиков, которым предоставлена лицензия, дата истечения срока подписки и т. д. Файл имеет цифровую подпись, поэтому не изменяйте его; даже случайное добавление дополнительного разрыва строки в файл сделает его недействительным.

Вам необходимо установить лицензию перед использованием Aspose.Cells, если вы хотите избежать ограничений ее оценки. Вам необходимо установить лицензию только один раз для каждого приложения или процесса.

Лицензию можно загрузить из потока или файла в следующих местах:

1. Явный путь.
1. Папка, содержащая файл Aspose.Cells.jar.

 Использовать[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) метод лицензирования компонента. Часто самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и Aspose.Cells.jar, и указать только имя файла без пути, как показано в следующем примере:

###  **Как применить лицензию с диска**

 В этом примере**Aspose.Cells**попытается найти файл лицензии в папке, содержащей JAR-файлы вашего приложения.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **Как применить лицензию из Stream**

Инициализирует лицензию из потока.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **Как применить лицензию в Aspose.Cells.GridWeb**

Рекомендуется поместить лицензионный код в то место вашего веб-приложения, где он должен быть обработан в первую очередь.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Как применить лимитную лицензию**

Aspose.Cells позволяет разработчикам применять дозированный ключ. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться наряду с существующим методом лицензирования. Те клиенты, которые хотят, чтобы им выставлялись счета на основе использования функций API, могут использовать дозированное лицензирование. Для получения более подробной информации см.[Измеренный Licensing Часто задаваемые вопросы](https://purchase.aspose.com/faqs/licensing/metered)раздел.

Новый класс[Измеренный](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)было введено применение дозированного ключа. Ниже приведен пример кода, демонстрирующий, как установить измеренный открытый и закрытый ключ.

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
