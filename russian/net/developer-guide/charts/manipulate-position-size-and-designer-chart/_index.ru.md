---
title: Управление позицией, размером и оформлением диаграммы
description: Узнайте, как эффективно управлять позицией, размером и оформлением диаграммы в Microsoft Excel с помощью Aspose.Cells for .NET. Наш руководитель продемонстрирует, как настроить эти свойства для улучшенного макета и визуализации.
keywords: Aspose.Cells for .NET, Позиция, Размер, Оформление диаграммы, Microsoft Excel, Макет, Визуализация.
type: docs
weight: 45
url: /ru/net/manipulate-position-size-and-designer-chart/
---

## **Позиция и размер диаграммы**
Иногда вам может потребоваться изменить позицию или размер новой или существующей диаграммы внутри листа. Aspose.Cells предоставляет свойство [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) для достижения этого. Вы можете использовать его подсвойства для изменения размера диаграммы с новой **высотой** и **шириной** или для изменения позиции с новыми координатами **X** и **Y**.
### **Управление позицией и размером диаграммы**
Чтобы изменить позицию диаграммы (координаты X, Y) или размер (высота, ширина), используйте эти свойства:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Следующий пример пояснит использование вышеуказанных API, он загружает существующую книгу, содержащую диаграмму на первом листе. Затем он изменяет размер и позицию диаграммы с использованием Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Манипулирование дизайнерскими диаграммами**
Иногда вам может потребоваться манипулировать или изменять диаграммы в файлах дизайнерских шаблонов. Aspose.Cells полностью поддерживает манипулирование содержимым и элементами дизайнерской диаграммы. Данные, содержимое диаграммы, фоновое изображение и форматирование могут быть сохранены с точностью.
### **Манипулирование дизайнерскими диаграммами в файле-шаблоне**
Для манипулирования дизайнерскими диаграммами в файлах-шаблонах используйте связанный с диаграммой API. Например, вы можете использовать свойство Worksheet.Charts для получения коллекции существующих диаграмм в файле-шаблоне.
#### **Создание диаграммы**
В следующем примере показано, как создать пирамидальную диаграмму. Позже мы будем изменять эту диаграмму.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Изменение диаграммы**
В следующем примере показано, как изменить существующую диаграмму. В этом примере мы модифицируем созданную выше диаграмму. В полученном выводе обратите внимание, что метка даты одной точки данных установлена на 'Великобритания, 30K'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Изменение линейной диаграммы в шаблоне конструктора**
В этом примере мы будем изменять линейную диаграмму. Мы добавим несколько рядов данных к существующей диаграмме и изменим цвета их линий.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
