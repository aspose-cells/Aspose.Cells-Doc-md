---
title: Автоподбор строк и столбцов
type: docs
weight: 20
url: /ru/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel предоставляет хорошую функцию автоматического изменения ширины и высоты ячейки в соответствии с ее содержимым. Эта функция также доступна для пользователей Aspose.Cells с возможностью автоматического изменения размеров ячейки во время выполнения.

{{% /alert %}} 
## **Автоматическая установка**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. В этой статье рассматривается использование[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)класс для автоподбора строк или столбцов.
### **Автоподбор строки — простой**
 Самый простой подход к автоматическому изменению ширины и высоты строки — вызвать метод[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс'[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) метод.[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) принимает индекс строки (строки, размер которой нужно изменить) в качестве параметра.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Автоподбор строки в диапазоне Cells**
 Строка состоит из множества столбцов. Aspose.Cells позволяет разработчикам автоматически подбирать строку на основе содержимого диапазона ячеек в строке, вызывая перегруженную версию[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) метод. Он принимает следующие параметры:

- **Индекс строки**, индекс строки, которая будет автоматически подобрана.
- **Индекс первого столбца**, индекс первого столбца строки.
- **Индекс последнего столбца**, индекс последнего столбца строки.

[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) проверяет содержимое всех столбцов в строке, а затем автоматически подбирает строку.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Столбец автоподбора — простой**
 Самый простой способ автоматически изменить ширину и высоту столбца — вызвать метод[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс'[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) метод.[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)принимает индекс столбца (столбца, размеры которого должны быть изменены) в качестве параметра.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Автоподбор столбца в диапазоне Cells**
 Столбец состоит из множества строк. Можно автоматически подогнать столбец на основе содержимого диапазона ячеек в столбце, вызвав перегруженную версию[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) метод, который принимает следующие параметры:

- **Индекс столбца**, представляет индекс столбца, содержимое которого должно быть автоматически подогнано
- **Индекс первой строки**, представляет индекс первой строки столбца
- **Индекс последней строки**, представляет индекс последней строки столбца

[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) проверяет содержимое всех строк в столбце, а затем автоматически подбирает размер столбца.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Автоподбор строк для объединенных Cells**
С помощью Aspose.Cells можно автоматически подбирать строки даже для ячеек, которые были объединены с помощью[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)класс предоставляет[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)свойство, которое можно использовать для автоподбора строк для объединенных ячеек.[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)принимает[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)перечислимое, которое имеет следующие члены.

- [НИКТО](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): игнорировать объединенные ячейки.
- [ПЕРВАЯ СТРОКА](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Увеличивает только высоту первой строки.
- [ПОСЛЕДНЯЯ ЛИНИЯ](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Увеличивает только высоту последней строки.
- [КАЖДАЯ СТРОКА](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): увеличивает только высоту каждой строки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 Вы также можете использовать перегруженные версии[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) методы, принимающие диапазон строк/столбцов и экземпляр[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) для автоматического подбора выбранных строк/столбцов с желаемым[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)соответственно.

Сигнатуры вышеуказанных методов следующие:

1.  autoFitRows(int startRow, int endRow,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)опции)
1.  autoFitColumns (int firstColumn, int lastColumn,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)опции)
## **Важно знать**
{{% alert color="primary" %}} 

 Если ячейка объединена, то*Автоподбор* методы не будут применяться, как и в Microsoft Excel. Более того, если текст в ячейке переносится,[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) метод также не будет применяться. Еще одна вещь, которую вам нужно знать, это то, что*Автоподбор*методы отнимают много времени. Таким образом, вы должны вызывать эти методы как можно реже, чтобы обеспечить эффективность вашего приложения.

{{% /alert %}}
