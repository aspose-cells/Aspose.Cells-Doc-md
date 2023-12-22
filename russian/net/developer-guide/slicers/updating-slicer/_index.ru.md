---
title: Обновление слайсера
type: docs
weight: 50
url: /ru/net/updating-slicer/
description: В этой статье показано, как обновить связанные сводные таблицы, обновив срез по номеру Aspose.Cells for .NET API.
keywords: Aspose.Cells C# Update slicer, C# how to change the slicer, how to adjust the slicer in C#, how to select or unselect he slicer items.
---
##  **Возможные сценарии использования**

Если вы хотите обновить срез в Excel Microsoft, выберите или отмените выбор его элементов, после чего он соответствующим образом обновит таблицу срезов или сводную таблицу. Пожалуйста, используйте[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)чтобы выбрать или отменить выбор элементов среза с помощью Aspose.Cells, а затем позвонить[**Слайсер.Обновить()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)метод для обновления таблицы среза или сводной таблицы.

##  **Как обновить слайсер**

 Следующий пример кода загружает[образец файла Excel](67338475.xlsx) который содержит существующий срез. Он отменяет выбор второго и третьего элементов среза и обновляет срез. Затем он сохраняет книгу как[выходной файл Excel](67338476.xlsx)На следующем снимке экрана показано влияние примера кода на образец файла Excel. Как вы можете видеть на снимке экрана, обновление среза выбранными элементами также соответствующим образом обновило сводную таблицу.

![задача: image_alt_text](updating-slicer_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
