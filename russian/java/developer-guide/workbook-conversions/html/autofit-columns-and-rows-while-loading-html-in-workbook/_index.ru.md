---
title: Автоматическое подгонка столбцов и строк при загрузке HTML в Рабочей книге
type: docs
weight: 70
url: /ru/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Возможные сценарии использования**

Вы можете автоматически подогнать столбцы и строки при загрузке вашего HTML-файла в объект [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Пожалуйста, установите свойство [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) в **true** для этой цели.

## **Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге**

Приведенный ниже примерный код сначала загружает образец HTML-файла в Книгу без каких-либо параметров загрузки и сохраняет его в формате XLSX. Затем он снова загружает образец HTML в Книгу, но на этот раз загружает HTML после установки свойства [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) в **true** и сохраняет его в формате XLSX. Пожалуйста, загрузите оба файла Excel-отправления, т. е. [Выходной файл Excel без подгонки столбцов и строк](outputWithout_AutoFitColsAndRows.xlsx) и [Выходной файл Excel с подгонкой столбцов и строк](outputWith_AutoFitColsAndRows.xlsx). Ниже приведен скриншот, показывающий эффект свойства [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) на обоих файлах Excel-отправления.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
{{< app/cells/assistant language="java" >}}
