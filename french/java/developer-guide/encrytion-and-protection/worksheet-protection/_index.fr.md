---
title: Protéger et déprotéger la feuille de travail
type: docs
weight: 50
url: /fr/java/protect-and-unprotect-worksheet/
---
## **Protéger les feuilles de calcul**

Lorsqu'une feuille de calcul est protégée, les actions qu'un utilisateur peut effectuer sont restreintes. Par exemple, ils ne peuvent pas saisir de données, insérer ou supprimer des lignes ou des colonnes, etc. Les options générales de protection dans Microsoft Excel sont :

- Contenu
- Objets
- Scénarios

Les feuilles de calcul protégées ne cachent ni ne protègent les données sensibles, elles sont donc différentes du chiffrement de fichiers. En règle générale, la protection des feuilles de calcul convient à des fins de présentation. Il empêche l'utilisateur final de modifier les données, le contenu et la mise en forme dans la feuille de calcul.

### **Ajouter ou supprimer une protection**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

 La classe Worksheet fournit les[**Protéger**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) méthode utilisée pour appliquer la protection à une feuille de calcul. La méthode Protect accepte les paramètres suivants :

-  Type de protection, le type de protection à appliquer sur la feuille de calcul. Le type de protection est appliqué à l'aide du[**Type de protection**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) énumération.
- Nouveau mot de passe, le nouveau mot de passe utilisé pour protéger la feuille de calcul.
- Ancien mot de passe, l'ancien mot de passe, si la feuille de calcul est déjà protégée par un mot de passe. Si la feuille de calcul n'est pas déjà protégée, passez simplement un null.

L'énumération ProtectionType contient les types de protection prédéfinis suivants :

|**Types de protection**|**Description**|
|:- |:- |
|[**TOUT**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|L'utilisateur ne peut rien modifier sur cette feuille de calcul|
|[**CONTENU**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|L'utilisateur ne peut pas entrer de données dans cette feuille de calcul|
|[**OBJETS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|L'utilisateur ne peut pas modifier les objets de dessin|
|[**SCÉNARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|L'utilisateur ne peut pas modifier les scénarios enregistrés|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|L'utilisateur ne peut pas modifier la structure enregistrée|
|[**LES FENÊTRES**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|L'utilisateur ne peut pas modifier les fenêtres enregistrées|
|[**RIEN**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Pas de protection|

L'exemple ci-dessous montre comment protéger une feuille de calcul avec un mot de passe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Une fois le code ci-dessus utilisé pour protéger la feuille de calcul, vérifiez la protection sur la feuille de calcul en l'ouvrant. Une fois que vous avez ouvert le fichier et essayé d'ajouter des données à la feuille de calcul, la boîte de dialogue suivante s'affiche :

**Une boîte de dialogue avertissant qu'un utilisateur ne peut pas modifier la feuille de calcul** 

![tâche : image_autre_texte](protect-and-unprotect-worksheet_1.png)

Pour travailler sur la feuille de calcul, déprotégez la feuille de calcul en sélectionnant le**protection** , ensuite**Déprotéger la feuille** du**Outils** élément de menu comme indiqué ci-dessous.

**Sélection de l'élément de menu Déprotéger la feuille** 

![tâche : image_autre_texte](protect-and-unprotect-worksheet_2.png)

Une boîte de dialogue s'ouvre demandant un mot de passe.

**Saisie du mot de passe pour déprotéger la feuille de calcul** 

![tâche : image_autre_texte](protect-and-unprotect-worksheet_3.png)

### **Protéger quelques-uns Cells**

 Il peut y avoir certains scénarios où vous devez verrouiller quelques cellules uniquement dans la feuille de calcul. Si vous souhaitez verrouiller certaines cellules spécifiques de la feuille de calcul, vous devez déverrouiller toutes les autres cellules de la feuille de calcul. Toutes les cellules d'une feuille de calcul sont déjà initialisées pour le verrouillage, vous pouvez vérifier cette ouverture de n'importe quel fichier Excel dans MS Excel et cliquer sur le**Formater | Cells...** montrer**Format Cells** boîte de dialogue, puis cliquez sur l'onglet Protection et voyez une case à cocher intitulée "Verrouillé" est cochée par défaut.

Voici les deux approches pour mettre en œuvre la tâche.

**Méthode1 :**

Les points suivants décrivent comment verrouiller quelques cellules à l'aide de MS Excel. Cette méthode s'applique aux versions Microsoft Office Excel 97, 2000, 2002, 2003 et supérieures.

1. Sélectionnez la feuille de calcul entière en cliquant sur le bouton Sélectionner tout (le rectangle gris directement au-dessus du numéro de ligne pour la ligne 1 et à gauche de la lettre de colonne A).
1. Cliquez sur Cells dans le menu Format, cliquez sur l'onglet Protection, puis décochez la case Verrouillé.

 Cela déverrouille toutes les cellules de la feuille de calcul

{{% alert color="primary" %}}

Si la commande Cellules n'est pas disponible, certaines parties de la feuille de calcul sont peut-être déjà verrouillées. Dans le menu Outils , pointez sur Protection , puis cliquez sur Supprimer la protection de la feuille .

{{% /alert %}}

1. Sélectionnez uniquement les cellules que vous souhaitez verrouiller et répétez l'étape 2, mais cette fois, cochez la case Verrouillé.
1.  Sur le**Outils** menu, sélectionnez**protection** , Cliquez sur**Feuille de protection** , puis cliquez sur**D'ACCORD**.

{{% alert color="primary" %}}

Dans la boîte de dialogue Protéger la feuille, vous avez la possibilité de spécifier un mot de passe et de sélectionner les éléments que vous souhaitez que les utilisateurs puissent modifier.

{{% /alert %}}

**Méthode2 :**

Dans cette méthode, nous utilisons Aspose.Cells API uniquement pour effectuer la tâche.

L'exemple suivant montre comment protéger quelques cellules dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille 3 cellules (A1, B1, C1). Enfin, il protège la feuille de calcul. Une ligne/colonne a un Style API qui contient en outre une méthode Locked définie. Vous pouvez utiliser cette méthode pour verrouiller ou déverrouiller la ligne/colonne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Protéger une ligne dans la feuille de calcul**

 Aspose.Cells vous permet de verrouiller facilement n'importe quelle ligne de la feuille de calcul. Ici, nous pouvons utiliser[**appliquerStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) méthode de[**Ligne**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) classe pour appliquer Style à une ligne particulière de la feuille de calcul. Cette méthode prend deux arguments : a[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objet et[**StyleDrapeau**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct qui contient tous les membres liés au formatage appliqué.

L'exemple suivant montre comment protéger une ligne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première ligne de celle-ci. Enfin, il protège la feuille de calcul. Une ligne/colonne a un Style API qui contient en outre une méthode setCellLocked. Vous pouvez verrouiller ou déverrouiller la ligne/colonne à l'aide de la structure StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Protéger une colonne dans la feuille de calcul**

 Aspose.Cells vous permet de verrouiller facilement n'importe quelle colonne de la feuille de calcul. Ici, nous pouvons utiliser[**appliquerStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) méthode de[**Colonne**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) class pour appliquer Style à une colonne particulière de la feuille de calcul. Cette méthode prend deux arguments : a[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objet et[**StyleDrapeau**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct qui contient tous les membres liés au formatage appliqué.

L'exemple suivant montre comment protéger une colonne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première colonne de celle-ci. Enfin, il protège la feuille de calcul. Une ligne/colonne a un Style API qui contient en outre une méthode Locked définie. Vous pouvez verrouiller ou déverrouiller la ligne/colonne à l'aide de la structure StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Déprotéger une feuille de calcul**

[Protéger les feuilles de calcul](/cells/fr/java/protect-and-unprotect-worksheet/#protect-worksheets) et[Paramètres de protection avancés depuis Excel XP](/cells/fr/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) ont discuté de différentes approches de protection des feuilles de calcul. Que se passe-t-il si un développeur doit supprimer la protection d'une feuille de calcul protégée lors de l'exécution afin que certaines modifications puissent être apportées au fichier ? Cela peut facilement être fait avec Aspose.Cells.

### **Utilisation d'Excel Microsoft**

Pour supprimer la protection d'une feuille de calcul :

 Du**Outils** menu, sélectionnez**protection** suivie par**Déprotéger la feuille**.

**Sélection de la feuille de protection** 

![tâche : image_autre_texte](protect-and-unprotect-worksheet_4.png)

La protection est supprimée, sauf si la feuille de calcul est protégée par un mot de passe. Dans ce cas, une boîte de dialogue demande le mot de passe.

**Saisie du mot de passe pour déprotéger la feuille de calcul** 

![tâche : image_autre_texte](protect-and-unprotect-worksheet_5.png)

### **En utilisant Aspose.Cells**

 Une feuille de calcul peut être déprotégée en appelant le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**Déprotéger**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect() ) méthode. Le[**Déprotéger**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()) peut être utilisée de deux manières, décrites ci-dessous.

### **Déprotéger une feuille de calcul simplement protégée**

Une feuille de calcul simplement protégée est une feuille qui n'est pas protégée par un mot de passe. Ces feuilles de calcul peuvent être déprotégées en appelant la méthode unprotect sans passer de paramètre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Déprotéger une feuille de calcul protégée par un mot de passe**

Une feuille de calcul protégée par un mot de passe est une feuille protégée par un mot de passe. Ces feuilles de calcul peuvent être déprotégées en appelant une version surchargée de la méthode Unprotect qui prend le mot de passe comme paramètre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Paramètres de protection avancés depuis Excel XP**

[Protéger les feuilles de calcul](/cells/fr/java/protect-and-unprotect-worksheet/#protect-worksheets) discuté de la protection d'une feuille de calcul dans Microsoft Excel 97 et 2000. Mais depuis la sortie d'Excel 2002 ou XP, Microsoft a ajouté de nombreux paramètres de protection avancés. Ces paramètres de protection limitent ou autorisent les utilisateurs à :

- Supprimer des lignes ou des colonnes.
- Modifiez des contenus, des objets ou des scénarios.
- Mettre en forme les cellules, les lignes ou les colonnes.
- Insérez des lignes, des colonnes ou des hyperliens.
- Sélectionnez les cellules verrouillées ou déverrouillées.
- Utilisez des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells prend en charge tous les paramètres de protection avancés offerts par Excel XP et les versions ultérieures.

### **Paramètres de protection avancés à l'aide d'Excel XP et des versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1.  Du**Outils** menu, sélectionnez**protection** suivie par**Feuille de protection**.
 Une boîte de dialogue s'affiche.

   **Boîte de dialogue pour afficher les options de protection dans Excel XP**

![tâche : image_autre_texte](protect-and-unprotect-worksheet_6.png)

1. Autorisez ou restreignez les fonctionnalités des feuilles de calcul ou appliquez un mot de passe.

### **Paramètres de protection avancés à l'aide de Aspose.Cells**

Aspose.Cells prend en charge tous les paramètres de protection avancés.

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La classe Workbook contient une collection WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

 La classe Worksheet fournit la propriété Protection qui est utilisée pour appliquer ces paramètres de protection avancés. La propriété Protection est en fait un objet de la[**protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) classe qui encapsule plusieurs propriétés booléennes pour désactiver ou activer des restrictions.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Ci-dessous un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Enregistrez le fichier au format EXCEL97TO2003 ou XLSX car ces paramètres de protection avancés ne sont pris en charge que par MS Excel XP et les versions ultérieures.

{{% /alert %}}

### **Cell Problème de verrouillage**

Si vous souhaitez empêcher les utilisateurs de modifier des cellules, les cellules doivent être verrouillées avant que les paramètres de protection ne soient appliqués. Sinon, les cellules peuvent être modifiées même si la feuille de calcul est protégée. Dans Microsoft Excel XP, les cellules peuvent être verrouillées via la boîte de dialogue suivante :

**Boîte de dialogue pour verrouiller les cellules dans Excel XP** 

![tâche : image_autre_texte](protect-and-unprotect-worksheet_7.png)

Il est également possible de verrouiller les cellules en utilisant le Aspose.Cells API. Chaque cellule a un style API qui contient en outre une méthode setLocked. Utilisez-le pour verrouiller ou déverrouiller des cellules.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
