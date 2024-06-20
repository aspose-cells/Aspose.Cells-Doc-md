---
title: Создание Промежуточных Итогов
type: docs
weight: 50
url: /ru/java/creating-subtotals/
---

{{% alert color="primary" %}}

Вы можете автоматически создавать промежуточные итоги для любых повторяющихся значений в электронной таблице. Aspose.Cells предоставляет функции API, которые помогают добавлять промежуточные итоги в электронные таблицы программно.

{{% /alert %}}

## **Использование Microsoft Excel**

Для создания промежуточных итогов в Microsoft Excel:

1. Создайте простой список данных на первом листе книги (как показано на рисунке ниже) и сохраните файл как Book1.xls.
1. Выберите любую ячейку в вашем списке.
1. В меню **Данные**, выберите **Промежуточные итоги**.
   Выводится диалоговое окно Промежуточные итоги. Определите, какую функцию использовать и куда поместить промежуточные итоги.

   **Выбор диапазона данных для добавления промежуточных итогов**

![todo:image_alt_text](creating-subtotals_1.png)

**Диалоговое окно Промежуточных итогов** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Использование API Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), позволяющий получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс предоставляет широкий спектр свойств и методов для управления листом и другими объектами. Каждый лист состоит из коллекции [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Для создания промежуточных итогов в листе используйте метод промежуточные_итоги класса [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Укажите соответствующие значения для параметров метода, чтобы получить нужный результат.

Приведенный ниже пример показывает, как создать промежуточные итоги на первом листе шаблонного файла (Book1.xls) с использованием API Aspose.Cells.

При выполнении кода создается лист с промежуточными итогами.

**Применение промежуточных итогов** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
