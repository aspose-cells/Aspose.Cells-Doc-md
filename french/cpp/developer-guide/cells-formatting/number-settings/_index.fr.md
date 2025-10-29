---
title: Paramètres de nombre avec C++
linktitle: Paramètres de nombre
description: Aspose.Cells est une bibliothèque C++ pour le travail avec des fichiers de tableur qui supporte de nombreux réglages de nombres dans les cellules. Cet article montre comment utiliser la bibliothèque Aspose.Cells pour gérer les paramètres de nombre des cellules afin que les utilisateurs puissent ajuster le format numérique selon leurs besoins.
keywords: Aspose.Cells, bibliothèque C++, tableur électronique, paramètres de nombre des cellules, mise en forme, gestion, formats de nombres et dates
type: docs
weight: 10
url: /fr/cpp/cells-number-settings/
---

## **Comment définir les formats d'affichage des nombres et des dates**

Une fonctionnalité très forte d'Excel de Microsoft est qu'elle permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que des données numériques peuvent être utilisées pour représenter différentes valeurs, y compris des valeurs décimales, monétaires, en pourcentage, en fraction ou en comptabilité, etc. Toutes ces valeurs numériques sont affichées sous différents formats en fonction du type d'informations qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peuvent être affichées.
Aspose.Cells prend en charge cette fonctionnalité et permet aux développeurs de définir tout format d'affichage pour un nombre ou une date.

### **Comment définir les formats d'affichage dans Microsoft Excel**

Pour définir les formats d'affichage dans Microsoft Excel:

1. Cliquez avec le bouton droit sur n'importe quelle cellule.
1. Sélectionnez **Format des cellules**. Une boîte de dialogue s'affichera qui est utilisée pour définir les formats d'affichage de n'importe quel type de valeur.

À gauche de la boîte de dialogue, il y a de nombreuses catégories de valeurs comme **Général**, **Nombre**, **Monétaire**, **Comptabilité**, **Date**, **Heure**, **Pourcentage**, etc. Aspose.Cells prend en charge tous ces formats d'affichage.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fournit des méthodes [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) et [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) pour la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Ces méthodes sont utilisées pour obtenir et définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fournit quelques propriétés utiles pour traiter les formats d'affichage des nombres et des dates.

### **Comment Utiliser les Formats de Nombre Intégrés**

Aspose.Cells propose quelques formats de nombre intégrés pour configurer les formats d'affichage des nombres et des dates. Ces formats de nombre intégrés peuvent être appliqués en utilisant la propriété [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Tous les formats de nombre intégrés ont des valeurs numériques uniques. Les développeurs peuvent attribuer n'importe quelle valeur numérique souhaitée à la propriété [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) pour appliquer le format d'affichage. Cette approche est rapide. Les formats de nombre intégrés pris en charge par Aspose.Cells sont énumérés ci-dessous.

|**Valeur**|**Type**|**Chaîne de format**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::time_t now = std::time(nullptr);
    double excelDate = static_cast<double>(now) / 86400.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetNumber(15);
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetNumber(9);
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetNumber(6);
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment Utiliser les Formats de Nombre Personnalisés**

Pour définir votre propre chaîne de format personnalisée pour définir le format d'affichage, utilisez la propriété [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) de l'objet [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Cette approche n'est pas aussi rapide que l'utilisation de formats prédéfinis, mais elle est plus flexible.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    auto hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    double excelDate = hours / 24.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetCustom(u"d-mmm-yy");
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetCustom(u"0.0%");
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetCustom(u"£#,##0;[Red]$-#,##0");
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si vous utilisez la propriété [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) pour définir le format de nombre, tout format précédemment défini en utilisant la propriété [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) est remplacé et vice versa.

{{% /alert %}}

## **Sujets avancés**
- [Vérifier le format personnalisé du nombre lors de la définition de la propriété de style personnalisé](/cells/fr/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [Liste des Formats de Nombre Supportés](/cells/fr/cpp/list-of-supported-number-formats/)
- [Rendre le modèle de format de date personnalisé g et ge mm dd](/cells/fr/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Spécifier les séparateurs de décimales et de groupe personnalisés pour le classeur](/cells/fr/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Spécifier la mise en forme du modèle personnalisé DBNum](/cells/fr/cpp/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="cpp" >}}
