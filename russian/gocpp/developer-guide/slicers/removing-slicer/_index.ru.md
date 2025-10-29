---
title: Удаление слайсера через Golang с помощью C++
linktitle: Удаление срезки
type: docs
weight: 30
url: /ru/go-cpp/removing-slicer/
description: Узнайте, как программно удалять слайсер для файлов Excel, используя API Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Если вы хотите удалить слайсер в Microsoft Excel, просто выберите его и нажмите кнопку *Delete*. Аналогично, чтобы удалить его программно с помощью API Aspose.Cells, используйте метод [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/go-cpp/slicercollection/remove/). Он удалит слайсер с рабочего листа.

## **Удаление срезки**

Следующий образец кода загружает [образец файла Excel](67338478.xlsx), содержащий существующую срезку. Он получает доступ к срезке, а затем удаляет ее. Наконец, он сохраняет книгу как [выходной файл Excel](67338477.xlsx). На следующем скриншоте показано, что срезка будет удалена после выполнения образца кода.

![todo:image_alt_text](removing-slicer_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingSlicer.go" >}}
