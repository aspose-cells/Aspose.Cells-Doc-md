---
title: Добавление модуля и кода VBA с использованием Aspose.Cells
type: docs
weight: 20
url: /ru/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells позволяет добавить новый модуль VBA и код макроса с помощью Aspose.Cells. Пожалуйста, используйте[**Рабочая книга.getVbaProject().getModules().добавить(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) метод добавления нового модуля VBA в книгу

{{% /alert %}}

## **Добавление модуля и кода VBA с использованием Aspose.Cells**

В следующем примере кода создается новая книга, добавляется новый модуль VBA и код макроса, а выходные данные сохраняются в формате XLSM. Один раз вы откроете выходной файл XLSM в Microsoft Excel и щелкните значок**Разработчик > Visual Basic** команд меню, вы увидите модуль с именем «TestModule», а внутри него вы увидите следующий код макроса.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Образец кода

Вот пример кода для создания выходного файла XLSM с модулем VBA и кодом макроса.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
