---
title: Protéger les feuilles de calcul avec C++
linktitle: Protéger les feuilles de calcul
type: docs
weight: 10
url: /fr/cpp/protecting-worksheets/
description: Apprenez comment protéger les feuilles de calcul, les lignes, les colonnes et les cellules spécifiques dans les fichiers Microsoft Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul est protégée, les actions qu'un utilisateur peut effectuer sont limitées. Par exemple, il ne peut pas saisir de données, insérer ou supprimer des lignes ou des colonnes, etc.

{{% /alert %}}

## **Protéger les feuilles de calcul**

### **Introduction**

Les options de protection générales dans Microsoft Excel sont :

- Contenu
- Objets
- Scénarios

Les feuilles de calcul protégées ne cachent ni ne protègent les données sensibles, donc c'est différent du chiffrement de fichier. Généralement, la protection de feuille de calcul est adaptée à des fins de présentation. Elle empêche l'utilisateur final de modifier les données, le contenu et la mise en forme dans la feuille de calcul.

### **Protéger une feuille de calcul**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit la méthode [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) qui est utilisée pour appliquer une protection sur la feuille de calcul. La méthode [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) accepte les paramètres suivants :

- Type de protection, le type de protection à appliquer sur la feuille de calcul. Le type de protection est appliqué avec l'aide de l'énumération [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/).
- Nouveau mot de passe, le nouveau mot de passe utilisé pour protéger la feuille de calcul.
- Ancien mot de passe, l'ancien mot de passe, si la feuille de calcul est déjà protégée par mot de passe. Si la feuille de calcul n'est pas déjà protégée, passez simplement null.

L'énumération [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) contient les types de protections prédéfinis suivants :

|**Types de protection**|**Description**|
| :- | :- |
|All|L'utilisateur ne peut rien modifier sur cette feuille de calcul|
|Contents|L'utilisateur ne peut pas saisir de données dans cette feuille de calcul|
|Objects|L'utilisateur ne peut pas modifier les objets de dessin|
|Scenarios|L'utilisateur ne peut pas modifier les scénarios sauvegardés|
|Structure|L'utilisateur ne peut pas modifier la structure|
|Windows|La protection est appliquée aux fenêtres|
|None|Aucune protection n'est appliquée|

L'exemple ci-dessous montre comment protéger une feuille de calcul avec un mot de passe.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Après le code ci-dessus est utilisé pour protéger la feuille de calcul, vous pouvez vérifier la protection sur la feuille de calcul en l'ouvrant. Une fois que vous ouvrez le fichier et essayez d'ajouter des données à la feuille de calcul, vous verrez le dialogue suivant:

|**Un avertissement de dialogue indiquant qu'un utilisateur ne peut pas modifier la feuille de calcul**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Pour travailler sur la feuille de calcul, protégez la feuille de calcul en sélectionnant la **Protection**, puis **Désactiver la protection de la feuille** dans le menu **Outils**.

Après avoir sélectionné l'élément de menu Désactiver la protection de la feuille, un dialogue s'ouvrira qui vous invitera à saisir le mot de passe afin que vous puissiez travailler sur la feuille de calcul comme indiqué ci-dessous:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Protéger quelques cellules dans la feuille de calcul à l'aide de Microsoft Excel**

Il peut y avoir certaines situations où vous devez verrouiller quelques cellules uniquement dans la feuille de calcul. Si vous souhaitez verrouiller certaines cellules spécifiques dans la feuille de calcul, vous devez déverrouiller toutes les autres cellules de la feuille de calcul. Toutes les cellules d'une feuille de calcul sont déjà initialisées pour le verrouillage, vous pouvez vérifier cela en ouvrant n'importe quel fichier Excel dans MS Excel et en cliquant sur le **Format | Cellules...** pour afficher la boîte de dialogue **Format de cellules**  puis cliquez sur l'onglet **Protection** et voyez que la case à cocher "Verrouillé" est cochée par défaut.

Les points suivants décrivent comment verrouiller quelques cellules à l'aide de MS Excel. Cette méthode s'applique aux versions Microsoft Office Excel 97, 2000, 2002, 2003 et supérieures.

1. Sélectionnez l'ensemble de la feuille de calcul en cliquant sur le bouton **Sélectionner tout** (le rectangle gris directement au-dessus du numéro de ligne pour la ligne 1 et à gauche de la lettre de colonne A).
1. Cliquez sur **Cellules** dans le menu **Format**, cliquez sur l'onglet **Protection**, puis décochez la case à cocher **Verrouillé**.
   Cela déverrouille toutes les cellules de la feuille de calcul
   Si la commande **Cellules** n'est pas disponible, certaines parties de la feuille de calcul peuvent déjà être verrouillées. Dans le menu **Outils**, pointez sur **Protection**, puis cliquez sur **Désactiver la protection de la feuille**.
1. Sélectionnez simplement les cellules que vous souhaitez verrouiller et répétez l'étape 2, mais cette fois-ci, cochez la case à cocher **Verrouillé**.
1. Dans le menu **Outils**, pointez sur **Protection**, cliquez sur **Protéger la feuille** puis cliquez sur **OK**.
1. Dans la boîte de dialogue **Protéger la feuille**, vous avez la possibilité de spécifier un mot de passe et de sélectionner les éléments que vous souhaitez que les utilisateurs puissent modifier.

### **Protéger quelques cellules dans la feuille de calcul en utilisant Aspose Cells**

Dans cette méthode, nous utilisons uniquement l'API Aspose.Cells pour effectuer la tâche.

Exemple: L'exemple suivant montre comment protéger quelques cellules dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille 3 cellules (A1, B1, C1) en elle. Ensuite, il protège la feuille de calcul. L'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contient une propriété booléenne, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Vous pouvez définir la propriété [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) sur true ou false et appliquer la méthode *Column/Row.ApplyStyle()* pour verrouiller ou déverrouiller la ligne/colonne avec les attributs souhaités.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Protéger une ligne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement n'importe quelle ligne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) de la classe [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) pour appliquer [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) à une ligne particulière dans la feuille de calcul. Cette méthode prend deux arguments: un objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) et un objet [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une ligne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première ligne en elle. Enfin, il protège la feuille de calcul. L'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contient une propriété booléenne, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Vous pouvez définir la propriété [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) sur true ou false pour verrouiller ou déverrouiller la ligne/colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Protéger une colonne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement n'importe quelle colonne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/) de la classe [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) pour appliquer [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) à une colonne particulière dans la feuille de calcul. Cette méthode prend deux arguments: un objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) et un objet [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une colonne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première colonne en elle. Enfin, il protège la feuille de calcul. L'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contient une propriété booléenne, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Vous pouvez définir la propriété [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) sur true ou false pour verrouiller ou déverrouiller la ligne/colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Autoriser les utilisateurs à modifier les plages**

L'exemple suivant montre comment autoriser les utilisateurs à modifier une plage dans une feuille de calcul protégée.

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

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
