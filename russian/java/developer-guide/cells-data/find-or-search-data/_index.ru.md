---
title: Поиск или поиск данных
type: docs
weight: 120
url: /ru/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 В Microsoft Excel пользователи могут искать ячейки, содержащие определенные данные. Например, нажав**Редактировать** а потом**Находить** открывает диалоговое окно поиска. Пользователи вводят значение и нажимают**ХОРОШО** искать его. Excel выделяет совпадающие поля.

**Использование диалогового окна «Найти» для поиска ячеек, содержащих определенное значение** 

![дело:изображение_альтернативный_текст](find-or-search-data_1.png)

В этом примере значением поиска является «Апельсины».

Aspose.Cells позволяет разработчикам искать ячейки на листе, чтобы найти те, которые содержат заданное значение.

{{% /alert %}} 
## **Обнаружение Cells, содержащих определенные данные**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , который представляет файл Excel.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) , коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)учебный класс.

[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) , коллекция, которая представляет все ячейки на листе.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection предоставляет несколько методов поиска ячеек на листе, содержащих указанные пользователем данные. Некоторые из этих методов обсуждаются ниже более подробно.

Все методы поиска возвращают ссылки на ячейки для любых ячеек, содержащих указанное значение поиска.
## **Поиск, содержащий формулу**
 Разработчики могут найти указанную формулу на листе, вызвав метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[найти](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) ), установив[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) к[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)и передать его в качестве параметра[найти](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) метод.

 Как правило,[найти](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) принимает два или более параметра:

- Объект для поиска: представляет объект, который необходимо найти на листе.
- Предыдущий Cell: представляет предыдущую ячейку с той же формулой. Этот параметр может быть установлен равным нулю при поиске с самого начала.
- Параметры поиска: представляет критерии поиска. В приведенных ниже примерах для отработки методов поиска используются следующие данные рабочего листа:

**Пример данных рабочего листа** 

![дело:изображение_альтернативный_текст](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Поиск строк**
Поиск ячеек, содержащих строковое значение, прост и гибок. Существуют различные способы поиска, например поиск ячеек, содержащих строки, начинающиеся с определенного символа или набора символов.
### **Поиск строк, начинающихся с определенных символов**
 Для поиска первого символа в строке вызовите функцию[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[найти](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), установите[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) к[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)и передать его как параметр в[найти](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Поиск строк, заканчивающихся определенными символами**
 Aspose.Cells также может найти строки, которые заканчиваются определенными символами. Чтобы найти последние символы в строке, вызовите функцию[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[найти](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), установите[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) к[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)и передать его как параметр в[найти](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Поиск с помощью регулярных выражений: функция RegEx**
Регулярное выражение предоставляет краткие и гибкие средства сопоставления (определения и распознавания) строк текста, таких как определенные символы, слова или шаблоны.

Например, шаблон регулярного выражения abc-* ~~xyz~~ соответствует строкам "abc-123-xyz", "abc-985-xyz" и "abc-pony-xyz".* является подстановочным знаком, поэтому шаблон соответствует любым строкам, начинающимся с «abc» и заканчивающимся на «-xyz», независимо от того, какие символы находятся в середине.

Aspose.Cells позволяет выполнять поиск с использованием регулярных выражений.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Предварительные темы**
- [Найти ячейки с определенным стилем](/cells/ru/java/find-cells-with-specific-style/)
- [Поиск данных с использованием исходных значений](/cells/ru/java/search-data-using-original-values/)
