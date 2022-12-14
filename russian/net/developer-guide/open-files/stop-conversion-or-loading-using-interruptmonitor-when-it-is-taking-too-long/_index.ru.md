---
title: Остановите преобразование или загрузку с помощью InterruptMonitor, если это занимает слишком много времени
type: docs
weight: 100
url: /ru/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Возможные сценарии использования**

Aspose.Cells позволяет остановить преобразование рабочей книги в различные форматы, такие как PDF, HTML и т. д., с помощью[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) объект, когда это занимает слишком много времени. Процесс преобразования часто интенсивно использует как ЦП, так и память, и часто бывает полезно остановить его, когда ресурсы ограничены. Вы можете использовать[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) как для остановки преобразования, так и для остановки загрузки огромной книги. Пожалуйста, используйте[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) свойство для остановки преобразования и[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) свойство для загрузки огромной книги.

## **Остановите преобразование или загрузку с помощью InterruptMonitor, если это занимает слишком много времени**

В следующем примере кода объясняется использование[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) объект. Код преобразует довольно большой файл Excel в PDF. Это займет несколько секунд (т.е.*более 30 секунд*), чтобы преобразовать его из-за этих строк кода.

{{< highlight "csharp" >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

 Как видишь**J1000000** довольно дальняя ячейка в файле XLSX. Тем не менее**Ждать для пока и потом прерывать ()**метод прерывает преобразование через 10 секунд, и программа завершается/завершается. Пожалуйста, используйте следующий код для выполнения примера кода.

{{< highlight "csharp" >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
