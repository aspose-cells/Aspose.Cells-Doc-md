---
title: Настройка глобализации для сводной таблицы
type: docs
weight: 50
url: /ru/net/customize-globalization-settings-for-pivot-table/
---

## **Возможные сценарии использования**

Иногда вам нужно настроить *Итог, Подытог, Общий итог, Все элементы, Несколько элементов, Заголовки столбцов, Заголовки строк, Пустые значения* текст в соответствии с вашими требованиями. Aspose.Cells позволяет настраивать настройки глобализации сводной таблицы для работы с такими сценариями. Вы также можете использовать эту функцию для изменения меток на другие языки, такие как арабский, хинди, польский и т.д.

## **Настройка глобализации для сводной таблицы**

В следующем примере кода показано, как настроить глобализацию для сводной таблицы. Создается класс *CustomPivotTableGlobalizationSettings*, производный от базового класса [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) и переопределяются все необходимые методы. Эти методы возвращают настраиваемый текст для *Итог итогов, Подытог, Общий итог, Все элементы, Несколько элементов, Метки столбцов, Метки строк, Пустые значения*. Затем он назначает объект этого класса свойству [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/). Код загружает [исходный excel-файл](40468488.xlsx), который содержит сводную таблицу, обновляет и рассчитывает ее данные и сохраняет его в виде [выходного PDF](40468487.pdf). На следующем снимке экрана показан эффект примерного кода на выходном PDF. Как вы видите на снимке экрана, различные части сводной таблицы теперь имеют настраиваемый текст, возвращаемый переопределенными методами класса [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
