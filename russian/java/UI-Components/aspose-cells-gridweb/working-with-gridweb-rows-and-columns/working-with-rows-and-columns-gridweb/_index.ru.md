---
title: Работа со строками и столбцами GridWeb
type: docs
weight: 20
url: /ru/java/working-with-rows-and-columns-gridweb/
---
##  **Вставка строк и столбцов**
В этом разделе объясняется, как вставлять новые строки и столбцы в лист с помощью Aspose.Cells.GridWeb API. Строки или столбцы можно вставлять в любое место листа.
###  **Вставка строк**
Чтобы вставить строку в любую позицию листа:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или страницу.
1. Откройте лист, в который вы добавляете строки.
1. Вставьте строку, указав индекс строки, в которую будет вставлена строка.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
###  **Вставка столбцов**
Чтобы вставить столбец в любую позицию листа:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или страницу.
1. Откройте лист, в который вы добавляете столбцы.
1. Вставьте столбец, указав индекс столбца, в который будет вставлен столбец.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Вы также можете использовать методы InsertRows()/insertColumns() для вставки нескольких строк/столбцов в листы соответственно.

{{% /alert %}} 
##  **Удаление строк и столбцов**
В этом разделе показано, как удалять строки и столбцы из листа с помощью Aspose.Cells.GridWeb API. С помощью этой функции разработчики могут удалять строки или столбцы во время выполнения.
###  **Удаление строк**
Чтобы удалить строку с листа:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или страницу.
1. Откройте лист, из которого вы хотите удалить строки.
1. Удалите строку с листа, указав ее индекс строки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
###  **Удаление столбцов**
Чтобы удалить столбец с листа:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или страницу.
1. Откройте лист, из которого вы хотите удалить столбцы.
1. Удалите столбец с листа, указав его индекс столбца.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
##  **Настройка высоты строки и ширины столбца**
Иногда значения ячеек шире ячейки, в которой они находятся, или располагаются на нескольких строках. Такие значения не полностью видны пользователям, если они не изменят высоту и ширину строк и столбцов. Aspose.Cells.GridWeb полностью поддерживает настройку высоты строк и ширины столбца. В этом разделе эти функции подробно обсуждаются с помощью примеров.
###  **Работа с высотой строк и шириной столбца**
####  **Установка высоты строки**
Чтобы установить высоту строки:

1. Добавьте элемент управления Aspose.Cells.GridWeb на свою веб-форму/страницу.
1. Получите доступ к коллекции GridCells листа.
1. Установите высоту всех ячеек в любой указанной строке.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb принимает измерения высоты строки и ширины столбца в пунктах, дюймах, пикселях и т. д.

{{% /alert %}} 

**Вывод: высота 1-й строки установлена на 50 пунктов.** 

![задача: image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
####  **Настройка ширины столбца**
Чтобы установить ширину столбца:

1. Добавьте элемент управления Aspose.Cells.GridWeb на свою веб-форму/страницу.
1. Получите доступ к коллекции GridCells листа.
1. Установите ширину всех ячеек в любом указанном столбце.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
##  **Настройка заголовков строк и столбцов**
Как и Microsoft Excel, Aspose.Cells.GridWeb также использует стандартные заголовки или подписи для строк (цифры, например 1, 2, 3 и т. д.) и столбцов (в алфавитном порядке, например A, B, C и т. д.). Aspose.Cells.GridWeb также позволяет настраивать подписи. В этом разделе обсуждается настройка заголовков строк и столбцов во время выполнения с использованием Aspose.Cells.GridWeb API.
###  **Настройка заголовка строки**
Чтобы настроить заголовок или заголовок строки:

1. Добавьте элемент управления Aspose.Cells.GridWeb на веб-форму/страницу.
1. Получите доступ к листу в GridWorksheetCollection.
1. Установите заголовок любой указанной строки.

**Заголовки строк 1 и 2 были настроены.** 

![задача: image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
###  **Настройка заголовка столбца**
Чтобы настроить заголовок или заголовок столбца:

1. Добавьте элемент управления Aspose.Cells.GridWeb на веб-форму/страницу.
1. Получите доступ к листу в GridWorksheetCollection.
1. Установите заголовок любого указанного столбца.

**Заголовки столбцов 1 и 2 были настроены.** 

![задача: image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
##  **Закрепить и разморозить строки и столбцы**
В этом разделе объясняется, как закрепить и разморозить строки и столбцы. Закрепление столбцов или строк позволяет пользователям сохранять заголовки столбцов или заголовки строк видимыми при прокрутке к другим частям листа. Эта функция очень полезна при работе с листами, содержащими большие объемы данных. Когда пользователи прокручивают вниз, прокручиваются только данные, а заголовки остаются на месте, что облегчает чтение даты. Функция закрепления панелей поддерживается только в Internet Explorer 6.0 или более поздней версии.
###  **Закрепление строк и столбцов**
Чтобы заморозить определенное количество строк и столбцов:

1. Добавьте элемент управления Aspose.Cells.GridWeb на веб-форму/страницу.
1. Доступ к рабочему листу.
1. Заморозьте несколько строк и столбцов.

{{% alert color="primary" %}} 

 Также можно заморозить определенное количество строк и столбцов с помощью интерфейса. Щелкните правой кнопкой мыши ячейку, в которой вы хотите закрепить строки и столбцы, и выберите**Заморозить** из списка.

{{% /alert %}} 

**Строки и столбцы в замороженном состоянии** 

![задача: image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
###  **Разморозка строк и столбцов**
Чтобы разморозить строки и столбцы:

1. Добавьте элемент управления Aspose.Cells.GridWeb на веб-форму/страницу.
1. Доступ к рабочему листу.
1. Разморозить строки и столбцы.

**Рабочий лист после размораживания** 

![задача: image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
##  **Защита строк и столбцов**
В этом разделе обсуждается несколько методов защиты ячеек в строках и столбцах от любых действий, выполняемых конечными пользователями. Разработчики могут реализовать эту защиту, используя два метода: сделав ячейки в строках и столбцах доступными только для чтения или ограничив параметры контекстного меню GridWeb.
###  **Ограничение параметров контекстного меню**
GridWeb предоставляет контекстное меню, которое конечные пользователи могут использовать для выполнения операций с элементом управления. Меню предоставляет множество опций для управления ячейками, строками и столбцами.

**Полные контекстные параметры** 

![задача: image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Можно ограничить любые операции на стороне клиента со строками и столбцами, ограничив параметры, доступные в контекстном меню. Это можно сделать, установив для атрибутов EnableClientColumnOperations и EnableClientRowOperations элемента управления GridWeb значение false. Также можно запретить пользователям замораживать строки и столбцы, установив для атрибута EnableClientFreeze элемента управления GridWeb значение false.

**Контекстное меню после ограничения параметров строк и столбцов** 

![задача: image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
