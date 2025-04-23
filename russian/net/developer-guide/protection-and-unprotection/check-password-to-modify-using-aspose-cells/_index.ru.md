---
title: Проверка пароля для изменения с использованием Aspose.Cells
type: docs
weight: 2400
url: /ru/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Иногда вам нужно проверить, совпадает ли данный пароль с **Паролем на доступ на изменение** программным путем. Aspose.Cells предоставляет метод WorkbookSettings.WriteProtection.ValidatePassword(), который можно использовать для проверки того, совпадает ли данный пароль на доступ на изменение или нет.

{{% /alert %}}

## **Проверка пароля на доступ на изменение в Microsoft Excel**

Вы можете указать **Пароль на открытие** и **Пароль на доступ на изменение** при создании ваших книг в Microsoft Excel. Пожалуйста, посмотрите этот скриншот, который показывает интерфейс, предоставляемый Microsoft Excel для указания этих паролей.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Проверьте пароль для изменения с использованием Aspose.Cells**

Следующие образцы кода загружают файл [исходного Excel](5112232.xlsx). В нем есть пароль для открытия - 1234 и пароль для изменения - 5678. Код сначала проверяет, является ли 567 правильным паролем для изменения, и возвращает false, а затем проверяет, является ли 5678 паролем для изменения, и возвращает true.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Вывод в консоль**

Вот консольный вывод вышеуказанного образца кода после загрузки файла [исходного Excel](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
