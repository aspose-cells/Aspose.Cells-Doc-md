---
title: Создание общей книги с Aspose.Cells
type: docs
weight: 40
url: /ru/net/create-shared-workbook-with-aspose-cells/
---

## **Возможные сценарии использования**

Microsoft Excel позволяет вам совместно использовать книгу, как показано на следующем скриншоте. Когда вы делитесь книгой, более одного пользователя может редактировать книгу в сети. Aspose.Cells позволяет создать общую книгу с помощью свойства [**Workbook.Settings.Shared**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/shared).

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)

## **Создание общей книги с Aspose.Cells**

В следующем примере кода создается общая книга, устанавливая свойство [**Workbook.Settings.Shared**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/shared) как **true**. Когда вы откроете [выходной файл Excel](55541786.xlsx) в Microsoft Excel, вы увидите **Shared** с именем выходной книги, как показано на этом скриншоте.

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-CreateSharedWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
