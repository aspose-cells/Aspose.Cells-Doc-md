---
title: Protéger les feuilles de calcul
type: docs
weight: 10
url: /fr/net/protecting-worksheets/
---
{{% alert color="primary" %}}

Lorsqu'une feuille de calcul est protégée, les actions qu'un utilisateur peut effectuer sont restreintes. Par exemple, ils ne peuvent pas saisir de données, insérer ou supprimer des lignes ou des colonnes, etc.

{{% /alert %}}

## **Protéger les feuilles de calcul**

### **Introduction**

Les options de protection générales dans Microsoft Excel sont :

- Contenu
- Objets
- Scénarios

Les feuilles de calcul protégées ne cachent ni ne protègent les données sensibles, elles sont donc différentes du chiffrement de fichiers. En règle générale, la protection des feuilles de calcul convient à des fins de présentation. Il empêche l'utilisateur final de modifier les données, le contenu et la mise en forme dans la feuille de calcul.

### **Protéger une feuille de calcul**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classer.

 La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit la[**Protéger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) méthode utilisée pour appliquer la protection sur la feuille de calcul.[**Protéger**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) La méthode accepte les paramètres suivants :

-  Type de protection, le type de protection à appliquer sur la feuille de calcul. Le type de protection est appliqué à l'aide du[**Type de protection**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)énumération.
- Nouveau mot de passe, le nouveau mot de passe utilisé pour protéger la feuille de calcul.
- Ancien mot de passe, l'ancien mot de passe, si la feuille de calcul est déjà protégée par un mot de passe. Si la feuille de calcul n'est pas déjà protégée, passez simplement null.

 La[**Type de protection**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)L'énumération contient les types de protections prédéfinis suivants :

|**Types de protection**|**La description**|
|:- |:- |
|Tout|L'utilisateur ne peut rien modifier sur cette feuille de calcul|
|Contenu|L'utilisateur ne peut pas entrer de données dans cette feuille de calcul|
|Objets|L'utilisateur ne peut pas modifier les objets de dessin|
|Scénarios|L'utilisateur ne peut pas modifier les scénarios enregistrés|
|Structure|L'utilisateur ne peut pas modifier la structure|
|Windows|La protection est appliquée aux fenêtres|
|Aucun|Aucune protection n'est appliquée|

L'exemple ci-dessous montre comment protéger une feuille de calcul avec un mot de passe.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Une fois le code ci-dessus utilisé pour protéger la feuille de calcul, vous pouvez vérifier la protection sur la feuille de calcul en l'ouvrant. Une fois que vous ouvrez le fichier et essayez d'ajouter des données à la feuille de calcul, vous verrez la boîte de dialogue suivante :

|**Une boîte de dialogue avertissant qu'un utilisateur ne peut pas modifier la feuille de calcul**|
|:- |
|![tâche : image_autre_texte](protecting-worksheets_1.png)|

Pour travailler sur la feuille de calcul, déprotégez la feuille de calcul en sélectionnant le**protection** , alors**Déprotéger la feuille** du**Outils** élément du menu.

Après avoir sélectionné l'élément de menu Déprotéger la feuille, une boîte de dialogue s'ouvrira qui vous invitera à entrer le mot de passe afin que vous puissiez travailler sur la feuille de calcul comme indiqué ci-dessous :

|![tâche : image_autre_texte](protecting-worksheets_2.png)|

### **Protégez quelques Cells dans la feuille de calcul à l'aide de Microsoft Excel**

 Il peut y avoir certains scénarios où vous devez verrouiller quelques cellules uniquement dans la feuille de calcul. Si vous souhaitez verrouiller certaines cellules spécifiques de la feuille de calcul, vous devez déverrouiller toutes les autres cellules de la feuille de calcul. Toutes les cellules d'une feuille de calcul sont déjà initialisées pour le verrouillage, vous pouvez vérifier cette ouverture de n'importe quel fichier Excel dans MS Excel et cliquer sur le**Formater | Cells...** montrer**Format Cells**boîte de dialogue, puis cliquez sur le**protection** onglet et voir une case à cocher intitulée "Verrouillé" est cochée par défaut.

Les points suivants décrivent comment verrouiller quelques cellules à l'aide de MS Excel. Cette méthode s'applique aux versions Microsoft Office Excel 97, 2000, 2002, 2003 et supérieures.

1.  Sélectionnez la feuille de calcul entière en cliquant sur le**Tout sélectionner** bouton (le rectangle gris directement au-dessus du numéro de ligne pour la ligne 1 et à gauche de la lettre de colonne A).
1.  Cliquez sur**Cells** sur le**Format** menu, cliquez sur le**protection** puis effacez l'onglet**Fermé à clé** case à cocher.
 Cela déverrouille toutes les cellules de la feuille de calcul
 Si la**Cells** n'est pas disponible, certaines parties de la feuille de calcul sont peut-être déjà verrouillées. Sur le**Outils** menu, pointez sur**protection** , puis cliquez sur**Déprotéger la feuille**.
1.  Sélectionnez uniquement les cellules que vous souhaitez verrouiller et répétez l'étape 2, mais cette fois sélectionnez le**Fermé à clé** case à cocher.
1.  Sur le**Outils** menu, pointez sur**protection** , Cliquez sur**Feuille de protection** puis cliquez**D'ACCORD**.
1.  Dans le**Feuille de protection** boîte de dialogue, vous avez la possibilité de spécifier un mot de passe et de sélectionner les éléments que vous souhaitez que les utilisateurs puissent modifier.

### **Protégez quelques Cells dans la feuille de travail en utilisant Aspose Cells**

Dans cette méthode, nous utilisons Aspose.Cells API uniquement pour effectuer la tâche.

 Exemple : L'exemple suivant montre comment protéger quelques cellules dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille 3 cellules (A1, B1, C1). Enfin, il protège la feuille de calcul. La[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet contient une propriété booléenne,[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Vous pouvez définir[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propriété à vrai ou faux et appliquez*Colonne/Ligne.ApplyStyle()* méthode pour verrouiller ou déverrouiller la ligne/colonne avec les attributs souhaités.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Protéger une ligne dans la feuille de calcul**

 Aspose.Cells vous permet de verrouiller facilement n'importe quelle ligne de la feuille de calcul. Ici, nous pouvons utiliser[**AppliquerStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) méthode de[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) classe à appliquer[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) à une ligne particulière de la feuille de calcul. Cette méthode prend deux arguments : a[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet et[**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objet qui a tous les membres liés à la mise en forme appliquée.

 L'exemple suivant montre comment protéger une ligne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première ligne de celle-ci. Enfin, il protège la feuille de calcul. La[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet contient une propriété booléenne,[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Vous pouvez définir[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propriété sur true ou false pour verrouiller ou déverrouiller la ligne/colonne à l'aide de la[**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Protéger une colonne dans la feuille de calcul**

 Aspose.Cells vous permet de verrouiller facilement n'importe quelle colonne de la feuille de calcul. Ici, nous pouvons utiliser[**AppliquerStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) méthode de[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) classe à appliquer[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) à une colonne particulière de la feuille de calcul. Cette méthode prend deux arguments : a[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet et[**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objet qui a tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une colonne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première colonne de celle-ci. Enfin, il protège la feuille de calcul. La[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet contient une propriété booléenne,[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Vous pouvez définir[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propriété sur true ou false pour verrouiller ou déverrouiller la ligne/colonne à l'aide de la[**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Autoriser les utilisateurs à modifier les plages**

L'exemple suivant montre comment autoriser les utilisateurs à modifier une plage dans une feuille de calcul protégée.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
