---
title: Обнаружение типа гиперссылки
type: docs
weight: 160
url: /ru/nodejs-cpp/detect-hyperlink-type/
description: Узнайте, как определять тип гиперссылки через API Aspose.Cells for Node.js via C++.
keywords: Определение типа гиперссылки Node.js через C++, Определение типа гиперссылки Node.js через C++, Получение типа гиперссылки Node.js через C++
---

## **Определение типа гиперссылки**

Файл Excel может иметь разные типы гиперссылок, такие как внешние, ссылка на ячейку, путь к файлу и др. Aspose.Cells for Node.js via C++ поддерживает функцию определения типа гиперссылки. Типы гиперссылок представлены перечислением [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). Перечисление [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) содержит следующие элементы.

- Внешний: Внешняя ссылка
- FilePath: Локальный и полный путь к файлам/папкам.
- Email: Электронная почта
- CellReference: Ссылка на ячейку или именованный диапазон.

Чтобы проверить тип гиперссылки, класс [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) предоставляет метод [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) с типом возврата [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). Следующий пример демонстрирует использование метода [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) с этим [исходным Excel файлом](94896195.xlsx).

### Исходный код

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


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
