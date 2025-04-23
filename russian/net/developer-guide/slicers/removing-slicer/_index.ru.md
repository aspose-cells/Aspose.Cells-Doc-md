---
title: Удаление срезки
type: docs
weight: 30
url: /ru/net/removing-slicer/
---

## **Возможные сценарии использования**

Если вы хотите удалить срезку в Microsoft Excel, просто выберите ее и нажмите кнопку *Удалить*. Точно так же, если вы хотите удалить ее с помощью API Aspose.Cells программно, пожалуйста, используйте метод [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/remove). Он удалит срезку из листа.

## **Удаление срезки**

Следующий образец кода загружает [образец файла Excel](67338478.xlsx), содержащий существующую срезку. Он получает доступ к срезке, а затем удаляет ее. Наконец, он сохраняет книгу как [выходной файл Excel](67338477.xlsx). На следующем скриншоте показано, что срезка будет удалена после выполнения образца кода.

![todo:image_alt_text](removing-slicer_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-RemovingSlicer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
