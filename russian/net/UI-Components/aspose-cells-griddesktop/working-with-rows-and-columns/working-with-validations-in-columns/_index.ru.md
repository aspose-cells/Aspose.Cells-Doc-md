---
title: Работа с проверками в столбцах
type: docs
weight: 80
url: /ru/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop,validation,validations
description: В этой статье рассматривается способ использования проверок в столбцах в GridDesktop.
---

{{% alert color="primary" %}} 

В одной из наших предыдущих тем мы обсуждали проверки, но это было в контексте [Проверки в рабочих листах](/cells/ru/net/working-with-validations-in-worksheets/) (для общей информации о проверке и режимах проверки разработчики могут обратиться к этой теме). В этой теме мы подробно объясним проверки в отношении столбцов. Используя эту функцию, разработчики могут применить правило проверки к любому столбцу в рабочем листе. Давайте обсудим это подробнее.

{{% /alert %}} 
## **Добавление проверки столбца**
Чтобы добавить любого рода проверку в столбец, выполните следующие шаги:

- Добавьте элемент управления Aspose.Cells.GridDesktop на ваш **Форм**
- Получить доступ к любому желаемому **Рабочему листу**
- **Добавьте** желаемую **Проверку** к любому столбцу

**ВАЖНО:** Дополнительную информацию о типах проверки (или режимах проверки, таких как **Обязательная проверка**, **Проверка с помощью регулярных выражений** и **Пользовательская проверка**) и реализации **Пользовательской проверки** смотрите в разделе [Работа с проверками в рабочих листах.](/cells/ru/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Доступ к проверке столбца**
Чтобы получить доступ к конкретной проверке столбца, выполните следующие шаги:

- Получите доступ к желаемому **Рабочему листу**
- Получите доступ к конкретной **Проверке столбца** на **Листе**
- Измените атрибуты **Проверки**, если необходимо



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Удаление проверки столбца**
Чтобы удалить конкретную проверку столбца с рабочего листа, выполните следующие шаги:

- Получите доступ к желаемому **Рабочему листу**
- Удалите конкретную **Проверку столбца** с **Листа**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
