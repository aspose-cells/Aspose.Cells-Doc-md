---
title: Управление VBA кодами книги Excel с поддержкой макросов
linktitle: Проект макросов
type: docs
weight: 200
url: /ru/nodejs-cpp/manage-vba-project/
description: Добавление модуля VBA и изменение VBA или макроса с помощью Aspose.Cells for Node.js via C++.
---

## **Добавить модуль VBA в Node.js**
{{% alert color="primary" %}}

Aspose.Cells позволяет добавлять новый модуль VBA и макрос-код с помощью Aspose.Cells for Node.js via C++. Используйте метод [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-) для добавления нового модуля VBA внутри книги.

{{% /alert %}}

Следующий пример создает новую книгу и добавляет новый модуль VBA и макрос-код, сохраняет результат в формате XLSM. После открытия файла XLSM в Microsoft Excel и выбора меню **Разработчик > Visual Basic**, вы увидите модуль с именем "TestModule" и внутри его — следующий макрос-код.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

Вот пример кода для генерации файла XLSM с модулем VBA и макросом.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **Изменение VBA или макроса в Node.js**

{{% alert color="primary" %}} 

Вы можете изменять VBA или макрос-код с помощью Aspose.Cells for Node.js via C++. Aspose.Cells добавила следующий модуль и классы для чтения и изменения VBA-проекта в файле Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Эта статья покажет вам, как изменить код VBA или макроса в исходном файле Excel с помощью Aspose.Cells.

{{% /alert %}} 

Следующий пример загружает исходный файл Excel, в котором содержится следующий VBA или макрос-код

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

После выполнения приведенного выше образца кода Aspose.Cells код VBA или макрос будет изменен таким образом.

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Вы можете загрузить [исходный файл Excel](5112508.xlsm) и [файл Excel для вывода](5112511.xlsm) по указанным ссылкам.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **Продвинутые темы**
- [Добавить ссылку на библиотеку в проект VBA в книге](/cells/ru/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Назначить макрос элементу управления формы](/cells/ru/nodejs-cpp/assign-macro-to-form-control/)
- [Проверить, действителен ли цифровая подпись кода VBA](/cells/ru/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Проверить, подписан ли код VBA](/cells/ru/nodejs-cpp/check-if-vba-code-is-signed/)
- [Проверить, подписан ли проект VBA в книге Excel](/cells/ru/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Проверить, защищен ли и заблокирован для просмотра проект VBA](/cells/ru/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу](/cells/ru/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Цифрово подписать проект кода VBA c сертификатом](/cells/ru/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Экспортировать сертификат VBA в файл или поток](/cells/ru/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Фильтрация проекта VBA при загрузке книги](/cells/ru/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [Узнать, защищен ли проект VBA](/cells/ru/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Защитить паролем проект VBA книги Excel](/cells/ru/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
