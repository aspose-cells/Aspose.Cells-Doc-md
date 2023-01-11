﻿---
title: Сохранение файла Excel
type: docs
weight: 20
url: /ru/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

Используя элемент управления Aspose.Cells.GridDesktop, пользователи могут не только создавать новые файлы Excel, но и управлять существующими. Но в обоих случаях необходимо сохранить содержимое файла Aspose.Cells.GridDesktop. Итак, это тема нашего обсуждения, чтобы наши пользователи знали, как они могут сохранить содержимое своей сетки в виде файла Excel.

{{% /alert %}} 
## **Вступление**
Чтобы сохранить содержимое элемента управления Aspose.Cells.GridDesktop в виде файла Excel, Aspose.Cells.GridDesktop предоставляет следующие методы.

1. **Сохранение в виде файла**
1. **Сохранение в виде потока**
## **Сохранение файла**
 Создайте настольное приложение и добавьте в форму две кнопки с элементом управления GridControl. Установите текстовые свойства кнопок как**Сохранить как файл** и**Сохранить как поток** соответственно.
### **Сохранение в виде файла**
 Создайте событие Click для**Сохранить как файл** кнопку и вставьте в нее следующий код.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

ВАЖНО: Важным моментом для обсуждения является то, что элемент управления Aspose.Cells.GridDesktop также содержит метод с именем SaveToExcel , который также используется для загрузки содержимого файла Excel в сетку. Но сейчас этот метод устарел. Таким образом, всем разработчикам рекомендуется использовать метод ExportExcelFile, который является более надежным и эффективным, чем устаревший.

{{% /alert %}} 
### **Сохранение в виде потока**
 Иногда разработчикам может потребоваться сохранить содержимое сетки в поток (например, MemoryStream). Для облегчения этой задачи элемент управления Aspose.Cells.GridDesktop также поддерживает сохранение данных Grid в поток. Создайте событие Click для**Сохранить как поток** кнопку и вставьте в нее следующий код.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

ВАЖНО: Microsoft Excel поддерживает листы Excel, которые могут содержать до 65 536 строк и 256 столбцов. Aspose.Cells.GridDesktop также следует тем же стандартам. В элементе управления Aspose.Cells.GridDesktop разработчики могут создавать больше строк и столбцов, чем стандартное ограничение, но при сохранении данных сетки в файл Excel будет выдано исключение. Это означает, что только данные, содержащиеся в 65 536 строках и 256 столбцах, могут быть сохранены в файл Excel с использованием Aspose.Cells.GridDesktop.

{{% /alert %}}