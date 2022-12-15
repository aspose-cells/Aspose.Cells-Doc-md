---
title: Подтвердите пароль зашифрованных файлов
type: docs
weight: 10
url: /ru/java/verify-password-of-encrypted-excel-and-ods-files/
description: Проверьте пароль зашифрованных файлов Excel (xlsx, xlsb, xls, xlsm) и Open Office (ODS), используя коды Java.
---
{{% alert color="primary" %}}
Если файлы Excel (xlsx, xlsb, xls, xlsm) и Open office (ODS) заблокированы паролем, Aspose.Cells for Java поддерживает простую проверку пароля без анализа конкретных данных файлов.
{{% /alert %}}

## **Проверьте пароль зашифрованного файла**

 Чтобы проверить пароль зашифрованного файла, Aspose.Cells for Java предоставляет[**Подтвердите пароль**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) метод. Методы принимают два параметра: файловый поток и пароль, который необходимо проверить.
 Следующий фрагмент кода демонстрирует использование[**Подтвердите пароль**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) для проверки правильности предоставленного пароля.

### **Образец кода:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

