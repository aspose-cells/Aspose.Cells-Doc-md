---
title: Обнаружение пустых рабочих листов
type: docs
weight: 710
url: /ru/java/detecting-empty-worksheets/
---

## **Проверка заполненных ячеек**
На рабочих листах может быть заполнено одна или несколько ячеек значениями, где значение может быть простым (текст, числовое, дата/время) или формулой или значением на основе формулы. В таком случае легко определить, пуст ли данный рабочий лист или нет. Все, что нужно проверить, это свойства [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) или [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn). Если вышеупомянутые свойства возвращают ноль или положительные значения, то это означает, что одна или несколько ячеек были заполнены, однако, если какое-либо из этих свойств возвращает -1, это означает, что ни одна из ячеек не была заполнена на данном рабочем листе.

{{% alert color="primary" %}} 

Коллекции строк и столбцов имеют нулевой индекс, поэтому ячейка в строке 0 и столбце 0 означает первую ячейку на листе - A1.

{{% /alert %}} 
## **Проверка пустых инициализированных ячеек**
Все ячейки, которые имеют значения, автоматически инициализируются, однако есть возможность, что на листе есть ячейки, на которые применено только форматирование. В таком сценарии свойства [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) или [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) вернут -1, указывая на отсутствие заполненных значений, но инициализированные ячейки из-за форматирования не могут быть обнаружены с помощью этого подхода. Чтобы проверить, есть ли на листе пустые инициализированные ячейки, рекомендуется использовать метод *Iterator.hasNext* на итераторе, полученном из коллекции Cells. Если метод *iterator.hasNext* возвращает true, то это означает, что на данном листе есть одна или несколько инициализированных ячеек.

{{% alert color="primary" %}} 

Существует несколько способов получения перечислителя ячеек, подробно описанных в [Как и где использовать итераторы](/cells/ru/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Проверка фигур**
Возможно, что на определенном листе нет заполненных ячеек, однако он может содержать фигуры и объекты, такие как элементы управления, диаграммы, изображения и т. д. Если нам нужно проверить, содержит ли лист какую-либо форму, мы можем сделать это, проверив свойство [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count). Любое положительное значение указывает на наличие фигуры(фигур) на листе.
## **Пример программирования**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
