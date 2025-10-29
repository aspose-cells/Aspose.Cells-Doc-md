---
title: Проверьте пароль для изменения с помощью Aspose.Cells for Python via .NET
type: docs
weight: 2400
url: /ru/python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Иногда нужно программно проверить, совпадает ли данный пароль с **Паролем для изменения**. API Aspose.Cells for Python via .NET предоставляет метод WorkbookSettings.write_protection.validate_password(), который можно использовать для проверки правильности введенного пароля для изменения.

{{% /alert %}}

## **Проверка пароля на доступ на изменение в Microsoft Excel**

Вы можете указать **Пароль на открытие** и **Пароль на доступ на изменение** при создании ваших книг в Microsoft Excel. Пожалуйста, посмотрите этот скриншот, который показывает интерфейс, предоставляемый Microsoft Excel для указания этих паролей.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Проверьте пароль для изменения с помощью Aspose.Cells for Python via .NET**

Следующие образцы кода загружают файл [исходного Excel](5112232.xlsx). В нем есть пароль для открытия - 1234 и пароль для изменения - 5678. Код сначала проверяет, является ли 567 правильным паролем для изменения, и возвращает false, а затем проверяет, является ли 5678 паролем для изменения, и возвращает true.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **Вывод в консоль**

Вот консольный вывод вышеуказанного образца кода после загрузки файла [исходного Excel](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
