---
title: Проверить пароль зашифрованных файлов
type: docs
weight: 10
url: /ru/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: Проверьте пароль зашифрованных файлов Excel (xlsx, xlsb, xls, xlsm) и OpenOffice (ODS) с использованием кодов CShape.
---

{{% alert color="primary" %}}
Если файлы Excel (xlsx, xlsb, xls, xlsm) и OpenOffice (ODS) защищены паролем, Aspose поддерживает простую проверку пароля без разбора конкретных данных файлов.
{{% /alert %}}

## **Проверьте пароль зашифрованного файла**

Для проверки пароля зашифрованного файла Aspose.Cells for Python via .NET предоставляет метод [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Эти методы принимают два параметра: файловый поток и пароль, который нужно проверить.
Следующий фрагмент кода демонстрирует использование метода [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) для проверки, является ли предоставленный пароль допустимым или нет.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


