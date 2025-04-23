---
title: Protéger les feuilles de calcul
type: docs
weight: 10
url: /fr/python-net/protecting-worksheets/
---

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul est protégée, les actions qu'un utilisateur peut entreprendre sont restreintes. Par exemple, ils ne peuvent pas saisir de données, insérer ou supprimer des lignes ou des colonnes, etc.

{{% /alert %}}

## **Protéger les feuilles de calcul**

### **Introduction**

Les options de protection générales dans Microsoft Excel sont :

- Contenu
- Objets
- Scénarios

Les feuilles de calcul protégées ne cachent ni ne protègent les données sensibles, donc c'est différent du chiffrement de fichier. Généralement, la protection de feuille de calcul est adaptée à des fins de présentation. Elle empêche l'utilisateur final de modifier les données, le contenu et la mise en forme dans la feuille de calcul.

### **Protéger une feuille de calcul**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d’accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit la méthode [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) qui est utilisée pour appliquer une protection sur la feuille de calcul. La méthode [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType-str-str) accepte les paramètres suivants :

- Type de protection, le type de protection à appliquer sur la feuille de calcul. Le type de protection est appliqué avec l'aide de l'énumération [**ProtectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/protectiontype).
- Nouveau mot de passe, le nouveau mot de passe utilisé pour protéger la feuille de calcul.
- Ancien mot de passe, l'ancien mot de passe, si la feuille de calcul est déjà protégée par mot de passe. Si la feuille de calcul n'est pas déjà protégée, passez simplement null.

L'énumération [**ProtectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/protectiontype) contient les types de protections prédéfinis suivants :

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectingWorksheet-1.py" >}}

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

Dans cette méthode, nous utilisons uniquement l’API Aspose.Cells pour Python via .NET pour effectuer la tâche.

Exemple: L'exemple suivant montre comment protéger quelques cellules dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille 3 cellules (A1, B1, C1) en elle. Ensuite, il protège la feuille de calcul. L'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) contient une propriété booléenne, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Vous pouvez définir la propriété [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) sur true ou false et appliquer la méthode *Column/Row.ApplyStyle()* pour verrouiller ou déverrouiller la ligne/colonne avec les attributs souhaités.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectingSpecificCellsinaWorksheet-1.py" >}}

### **Protéger une ligne dans la feuille de calcul**

Aspose.Cells pour Python via .NET vous permet de verrouiller facilement n’importe quelle ligne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) de la classe [**Aspose.Cells.Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) pour appliquer [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) à une ligne particulière dans la feuille de calcul. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) et un objet [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une ligne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première ligne en elle. Enfin, il protège la feuille de calcul. L'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) contient une propriété booléenne, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Vous pouvez définir la propriété [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) sur true ou false pour verrouiller ou déverrouiller la ligne/colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectingSpecificRowInWorksheet-1.py" >}}

### **Protéger une colonne dans la feuille de calcul**

Aspose.Cells pour Python via .NET vous permet de verrouiller facilement n’importe quelle colonne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/column/apply_style) de la classe [**Aspose.Cells.Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) pour appliquer [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) à une colonne particulière dans la feuille de calcul. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) et un objet [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une colonne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première colonne en elle. Enfin, il protège la feuille de calcul. L'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) contient une propriété booléenne, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Vous pouvez définir la propriété [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) sur true ou false pour verrouiller ou déverrouiller la ligne/colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-ProtectColumnWorksheet-1.py" >}}

### **Autoriser les utilisateurs à modifier les plages**

L'exemple suivant montre comment autoriser les utilisateurs à modifier une plage dans une feuille de calcul protégée.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EditRangesWorksheet-1.py" >}}

