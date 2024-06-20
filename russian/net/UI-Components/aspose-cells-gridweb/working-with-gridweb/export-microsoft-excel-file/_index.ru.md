---
title: Экспорт файла Microsoft Excel
type: docs
weight: 50
url: /ru/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb, экспорт
description: В данной статье рассматривается способ экспорта файлов в GridWeb.
---

{{% alert color="primary" %}} 

Веб-сайты поддерживают создание новых или изменение существующих файлов Microsoft Excel в режиме GUI с использованием элемента управления Aspose.Cells.GridWeb. Затем файлы могут быть сохранены в формате Excel. Aspose.Cells.GridWeb эффективно работает как онлайн-редактор электронных таблиц. В данной теме описывается, как сохранить содержимое сетки в файлы Excel.

{{% /alert %}} 
## **Экспорт файлов Excel**
### **Экспорт в виде файла**
Для сохранения содержимого элемента управления Aspose.Cells.GridWeb в файл Excel:

1. Добавьте элемент управления Aspose.Cells.GridWeb на свою веб-форму.
1. Сохраните свою работу в файл Excel в указанном пути.
1. Запустите приложение.

{{% alert color="primary" %}} 

Если вы не знаете, как добавить элемент управления Aspose.Cells.GridWeb на свою веб-форму, то вы можете обратиться к [Добавление GridWeb на веб-форму](/cells/ru/net/aspose-cells-gridweb/add-gridweb-to-web-form/).

{{% /alert %}} 

Когда элемент управления Aspose.Cells.GridWeb добавлен на форму Windows, элемент управления автоматически создается и добавляется на форму с ​​стандартным размером. Вам не нужно создавать объект элемента управления Aspose.Cells.GridWeb, вам нужно только перетащить элемент управления и начать его использовать.

Приведенный ниже пример кода иллюстрирует, как сохранить содержимое сетки в файл Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Если ваша файловая система NTFS, предоставьте пользовательским учетным записям ASPNET или Everyone права на чтение/запись, иначе вы получите исключение при выполнении доступа.

{{% /alert %}} 

Приведенный выше фрагмент кода может быть использован несколькими способами. Обычным способом является добавление кнопки, которая сохраняет содержимое сетки в файл Excel при нажатии. Aspose.Cells.GridWeb предлагает более простой подход к этой задаче. У Aspose.Cells.GridWeb есть событие, называемое SaveCommand. Приведенный выше фрагмент кода можно добавить в обработчик события SaveCommand, что позволит пользователям сохранять свою работу, нажав встроенную кнопку **Сохранить** в Aspose.Cells.GridWeb.

**Событие SaveCommand GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**Сохранение содержимого сетки в Excel при нажатии на встроенную кнопку «Сохранить» GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Если вы работаете в Visual Studio, вы можете легко создать обработчик события SaveCommand, дважды щелкнув на событие в панели **Свойства**. Для получения дополнительной информации обратитесь к [Работа с событиями GridWeb](/cells/ru/net/aspose-cells-gridweb/working-with-gridweb-events/).

{{% /alert %}} 
### **Экспорт в виде потока**
Также возможно сохранить содержимое сетки в поток (например, в MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
