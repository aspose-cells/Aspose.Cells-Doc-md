---
title: Оптимизация использования памяти при работе с большими файлами с большими наборами данных
type: docs
weight: 180
url: /ru/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

При создании рабочей книги с большими наборами данных или при чтении большого файла Excel Microsoft общий объем оперативной памяти, который потребуется процессу, всегда вызывает беспокойство. Существуют меры, которые можно адаптировать для решения этой проблемы. Aspose.Cells предоставляет некоторые соответствующие параметры, а API вызывает снижение, сокращение и оптимизацию использования памяти. Кроме того, это может помочь процессу работать более эффективно и быстрее.

 Использовать[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) возможность оптимизировать использование памяти для данных ячеек и снизить общую стоимость памяти. При построении большого набора данных для ячеек может сэкономить определенный объем памяти по сравнению с использованием настройки по умолчанию ([**MemorySetting.Нормальный**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Оптимизация памяти**

### **Чтение больших файлов Excel**

В следующем примере показано, как прочитать большой файл Excel Microsoft в оптимизированном режиме.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Запись больших файлов Excel**

В следующем примере показано, как записать большой набор данных на лист в оптимизированном режиме.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Осторожность**

 Вариант по умолчанию,[**MemorySetting.Нормальный**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)применяется для всех версий. В некоторых ситуациях, например при создании рабочей книги с большим набором данных для ячеек,[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)Параметр может оптимизировать использование памяти и снизить затраты памяти для приложения. Однако этот параметр может снизить производительность в некоторых особых случаях, таких как следующие.

1. **Доступ к Cells в случайном порядке и повторно** : наиболее эффективная последовательность для доступа к коллекции ячеек — ячейка за ячейкой в одной строке, а затем строка за строкой. Особенно, если вы обращаетесь к строкам/ячейкам с помощью Enumerator, полученного из[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) а также[**Строка**](https://reference.aspose.com/cells/net/aspose.cells/row) , производительность будет максимальной при[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Вставка и удаление Cells и строк** : Обратите внимание, что при большом количестве операций вставки/удаления для Cells/Rows снижение производительности будет заметным для*ПамятьPreference* режим по сравнению с*Обычный*режим.
1. **Работа с различными типами Cell** : если большинство ячеек содержат строковые значения или формулы, затраты памяти будут такими же, как*Обычный* режиме, но если есть много пустых ячеек или значения ячеек являются числовыми, логическими и т. д.,[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)вариант даст лучшую производительность.
