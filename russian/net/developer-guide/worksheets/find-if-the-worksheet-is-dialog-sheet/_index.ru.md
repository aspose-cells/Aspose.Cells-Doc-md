---
title: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 90
url: /ru/net/find-if-the-worksheet-is-dialog-sheet/
description: Диалоговый лист  это старый формат листа. В этой статье представлены инструкции и образец кода для определения программным образом, является ли лист Excel диалоговым с использованием C# API или библиотеки .NET.
keywords: обнаружить тип диалогового листа Excel c#, диалоговый лист c#
---

## **Возможные сценарии использования**

Диалоговый лист - это старый формат листа, который содержит диалоговое окно. Такой лист мог быть вставлен в старой версии Microsoft Excel, например, в 2003 году, как показано на этом скриншоте. Его также можно вставить с помощью VBA в новых версиях, например, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым листом или каким-либо другим типом листа с помощью свойства [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type), предоставленного Aspose.Cells. Если он возвращает значение перечисления [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), то это означает, что вы имеете дело с диалоговым листом.

## **Определить, является ли рабочий лист диалоговым листом**

В следующем примере кода загружается [образец файла Excel](64716820.xlsx), который содержит диалоговый лист. Он проверяет свойство [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type), сравнивает его с [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), и затем выводит сообщение. Пожалуйста, обратитесь к выводу консоли приведенного ниже примера кода для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
