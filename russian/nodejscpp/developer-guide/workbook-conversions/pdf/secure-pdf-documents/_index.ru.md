---
title: Обеспечение безопасности PDF документов с помощью Node.js через C++
linktitle: Защищенные PDF документы
type: docs
weight: 120
url: /ru/nodejs-cpp/secure-pdf-documents/
description: Научитесь защищать PDF документы, используя пароли владельца и пользователя, а также устанавливать разрешения для файлов PDF с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Иногда разработчикам приходится работать с зашифрованными PDF-файлами. Например:

- Защитите документы паролями владельца и пользователя, чтобы открыть его могли не все.
- Установите ограничения или разрешения для документа после его открытия. например, ограничьте, можно ли печатать или извлекать содержимое документа.

Эта статья объясняет, как передавать параметры безопасности PDF при сохранении электронных таблиц в PDF.

{{% /alert %}}

Aspose.Cells предоставляет [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) для работы с безопасностью. Вы можете установить пароли владельца и пользователя при сохранении в PDF. Пароль владельца или пользователя потребуется для открытия зашифрованного PDF-документа для просмотра.

- Пароль пользователя может быть равен null или пустой строке; в этом случае пользователю не потребуется пароль при открытии PDF-документа.
- Открытие PDF-документа с правильным паролем владельца обеспечивает полный доступ (без указанных ограничений доступа) к документу.
- Открытие PDF-документа с правильным паролем пользователя (или открытие документа без пароля пользователя) дает ограниченный доступ в соответствии с установленными разрешениями.

Приведенный ниже пример кода описывает, как защищать PDF с помощью Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

Если электронная таблица содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием ее в PDF. Это гарантирует, что значения, зависящие от формул, пересчитываются верно и отображаются правильные значения в PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
