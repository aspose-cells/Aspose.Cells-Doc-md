---
title: Обнаружение типа гиперссылки
type: docs
weight: 160
url: /ru/net/detect-hyperlink-type/
description: Узнайте, как определить тип гиперссылки через API Aspose.Cells for .NET.
keywords: Определить тип гиперссылки, Определить тип гиперссылки, Получить тип гиперссылки
---

## **Обнаружение типа гиперссылки**

В электронной таблице Excel могут быть разные типы гиперссылок, такие как внешние, ссылки на ячейки, пути к файлам и т. д. Aspose.Cells поддерживает возможность определить тип гиперссылки. Типы гиперссылок представлены перечислением [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Перечисление [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) имеет следующие элементы.

- Внешние: внешняя ссылка
- Путь к файлу: Локальный и полный путь к файлам\папкам.
- Электронная почта: Электронная почта
- СсылкаНаКлетку: Ссылка на клетку или именованный диапазон.

Для проверки типа гиперссылки, класс [**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) предоставляет свойство [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) с возвращаемым типом [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). В следующем фрагменте кода демонстрируется использование свойства [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype), используя этот [исходный файл Excel](94896195.xlsx).

### Исходный код

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Ниже приведен вывод, сгенерированный указанным выше фрагментом кода.

### Вывод в консоли
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
