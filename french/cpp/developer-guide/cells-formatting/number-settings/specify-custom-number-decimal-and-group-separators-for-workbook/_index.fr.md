---
title: Spécifiez les séparateurs décimaux et de groupe personnalisés pour le classeur avec C++
linktitle: Spécifiez les séparateurs décimaux et de groupe personnalisés
type: docs
weight: 110
url: /fr/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Modifier le séparateur décimal et de groupe dans MS Excel avec du code C++ en utilisant l API Aspose.Cells for C++.
keywords: spécifier séparateur décimal personnalisé excel, spécifier séparateur décimal personnalisé excel c++, spécifier séparateur de groupe personnalisé excel, spécifier séparateur de groupe personnalisé excel c++, spécifier séparateur décimal et de groupe personnalisé excel, spécifier séparateur décimal et de groupe personnalisé excel c++, changer le séparateur décimal et de groupe dans excel, changer le séparateur décimal dans excel, changer le séparateur de groupe dans excel c++, changer le séparateur de groupe dans excel c++
---

{{% alert color="primary" %}}

Dans Microsoft Excel, vous pouvez spécifier les séparateurs décimaux et de milliers personnalisés au lieu d'utiliser les Séparateurs Système à partir des **Options Excel Avancées** comme indiqué dans la capture d'écran ci-dessous.

Aspose.Cells fournit les propriétés [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) et [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) pour définir les séparateurs personnalisés pour le formatage/analyse des nombres.

{{% /alert %}}

## **Spécification des séparateurs personnalisés à l'aide de Microsoft Excel**

La capture d'écran suivante montre les **Options Excel Avancées** et met en évidence la section pour spécifier les **Séparateurs Personnalisés**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Spécification des séparateurs personnalisés à l'aide de Aspose.Cells**

Le code d'exemple suivant illustre comment spécifier les séparateurs personnalisés à l'aide de l'API Aspose.Cells. Il spécifie les séparateurs de décimales et de groupes numériques personnalisés comme point et espace respectivement.

### Code C++ pour spécifier les séparateurs décimaux et de groupe personnalisés

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
