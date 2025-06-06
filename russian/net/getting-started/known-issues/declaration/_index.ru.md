---
title: Объявление
type: docs
weight: 30
url: /ru/net/declaration/
---

{{% alert color="primary" %}} 

В общем, все компоненты Aspose .NET требуют установки полномочий Полного доверия. Причина в том, что компоненты Aspose для .NET должны иметь доступ к настройкам реестра, системным файлам, отличным от виртуального каталога для определенных операций, таких как анализ шрифтов и т. д. Более того, компоненты Aspose для .NET (включая Aspose.Cells for .NET) основаны на основных классах системы .NET, которые также требуют установки полномочий Полного доверия во многих случаях.

{{% /alert %}} 
## **Частичное доверие / Задача среднего доверия**
Провайдеры интернет-услуг, размещающие несколько приложений различных компаний, чаще всего налагают уровень безопасности Среднего доверия. Более того, иногда вам нужно разместить несколько приложений на общем сервере, например, в ESP или других сценариях, вам придется использовать уровень доверия Среднего уровня, чтобы ограничить приложения. Уровень доверия ASP.NET обеспечивает ограниченную среду выполнения, подходящую для изоляции нескольких приложений, размещенных на серверах ISP. В случае .NET 2.0 такой уровень безопасности может устанавливать следующие ограничения, которые могут повлиять на возможность Aspose.Cells for .NET выполняться должным образом, например:

- **RegistryPermission недоступен**. Это означает, что вы не можете получить доступ к реестру, что требуется для перечисления установленных шрифтов при рендеринге электронных таблиц или других документов.
- **FileIOPermission ограничен**. Это означает, что вы можете получить доступ только к файлам в иерархии виртуального каталога вашего приложения. Это потенциально означает, что шрифты не могут быть прочитаны во время экспорта.
## **Использование Aspose.Cells for .NET с установленным разрешением Среднего доверия**
Вы можете следовать некоторым рекомендациям для запуска Aspose.Cells for .NET на уровне среднего доверия или в среде общего сервера:

- Чтобы установить файл лицензии в своем коде, лучше вызовите метод License.SetLicense(Stream) после получения файла лицензии в потоки.
- Должен быть установлен каталог шрифтов (к которому можно обратиться с разрешением). Если нет возможности получить доступ к файлу на сервере, добавьте необходимые файлы шрифтов в ваше приложение.
- В режиме частичного доверия не поддерживается преобразование Shape в EMF, поэтому установите тип экспортируемого изображения (для форм) в другие форматы изображений.

Посмотрите следующий пример, демонстрирующий, как использовать/запустить Aspose.Cells for .NET в режиме Medium Trust.

{{< highlight csharp >}}

 // Instantiate the License object

Aspose.Cells.License lic = new Aspose.Cells.License();

// Get the license file into stream

System.IO.Stream stream = System.IO.File.OpenRead(MapPath("~") + @"\Aspose.Cells.lic");

// Set the License stream

lic.SetLicense(stream);

// Close the stream

stream.Close();

// Set the fonts directory

CellsHelper.FontDir = MapPath("~") + @"\Fonts";

//Open the template file

Workbook workbook = new Workbook(MapPath("~") + @"\test.xlsx");

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

// Set the image type to other format instead of using the default image type, that is, EMF

pdfSaveOptions.ImageType = System.Drawing.Imaging.ImageFormat.Png;

// Save the PDF file

workbook.Save(MapPath("~") + @"\dest.pdf", pdfSaveOptions);

// Save the XLSX file

workbook.Save(MapPath("~") + @"\dest.xlsx");



{{< /highlight >}}





{{< app/cells/assistant language="csharp" >}}
