---
title: Реализация привязки данных GridDesktop в листах
type: docs
weight: 10
url: /ru/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop,привязка данных,данные,привязать
description: В этой статье рассматривается, как осуществлять привязку данных в GridDesktop.
---

{{% alert color="primary" %}} 

Привязка данных - это интересная функция, предлагаемая .NET Framework от Microsoft. Мы знаем, что элемент управления DataGrid, предлагаемый Microsoft, поддерживает привязку данных, что означает, что DataGrid может быть привязан к любому источнику данных (используя объекты DataSet, DataTable и DataView). Эта функция значительно облегчила жизнь разработчиков. Основываясь на этой же концепции, Aspose.Cells.GridDesktop также поддерживает привязку данных, позволяя разработчикам привязывать рабочие листы к любому источнику данных. В данной статье исследуется эта функция.

{{% /alert %}} 
## **Создание образца базы данных**
1. Создайте образец базы данных для использования в примере. Мы использовали Microsoft Access для создания образца базы данных с таблицей Products (схема ниже). 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. В таблицу Products добавлены три фиктивные записи.
   **Записи в таблице Products** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Создание образца приложения**
Теперь создайте простое десктопное приложение в Visual Studio и выполните следующие действия.

1. Перетащите элемент управления "GridControl" из панели инструментов на форму.
1. Перетащите четыре кнопки из панели инструментов внизу формы и установите их текстовое свойство соответственно как **Привязать рабочий лист**, **Добавить строку**, **Удалить строку** и **Обновить в базе данных**.
## **Добавление пространства имен и объявление глобальных переменных**
Поскольку в этом примере используется база данных Microsoft Access, добавьте пространство имен System.Data.OleDb в верхней части кода.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Теперь вы можете использовать классы, упакованные в этом пространстве имен.

1. Объявите глобальные переменные.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Заполнение DataSet данными из базы данных**
Теперь подключитесь к образцовой базе данных, чтобы извлечь данные и заполнить объект DataSet.

1. Используйте объект OleDbDataAdapter для соединения с нашей образцовой базой данных и заполните DataSet данными, извлеченными из таблицы Products в базе данных, как показано в приведенном ниже коде.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Привязка рабочего листа с DataSet**
Привяжите рабочий лист с таблицей Products из DataSet:

1. Получить доступ к желаемому рабочему листу.
1. Привязать рабочий лист к таблице продуктов DataSet.

Добавьте следующий код в событие нажатия кнопки **Привязать рабочий лист**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Установка заголовков столбцов рабочего листа**
Привязанный рабочий лист успешно загружает данные, но заголовки столбцов по умолчанию обозначены A, B и C. Было бы лучше установить заголовки столбцов в имена столбцов в таблице базы данных.

Для установки заголовков столбцов рабочего листа:

1. Получить подписи для каждого столбца DataTable (Products) в DataSet.
1. Назначить подписи заголовкам столбцов рабочего листа.

Добавьте код, написанный в событии нажатия кнопки **Привязать рабочий лист**, со следующим отрывком кода. Таким образом, старые заголовки столбцов (A, B и C) будут заменены на ProductID, ProductName и ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Настройка ширины и стилей столбцов**
Для улучшения внешнего вида рабочего листа можно установить ширину и стили столбцов. Например, иногда заголовок столбца или значение внутри столбца состоит из большого количества символов, которые не помещаются в ячейке. Для решения таких проблем Aspose.Cells.GridDesktop поддерживает изменение ширин столбцов.

Добавьте следующий код в кнопку **Привязать рабочий лист**. Ширина столбцов будет настроена в соответствии с новыми параметрами.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop также поддерживает применение пользовательских стилей к столбцам. Следующий код, добавленный к кнопке **Привязать рабочий лист**, настраивает стили столбцов, делая их более презентабельными.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


Теперь запустите приложение и нажмите кнопку **Привязать рабочий лист**.
## **Добавление строк**
Чтобы добавить новые строки на рабочий лист, используйте метод AddRow класса Worksheet. Это добавляет пустую строку внизу, а новая строка данных добавляется в источник данных (здесь новая строка данных добавляется в DataTable набора данных). Разработчики могут добавлять столько строк, сколько им нужно, вызывая метод AddRow снова и снова. Когда строка добавлена, пользователи могут ввести в нее значения.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Удаление строк**
Aspose.Cells.GridDesktop также поддерживает удаление строк с помощью метода RemoveRow класса Worksheet. Удаление строки с использованием Aspose.Cells.GridDesktop требует указания индекса удаляемой строки.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


Добавьте вышеуказанный код в кнопку **Удалить строку** и запустите приложение. Несколько записей отображаются до удаления строки. Выбор строки и нажатие кнопки **Удалить строку** удаляет выбранную строку.
## **Сохранение изменений в базе данных**
Наконец, чтобы сохранить любые изменения, внесенные пользователями в таблицу, обратно в базу данных, используйте метод Update объекта OleDbDataAdapter. Метод Update принимает источник данных (DataSet, DataTable и т. д.) таблицы для обновления базы данных.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. Добавьте вышеуказанный код к кнопке **Обновить в базе данных**.
1. Запустите приложение.
1. Выполните некоторые операции с данными таблицы, возможно, добавив новые строки и редактируя или удаляя существующие данные.
1. Затем щелкните по **Обновить в базе данных**, чтобы сохранить изменения в базе данных.
1. Проверьте базу данных, чтобы убедиться, что записи таблицы были соответственно обновлены.
