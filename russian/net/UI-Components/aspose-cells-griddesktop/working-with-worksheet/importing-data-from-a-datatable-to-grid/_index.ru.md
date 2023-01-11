﻿---
title: Импорт данных из таблицы данных в сетку
type: docs
weight: 50
url: /ru/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

С момента выпуска .NET Framework Microsoft предоставляет отличный способ хранения данных в автономном режиме в форме объекта DataTable. Понимая потребности разработчиков, Aspose.Cells.GridDesktop также поддерживает импорт данных из таблицы данных. В этой теме обсуждается, как это сделать.

{{% /alert %}} 
## **Пример**
Чтобы импортировать содержимое таблицы данных с помощью элемента управления Aspose.Cells.GridDesktop:

1. Добавьте в форму элемент управления Aspose.Cells.GridDesktop.
1. Создайте объект DataTable, содержащий данные для импорта.
1. Получите ссылку на нужный рабочий лист.
1. Импортируйте содержимое таблицы данных на рабочий лист.
1. Установите заголовки столбцов рабочего листа в соответствии с именами столбцов таблицы данных.
1. Установите ширину столбцов, если хотите /
1. Отобразите рабочий лист.

В приведенном ниже примере мы создали объект DataTable и заполнили его некоторыми данными, полученными из таблицы базы данных с именем Products. Наконец, мы импортировали данные из этого объекта DataTable на нужный рабочий лист, используя Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}