---
title: Реализация пользовательского размера бумаги для рендеринга листа
type: docs
weight: 70
url: /ru/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: В этой статье объясняется, как использовать образец кода на C# API или .NET Library для установки пользовательского размера бумаги ваших желаемых листов при конвертации файла Excel в файл PDF программным образом.
keywords: установить пользовательский размер бумаги при конвертации Excel в PDF на C#
---

## **Возможные сценарии использования**

Прямой опции для создания пользовательских размеров бумаги в MS Excel нет, однако вы можете установить пользоватский размер бумаги для нужных ваших листов при конвертации файла Excel в файл PDF. В этом документе объясняется, как установить пользовательский размер бумаги листа с использованием Aspose.Cells APIs.

## **Настройка пользовательского размера бумаги для отображения на листе**

Aspose.Cells позволяет вам реализовать желаемый размер бумаги листа. Вы можете использовать метод [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) для указания пользоватского размера страницы. Следующий образец кода иллюстрирует, как указать пользоватский размер бумаги для первого листа в книге. Пожалуйста, также обратите внимание на [сгенерированный файл PDF](45056028.pdf) с использованием следующего кода для справки.

## **Снимок экрана**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
{{< app/cells/assistant language="csharp" >}}
