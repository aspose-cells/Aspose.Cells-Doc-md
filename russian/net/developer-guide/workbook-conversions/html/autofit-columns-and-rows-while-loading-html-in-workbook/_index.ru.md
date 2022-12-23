---
title: Автоподбор столбцов и строк при загрузке HTML в книгу
type: docs
weight: 120
url: /ru/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Возможные сценарии использования**

Вы можете автоматически подогнать столбцы и строки при загрузке файла HTML внутри объекта Workbook. Пожалуйста, установите**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** собственность на**истинный**для этой цели.

## **Автоподбор столбцов и строк при загрузке HTML в книгу**

 Следующий пример кода сначала загружает образец HTML в книгу без каких-либо параметров загрузки и сохраняет его в формате XLSX. Затем он снова загружает образец HTML в Workbook, но на этот раз он загружает HTML после установки**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** собственность на**истинный**и сохраняет его в формате XLSX. Загрузите оба выходных файла Excel, т.е.[Выходной файл Excel без AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) и[Выходной файл Excel с AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . На следующем снимке экрана показан эффект**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**в обоих выходных файлах Excel.

![дело:изображение_альтернативный_текст](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

