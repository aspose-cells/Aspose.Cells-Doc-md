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
Наиболее простой подход к автоматическому изменению ширины и высоты строки - вызов метода [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Метод [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) принимает индекс строки (строки, которую необходимо изменить) в качестве параметра.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Автоподбор высоты строки в диапазоне ячеек**
Строка состоит из множества столбцов. Aspose.Cells позволяет разработчикам автоматически подогнать строку под содержимое диапазона ячеек внутри строки, вызвав перегруженную версию метода [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)). Он принимает следующие параметры:

- Индекс строки, индекс строки, которую нужно автоматически подогнать.
- Индекс первого столбца, индекс первого столбца строки.
- Индекс последнего столбца, индекс последнего столбца строки.

Метод [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) проверяет содержимое всех столбцов строки и автоматически подгоняет размер строки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Автоподгонка столбца - Простая**
Самый простой способ автоматически установить ширину и высоту столбца - вызвать метод [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Метод [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) принимает индекс столбца (столбец, который будет изменен в размере) в качестве параметра.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Автоподгонка столбца в диапазоне ячеек**
Столбец состоит из множества строк. Можно подогнать столбец по содержимому диапазона ячеек в столбце, вызвав перегруженную версию метода [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)), который принимает следующие параметры:

- **Индекс столбца**, представляет индекс столбца, содержимое которого должно быть автоматически подогнано
- **Индекс первой строки**, представляет индекс первой строки столбца
- **Индекс последней строки**, представляет индекс последней строки столбца

Метод [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) проверяет содержимое всех строк в столбце и автоматически подгоняет размер столбца.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **AutoFit строк для объединенных ячеек**
С помощью Aspose.Cells можно автоматически подогнать строки даже для объединенных ячеек, используя API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). Класс [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) предоставляет свойство [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType), которое можно использовать для автоматической подгонки строк для объединенных ячеек. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) принимает перечисление [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) со следующими элементами:

- [НИКАКОЙ](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Игнорирует объединенные ячейки.
- [ПЕРВАЯ_СТРОКА](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Расширяет только высоту первой строки.
- [ПОСЛЕДНЯЯ_СТРОКА](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Расширяет только высоту последней строки.
- [КАЖДАЯ_СТРОКА](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Расширяет только высоту каждой строки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Также можно использовать перегруженные версии методов [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) и [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)), принимающих диапазон строк/столбцов и экземпляр [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) для автоматической подгонки выбранных строк/столбцов с желаемыми [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) в соответствии.

Сигнатуры вышеперечисленных методов следующие:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Важно знать**
{{% alert color="primary" %}} 

Если ячейка объединена, то метод *AutoFit* не будет применен, что соответствует поведению в Microsoft Excel. Более того, если текст в ячейке перенесен, то метод [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) также не будет применен. Еще одна важная вещь, которую вам следует знать, заключается в том, что методы *AutoFit* занимают много времени. Поэтому вы должны вызывать эти методы как можно реже, чтобы обеспечить эффективность вашего приложения.

{{% /alert %}}
