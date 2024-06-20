---
title: Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени
type: docs
weight: 100
url: /ru/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет вам прекратить преобразование рабочей книги в различные форматы, такие как PDF, HTML и т. д., используя объект [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor), когда это занимает слишком много времени. Процесс преобразования часто требует много ресурсов ЦП и памяти, и часто бывает полезно останавливать его, если ресурсы ограничены. Вы можете использовать [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) как для остановки преобразования, так и для остановки загрузки большой рабочей книги. Пожалуйста, используйте свойство [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor) для остановки преобразования и свойство [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor) для загрузки большой рабочей книги.

## **Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени**

Приведенный ниже образец кода объясняет использование объекта [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor). Код преобразует довольно большой файл Excel в PDF. Это займет несколько секунд (т. е. *более 30 секунд*), чтобы его преобразовать из-за этих строк кода.

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Как видите, **AB1000000** - довольно удаленная ячейка в файле XLSX. Тем не менее метод *WaitForWhileAndThenInterrupt()* прерывает преобразование после 10 секунд, и программа завершается/прерывается. Пожалуйста, используйте следующий код для выполнения образца кода.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
