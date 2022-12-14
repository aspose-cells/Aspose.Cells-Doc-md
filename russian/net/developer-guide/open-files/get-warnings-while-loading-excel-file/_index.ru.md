---
title: Получать предупреждения при загрузке файла Excel
type: docs
weight: 110
url: /ru/net/get-warnings-while-loading-excel-file/
---
## **Возможные сценарии использования**

Иногда пользователь пытается загрузить книгу, которая несколько повреждена, но загружается. В таком случае Aspose.Cells выдает предупреждения при загрузке книги. Вы можете поймать эти предупреждения, реализовав**[IWarningCallback](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)** интерфейс и настройка**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**имущество.

## **Получать предупреждения при загрузке файла Excel**

 В следующем примере кода объясняется, как получать предупреждения при загрузке файла Excel. Код загружает[образец эксель файла](sampleDuplicateDefinedName.xlsx) который бросает**[DuplicateDefinedName] (https://reference.aspose.com/cells/net/aspose.cells/warningtype)** предупреждение при загрузке. Затем это предупреждение перехватывается**[IWarningCallback.Warning()](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)** метод, выводящий предупреждающие сообщения на консоль. Затем код сохраняет книгу как[выходной файл excel](outputDuplicateDefinedName.xlsx)Если вы откроете образец файла Excel в Microsoft Excel, он также отобразит вам это предупреждение, как показано на этом снимке экрана. Пожалуйста, также проверьте консольный вывод кода, приведенного ниже, для большего понимания.

![дело:изображение_альтернативный_текст](get-warnings-while-loading-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Консольный вывод**

 Вот консольный вывод приведенного выше кода при выполнении с предоставленным[образец эксель файла](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
