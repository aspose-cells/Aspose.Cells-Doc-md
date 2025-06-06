---
title: Как добавить условное форматирование текста
description: Как использовать библиотеку Aspose.Cells на C# для применения условного форматирования текста. Настраивая эти критерии, вы получаете больший контроль над внешним видом и отображением ячеек.
keywords: Aspose.Cells, условное форматирование текста, C#, Условное, форматирование
type: docs
weight: 70
url: /ru/net/how-to-add-text-conditional-formatting/
---

## **Возможные сценарии использования**
Использование условного форматирования на основе текста в таблицах полезно для выделения ячеек, соответствующих определенным текстовым критериям. Это может улучшить анализ данных и упростить поиск ключевой информации в большом наборе данных. Вот причины использования условного форматирования по тексту:

1. Выделение конкретного текста: Вы можете применять форматирование на основе определенных слов, фраз или символов. Например, вы можете выделить все ячейки со словом "Срочно" или "Завершено", чтобы легко отличать задачи в проекте.
1. Выявление шаблонов или трендов: Если вы работаете с категориями или статусами (например, "Высокий", "Средний", "Низкий"), условное форматирование на основе текста поможет визуально отличить их, что облегчит отслеживание прогресса или приоритизацию задач.
1. Предупреждения об ошибках или вводе данных: Форматирование текста может сигнализировать о несогласованных или ошибочных записях, таких как орфографические ошибки, неполный текст или неверные значения. Особенно полезно при работе с большим количеством текста в данных.
1. Повышенная читаемость: Цветное кодирование текста или изменение его стиля (жирный, курсив и т. д.) помогает выделить важную информацию, улучшая общую читаемость вашего листа.
1. Динамическая обратная связь: Вы можете создавать правила, которые автоматически регулируют форматирование при совпадении текста с определенными условиями. Это означает, что вам не нужно вручную обновлять форматирование при изменении данных.

По сути, условное форматирование текста помогает быстро обнаруживать актуальную информацию, ошибки и тенденции, делая этот инструмент мощным средством для управления и анализа текстовых данных.

## **Как добавить условное форматирование текста с помощью Excel**
Чтобы добавить условное форматирование на основе текста в Excel, выполните следующие шаги:

1. Выделите диапазон ячеек: выделите ячейки, к которым хотите применить условное форматирование.
1. Откройте меню Условное форматирование: перейдите на вкладку Главная в ленте Excel. Нажмите на Условное форматирование в группе "Стили".
1. Выберите «Новое правило»: из раскрывающегося меню выберите Новое правило.
1. Выберите «Форматировать только ячейки, которые содержат»: в диалоговом окне Новое правило форматирования выберите Форматировать только ячейки, которые содержат в разделе "Выберите тип правила".
1. Установите критерии правила: в разделе "Форматировать ячейки с" выберите Specific Text из раскрывающегося списка. Выберите либо содержащий, начинающийся с, либо заканчивающийся, в зависимости от условия, которое хотите применить. Введите текст, который нужно форматировать (например, конкретное слово "Срочно" или "Завершено").
1. Выберите форматирование: нажмите кнопку Форматировать. В диалоговом окне Формат ячеек выберите цвет шрифта, цвет заливки или другие параметры форматирования по вашему усмотрению.
1. Примените правило: установив желаемый формат, нажмите ОК, чтобы применить правило. Еще раз нажмите ОК в диалоговом окне Нового правила форматирования, чтобы закрыть его.
1. Посмотрите результаты: ячейки, содержащие указанный вами текст, теперь будут иметь примененное форматирование, что упростит обнаружение релевантной информации.


## **Как добавить условное форматирование текста с помощью Aspose.Cells for .NET**

Aspose.Cells полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более новыми версиями в формате XLSX для ячеек во время выполнения. Этот пример демонстрирует расширенные виды условного форматирования, такие как BeginsWith, ContainsBlank, ContainsText и другие.

### **Форматировать ячейку, когда значение начинается с указанного текста**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **Форматировать ячейку, если значение содержит пустое**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **Форматировать ячейку, если значение содержит ошибки**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **Форматировать ячейку, если значение содержит указанный текст**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **Форматировать ячейку, если значение содержит дублирующиеся значения**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **Форматировать ячейку, если значение заканчивается указанным текстом**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **Форматировать ячейку, если значение не содержит пустое**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **Форматировать ячейку, если значение не содержит ошибок**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **Форматировать ячейку, если значение не содержит указанный текст**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **Форматировать ячейку, если значение содержит уникальные значения**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
