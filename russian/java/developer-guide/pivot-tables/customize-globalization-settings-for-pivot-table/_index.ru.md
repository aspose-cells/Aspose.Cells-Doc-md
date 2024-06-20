---
title: Настройка глобализации для сводной таблицы
type: docs
weight: 20
url: /ru/java/customize-globalization-settings-for-pivot-table/
---

## **Возможные сценарии использования**

Иногда вам нужно настроить *Итог, Подытог, Общий итог, Все элементы, Несколько элементов, Заголовки столбцов, Заголовки строк, Пустые значения* текст в соответствии с вашими требованиями. Aspose.Cells позволяет настраивать настройки глобализации сводной таблицы для работы с такими сценариями. Вы также можете использовать эту функцию для изменения меток на другие языки, такие как арабский, хинди, польский и т.д.

## **Настройка глобализации для сводной таблицы**

Следующий образец кода объясняет, как настроить глобализацию для сводной таблицы. Он создает класс *CustomPivotTableGlobalizationSettings*, производный от базового класса [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) и переопределяет все необходимые методы. Эти методы возвращают настроенный текст для *Итог, Подытог, Общий итог, Все элементы, Несколько элементов, Заголовки столбцов, Заголовки строк, Пустые значения*. Затем он присваивает объект этого класса свойству [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings). Код загружает [исходный файл Excel](40468491.xlsx), который содержит сводную таблицу, обновляет и вычисляет ее данные и сохраняет его в виде [файла PDF вывода](40468490.pdf). Ниже приведен скриншот, показывающий эффект образца кода на выходном PDF. Как видно на скриншоте, различные части сводной таблицы теперь имеют настраиваемый текст, возвращаемый переопределенными методами класса [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
