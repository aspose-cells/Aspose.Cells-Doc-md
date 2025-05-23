---
title: Обновление срезки
type: docs
weight: 50
url: /ru/net/updating-slicer/
description: Эта статья показывает, как обновить связанные сводные таблицы, обновив элемент фильтра на Aspose.Cells for .NET API.
keywords: Aspose.Cells C# Обновление фильтра, C# как изменить фильтр, как настроить фильтр в C#, как выбрать или отменить выбор элементов фильтра.
---

## **Возможные сценарии использования**

Если вы хотите обновить фильтр в Microsoft Excel, выбрать или отменить выбор его элементов, затем фильтр таблицы или сводная таблица будут соответственно обновлены. Пожалуйста, используйте [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems), чтобы выбрать или отменить выбор элементов фильтра с помощью Aspose.Cells, а затем вызовите метод [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh), чтобы обновить фильтр таблицы или сводную таблицу.

## **Как обновить фильтр**

Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий фильтр. Он отменяет выбор 2-го и 3-го элементов фильтра и обновляет фильтр. Затем сохраняет рабочую книгу в [выходной файл Excel](67338476.xlsx). На следующем скриншоте показан эффект образца кода на образцовый файл Excel. Как вы можете видеть на скриншоте, обновление фильтра с выбранными элементами также обновило сводную таблицу соответственно.

![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
