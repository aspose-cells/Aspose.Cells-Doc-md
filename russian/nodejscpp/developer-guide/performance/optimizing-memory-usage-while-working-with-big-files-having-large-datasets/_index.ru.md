---
title: Оптимизация использования памяти при работе с большими файлами с большими наборами данных
type: docs
weight: 110
url: /ru/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

При создании книги с большими наборами данных или чтении большого файла Microsoft Excel общий объем оперативной памяти, которую займет процесс, всегда вызывает беспокойство. Существуют меры, которые можно адаптировать для справления с этим вызовом. Aspose.Cells предоставляет некоторые соответствующие варианты и вызовы API для снижения, уменьшения и оптимизации использования памяти. Кроме того, это может помочь процессу работать более эффективно и быстрее.

Используйте опцию [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), чтобы оптимизировать использование памяти для данных ячеек и уменьшить общую стоимость памяти. При создании большого набора данных для ячеек это может сэкономить определенное количество памяти по сравнению с использованием параметров по умолчанию [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).

{{% /alert %}}

## **Оптимизация памяти**

Следующий пример показывает, как оптимизировать использование памяти при работе с большими данными в Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "OptimizingMemory.js" >}}

## **Предостережение**

По умолчанию, опция [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) применяется ко всем версиям. В некоторых случаях, таких как создание книги с большим набором данных для ячеек, параметр [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) может оптимизировать использование памяти и снизить стоимость памяти для приложения. Однако в некоторых специальных случаях это может снизить производительность, таких как следующие.

1. **Доступ к ячейкам в произвольном порядке и повторно**: Самая эффективная последовательность доступа к коллекции ячеек - путем перебора ячеек по одной строке, а затем строка за строкой. Особенно, если вы получаете доступ к строкам/ячейкам с помощью перечислителя, полученного из [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) и [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), производительность будет максимальной с [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).
1. **Вставка и удаление ячеек и строк**: Обратите внимание, что если выполняется много операций вставки/удаления для ячеек/строк, производительность в режиме [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) будет значительно снижена по сравнению с режимом [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).
1. **Работа с различными типами ячеек**: Если большинство ячеек содержат строковые значения или формулы, стоимость памяти будет такой же, как в режиме [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), но если есть много пустых ячеек, или значения ячеек являются числовыми, логическими и т.д., опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) обеспечит лучшую производительность.

