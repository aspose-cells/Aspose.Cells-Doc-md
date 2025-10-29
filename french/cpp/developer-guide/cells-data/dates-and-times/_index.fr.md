---
title: Comment gérer les dates et les heures avec C++
linktitle: Comment gérer les dates et heures
type: docs
weight: 600
url: /fr/cpp/how-to-manage-dates-and-times/
description: Apprenez comment gérer les dates et heures via l’API Aspose.Cells for C++.
keywords: Comment gérer les dates et heures, le système de date 1900, le système de date 1904, définir les dates et heures, obtenir les dates et heures, gérer les dates et heures, stocker les dates et heures dans Excel, afficher les dates et heures dans les cellules.
---

## **Comment stocker les dates et heures dans Excel**
Les dates et heures sont stockées dans les cellules sous forme de nombres. Ainsi, les valeurs des cellules contenant des dates et heures sont du type numérique. Un nombre qui spécifie une date et une heure se compose des composants de la date (partie entière) et de l’heure (partie fractionnaire). La méthode `Cell::GetDoubleValue()` retourne ce nombre.

## **Comment afficher les dates et heures dans Aspose.Cells**
Pour afficher un nombre comme une date et une heure, appliquez le format de date et d’heure requis à une cellule via la méthode `Style::SetNumber()` ou `Style::SetCustom()`. La méthode `Cell::GetDateTimeValue()` retourne l’objet `DateTime`, qui indique la date et l’heure représentées par le nombre contenu dans la cellule.
<br>
<image src="1.png" width="70%" />

## **Comment passer de deux systèmes de dates dans Aspose.Cells**
MS-Excel stocke les dates sous forme de nombres appelés valeurs sérielles. Une valeur sérielle est un entier qui représente le nombre de jours écoulés depuis le premier jour du système de date. Excel prend en charge les systèmes de date suivants pour les valeurs sérielles:

1. Le système de date 1900. La première date est le 1er janvier 1900, et sa valeur sérielle est 1. La dernière date est le 31 décembre 9999, et sa valeur sérielle est 2 958 465. Ce système de date est utilisé par défaut dans le classeur.
1. Le système de dates 1904. La première date est le 1er janvier 1904, sa valeur sériale est 0. La dernière date est le 31 décembre 9999, et sa valeur sériale est 2 957 003. Pour utiliser ce système de dates dans le classeur, définissez la propriété `Workbook::GetSettings()->SetDate1904(true)`.

Cet exemple montre que les valeurs sérielles stockées à la même date dans différents systèmes de dates sont différentes.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
Résultat de la sortie :
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Comment définir la valeur DateTime dans Aspose.Cells**
Cet exemple définit une valeur `DateTime` dans les cellules A1 et A2, définit un format personnalisé pour A1 et un format numérique pour A2, puis affiche les types de valeur.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Résultat de la sortie :
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Comment obtenir la valeur DateTime dans Aspose.Cells**
Cet exemple définit une valeur `DateTime` dans les cellules A1 et A2, définit un format personnalisé pour A1 et un format numérique pour A2, vérifie les types de valeur des deux cellules, puis affiche la valeur `DateTime` et la chaîne formatée.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Résultat de la sortie :
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
{{< app/cells/assistant language="cpp" >}}
