---
title: Остановите преобразование или загрузку с помощью InterruptMonitor, если это занимает слишком много времени
type: docs
weight: 100
url: /ru/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Возможные сценарии использования**

Aspose.Cells позволяет остановить преобразование рабочей книги в различные форматы, такие как PDF, HTML и т. д., с помощью[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)объект, когда это занимает слишком много времени. Процесс преобразования часто интенсивно использует как ЦП, так и память, и часто бывает полезно остановить его, когда ресурсы ограничены. Ты можешь использовать[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)как для остановки преобразования, так и для остановки загрузки огромной книги. Пожалуйста, используйте[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)свойство для остановки преобразования и[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)свойство для загрузки огромной книги.

## **Остановите преобразование или загрузку с помощью InterruptMonitor, если это занимает слишком много времени**

В следующем примере кода объясняется использование[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)объект. Код преобразует довольно большой файл Excel в PDF. Это займет несколько секунд (т.е.*более 30 секунд*), чтобы преобразовать его из-за этих строк кода.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Как вы видите**АВ1000000**это довольно дальняя ячейка в файле XLSX. Однако*Ждать для пока и потом прерывать ()*метод прерывает преобразование через 10 секунд, и программа завершается/завершается. Пожалуйста, используйте следующий код для выполнения примера кода.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
