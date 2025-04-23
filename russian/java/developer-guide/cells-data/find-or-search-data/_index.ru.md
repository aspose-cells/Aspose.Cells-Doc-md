---
title: Нахождение или Поиск Данных
type: docs
weight: 120
url: /ru/java/find-or-search-data/
---

{{% alert color="primary" %}} 

В Microsoft Excel пользователи могут искать ячейки, содержащие определенные данные. Например, щелчок на **Редактирование** и затем на **Поиск** открывает диалоговое окно поиска. Пользователи вводят значение и нажимают **OK**, чтобы найти его. Excel выделяет соответствующие поля.

**Использование диалогового окна Поиска для поиска ячеек с определенным значением** 

![todo:image_alt_text](find-or-search-data_1.png)

В этом примере для поиска используется значение "Апельсины".

Aspose.Cells позволяет разработчикам искать ячейки в листе электронной таблицы, содержащие заданное значение.

{{% /alert %}} 
## **Поиск ячеек, содержащих определенные данные**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет собой файл Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), коллекцию, позволяющую получить доступ к каждому из листов в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), коллекцию, представляющую все ячейки на листе. Коллекция [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) предоставляет несколько методов для поиска ячеек на листе, содержащих указанные пользовательские данные. Несколько из этих методов подробно рассматриваются ниже.

Все методы поиска возвращают ссылки на ячейки, содержащие указанное значение поиска.
## **Поиск, содержащий формулу**
Разработчики могут найти заданную формулу в листе, вызвав метод [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекции [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/Cell-) с установкой [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) в [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) и передачей её в качестве параметра в метод [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/Cell-).

Обычно метод [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/Cell-) принимает два или более параметров:

- Объект для поиска: представляет объект, который необходимо найти на листе.
- Предыдущая ячейка: представляет предыдущую ячейку с той же формулой. Этот параметр можно установить на null при поиске с начала.
- Опции поиска: представляют критерии поиска. В приведенных ниже примерах используются следующие данные листа для практики методов поиска:

**Пример данных листа** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Поиск строк**
Поиск ячеек, содержащих строковое значение, прост и гибок. Есть разные способы поиска, например, поиск ячеек, содержащих строки, начинающиеся с определенного символа, или набора символов.
### **Поиск строк, начинающихся с определенных символов**
Чтобы искать первый символ в строке, вызовите метод [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекции [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/Cell-), установите [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) в [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START-WITH) и передайте его в качестве параметра в метод [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/Cell-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Поиск строк, заканчивающихся определенными символами**
Aspose.Cells также может найти строки, которые заканчиваются на определенные символы. Чтобы искать последние символы в строке, вызовите метод [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекции [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/Cell-), установите [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) в [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END-WITH) и передайте его в качестве параметра в метод [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/Cell-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Поиск с использованием регулярных выражений: функция RegEx**
Регулярное выражение предоставляет краткий и гибкий способ сопоставления (указания и распознавания) строк текста, таких как определенные символы, слова или шаблоны.

Например, шаблон регулярного выражения abc-*~~xyz~~ сопоставляет строки "abc-123-xyz", "abc-985-xyz" и "abc-pony-xyz". * - это символ подстановки, поэтому шаблон соответствует любым строкам, начинающимся с "abc" и заканчивающимся на "-xyz", независимо от того, какие символы находятся посередине.

Aspose.Cells позволяет выполнять поиск с использованием регулярных выражений.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Продвинутые темы**
- [Находить ячейки с определенным стилем](/cells/ru/java/find-cells-with-specific-style/)
- [Поиск данных с использованием исходных значений](/cells/ru/java/search-data-using-original-values/)
{{< app/cells/assistant language="java" >}}
