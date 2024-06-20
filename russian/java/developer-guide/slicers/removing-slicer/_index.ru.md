---
title: Удаление срезки
type: docs
weight: 30
url: /ru/java/removing-slicer/
---

## **Возможные сценарии использования**
Если вы хотите удалить срез в Microsoft Excel, просто выберите его и нажмите кнопку *Удалить*. Аналогично, если вы хотите удалить его с использованием программного интерфейса Aspose.Cells API, используйте метод [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)). Он удалит срез из листа. 
## **Удаление срезки**
Следующий образец кода загружает [образец Excel-файла](67338504.xlsx), который содержит существующий срез. Он получает доступ к срезам и затем удаляет их. Наконец, он сохраняет книгу как [выходной Excel-файл](67338502.xlsx). На следующем скриншоте показан срез, который будет удален после выполнения образца кода.

![todo:image_alt_text](removing-slicer_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
