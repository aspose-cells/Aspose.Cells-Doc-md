---
title: Проверить пароль зашифрованных файлов
type: docs
weight: 10
url: /ru/net/verify-password-of-encrypted-excel-and-ods-files/
description: Проверьте пароль зашифрованных файлов Excel (xlsx, xlsb, xls, xlsm) и OpenOffice (ODS) с использованием кодов CShape.
---

{{% alert color="primary" %}}
Если файлы Excel (xlsx, xlsb, xls, xlsm) и OpenOffice (ODS) защищены паролем, Aspose поддерживает простую проверку пароля без разбора конкретных данных файлов.
{{% /alert %}}

## **Проверьте пароль зашифрованного файла**

Чтобы проверить пароль зашифрованного файла, Aspose.Cells for .NET предоставляет метод [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Эти методы принимают два параметра: поток файла и пароль, который нужно проверить.
Следующий фрагмент кода демонстрирует использование метода [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) для проверки, является ли предоставленный пароль допустимым или нет.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
