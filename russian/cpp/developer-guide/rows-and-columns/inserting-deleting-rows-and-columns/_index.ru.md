---
title: Вставка, удаление строк и столбцов
type: docs
weight: 40
url: /ru/cpp/inserting-deleting-rows-and-columns/
---
## **Введение**
Независимо от того, создаете ли вы новый рабочий лист с нуля или работаете с существующим рабочим листом, нам может потребоваться добавить дополнительные строки или столбцы для размещения большего количества данных. И наоборот, нам также может понадобиться удалить строки или столбцы из указанных позиций на листе. Чтобы выполнить эти требования, Aspose.Cells предоставляет очень простой набор классов и методов, обсуждаемых ниже.
### **Управление строками и столбцами**
 Aspose.Cells предоставляет класс,[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) , представляющий файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс предоставляет[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция, представляющая все ячейки рабочего листа.

[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection предоставляет несколько методов управления строками и столбцами на листе. Некоторые из них обсуждаются ниже.

{{% alert color="primary" %}} 

При добавлении строк или столбцов содержимое рабочего листа сдвигается вниз или вправо, а при удалении строк или столбцов содержимое сдвигается вверх или влево.

{{% /alert %}} 
#### **Вставить строку**
 Вставьте строку в рабочий лист в любом месте, вызвав метод[Вставить строку](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция.[Вставить строку](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)Метод принимает индекс строки, в которую будет вставлена новая строка.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **Вставка нескольких строк**
 Чтобы вставить несколько строк на лист, вызовите метод[Инсерровс](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция.[Инсерровс](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)метод принимает два параметра:

- Индекс строки, индекс строки, из которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **Удаление нескольких строк**
Чтобы удалить несколько строк с рабочего листа, вызовите метод[УдалитьРовс](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция.[УдалитьРовс](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)метод принимает два параметра:

- Индекс строки, индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **Вставить столбец**
 Разработчики также могут вставить столбец в рабочий лист в любом месте, вызвав метод[ВставитьКолонку](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция.[ВставитьКолонку](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)Метод принимает индекс столбца, в который будет вставлен новый столбец.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **Удалить столбец**
 Чтобы удалить столбец из рабочего листа в любом месте, вызовите[УдалитьКолонку](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) метод[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция.[УдалитьКолонку](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)Метод принимает индекс удаляемого столбца.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
