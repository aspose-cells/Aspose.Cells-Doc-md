---
title: Реализовать пользовательский размер бумаги рабочего листа для рендеринга
type: docs
weight: 70
url: /ru/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: В этой статье объясняется, как использовать пример кода библиотеки C# API или .NET, чтобы установить пользовательский размер бумаги для желаемых рабочих листов при программном преобразовании файла Excel в формат файла PDF.
keywords: set custom paper size while rendering excel to pdf c#
---
##  **Возможные сценарии использования**

В MS Excel нет прямого варианта создания нестандартных размеров бумаги, однако вы можете установить нестандартный размер бумаги для желаемых рабочих листов при преобразовании файла Excel в формат файла PDF. В этом документе объясняется, как установить пользовательский размер бумаги для рабочего листа с помощью API-интерфейсов Aspose.Cells.

##  **Реализовать пользовательский размер бумаги рабочего листа для рендеринга**

 Aspose.Cells позволяет реализовать желаемый размер бумаги рабочего листа. Вы можете использовать[**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) метод[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) класс, чтобы указать пользовательский размер страницы. В следующем примере кода показано, как указать нестандартный размер бумаги для первого рабочего листа в книге. См. также[вывод PDF](45056028.pdf)генерируется со следующим кодом для справки.

##  **Скриншот**

![дело:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
