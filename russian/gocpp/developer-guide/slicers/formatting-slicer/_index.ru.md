---
title: Форматирование среза с Golang через C++
linktitle: Форматирование фильтра
type: docs
weight: 20
url: /ru/go-cpp/formatting-slicer/
description: Форматировать срезы в Microsoft Excel с помощью Aspose.Cells с Golang через C++.
---

## **Возможные сценарии использования**

Вы можете форматировать слайсер в Microsoft Excel, устанавливая его количество колонок или стиль и т.д. Aspose.Cells также позволяет сделать это с использованием свойств [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/go-cpp/slicer/getnumberofcolumns/) и [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/).

## **Форматирование фильтра**

Пожалуйста, ознакомьтесь с следующим кодом; он загружает [пример файла Excel](67338473.xlsx), содержащий слайсер. Он обращается к слайсеру, устанавливает его количество колонок и тип стиля, а затем сохраняет его как [выходной файл Excel](67338474.xlsx). Скриншот показывает, как выглядит слайсер после выполнения примера кода.

![todo:image_alt_text](formatting-slicer_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingSlicer.go" >}}
