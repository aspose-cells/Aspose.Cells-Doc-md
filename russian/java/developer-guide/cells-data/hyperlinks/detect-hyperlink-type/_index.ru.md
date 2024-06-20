---
title: Обнаружение типа гиперссылки
type: docs
weight: 180
url: /ru/java/detect-hyperlink-type/
---

## **Обнаружение типа гиперссылки**

Файл Excel может содержать различные типы гиперссылок, такие как внешние, ссылки на ячейки, пути к файлам и т. д. Aspose.Cells поддерживает функцию обнаружения типа гиперссылки. Типы гиперссылок представлены перечислением [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). У перечисления [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType) есть следующие элементы.

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Внешняя ссылка
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Локальный и полный путь к файлам\папкам.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): Электронная почта
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Ссылка на ячейку или именованный диапазон.

Для проверки типа гиперссылки класс [**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) предоставляет свойство [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) с возвращаемым типом [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). В следующем фрагменте кода демонстрируется использование свойства [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) с помощью этого [исходного файла Excel](LinkTypes.xlsx).

## Исходный код

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Ниже приведен вывод, сгенерированный указанным выше фрагментом кода.

## Вывод в консоль
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
