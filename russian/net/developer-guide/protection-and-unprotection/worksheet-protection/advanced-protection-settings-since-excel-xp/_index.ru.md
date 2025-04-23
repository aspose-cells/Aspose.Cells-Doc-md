---
title: Расширенные настройки защиты с Excel XP
type: docs
weight: 30
url: /ru/net/advanced-protection-settings-since-excel-xp/
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

Aspose.Cells поддерживает все продвинутые настройки защиты, предлагаемые Excel XP или более поздними версиями.

### **Настройки расширенной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть доступные настройки защиты в Excel XP:

1. Из меню **Инструменты** выберите **Защита**, а затем **Защитить лист**. Будет отображено диалоговое окно.

Для просмотра доступных настроек защиты в Excel 2016

1. В меню **Файл** выберите **Защита книги**, а затем **Защитить текущий лист**.
1. Выберите **Защитить лист** в меню **Проверка**.

Последование вышеупомянутых шагов отображает диалоговое окно, где вы можете разрешить или ограничить функции листов или применить пароль к листу.

### **Настройки расширенной защиты с использованием Aspose.Cells**

Aspose.Cells поддерживает все расширенные настройки защиты.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), обеспечивающую доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет свойство [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection), которое используется для применения этих расширенных настроек защиты. Свойство [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection), на самом деле, является объектом класса [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection), который инкапсулирует несколько булевых свойств для отключения или включения ограничений.

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство поддерживаемых Excel XP и более поздних версий настроек защиты.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

Пожалуйста, не вызывайте метод [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) при использовании свойства [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection). Также, сохраните файл в формате Excel97To2003 или Xlsx, потому что расширенные настройки защиты поддерживаются только в Excel XP и более поздних версиях.

{{% /alert %}}

### **Проблема блокировки ячеек**

Если вы хотите ограничить пользователей от редактирования ячеек, ячейки должны быть заблокированы перед применением настроек защиты. В противном случае, ячейки можно редактировать, даже если лист защищен. В Microsoft Excel XP ячейки можно заблокировать через следующий диалог:

|**Диалог для блокировки ячеек в Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Хранение ячеек также можно осуществить с использованием API Aspose.Cells. Каждая ячейка может получить [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) формат, который содержит логическое свойство, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Установите свойство [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) в **true** или **false** для блокировки или разблокировки ячейки.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
