---
title: Обновление срезки
type: docs
weight: 50
url: /ru/python-net/updating-slicer/
description: Узнайте, как обновлять фильтр с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, обновление фильтра Python без Excel, Обновление фильтра с использованием Aspose.Cells для Python.
---

## **Возможные сценарии использования**

Если вы хотите обновить фильтр в Microsoft Excel, выберите или отмените выбор его элементов, он затем будет обновлять таблицу фильтров или сводную таблицу соответственно. Пожалуйста, используйте [**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/) для выбора или отмены выбора элементов фильтра с помощью Aspose.Cells для Python via .NET, а затем вызовите метод [**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#) для обновления таблицы фильтров или сводной таблицы.

## **Как обновить фильтр с помощью библиотеки Aspose.Cells для Python Excel**

Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий фильтр. Он отменяет выбор 2-го и 3-го элементов фильтра и обновляет фильтр. Затем сохраняет рабочую книгу в [выходной файл Excel](67338476.xlsx). На следующем скриншоте показан эффект образца кода на образцовый файл Excel. Как вы можете видеть на скриншоте, обновление фильтра с выбранными элементами также обновило сводную таблицу соответственно.

![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
