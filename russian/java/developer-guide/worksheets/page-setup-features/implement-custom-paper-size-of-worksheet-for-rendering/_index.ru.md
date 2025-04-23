---
title: Реализация пользовательского размера бумаги для рендеринга листа
type: docs
weight: 30
url: /ru/java/implement-custom-paper-size-of-worksheet-for-rendering/
---

## **Возможные сценарии использования**

Нет прямой опции для создания настраиваемых размеров бумаги в MS Excel, однако вы можете задать настраиваемый размер бумаги для нужных листов при отображении файла Excel в формате PDF. В этом документе объясняется, как задать настраиваемый размер бумаги листа с помощью API Aspose.Cells.

## **Настройка пользовательского размера бумаги для отображения на листе**

Aspose.Cells позволяет реализовать необходимый пользовательский размер бумаги для листа с помощью метода [**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize-double-double-) объекта [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup). Нижеприведенный образец кода показывает, как указать пользовательский формат бумаги для первого листа в книге. Пожалуйста, также ознакомьтесь с [выходным PDF](45056030.pdf), сгенерированным при помощи приведенного ниже кода, в качестве справки.

## **Снимок экрана**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
{{< app/cells/assistant language="java" >}}
