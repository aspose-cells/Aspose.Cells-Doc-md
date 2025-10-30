---
title: Implementera Anpassad Papperstorlek på Arbetsbladet för Rendering
type: docs
weight: 70
url: /sv/python-net/implement-custom-paper-size-of-worksheet-for-rendering/
description: Denna artikel förklarar hur man använder exempel kod för Aspose.Cells för Python via .NET för att ställa in anpassad pappersstorlek för dina önskade arbetsblad när du renderar Excel filen till PDF format programmässigt.
keywords: Python Excel bibliotek, Python ställa in anpassad pappersstorlek när du renderar Excel till PDF, Implementera anpassad pappersstorlek för arbetsblad vid rendering i Python.
---

## **Möjliga användningsscenario**

Det finns inget direkt alternativ för att skapa anpassade pappersstorlekar i MS Excel, men du kan ställa in anpassad pappersstorlek för dina önskade arbetsblad när du konverterar Excel till PDF. Denna dokument förklarar hur man ställer in en anpassad pappersstorlek för ett arbetsblad med Aspose.Cells för Python via .NET API:er.

## **Implementera anpassad pappersstorlek för arbetsblad för rendering**

Aspose.Cells för Python via .NET tillåter dig att implementera önskad pappersstorlek för arbetsbladet. Du kan använda [**custom_paper_size**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/custom_paper_size/#float-float)-metoden i [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen för att ange en anpassad sidstorlek. Följande exempel visar hur man specificerar en anpassad pappersstorlek för det första arbetsbladet i arbetsboken. Se även den [utgångs-PDF](45056028.pdf) som genererats med denna kod för referens.

## **Skärmdump**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.py" >}}
{{< app/cells/assistant language="python-net" >}}
