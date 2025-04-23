---
title: Отправить форму вперед или назад внутри листа
type: docs
weight: 3400
url: /ru/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **Возможные сценарии использования**

Когда в одном положении присутствует несколько фигур, то их видимость определяется их порядком по z-вешению. Aspose.Cells for Python via .NET предоставляет метод [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back), который изменяет порядок по z-вешению фигуры. Если вы хотите отправить фигуру назад, используйте отрицательное число, например -1, -2, -3 и так далее. Если хотите вывести фигуру на передний план, используйте положительное число, например 1, 2, 3 и так далее.

## **Отправить форму вперед или назад внутри листа**

Следующий образец кода объясняет использование метода [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back). Пожалуйста, обратитесь к [образцу файла Excel](50528330.xlsx), использованному в коде, и [выходному файлу Excel](50528331.xlsx), сгенерированному им. Скриншот показывает эффект кода на образце файла Excel при выполнении.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
