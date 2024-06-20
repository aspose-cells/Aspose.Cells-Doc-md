---
title: Получать предупреждения при загрузке файла Excel
type: docs
weight: 60
url: /ru/java/get-warnings-while-loading-excel-file/
---

## **Возможные сценарии использования**

Иногда пользователь пытается загрузить книгу, которая отчасти повреждена, но загружаема. В таком случае Aspose.Cells выдает предупреждения при загрузке рабочей книги. Можно перехватить эти предупреждения, реализовав интерфейс [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) и установив свойство [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback).

## **Получение предупреждений при загрузке файла Excel**

Приведенный ниже образец кода объясняет, как получить предупреждения при загрузке файла Excel. Код загружает [образец файла Excel](sampleDuplicateDefinedName.xlsx), который выдает предупреждение [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME) при загрузке. Это предупреждение затем перехватывается методом [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo)), который выводит сообщения предупреждения в консоль. Затем код сохраняет книгу в виде [выходного файла Excel](outputDuplicateDefinedName.xlsx). Если вы откроете образец файла Excel в Microsoft Excel, он также отобразит вам это предупреждение, как показано на этом скриншоте. Пожалуйста, также проверьте вывод консоли кода ниже для более полного понимания.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Вывод в консоль**

Ниже приведен вывод консольного вывода вышеуказанного кода при выполнении с предоставленным [образцом файла Excel](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
