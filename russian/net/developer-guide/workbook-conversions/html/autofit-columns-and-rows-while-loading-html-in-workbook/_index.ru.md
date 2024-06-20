---
title: Автоматическое подгонка столбцов и строк при загрузке HTML в Рабочей книге
type: docs
weight: 120
url: /ru/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Возможные сценарии использования**

Вы можете автоматически подобрать ширину столбцов и строк при загрузке вашего HTML-файла в объект рабочей книги. Установите свойство [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) в **true** для этой цели.

## **Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге**

Приведенный ниже образец кода сначала загружает образец HTML в рабочую книгу без каких-либо параметров загрузки и сохраняет его в формате XLSX. Затем снова загружает образец HTML в рабочую книгу, но на этот раз загружает HTML после установки свойства [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) в **true** и сохраняет его в формате XLSX. Пожалуйста, скачайте оба выходных файла Excel, т.е. [Выходной файл Excel без автоподгонки столбцов и строк](outputWithout_AutoFitColsAndRows.xlsx) и [Выходной файл Excel с автоподгонкой столбцов и строк](outputWith_AutoFitColsAndRows.xlsx). На следующем снимке экрана показан эффект свойства [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) на оба выходных файла Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

