---
title: Получать предупреждения при загрузке файла Excel
type: docs
weight: 60
url: /ru/java/get-warnings-while-loading-excel-file/
---
## **Возможные сценарии использования**

Иногда пользователь пытается загрузить книгу, которая несколько повреждена, но загружается. В таком случае Aspose.Cells выдает предупреждения при загрузке книги. Вы можете поймать эти предупреждения, реализовав**[IWarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)** интерфейс и настройка**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)**имущество.

## **Получать предупреждения при загрузке файла Excel**

 В следующем примере кода объясняется, как получать предупреждения при загрузке файла Excel. Код загружает[образец эксель файла](sampleDuplicateDefinedName.xlsx) который бросает**[DuplicateDefinedName](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)** предупреждение при загрузке. Затем это предупреждение перехватывается**[IWarningCallback.Warning()](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo))** метод, выводящий предупреждающие сообщения на консоль. Затем код сохраняет книгу как[выходной файл excel](outputDuplicateDefinedName.xlsx)Если вы откроете образец файла Excel в Microsoft Excel, он также отобразит вам это предупреждение, как показано на этом снимке экрана. Пожалуйста, также проверьте консольный вывод кода, приведенного ниже, для большего понимания.

![дело:изображение_альтернативный_текст](get-warnings-while-loading-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Консольный вывод**

 Вот консольный вывод приведенного выше кода при выполнении с предоставленным[образец эксель файла](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
