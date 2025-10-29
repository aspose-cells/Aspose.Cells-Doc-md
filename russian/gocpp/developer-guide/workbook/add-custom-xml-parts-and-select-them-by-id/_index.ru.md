---
title: Добавление пользовательских XML частей и их выбор по ID с помощью Golang через C++
linktitle: Добавление пользовательских XML частей и выбор их по идентификатору
type: docs
weight: 70
url: /ru/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Узнайте, как добавлять и выбирать пользовательские XML части в файлах Excel с помощью Aspose.Cells и Golang через C++
---

## **Возможные сценарии использования**

Пользовательские XML-части — это XML-данные, хранящиеся внутри документов Microsoft Excel и используемые приложениями, взаимодействующими с ними. В настоящее время нет прямого способа добавления их через пользовательский интерфейс Microsoft Excel. Однако их можно добавлять программным способом различными способами, например, с помощью VSTO или Aspose.Cells. Используйте метод [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) для добавления пользовательской XML-части с помощью API Aspose.Cells. Также можно установить её ID с помощью свойства [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Аналогично, если вы хотите выбрать пользовательскую XML-часть по ID, используйте метод [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Добавление пользовательских XML-частей и выбор их по идентификатору**

Следующий пример кода сначала добавляет четыре пользовательские XML-части с помощью метода [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/). Затем он устанавливает их ID с помощью свойства [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). В конце он находит или выбирает одну из добавленных пользовательских XML-частей с помощью метода [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Также для справки приводится вывод кода в консоли ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Вывод в консоль**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
