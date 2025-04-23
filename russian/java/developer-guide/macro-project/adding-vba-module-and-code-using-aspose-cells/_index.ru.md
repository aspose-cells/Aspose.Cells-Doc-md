---
title: Добавление VBA модуля и кода с использованием Aspose.Cells
type: docs
weight: 20
url: /ru/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет добавлять новый модуль VBA и макросы с помощью Aspose.Cells. Пожалуйста, используйте [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add-com.aspose.cells.Worksheet-) для добавления нового модуля VBA внутри рабочей книги

{{% /alert %}}

## **Добавление VBA-модуля и кода с использованием Aspose.Cells**

В следующем образце кода создается новая книга и добавляется новый модуль VBA и код макроса, и сохраняется в формате XLSM. Когда вы откроете файл XLSM в Microsoft Excel и нажмете команды **Разработчик > Визуальный Basic**, вы увидите модуль под названием "TestModule" и внутри него будет следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Образец кода

Вот пример кода для создания файла XLSM с VBA-модулем и макросным кодом.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
{{< app/cells/assistant language="java" >}}
