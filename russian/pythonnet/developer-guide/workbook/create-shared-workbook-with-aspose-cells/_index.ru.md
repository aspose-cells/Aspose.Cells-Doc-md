---
title: Создание общей книги с Aspose.Cells
type: docs
weight: 40
url: /ru/python-net/create-shared-workbook-with-aspose-cells/
---

## **Возможные сценарии использования**

Microsoft Excel позволяет делиться рабочей книгой, как показано на следующем снимке экрана. Когда вы делитесь рабочей книгой, несколько пользователей могут одновременно редактировать её по сети. Aspose.Cells для Python via .NET позволяет создать совместно используемую рабочую книгу с помощью свойства [**Workbook.settings.shared**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/shared).

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)

## **Создать совместно используемую рабочую книгу с Aspose.Cells для Python via .NET**

В следующем примере кода создается общая книга, устанавливая свойство [**Workbook.settings.shared**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/shared) как **true**. Когда вы откроете [выходной файл Excel](55541786.xlsx) в Microsoft Excel, вы увидите **Shared** с именем выходной книги, как показано на этом скриншоте.

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CreateSharedWorkbook.py" >}}

