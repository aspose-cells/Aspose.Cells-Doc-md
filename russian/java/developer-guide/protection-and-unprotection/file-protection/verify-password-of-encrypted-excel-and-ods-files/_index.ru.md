---
title: Проверить пароль зашифрованных файлов
type: docs
weight: 10
url: /ru/java/verify-password-of-encrypted-excel-and-ods-files/
description: Проверьте пароль зашифрованного Excel (xlsx, xlsb, xls, xlsm) и файлов Open office (ODS) с помощью Java кода.
---

{{% alert color="primary" %}}
Если файлы Excel (xlsx, xlsb, xls, xlsm) и файлы Open office (ODS) заблокированы паролем, Aspose.Cells for Java поддерживает простую проверку пароля без анализа конкретных данных файлов.
{{% /alert %}}

## **Проверьте пароль зашифрованного файла**

Для проверки пароля зашифрованного файла Aspose.Cells for Java предоставляет метод [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-). Метод принимает два параметра: поток файла и пароль, который необходимо проверить.
Следующий фрагмент кода демонстрирует использование метода [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) для проверки, является ли предоставленный пароль допустимым или нет.

### **Образец кода:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

{{< app/cells/assistant language="java" >}}
