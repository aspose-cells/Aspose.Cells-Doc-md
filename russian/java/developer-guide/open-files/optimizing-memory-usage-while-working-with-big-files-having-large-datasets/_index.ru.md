---
title: Оптимизация использования памяти при работе с большими файлами с большими наборами данных
type: docs
weight: 110
url: /ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

При создании рабочей книги с большими наборами данных или при чтении большого файла Excel Microsoft общий объем оперативной памяти, который потребуется процессу, всегда вызывает беспокойство. Существуют меры, которые можно адаптировать для решения этой проблемы. Aspose.Cells предоставляет некоторые соответствующие параметры, а API вызывает снижение, сокращение и оптимизацию использования памяти. Кроме того, это может помочь процессу работать более эффективно и быстрее.

 Использовать[**Настройка памяти.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) возможность оптимизировать память, используемую для данных ячеек, чтобы снизить общую стоимость памяти. При создании большого набора данных для ячеек это может сэкономить определенный объем памяти по сравнению с использованием настройки по умолчанию.[**ПамятьНастройка.НОРМАЛЬНЫЙ**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Оптимизация памяти**

### **Чтение больших файлов Excel**

В следующем примере показано, как прочитать большой файл Excel Microsoft в оптимизированном режиме.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **Запись больших файлов Excel**

В следующем примере показано, как записать большой набор данных на лист в оптимизированном режиме.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **Осторожность**

 Вариант по умолчанию,[**ПамятьНастройка.НОРМАЛЬНЫЙ**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)применяется для всех версий. В некоторых ситуациях, например при создании рабочей книги с большим набором данных для ячеек,[**Настройка памяти.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)Параметр может оптимизировать использование памяти и снизить затраты памяти для приложения. Однако этот параметр может снизить производительность в некоторых особых случаях, таких как следующие.

1. **Доступ к Cells в случайном порядке и повторно** : наиболее эффективная последовательность для доступа к коллекции ячеек — ячейка за ячейкой в одной строке, а затем строка за строкой. Особенно, если вы обращаетесь к строкам/ячейкам с помощью Enumerator, полученного из[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) а также[**Строка**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) , производительность будет максимальной при[**Настройка памяти.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Вставка и удаление Cells и строк** : Обратите внимание, что при большом количестве операций вставки/удаления для Cells/Rows снижение производительности будет заметным для[**Настройка памяти.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) режим по сравнению с[**ПамятьНастройка.НОРМАЛЬНЫЙ**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)режим.
1. **Работа с различными типами Cell** : если большинство ячеек содержат строковые значения или формулы, затраты памяти будут такими же, как[**ПамятьНастройка.НОРМАЛЬНЫЙ**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)режиме, но если есть много пустых ячеек или значения ячеек являются числовыми, логическими и т. д.,[**Настройка памяти.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)вариант даст лучшую производительность.
