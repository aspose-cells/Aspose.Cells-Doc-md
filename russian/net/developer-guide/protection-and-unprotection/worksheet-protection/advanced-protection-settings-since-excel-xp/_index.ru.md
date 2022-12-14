---
title: Дополнительные параметры защиты начиная с Excel XP
type: docs
weight: 30
url: /ru/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

После выпуска Excel 2002 или XP в Microsoft было добавлено множество расширенных настроек защиты.

{{% /alert %}}

## **Введение**

Эти параметры защиты ограничивают или разрешают пользователям:

- Удалить строки или столбцы.
- Редактируйте содержимое, объекты или сценарии.
- Отформатируйте ячейки, строки или столбцы.
- Вставьте строки, столбцы или гиперссылки.
- Выберите заблокированные или разблокированные ячейки.
- Используйте сводные таблицы и многое другое.

Aspose.Cells поддерживает все параметры расширенной защиты, предлагаемые в Excel XP или более поздних версиях.

### **Параметры дополнительной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть параметры защиты, доступные в Excel XP:

1.  От**Инструменты** меню, выберите**Защита** с последующим**Защитить лист**. Отобразится диалоговое окно.

Чтобы просмотреть параметры защиты, доступные в Excel 2016

1.  От**Файл** меню, выберите**Защитить книгу** с последующим**Защитить текущий лист**.
1.  Выберите**Защитить лист** в**Обзор** меню.

Выполнение шагов, упомянутых выше, отобразит диалоговое окно, в котором вы можете разрешить или ограничить функции рабочих листов или применить пароль к рабочему листу.

### **Параметры дополнительной защиты с использованием Aspose.Cells**

Aspose.Cells поддерживает все дополнительные параметры защиты.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)учебный класс.

[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)класс обеспечивает[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) свойство, которое используется для применения этих дополнительных параметров защиты.[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) Собственность фактически является объектом[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/protection)класс, который инкапсулирует несколько логических свойств для отключения или включения ограничений.

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство дополнительных параметров защиты, поддерживаемых Excel XP и более поздних версиях.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 Пожалуйста, не звоните[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Защищать**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) метод при использовании[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)имущество. Кроме того, сохраните файл в формате Excel97To2003 или Xlsx, поскольку дополнительные параметры защиты поддерживаются только в Excel XP и более поздних версиях.

{{% /alert %}}

### **Cell Проблема с блокировкой**

Если вы хотите запретить пользователям редактировать ячейки, ячейки должны быть заблокированы, прежде чем будут применены какие-либо параметры защиты. В противном случае ячейки можно редактировать, даже если рабочий лист защищен. В Microsoft Excel XP ячейки можно заблокировать с помощью следующего диалогового окна:

|**Диалоговое окно для блокировки ячеек в Excel XP**|
|:- |
|![дело:изображение_альтернативный_текст](advanced-protection-settings-since-excel-xp_1.png)|

Также можно заблокировать ячейки с помощью Aspose.Cells API. Каждая ячейка может получить[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) форматирование, содержащее логическое свойство,[**Заблокировано**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Установить[**Заблокировано**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) собственность на**истинный** или же**ЛОЖЬ** чтобы заблокировать или разблокировать ячейку.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
