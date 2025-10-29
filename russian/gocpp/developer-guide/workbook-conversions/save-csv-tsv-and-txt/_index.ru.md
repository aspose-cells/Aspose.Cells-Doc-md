---
title: Преобразование Excel в CSV, TSV и Txt с помощью Golang через C++
linktitle: Сохранить как CSV, TSV и Txt
type: docs
weight: 40
url: /ru/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Легко преобразуйте файлы Excel в форматы CSV, TSV и TXT с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет конвертировать файлы Excel, ODS, JSON и другие форматы в CSV, TSV и TXT.

{{% /alert %}}

## **Сохранение рабочей книги в текстовом или CSV формате**

Иногда вам может потребоваться конвертировать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) как Microsoft Excel, так и Aspose.Cells по умолчанию сохраняют только содержимое активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить тот же пример, чтобы сохранить ваш файл в CSV. По умолчанию [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) — запятая, поэтому не указывайте сепаратор при сохранении в формате CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **Продвинутые темы**
- [Сохранять разделители для пустых строк при экспорте таблиц в формат CSV](/cells/ru/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
