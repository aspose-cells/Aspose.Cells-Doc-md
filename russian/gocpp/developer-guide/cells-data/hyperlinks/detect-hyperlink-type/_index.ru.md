---
title: Обнаружение типа гиперссылки с помощью Golang через C++
linktitle: Обнаружение типа гиперссылки
type: docs
weight: 160
url: /ru/go-cpp/detect-hyperlink-type/
description: Узнайте, как обнаруживать тип гиперссылки через API Aspose.Cells for C++.
keywords: Определить тип гиперссылки, Определить тип гиперссылки, Получить тип гиперссылки
---

## **Определение типа гиперссылки**

В электронной таблице Excel могут быть разные типы гиперссылок, такие как внешние, ссылки на ячейки, пути к файлам и т. д. Aspose.Cells поддерживает возможность определить тип гиперссылки. Типы гиперссылок представлены перечислением [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/). Перечисление [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) имеет следующие элементы.

- Внешние: внешняя ссылка
- Путь к файлу: Локальный и полный путь к файлам\папкам.
- Электронная почта: Электронная почта
- СсылкаНаКлетку: Ссылка на клетку или именованный диапазон.

Для проверки типа гиперссылки, класс [**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/) предоставляет свойство [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) с возвращаемым типом [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). В следующем фрагменте кода демонстрируется использование свойства [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/), используя этот [исходный файл Excel](94896195.xlsx).

### Исходный код

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
Ниже приведен вывод, сгенерированный указанным выше фрагментом кода.

### Вывод в консоли
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
