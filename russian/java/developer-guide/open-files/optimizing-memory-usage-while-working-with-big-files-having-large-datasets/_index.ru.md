---
title: Оптимизация использования памяти при работе с большими файлами с большими наборами данных
type: docs
weight: 110
url: /ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

При создании книги с большими наборами данных или чтении большого файла Microsoft Excel общий объем оперативной памяти, которую займет процесс, всегда вызывает беспокойство. Существуют меры, которые можно адаптировать для справления с этим вызовом. Aspose.Cells предоставляет некоторые соответствующие варианты и вызовы API для снижения, уменьшения и оптимизации использования памяти. Кроме того, это может помочь процессу работать более эффективно и быстрее.

Используйте опцию [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE), чтобы оптимизировать использование памяти для данных ячеек и уменьшить общую стоимость памяти. При создании большого набора данных для ячеек это может сэкономить определенное количество памяти по сравнению с использованием параметров по умолчанию [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Оптимизация памяти**

### **Чтение больших файлов Excel**

Следующий пример показывает, как считать большой файл Microsoft Excel в оптимизированном режиме.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **Запись больших файлов Excel**

Приведенный ниже пример показывает, как записать большой набор данных на листе в оптимизированном режиме.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **Предостережение**

По умолчанию, опция [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) применяется ко всем версиям. В некоторых случаях, таких как создание книги с большим набором данных для ячеек, параметр [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) может оптимизировать использование памяти и снизить стоимость памяти для приложения. Однако в некоторых специальных случаях это может снизить производительность, таких как следующие.

1. **Доступ к ячейкам в произвольном порядке и повторно**: Самая эффективная последовательность доступа к коллекции ячеек - путем перебора ячеек по одной строке, а затем строка за строкой. Особенно, если вы получаете доступ к строкам/ячейкам с помощью перечислителя, полученного из [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) и [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row), производительность будет максимальной с [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE).
1. **Вставка и удаление ячеек и строк**: Обратите внимание, что если выполняется много операций вставки/удаления для ячеек/строк, производительность в режиме [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) будет значительно снижена по сравнению с режимом [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).
1. **Работа с различными типами ячеек**: Если большинство ячеек содержат строковые значения или формулы, стоимость памяти будет такой же, как в режиме [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL), но если есть много пустых ячеек, или значения ячеек являются числовыми, логическими и т.д., опция [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) обеспечит лучшую производительность.
{{< app/cells/assistant language="java" >}}
