---
title: Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени
type: docs
weight: 100
url: /ru/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет остановить преобразование рабочей книги в различные форматы, такие как PDF, HTML и т. д., используя объект [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor), когда оно занимает слишком много времени. Процесс преобразования часто интенсивно использует ресурсы ЦП и памяти, поэтому полезно останавливать его, когда ресурсы ограничены. Вы можете использовать [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) как для остановки преобразования, так и для остановки загрузки большой рабочей книги. Пожалуйста, используйте свойство [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) для остановки преобразования и свойство [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) для загрузки большой рабочей книги.

## **Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени**

В следующем образце кода объясняется использование объекта [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor). Код преобразует довольно большой файл Excel в PDF. Это займет несколько секунд (т.е. *более 30 секунд*) для преобразования из-за этих строк кода.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

Как видите, **J1000000** находится довольно далеко от ячейки в файле XLSX. Однако метод **WaitForWhileAndThenInterrupt()** прерывает преобразование после 10 секунд, и программа завершается. Пожалуйста, используйте следующий код для выполнения образца кода.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
