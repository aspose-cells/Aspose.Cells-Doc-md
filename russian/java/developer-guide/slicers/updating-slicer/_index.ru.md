---
title: Обновление срезки
type: docs
weight: 50
url: /ru/java/updating-slicer/
---

## **Возможные сценарии использования**
Если нужно обновить срез в Microsoft Excel, выберите или отмените выбор его элементов, и он автоматически обновит таблицу среза или сводную таблицу. Используйте [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems), чтобы выбрать или отменить выбор элементов среза, и вызовите [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh--) для обновления таблицы среза или сводной таблицы. 
## **Обновление среза**
Следующий образец кода загружает [образец Excel-файла](67338506.xlsx), который содержит существующий срез. Он отменяет выбор 2-го и 3-го элементов среза и обновляет срез. Затем он сохраняет книгу как [выходной Excel-файл](67338505.xlsx). На следующем скриншоте показано, как образец кода повлиял на образец Excel-файла. Как видите на скриншоте, обновление среза с выбранными элементами также обновило сводную таблицу соответственно.

![todo:image_alt_text](updating-slicer_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
