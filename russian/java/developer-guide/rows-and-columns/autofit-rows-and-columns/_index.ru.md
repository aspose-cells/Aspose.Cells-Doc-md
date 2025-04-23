---
title: Автоподбор высоты и ширины строк и столбцов
type: docs
weight: 20
url: /ru/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel предоставляет хорошую возможность автоматического изменения ширины и высоты ячейки в соответствии с её содержимым. Эта возможность также доступна пользователям Aspose.Cells с возможностью автоматического изменения размеров ячейки во время выполнения.

{{% /alert %}} 
## **Автоматическая подгонка размера**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), позволяющую получать доступ к каждому листу в файле Excel.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет множество свойств и методов для управления листом. В этой статье рассматривается использование класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) для автоподбора высоты строк или ширины столбцов.
### **Автоматическая подгонка строки - простой**
Самый простой способ автоматически подогнать ширину и высоту строки — вызвать метод [Worksheet.autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-). Он принимает индекс строки, которую нужно изменить.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Автоподбор высоты строки в диапазоне ячеек**
Строка состоит из множества столбцов. Aspose.Cells позволяет автоматического подогнать строку по содержимому диапазона ячеек внутри строки, вызвав перегруженную версию метода [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-). Этот метод принимает параметры:

- Индекс строки, индекс строки, которую нужно автоматически подогнать.
- Индекс первого столбца, индекс первого столбца строки.
- Индекс последнего столбца, индекс последнего столбца строки.

Метод [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) проверяет содержимое всех столбцов строки и автоматически настраивает высоту строки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Автоподгонка столбца - Простая**
Самый простой способ автоматически подогнать ширину и высоту столбца — вызвать метод [Worksheet.autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-). Он принимает индекс столбца, который нужно изменить.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Автоподгонка столбца в диапазоне ячеек**
Столбец состоит из множества строк. Можно автоматически подогнать ширину столбца на основе содержимого диапазона ячеек этого столбца, вызвав перегруженную версию метода [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-), которая принимает параметры:

- **Индекс столбца**, представляет индекс столбца, содержимое которого должно быть автоматически подогнано
- **Индекс первой строки**, представляет индекс первой строки столбца
- **Индекс последней строки**, представляет индекс последней строки столбца

Метод [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) проверяет содержимое всех строк в столбце и автоматически подгоняет ширину.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **AutoFit строк для объединенных ячеек**
С помощью Aspose.Cells можно автоматически подогнать строки даже для объединенных ячеек, используя API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). Класс [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) предоставляет свойство [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType), которое можно использовать для автоматической подгонки строк для объединенных ячеек. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) принимает перечисление [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) со следующими элементами:

- [НИКАКОЙ](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Игнорирует объединенные ячейки.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE): расширяет высоту только первой строки.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE): расширяет высоту только последней строки.
- [КАЖДАЯ_СТРОКА](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE): Только увеличивает высоту каждой строки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Вы также можете использовать перегруженные версии методов [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) и [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--), которые принимают диапазон строк/столбцов и экземпляр [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) для автоматической настройки выбранных строк/столбцов с нужными [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions).

Сигнатуры вышеперечисленных методов следующие:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Важно знать**
{{% alert color="primary" %}} 

Если ячейка объединена, то методы *AutoFit* не применяются, что соответствует поведению в Microsoft Excel. Более того, если текст в ячейке обернут, метод [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) также не будет применен. Еще одно важное замечание — методы *AutoFit* занимают много времени, поэтому их следует вызывать как можно реже для повышения эффективности вашего приложения.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
