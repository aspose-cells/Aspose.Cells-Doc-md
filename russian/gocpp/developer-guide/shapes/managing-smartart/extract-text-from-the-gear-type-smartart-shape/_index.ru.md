---
title: Извлечь текст из фигуры SmartArt типа Gear с помощью Golang через C++
linktitle: Извлечение текста из формы SmartArt типа Gear
type: docs
weight: 500
url: /ru/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Узнайте, как извлечь текст из фигур SmartArt типа Gear в Excel с помощью Aspose.Cells for C++, предоставляя пошаговое руководство и примеры кода.
---

## **Возможные сценарии использования**

Aspose.Cells for C++ умеет извлекать текст из фигуры SmartArt типа Gear. Для этого выполните следующие шаги:
1. Преобразовать фигуру SmartArt в групповую фигуру с помощью метода [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/).
2. Получить все отдельные фигуры, формирующие групповую фигуру, с помощью метода [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/).
3. Проходить по каждой отдельной фигуре и извлекать текст с помощью метода [**GetText()**](https://reference.aspose.com/cells/go-cpp/).

## **Извлечение текста из формы SmartArt с шестеренчатым типом**

Следующий пример кода загружает [пример файла Excel](67338483.xlsx), содержащего фигуру SmartArt типа Gear, и извлекает текст из его отдельных фигур. Результаты смотрите в выводе консоли ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Вывод в консоль**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
