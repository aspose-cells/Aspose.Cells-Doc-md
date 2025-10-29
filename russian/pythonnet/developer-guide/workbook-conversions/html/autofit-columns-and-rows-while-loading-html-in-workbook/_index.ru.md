---
title: Автоматическое подгонка столбцов и строк при загрузке HTML в Рабочей книге
type: docs
weight: 120
url: /ru/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Эта тема показывает, как автоматически подстроить столбцы и строки при загрузке HTML в книгу с помощью Aspose.Cells для Python via NET.
keywords: Автоматическая подгонка столбцов и строк при загрузке HTML в книгу, автоматическая подгонка столбцов и строк для загрузки HTML.
---

## **Возможные сценарии использования**

Вы можете автоматически подобрать ширину столбцов и строк при загрузке вашего HTML-файла в объект рабочей книги. Установите свойство [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) в **true** для этой цели.

## **Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге**

Приведенный ниже образец кода сначала загружает образец HTML в рабочую книгу без каких-либо параметров загрузки и сохраняет его в формате XLSX. Затем снова загружает образец HTML в рабочую книгу, но на этот раз загружает HTML после установки свойства [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) в **true** и сохраняет его в формате XLSX. Пожалуйста, скачайте оба выходных файла Excel, т.е. [Выходной файл Excel без автоподгонки столбцов и строк](outputWithout_AutoFitColsAndRows.xlsx) и [Выходной файл Excel с автоподгонкой столбцов и строк](outputWith_AutoFitColsAndRows.xlsx). На следующем снимке экрана показан эффект свойства [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) на оба выходных файла Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
