---
title: Вставка и удаление строк и столбцов файла Excel
linktitle: Вставка и удаление строк и столбцов
type: docs
weight: 70
url: /ru/net/inserting-and-deleting-rows-and-columns/
---
## **Введение**

Независимо от того, создаете ли вы новый рабочий лист с нуля или работаете с существующим рабочим листом, нам может потребоваться добавить дополнительные строки или столбцы для размещения большего количества данных. И наоборот, нам также может понадобиться удалить строки или столбцы из указанных позиций на листе.
Чтобы выполнить эти требования, Aspose.Cells предоставляет очень простой набор классов и методов, обсуждаемых ниже.

### **Управление строками и столбцами**

Aspose.Cells предоставляет класс[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция, представляющая все ячейки рабочего листа.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection предоставляет несколько методов управления строками и столбцами на листе. Некоторые из них обсуждаются ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое рабочего листа сдвигается вниз или вправо, а при удалении строк или столбцов содержимое сдвигается вверх или влево.

{{% /alert %}}


## **Вставка строк и столбцов**

### **Вставить строку**

 Вставьте строку в рабочий лист в любом месте, вызвав метод[**Вставить строку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Вставить строку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)Метод принимает индекс строки, в которую будет вставлена новая строка.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Вставить несколько строк**

 Чтобы вставить несколько строк на лист, вызовите метод[**Инсерровс**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Инсерровс**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)метод принимает два параметра:

- Индекс строки, индекс строки, из которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Вставить строку с форматированием**

Чтобы вставить строку с параметрами форматирования, используйте кнопку[**Инсерровс**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)перегрузка, которая требует[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) как параметр. Установить[**КопироватьФорматТип**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) свойство[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) класс с[**КопироватьФорматТип**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Перечисление.[**КопироватьФорматТип**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Перечисление состоит из трех членов, перечисленных ниже.

- SameAsAbove: форматирует строку так же, как строку выше.
- SameAsBelow: форматирует строку так же, как строку ниже.
- Очистить: очищает форматирование.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Вставить столбец**

 Разработчики также могут вставить столбец в рабочий лист в любом месте, вызвав метод[**ВставитьКолонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.[**ВставитьКолонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)Метод принимает индекс столбца, в который будет вставлен новый столбец.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Удалить строки и столбцы**

### **Удалить несколько строк**

Чтобы удалить несколько строк с рабочего листа, вызовите метод[**УдалитьРовс**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**УдалитьРовс**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)метод принимает два параметра:

- Индекс строки, индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Удалить столбец**

 Чтобы удалить столбец из рабочего листа в любом месте, вызовите[**УдалитьКолонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**УдалитьКолонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)Метод принимает индекс удаляемого столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
