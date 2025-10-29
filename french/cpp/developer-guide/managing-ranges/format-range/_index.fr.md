---
title: Mise en forme des plages avec C++
linktitle: Formater les plages
type: docs
weight: 105
url: /fr/cpp/how-to-format-a-range/
description: Apprenez comment formater des plages dans Excel en utilisant Aspose.Cells avec C++. Appliquez des styles, des polices et des couleurs aux plages de cellules de manière programmatique.
---

## **Scénarios d'utilisation possibles**
Lorsque vous devez appliquer un style à une plage, vous pouvez utiliser le formatage des plages.

## **Comment formater une plage dans Excel**

Pour formater une plage de cellules dans Excel, vous pouvez utiliser les options de formatage intégrées fournies par Excel. Voici comment vous pouvez formater une plage de cellules directement dans Excel:

1. Ouvrez Excel et ouvrez le classeur qui contient la plage que vous souhaitez formater.

2. Sélectionnez la plage de cellules que vous souhaitez formater. Vous pouvez cliquer et faire glisser pour sélectionner la plage, ou vous pouvez utiliser des raccourcis clavier comme Maj + touches de direction pour étendre la sélection.

3. Une fois la plage sélectionnée, faites un clic droit sur la plage sélectionnée et choisissez "Format de cellule" dans le menu contextuel. Alternativement, vous pouvez aller dans l'onglet Accueil dans le ruban Excel, cliquer sur la liste déroulante "Format" dans le groupe "Cellules", et sélectionner "Format de cellule".

4. La boîte de dialogue "Format de cellule" apparaîtra. Ici, vous pouvez choisir différentes options de formatage à appliquer à la plage sélectionnée. Par exemple, vous pouvez changer le style de police, la taille de police, la couleur de police, le format de nombre, les bordures, la couleur de fond, etc. Explorez les différents onglets de la boîte de dialogue pour accéder à diverses options de formatage.

5. Après avoir apporté les modifications de formatage souhaitées, cliquez sur le bouton "OK" pour appliquer le formatage à la plage sélectionnée.

## **Comment formater une plage en utilisant C++**

Pour formater une plage en utilisant Aspose.Cells, vous pouvez utiliser les méthodes suivantes :
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **Code d'exemple**
Dans cet exemple, nous créons un classeur Excel, ajoutons des données d'exemple, accédons à la première feuille de calcul, et définissons deux plages (« A1:C3 » et « A4:C5 »). Ensuite, nous créons de nouveaux styles, définissons diverses options de mise en forme (par exemple, couleur de police, Gras), et appliquons le style à la plage. Enfin, nous enregistrons le classeur dans un nouveau fichier.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
