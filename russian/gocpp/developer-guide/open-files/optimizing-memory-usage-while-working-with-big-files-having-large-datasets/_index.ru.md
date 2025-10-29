---
title: Оптимизация использования памяти при работе с большими файлами с массивом данных с помощью Golang через C++
linktitle: Оптимизация использования памяти
type: docs
weight: 180
url: /ru/go-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Научитесь оптимизировать использование памяти при работе с большими файлами Excel с Aspose.Cells на Golang через C++.
---

{{% alert color="primary" %}}

При создании книги с большими наборами данных или чтении большого файла Microsoft Excel всегда возникает вопрос - какой объем ОЗУ займет данный процесс. Предлагаются меры, которые можно принять для справки с этим вызовом. Aspose.Cells предоставляет некоторые соответствующие параметры и вызовы API для снижения, уменьшения и оптимизации использования памяти. Кроме того, это может помочь процессу работать более эффективно и быстро.

Используйте опцию [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) для оптимизации использования памяти для данных ячеек и уменьшения общей затраты памяти. При создании большого набора данных для ячеек можно сохранить определенное количество памяти по сравнению с использованием настройки по умолчанию ([**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/)).

{{% /alert %}}

## **Оптимизация памяти**

### **Чтение больших файлов Excel**

Следующий пример показывает, как считать большой файл Microsoft Excel в оптимизированном режиме.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets.go" >}}
### **Запись больших файлов Excel**

Следующий пример показывает, как записать большой набор данных на листе в оптимизированном режиме.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets-1.go" >}}
## **Предостережение**

Настройка по умолчанию, [**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/), применяется ко всем версиям. В некоторых ситуациях, таких как создание книги с большим набором данных для ячеек, опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) может оптимизировать использование памяти и уменьшить затраты памяти для приложения. Однако, эта опция может ухудшить производительность в некоторых специальных случаях, таких как следующие.

1. **Доступ к ячейкам в произвольном порядке и повторно**: Самая эффективная последовательность доступа к коллекции ячеек - путем перебора ячеек по одной строке, а затем строка за строкой. Особенно, если вы получаете доступ к строкам/ячейкам с помощью перечислителя, полученного из [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) и [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), производительность будет максимальной с [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Вставка и удаление ячеек и строк**: Обратите внимание, что если есть много операций вставки/удаления для Ячеек/Строк, деградация производительности будет значительной в режиме *MemoryPreference* по сравнению с режимом *Normal*.
1. **Работа с различными типами ячеек**: Если большинство ячеек содержат строковые значения или формулы, затраты памяти будут такими же, как в режиме *Normal*, но если есть много пустых ячеек, или значения ячейки являются числовыми, логическими и т. д., то [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) позволит добиться лучшей производительности.
