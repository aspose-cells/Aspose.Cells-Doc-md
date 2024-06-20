---
title: Импорт данных из DataTable в сетку
type: docs
weight: 50
url: /ru/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop,импорт,данные,datatable
description: Эта статья представляет способы импорта данных в GridDesktop.
---

{{% alert color="primary" %}} 

С момента выпуска .NET Framework, Microsoft предоставила отличный способ сохранения данных в автономном режиме в виде объекта DataTable. Понимая потребности разработчиков, Aspose.Cells.GridDesktop также поддерживает импорт данных из таблицы данных. В этой теме обсуждается, как это сделать.

{{% /alert %}} 
## **Пример**
Для импорта содержимого таблицы данных с использованием элемента управления Aspose.Cells.GridDesktop:

1. Добавить элемент управления Aspose.Cells.GridDesktop на форму.
1. Создать объект DataTable, содержащий данные для импорта.
1. Получите ссылку на нужный лист.
1. Импортировать содержимое таблицы данных на лист.
1. Установить заголовки столбцов на листе в соответствии с именами столбцов таблицы данных.
1. Установить ширину столбцов, при необходимости.
1. Отобразить лист.

В приведенном ниже примере мы создали объект DataTable и заполнили его данными, полученными из таблицы базы данных с названием Products. Наконец, мы импортировали данные из этого объекта DataTable на нужный лист, используя Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
