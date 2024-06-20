---
title: Форматирование и изменение именованных диапазонов
type: docs
weight: 85
url: /ru/net/format-and-modify-named-ranges/
---

## **Форматирование диапазонов**

### **Установка цвета фона и атрибутов шрифта для именованного диапазона**

Чтобы применить форматирование, определите объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style), чтобы указать настройки стиля, и примените его к объекту [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

В следующем примере показано, как установить сплошной цвет заливки (цвет заливки) с настройками шрифта для диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Добавление границ к именованному диапазону**

Возможно добавить границы к диапазону ячеек вместо одной ячейки. Объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) предоставляет метод [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder), который принимает следующие параметры для добавления границы к диапазону ячеек:

- Тип границы, тип границы, выбранный из перечисления [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- Стиль линии, стиль линии, выбранный из перечисления [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- Цвет, цвет линии, выбранный из перечисления Color.

В следующем примере показано, как установить контурную границу для диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

В следующем примере показано, как установить границы вокруг каждой ячейки в диапазоне.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Переименование именованного диапазона**

Aspose.Cells позволяет переименовывать именованный диапазон по вашему желанию. Вы можете получить именованный диапазон и переименовать его, используя атрибут [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text). В следующем примере показано, как переименовать именованный диапазон.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Объединение диапазонов**

Aspose.Cells предоставляет метод [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) для объединения диапазонов, метод возвращает объект [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8). В следующем примере показано, как выполнить объединение диапазонов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Пересечение диапазонов**

Aspose.Cells предоставляет метод [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) для пересечения двух диапазонов. Метод возвращает объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Чтобы проверить, пересекается ли диапазон с другим диапазоном, используйте метод [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect), который возвращает логическое значение. Ниже приведен пример того, как найти пересечение диапазонов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Объединение ячеек в именованном диапазоне**

Aspose.Cells предоставляет метод [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) для объединения ячеек в диапазоне. В следующем примере показано, как объединить отдельные ячейки именованного диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Удалить именованный диапазон**

Aspose.Cells предоставляет метод [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) для удаления названия диапазона. Для очистки содержимого диапазона используйте метод [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index). В следующем примере показано, как удалить именованный диапазон вместе с его содержимым.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
