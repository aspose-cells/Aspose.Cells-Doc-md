---
title: Получать предупреждения при загрузке файла Excel
type: docs
weight: 110
url: /ru/net/get-warnings-while-loading-excel-file/
---

## **Возможные сценарии использования**

Иногда пользователь пытается загрузить книгу, которая отчасти повреждена, но загружаема. В таком случае Aspose.Cells выдает предупреждения при загрузке рабочей книги. Можно перехватить эти предупреждения, реализовав интерфейс [**IWarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback) и установив свойство [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback).

## **Получение предупреждений при загрузке файла Excel**

Приведенный ниже образец кода объясняет, как получить предупреждения при загрузке файла Excel. Код загружает [образец файла Excel](sampleDuplicateDefinedName.xlsx), который выдает предупреждение [**DuplicateDefinedName**](https://reference.aspose.com/cells/net/aspose.cells/warningtype) при загрузке. Это предупреждение затем перехватывается методом [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning), который выводит сообщения предупреждения в консоль. Затем код сохраняет книгу в виде [выходного файла Excel](outputDuplicateDefinedName.xlsx). Если вы откроете образец файла Excel в Microsoft Excel, он также отобразит вам это предупреждение, как показано на этом скриншоте. Пожалуйста, также проверьте вывод консоли кода ниже для более полного понимания.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Вывод в консоль**

Ниже приведен вывод консольного вывода вышеуказанного кода при выполнении с предоставленным [образцом файла Excel](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
