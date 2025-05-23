---
title: Изменить существующий стиль.
linktitle: Изменить существующий стиль.
description: Aspose.Cells — это библиотека Node.js для работы с файлами таблиц, которая позволяет пользователям изменять существующие стили ячеек. В этой статье будет рассказано о том, как изменять существующий стиль ячейки с помощью библиотеки Aspose.Cells, чтобы вы могли изменять внешний вид ячеек по необходимости.
keywords: Изменение существующих стилей, настройка внешнего вида вашего приложения, руководства, учебные пособия, справочная документация, документация по разработке, ссылки на API, образцы кода, загрузки, поддержка.
type: docs
weight: 90
url: /ru/nodejs-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Для применения одинаковых параметров форматирования к ячейкам создайте новый объект стиля форматирования. Объект стиля форматирования представляет собой комбинацию параметров форматирования, таких как шрифт, размер шрифта, отступ, номер, граница, узоры и т. д., названных и сохраненных в виде набора. При применении все форматирование в этом стиле применяется.

Вы также можете использовать существующий стиль, сохранить его с книгой и использовать для форматирования информации с теми же атрибутами.

Когда ячейки не явно форматируются, применяется стиль **Обычный** (стандартный стиль книги). В Microsoft Excel предопределено несколько стилей, кроме стиля Нормальный, включая запятую, валюту и процент.

Aspose.Cells позволяет изменять любой из этих стилей или любой другой стиль, который вы определяете с желаемыми атрибутами.

{{% /alert %}}

## **Использование Microsoft Excel**

Для обновления стиля в Microsoft Excel 97-2003:

1. В меню **Формат**, выберите **Стиль**.
1. Выберите стиль, который вы хотите изменить в списке **Имя стиля**.
1. Нажмите **Изменить**.
1. Выберите параметры стиля, которые вы хотите с помощью вкладок в диалоговом окне Формат ячеек.
1. Нажмите **ОК**.
1. В разделе **Стиль включает**, укажите нужные особенности стиля.
1. Нажмите **OK**, чтобы сохранить стиль и применить его к выбранному диапазону.

## **Использование Aspose.Cells for Node.js via C++**

Следующие примеры демонстрируют, как использовать метод [**Style.update()**](https://reference.aspose.com/cells/nodejs-cpp/style/#update--).

### **Создание и изменение стиля**

Этот пример создает объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style), применяет его к диапазону ячеек и изменяет объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Изменения автоматически применяются к ячейке и диапазону, к которому был применен стиль.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-CreateAndModifyStyle.js" >}}


### **Изменение существующего стиля**

В этом примере используется простой шаблонный файл Excel, к которому уже был применен стиль Percent к диапазону. Пример:

1. получает стиль,
1. создает объект стиля и
1. изменяет форматирование стиля.

Изменения автоматически применяются к диапазону, к которому был применен стиль.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ModifyExistingStyle.js" >}}


