﻿---
title: Реализация функции привязки данных GridDesktop на листах
type: docs
weight: 10
url: /ru/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

Привязка данных — это интересная функция, предлагаемая платформой Microsoft .NET. Мы знаем, что элемент управления DataGrid, предлагаемый Microsoft, поддерживает привязку данных, что означает, что DataGrid может быть привязан к любому источнику данных (с использованием объектов DataSet, DataTable и DataView). Эта функция значительно облегчила жизнь разработчикам. Основываясь на той же концепции, Aspose.Cells.GridDesktop также поддерживает привязку данных, что позволяет разработчикам привязывать рабочие листы к любому источнику данных. В этой статье рассматривается эта функция.

{{% /alert %}} 
## **Создание образца базы данных**
1.  Создайте образец базы данных для использования в примере. Мы использовали Microsoft Access для создания примера базы данных с таблицей Products (схема ниже).

![дело:изображение_альтернативный_текст](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. В таблицу «Продукты» добавляются три фиктивные записи.
   **Записи в таблице продуктов** 

![дело:изображение_альтернативный_текст](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Создайте образец приложения**
Теперь создайте простое настольное приложение в Visual Studio и выполните следующие действия.

1. Перетащите элемент управления «GridControl» из панели инструментов и поместите его на форму.
1. Перетащите четыре кнопки из панели инструментов в нижнюю часть формы и установите для их текстового свойства значение**Связать рабочий лист**, **Добавить ряд**, **Удалить строку** и**Обновление базы данных** соответственно.
## **Добавление пространства имен и объявление глобальных переменных**
Поскольку в этом примере используется база данных Access Microsoft, добавьте пространство имен System.Data.OleDb в начало кода.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Теперь вы можете использовать классы, упакованные в этом пространстве имен.

1. Объявите глобальные переменные.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Заполнение набора данных данными из базы данных**
Теперь подключитесь к образцу базы данных, чтобы получить и заполнить данные в объекте DataSet.

1. Используйте объект OleDbDataAdapter для подключения к нашей тестовой базе данных и заполните DataSet данными, полученными из таблицы Products в базе данных, как показано в приведенном ниже коде.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Связывание рабочего листа с набором данных**
Свяжите рабочий лист с таблицей Products набора данных:

1. Доступ к нужному рабочему листу.
1. Свяжите рабочий лист с таблицей продуктов набора данных.

 Добавьте следующий код в**Связать рабочий лист** событие нажатия кнопки.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Настройка заголовков столбцов рабочего листа**
Связанный рабочий лист теперь успешно загружает данные, но заголовки столбцов по умолчанию помечены буквами A, B и C. Было бы лучше установить заголовки столбцов на имена столбцов в таблице базы данных.

Чтобы установить заголовки столбцов рабочего листа:

1. Получите заголовки для каждого столбца DataTable (Products) в наборе данных.
1. Назначьте заголовки заголовкам столбцов рабочего листа.

 Добавьте код, написанный в**Связать рабочий лист** событие нажатия кнопки со следующим фрагментом кода. При этом старые заголовки столбцов (A, B и C) будут заменены на ProductID, ProductName и ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Настройка ширины и стилей столбцов**
Чтобы еще больше улучшить внешний вид рабочего листа, можно установить ширину и стили столбцов. Например, иногда заголовок столбца или значение внутри столбца состоит из большого количества символов, которые не помещаются внутри ячейки. Для решения таких проблем Aspose.Cells.GridDesktop поддерживает изменение ширины столбцов.

 Добавьте следующий код в**Связать рабочий лист** кнопка. Ширина столбцов будет настроена в соответствии с новыми настройками.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop также поддерживает применение пользовательских стилей к столбцам. Следующий код, добавленный к**Связать рабочий лист** Кнопка настраивает стили столбцов, чтобы сделать их более презентабельными.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 Теперь запустите приложение и нажмите кнопку**Связать рабочий лист** Кнопка.
## **Добавление строк**
Чтобы добавить новые строки на лист, используйте метод AddRow класса Worksheet. Это добавит пустую строку внизу, и в источник данных будет добавлена новая строка DataRow (здесь новая строка данных добавляется в DataTable набора данных). Разработчики могут добавлять столько строк, сколько хотят, снова и снова вызывая метод AddRow. После добавления строки пользователи могут вводить в нее значения.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Удаление строк**
Aspose.Cells.GridDesktop также поддерживает удаление строк путем вызова метода RemoveRow класса Worksheet. Удаление строки с помощью Aspose.Cells.GridDesktop требует удаления индекса строки.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 Добавление приведенного выше кода в**Удалить строку** кнопку и запустите приложение. Перед удалением строки отображается несколько записей. Выбор строки и нажатие кнопки**Удалить строку** Кнопка удаляет выбранную строку.
## **Сохранение изменений в базе данных**
Наконец, чтобы сохранить любые изменения, внесенные пользователями в рабочий лист, обратно в базу данных, используйте метод Update объекта OleDbDataAdapter. Метод Update использует источник данных (DataSet, DataTable и т. д.) рабочего листа для обновления базы данных.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  Добавьте приведенный выше код в**Обновление базы данных** кнопка.
1. Запустите приложение.
1. Выполните некоторые операции с данными рабочего листа, возможно, добавьте новые строки и отредактируйте или удалите существующие данные.
1.  Затем нажмите**Обновление базы данных** для сохранения изменений в базе данных.
1. Проверьте базу данных, чтобы убедиться, что записи в таблице обновлены соответствующим образом.
