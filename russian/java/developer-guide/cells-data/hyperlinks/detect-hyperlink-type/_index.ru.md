---
title: Определить тип гиперссылки
type: docs
weight: 180
url: /ru/java/detect-hyperlink-type/
---
## **Определить тип гиперссылки**

Файл Excel может иметь различные типы гиперссылок, такие как внешние ссылки, ссылки на ячейки, пути к файлам и т. д. Aspose.Cells поддерживает функцию определения типа гиперссылок. Типы гиперссылок представлены[**Тип таргетмоде**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Перечисление.[**Тип таргетмоде**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Перечисление имеет следующие члены.

- [**ВНЕШНИЙ**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Внешняя ссылка
- [**ПУТЬ ФАЙЛА**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Локальный и полный путь к файлам\папкам.
- [**ЭЛЕКТРОННОЕ ПИСЬМО**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): Электронное письмо
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): ссылка на ячейку или именованный диапазон.

Чтобы проверить тип гиперссылки,[**Гиперссылка**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) класс предоставляет[**Тип ссылки**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) свойство с возвращаемым типом[**Тип таргетмоде**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Следующий фрагмент кода демонстрирует использование[**Тип ссылки**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)свойство с помощью этого[исходный файл excel](LinkTypes.xlsx).

## Исходный код

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Ниже приведен вывод, созданный фрагментом кода, приведенным выше.

## Консольный вывод
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
