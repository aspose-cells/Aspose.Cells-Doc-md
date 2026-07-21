---
title: Настройка глобальных параметров глобализации для сводной таблицы с Golang через C++
linktitle: Настройка глобализации для сводной таблицы
type: docs
weight: 50
url: /ru/go-cpp/customize-globalization-settings-for-pivot-table/
description: Научитесь настраивать параметры глобализации сводной таблицы с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда вам нужно настроить текст *Общая сумма по сводной, Итоговая сумма, Общий итог, Все элементы, Несколько элементов, Метки столбцов, Метки строк, Пустые значения* в соответствии с вашими требованиями. Aspose.Cells for C++ позволяет настраивать параметры глобализации сводной таблицы для подобных сценариев. Вы также можете использовать эту функцию для изменения ярлыков на другие языки, такие как арабский, хинди, польский и др.

## **Настройка глобализации для сводной таблицы**

Следующий пример кода показывает, как настроить параметры глобализации для сводной таблицы на C++. Создается класс *CustomPivotTableGlobalizationSettings*, унаследованный от базового класса [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/), и переопределяются все необходимые методы. Эти методы возвращают настроенный текст для различных элементов сводной таблицы. Затем эта реализация присваивается свойству [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). Пример загружает [исходный файл Excel](40468488.xlsx), обновляет данные сводной таблицы и сохраняет его как [выходной PDF](40468487.pdf). Ниже изображение с настройками ярлыков в выходном файле.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
