---
title: Получить диапазон с внешними ссылками с помощью Golang через C++
linktitle: Получить диапазон с внешними ссылками
type: docs
weight: 120
url: /ru/go-cpp/get-range-with-external-links/
description: Изучите, как получать диапазоны с внешними ссылками в файлах Excel с использованием Aspose.Cells с Golang через C++.
---

## **Получить диапазон с внешними ссылками**

Во многих случаях файлы Excel обращаются к данным из других файлов Excel через внешние связи. Aspose.Cells предоставляет возможность получать эти внешние связи с помощью метода [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/). Метод [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) возвращает массив типа [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). Класс [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) содержит свойство [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/), которое возвращает имя внешнего файла. Класс [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) раскрывает следующие члены.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): Конечный столб области
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): Конечная строка области
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): Получить имя внешнего файла, если это внешний ссылка
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): Указывает, является ли это областью
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): Указывает, является ли это внешней ссылкой
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): Указывает, в каком листе находится эта ссылка
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): Начальный столб области
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): Начальная строка области

Пример кода, приведенный ниже, демонстрирует использование метода [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) для получения диапазонов с внешними ссылками.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
