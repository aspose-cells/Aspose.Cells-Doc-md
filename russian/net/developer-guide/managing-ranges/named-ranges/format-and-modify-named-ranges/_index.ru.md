---
title: Форматирование и изменение именованных диапазонов
type: docs
weight: 85
url: /ru/net/format-and-modify-named-ranges/
---
## **Диапазоны форматов**

### **Установка цвета фона и атрибутов шрифта для именованного диапазона**

 Чтобы применить форматирование, определите[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекта, чтобы указать настройки стиля и применить их к[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range)объект.

В следующем примере показано, как установить сплошной цвет заливки (цвет заливки) с настройками шрифта в диапазоне.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Добавление границ к именованному диапазону**

 Можно добавить границы к диапазону ячеек, а не только к одной ячейке.[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range) объект обеспечивает[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)метод, который принимает следующие параметры для добавления границы к диапазону ячеек:

-  Тип границы, тип границы, выбранный из[**Тип границы**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)перечисление.
-  Стиль линии, стиль линии, выбранный из[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)перечисление.
- Color, цвет линии, выбранный из перечисления Color.

В следующем примере показано, как установить границу контура для диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

В следующем примере показано, как установить границы вокруг каждой ячейки в диапазоне.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Переименовать именованный диапазон**

 Aspose.Cells позволяет вам переименовать именованный диапазон для ваших нужд. Вы можете получить именованный диапазон и переименовать его, используя[**Имя.Текст**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)атрибут. В следующем примере показано, как переименовать именованный диапазон.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Союз диапазонов**

 Aspose.Cells предоставляет[**Диапазон.Союз**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)метод для объединения диапазонов, метод возвращает[*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)объект. В следующем примере показано, как использовать объединение для диапазонов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Пересечение диапазонов**

 Aspose.Cells обеспечивает[**Диапазон.Пересечение**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) метод пересечения двух диапазонов. Метод возвращает[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range) объект. Чтобы проверить, пересекается ли диапазон с другим диапазоном, используйте[**Диапазон.Пересечение**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)метод, который возвращает логическое значение. В следующем примере показано, как пересекать диапазоны.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Объединить Cells в именованном диапазоне**

 Aspose.Cells предоставляет[**Диапазон.Объединить()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)способ объединения ячеек в диапазоне. В следующем примере показано, как объединить отдельные ячейки именованного диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Удалить именованный диапазон**

 Aspose.Cells обеспечивает[**Коллекция Имен. Удалить В ()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) способ стереть имя диапазона. Чтобы очистить содержимое диапазона, используйте[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)метод. В следующем примере показано, как удалить именованный диапазон вместе с его содержимым.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
