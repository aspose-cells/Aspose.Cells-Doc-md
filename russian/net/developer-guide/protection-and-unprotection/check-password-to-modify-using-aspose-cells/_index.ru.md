---
title: Проверьте пароль для изменения, используя Aspose.Cells
type: docs
weight: 2400
url: /ru/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Иногда вам нужно проверить, совпадает ли данный пароль с**Пароль для изменения** программно. Aspose.Cells предоставляет метод WorkbookSettings.WriteProtection.ValidatePassword(), который вы можете использовать для проверки правильности данного пароля для изменения.

{{% /alert %}}

## **Проверьте пароль для изменения в Microsoft Excel**

 Вы можете назначить**Пароль для открытия** и**Пароль для изменения** при создании книг в Microsoft Excel. Посмотрите этот снимок экрана, на котором показан интерфейс Microsoft, который Excel предоставляет для указания этих паролей.

|![дело:изображение_альтернативный_текст](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Проверьте пароль для изменения, используя Aspose.Cells**

 Следующие примеры кодов загружают[исходный файл Excel](5112232.xlsx) файл. У него есть пароль для открытия как 1234 и пароль для изменения как 5678. Код сначала проверяет, является ли 567 правильным паролем для изменения, и возвращает false, а затем проверяет, является ли 5678 паролем для изменения, и возвращает true.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Консольный вывод**

 Вот консольный вывод приведенного выше примера кода после загрузки[исходный файл Excel](5112232.xlsx) файл.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
