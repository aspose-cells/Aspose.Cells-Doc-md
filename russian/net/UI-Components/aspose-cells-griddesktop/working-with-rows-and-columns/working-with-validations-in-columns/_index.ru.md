---
title: Работа с проверками в столбцах
type: docs
weight: 80
url: /ru/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 В одной из наших предыдущих тем мы обсуждали проверки, но это было в контексте[Валидации в рабочих листах](/cells/ru/net/working-with-validations-in-worksheets/) (чтобы получить общую информацию о проверке и режимах проверки, разработчики могут обратиться к этому разделу). В этом разделе мы объясним проверки в отношении столбцов. Используя эту функцию, разработчики могут применять правило проверки к любому столбцу рабочего листа. Давайте обсудим это подробно.

{{% /alert %}} 
## **Добавление проверки столбца**
Чтобы добавить какую-либо проверку в столбец, выполните следующие действия:

-  Добавьте элемент управления Aspose.Cells.GridDesktop в свой**Форма**
-  Доступ к любому желаемому**Рабочий лист**
- **Добавлять** желаемый**Проверка** в любую колонку

**ВАЖНЫЙ:**Для получения дополнительной информации о типах проверки (или режимах проверки, таких как**Требуется проверка**, **Проверка регулярных выражений** а также**Пользовательская проверка** ) и реализация**Пользовательская проверка** , пожалуйста, обратитесь к[Работа с проверками в рабочих листах.](/cells/ru/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Доступ к проверке столбца**
Чтобы получить доступ к проверке определенного столбца, выполните следующие действия:

-  Доступ к желаемому**Рабочий лист**
-  Доступ к определенному столбцу**Проверка** в**Рабочий лист**
-  Редактировать**Проверка** атрибуты по желанию



{{< highlight "csharp" >}}

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
Чтобы удалить проверку определенного столбца с рабочего листа, выполните следующие действия:

-  Доступ к желаемому**Рабочий лист**
-  Удалить конкретный столбец**Проверка** от**Рабочий лист**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
