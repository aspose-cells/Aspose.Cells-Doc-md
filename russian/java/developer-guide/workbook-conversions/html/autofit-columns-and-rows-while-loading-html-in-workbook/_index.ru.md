---
title: Автоподбор столбцов и строк при загрузке HTML в книгу
type: docs
weight: 70
url: /ru/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Возможные сценарии использования**

 Вы можете автоматически подогнать столбцы и строки при загрузке HTML-файла внутри**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** объект. Пожалуйста, установите**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** собственность на**истинный**для этой цели.

## **Автоподбор столбцов и строк при загрузке HTML в книгу**

 Следующий пример кода сначала загружает образец HTML в Workbook без каких-либо параметров загрузки и сохраняет его в формате XLSX. Затем он снова загружает образец HTML в Workbook, но на этот раз он загружает HTML после установки**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** собственность на**истинный**и сохраняет его в формате XLSX. Загрузите оба выходных файла Excel, т.е.[Выходной файл Excel без AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) а также[Выходной файл Excel с AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . На следующем снимке экрана показан эффект**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)**в обоих выходных файлах Excel.

![дело:изображение_альтернативный_текст](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
