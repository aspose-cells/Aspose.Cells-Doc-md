---
title: Расширенные настройки защиты с Excel XP
type: docs
weight: 30
url: /ru/python-net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

С момента выпуска Excel 2002 или XP, Microsoft добавила множество расширенных настроек защиты.

{{% /alert %}}

## **Введение**

Эти настройки защиты ограничивают или разрешают пользователям:

- Удалить строки или столбцы.
- Изменить содержимое, объекты или сценарии.
- Форматировать ячейки, строки или столбцы.
- Вставить строки, столбцы или гиперссылки.
- Выбирать заблокированные или разблокированные ячейки.
- Использовать сводные таблицы и многое другое.

Aspose.Cells для Python via .NET поддерживает все расширенные настройки защиты, предлагаемые Excel XP или более поздними версиями.

### **Настройки расширенной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть доступные настройки защиты в Excel XP:

1. Из меню **Инструменты** выберите **Защита**, а затем **Защитить лист**. Будет отображено диалоговое окно.

Для просмотра доступных настроек защиты в Excel 2016

1. В меню **Файл** выберите **Защита книги**, а затем **Защитить текущий лист**.
1. Выберите **Защитить лист** в меню **Проверка**.

Последование вышеупомянутых шагов отображает диалоговое окно, где вы можете разрешить или ограничить функции листов или применить пароль к листу.

### **Расширенные настройки защиты с помощью Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET поддерживает все расширенные настройки защиты.

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), позволяющую получать доступ к каждому листу в Excel-файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет свойство [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection), которое используется для применения этих расширенных настроек защиты. Свойство [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection), на самом деле, является объектом класса [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection), который инкапсулирует несколько булевых свойств для отключения или включения ограничений.

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство поддерживаемых Excel XP и более поздних версий настроек защиты.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AdvancedProtectionSettings-1.py" >}}

{{% alert color="primary" %}}

Пожалуйста, не вызывайте метод [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) при использовании свойства [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection). Также, сохраните файл в формате Excel97To2003 или Xlsx, потому что расширенные настройки защиты поддерживаются только в Excel XP и более поздних версиях.

{{% /alert %}}

### **Проблема блокировки ячеек**

Если вы хотите ограничить пользователей от редактирования ячеек, ячейки должны быть заблокированы перед применением настроек защиты. В противном случае, ячейки можно редактировать, даже если лист защищен. В Microsoft Excel XP ячейки можно заблокировать через следующий диалог:

|**Диалог для блокировки ячеек в Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Также возможно заблокировать ячейки с помощью API Aspose.Cells для Python via .NET. Каждая ячейка может иметь формат [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), содержащий булевое свойство [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Установите свойство [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) в значение **true** или **false**, чтобы заблокировать или разблокировать ячейку.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-LockCell-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
