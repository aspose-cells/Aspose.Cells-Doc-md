---
title: Rendu de la chronologie avec C++
type: docs
weight: 40
url: /fr/cpp/rendering-timeline/
description: Gérer les chronologies des fichiers Excel avec Aspose.Cells avec C++.
keywords: Rendu de la chronologie sans Office 2013, Office 2016, Office 2019 et Office 365
---

## **Scénarios d'utilisation possibles**
Aspose.Cells prend en charge le rendu de la forme de chronologie sans utiliser Office 2013, Office 2016, Office 2019 et Office 365. Si vous convertissez votre feuille de calcul en image ou si vous enregistrez votre classeur au format PDF ou HTML, vous verrez que les chronologies sont rendues correctement.

## **Rendu de la chronologie**
Le code d'exemple suivant charge le [fichier Excel d'exemple](input.xlsx) contenant une chronologie existante. Obtenez l'objet de forme en fonction du nom de la chronologie, puis rendez-le en une image à travers la méthode Shape.ToImage(). L'image qui suit est la [image de sortie](out.png) qui montre la chronologie rendue. Comme vous pouvez le voir, la chronologie a été rendue correctement et elle ressemble à celle du fichier Excel d'exemple.

![todo:image_alt_text](out.png)
### **Code d'exemple**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
